#
# @BEGIN LICENSE
#
# Psi4: an open-source quantum chemistry software package
#
# Copyright (c) 2007-2019 The Psi4 Developers.
#
# The copyrights for code used from other parties are included in
# the corresponding files.
#
# This file is part of Psi4.
#
# Psi4 is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, version 3.
#
# Psi4 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License along
# with Psi4; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# @END LICENSE
#

from typing import Union, List

import numpy as np

from psi4 import core
from psi4.driver import constants
from psi4.driver.p4util import solvers
from psi4.driver.p4util.exceptions import *
from psi4.driver.procrouting.response.scf_products import (TDRSCFEngine, TDUSCFEngine)

dipole = {
    'name': 'Dipole polarizabilities',
    'printout_labels': ['X', 'Y', 'Z'],
    'mints_function': core.MintsHelper.ao_dipole,
    'vector names': ['AO Mux', 'AO Muy', 'AO Muz']
}

quadrupole = {
    'name': 'Quadrupole polarizabilities',
    'printout_labels': ['XX', 'XY', 'XZ', 'YY', 'YZ', 'ZZ'],
    'mints_function': core.MintsHelper.ao_quadrupole,
}
quadrupole['vector names'] = ["AO Quadrupole " + x for x in quadrupole["printout_labels"]]

traceless_quadrupole = {
    'name': 'Traceless quadrupole polarizabilities',
    'printout_labels': ['XX', 'XY', 'XZ', 'YY', 'YZ', 'ZZ'],
    'mints_function': core.MintsHelper.ao_traceless_quadrupole,
}
traceless_quadrupole['vector names'] = [
    "AO Traceless Quadrupole " + x for x in traceless_quadrupole["printout_labels"]
]

property_dicts = {
    'DIPOLE_POLARIZABILITIES': dipole,
    'QUADRUPOLE_POLARIZABILITIES': quadrupole,
    'TRACELESS_QUADRUPOLE_POLARIZABILITIES': traceless_quadrupole
}


def cpscf_linear_response(wfn, *args, **kwargs):
    """
    Compute the static properties from a reference wavefunction. The currently implemented properties are
      - dipole polarizability
      - quadrupole polarizability

    Parameters
    ----------
    wfn : psi4 wavefunction
        The reference wavefunction.
    args : list
        The list of arguments. For each argument, such as ``dipole polarizability``, will return the corresponding
        response. The user may also choose to pass a list or tuple of custom vectors.
    kwargs : dict
        Options that control how the response is computed. The following options are supported (with default values):
          - ``conv_tol``: 1e-5
          - ``max_iter``: 10
          - ``print_lvl``: 2

    Returns
    -------
    responses : list
        The list of responses.
    """
    mints = core.MintsHelper(wfn.basisset())

    # list of dictionaries to control response calculations, count how many user-supplied vectors we have
    complete_dict = []
    n_user = 0

    for arg in args:

        # for each string keyword, append the appropriate dictionary (vide supra) to our list
        if isinstance(arg, str):
            ret = property_dicts.get(arg)
            if ret:
                complete_dict.append(ret)
            else:
                raise ValidationError('Do not understand {}. Abort.'.format(arg))

        # the user passed a list of vectors. absorb them into a dictionary
        elif isinstance(arg, tuple) or isinstance(arg, list):
            complete_dict.append({
                'name': 'User Vectors',
                'length': len(arg),
                'vectors': arg,
                'vector names': ['User Vector {}_{}'.format(n_user, i) for i in range(len(arg))]
            })
            n_user += len(arg)

        # single vector passed. stored in a dictionary as a list of length 1 (can be handled as the case above that way)
        # note: the length is set to '0' to designate that it was not really passed as a list
        else:
            complete_dict.append({
                'name': 'User Vector',
                'length': 0,
                'vectors': [arg],
                'vector names': ['User Vector {}'.format(n_user)]
            })
            n_user += 1

    # vectors will be passed to the cphf solver, vector_names stores the corresponding names
    vectors = []
    vector_names = []

    # construct the list of vectors. for the keywords, fetch the appropriate tensors from MintsHelper
    for prop in complete_dict:
        if 'User' in prop['name']:
            for name, vec in zip(prop['vector names'], prop['vectors']):
                vectors.append(vec)
                vector_names.append(name)

        else:
            tmp_vectors = prop['mints_function'](mints)
            for tmp in tmp_vectors:
                tmp.scale(-2.0)  # RHF only
                vectors.append(tmp)
                vector_names.append(tmp.name)

    # do we have any vectors to work with?
    if len(vectors) == 0:
        raise ValidationError('I have no vectors to work with. Aborting.')

    # print information on module, vectors that will be used
    _print_header(complete_dict, n_user)

    # fetch wavefunction information
    nbf = wfn.nmo()
    ndocc = wfn.nalpha()
    nvirt = nbf - ndocc

    c_occ = wfn.Ca_subset("AO", "OCC")
    c_vir = wfn.Ca_subset("AO", "VIR")

    # the vectors need to be in the MO basis. if they have the shape nbf x nbf, transform.
    for i in range(len(vectors)):
        shape = vectors[i].shape

        if shape == (nbf, nbf):
            vectors[i] = core.triplet(c_occ, vectors[i], c_vir, True, False, False)

        # verify that this vector already has the correct shape
        elif shape != (ndocc, nvirt):
            raise ValidationError('ERROR: "{}" has an unrecognized shape. Must be either ({}, {}) or ({}, {})'.format(
                vector_names[i], nbf, nbf, ndocc, nvirt))

    # compute response vectors for each input vector
    params = [kwargs.pop("conv_tol", 1.e-5), kwargs.pop("max_iter", 10), kwargs.pop("print_lvl", 2)]

    responses = wfn.cphf_solve(vectors, *params)

    # zip vectors, responses for easy access
    vectors = {k: v for k, v in zip(vector_names, vectors)}
    responses = {k: v for k, v in zip(vector_names, responses)}

    # compute response values, format output
    output = []
    for prop in complete_dict:

        # try to replicate the data structure of the input
        if 'User' in prop['name']:
            if prop['length'] == 0:
                output.append(responses[prop['vector names'][0]])
            else:
                buf = []
                for name in prop['vector names']:
                    buf.append(responses[name])
                output.append(buf)

        else:
            names = prop['vector names']
            dim = len(names)

            buf = np.zeros((dim, dim))

            for i, i_name in enumerate(names):
                for j, j_name in enumerate(names):
                    buf[i, j] = -1.0 * vectors[i_name].vector_dot(responses[j_name])

            output.append(buf)

    _print_output(complete_dict, output)

    return output


def _print_header(complete_dict, n_user):
    core.print_out('\n\n         ---------------------------------------------------------\n'
                   '         {:^57}\n'.format('CPSCF Linear Response Solver') +
                   '         {:^57}\n'.format('by Marvin Lechner and Daniel G. A. Smith') +
                   '         ---------------------------------------------------------\n')

    core.print_out('\n   ==> Requested Responses <==\n\n')

    for prop in complete_dict:
        if 'User' not in prop['name']:
            core.print_out('    {}\n'.format(prop['name']))

    if n_user != 0:
        core.print_out('    {} user-supplied vector(s)\n'.format(n_user))


def _print_matrix(descriptors, content, title):
    length = len(descriptors)

    matrix_header = '         ' + ' {:^10}' * length + '\n'
    core.print_out(matrix_header.format(*descriptors))
    core.print_out('    -----' + ' ----------' * length + '\n')

    for i, desc in enumerate(descriptors):
        core.print_out('    {:^5}'.format(desc))
        for j in range(length):
            core.print_out(' {:>10.5f}'.format(content[i, j]))

            # Set the name
            var_name = title + " " + descriptors[i] + descriptors[j]
            core.set_variable(var_name, content[i, j])
        core.print_out('\n')


def _print_output(complete_dict, output):
    core.print_out('\n   ==> Response Properties <==\n')

    for i, prop in enumerate(complete_dict):
        if not 'User' in prop['name']:
            core.print_out('\n    => {} <=\n\n'.format(prop['name']))
            directions = prop['printout_labels']
            var_name = prop['name'].upper().replace("IES", "Y")
            _print_matrix(directions, output[i], var_name)


def _print_tdscf_header(**options):
    core.print_out("\n\n         ---------------------------------------------------------\n"
                   f"         {'TDSCF excitation energies':^57}\n" +
                   f"         {'by Andrew M. James and Daniel G. A. Smith':^57}\n" +
                   "         ---------------------------------------------------------\n")

    core.print_out("\n  ==> Requested Excitations <==\n\n")
    state_info = options.pop('states')
    for nstate, state_sym in state_info:
        core.print_out(f"      {nstate} states with {state_sym} symmetry\n")

    core.print_out("\n  ==> Options <==\n\n")
    for k, v in options.items():
        core.print_out(f"     {k:<10s}:              {v}\n")

    core.print_out("\n")


def tdscf_excitations(wfn,
                      *,
                      states: Union[int, List[int]],
                      triplets: str = "none",
                      tda: bool = False,
                      r_tol: float = 1.0e-4,
                      max_ss_vec: int = 50,
                      maxiter: int = 60,
                      guess: str = "denominators",
                      print_lvl: int = 1):
    """Compute excitations from a SCF(HF/KS) wavefunction

    Parameters
    -----------
    wfn : :py:class:`psi4.core.Wavefunction`
       The reference wavefunction
    states : Union[int, List[int]]
       How many roots (excited states) should the solver seek to converge?
       This function accepts either an integer or a list of integers:
         - The list has :math:`n_{\mathrm{irrep}}` elements and is only
           acceptable if the system has symmetry. It tells the solver how many
           states per irrep to calculate.
         - If an integer is given _and_ the system has symmetry, the states
           will be distributed among irreps.
           For example, ``states = 10`` for a D2h system will compute 10 states
           distributed as ``[2, 2, 1, 1, 1, 1, 1, 1]`` among irreps.
    triplets : {"none", "only", "also"}
       Should the solver seek to converge states of triplet symmetry?
       Default is `none`: do not seek to converge triplets.
       Valid options are:
         - `none`. Do not seek to converge triplets.
         - `only`. Only seek to converge triplets.
         - `also`. Seek to converge both triplets and singlets. This choice is
           only valid for restricted reference wavefunction. Moreover, it will
           **at least double** the cost of the response calculation: singlet
           and triplet solutions are found separately and `also` will seek to
           converge the same number of `states` for both spin symmetries.
    tda :  bool, optional.
       Should the solver use the Tamm-Dancoff approximation (TDA) or the
       random-phase approximation (RPA)?
       Default is ``False``: use RPA.
       Note that TDA is equivalent to CID for HF references.
    r_tol : float, optional.
       The convergence threshold for the norm of the residual vector.
       Default: 1.0e-4
       Using a tighter convergence threshold here requires tighter SCF ground
       state convergence threshold. As a rule of thumb, with the SCF ground
       state density converged to :math:`10^{-N}` (``D_CONVERGENGE = 1.0e-N``),
       you can afford converging a corresponding TDSCF calculation to
       :math:`10^{-(N-2)}`.
       The default value is consistent with the default value for
       ``D_CONVERGENCE``.
    max_ss_vec: int, optional.
       The maximum number of trial vectors in the iterative subspace that will
       be stored before a collapse is done.
       Default: 50
    guess : str, optional.
       How should the starting trial vectors be generated?
       Default: `denominators`, i.e. use orbital energy differences to generate
       guess vectors.
    print_lvl : int, optional.
       How verbose should the solver be?
       Default: 1


    Notes
    -----
    The algorithm employed to solve the non-Hermitian eigenvalue problem (``tda = False``)
    will fail when the SCF wavefunction has a triplet instability.

    This function can be used for:
      - restricted singlets: RPA or TDA, any functional
      - restricted triplets: RPA or TDA, Hartree-Fock only
      - unresctricted: RPA or TDA, Hartre-Fock and LDA only

    References
    ----------
    For the expression of the transition moments in length and velocity gauges:

    .. [Pedersen1995-du] T. B. Pedersen, A. E. Hansen, "Ab Initio Calculation and Display of the Rotary Strength Tensor in the Random Phase Approximation. Method and Model Studies." Chem. Phys. Lett., 246, 1 (1995)
    """
    ssuper_name = wfn.functional().name()

    # validate states
    if not (isinstance(states, int) or isinstance(states, list)):
        raise ValidationError("Number of states must be either an integer or a list of integers")

    # determine how many singlet states per irrep to seek
    singlets_per_irrep = []
    if isinstance(states, list):
        # list of states per irrep given, validate it
        if len(states) != wfn.nirrep():
            raise ValidationError(f"States requested ({states}) do not match with number of irreps ({wfn.nirrep()})")
        else:
            singlets_per_irrep = states
    else:
        # total number of states given, distribute them among irreps
        singlets_per_irrep = [states // wfn.nirrep()] * wfn.nirrep()
        for i in range(states % wfn.nirrep()):
            singlets_per_irrep[i] += 1

    # do triplets?
    restricted = wfn.same_a_b_orbs()
    do_triplets = False if triplets == "none" else True
    triplets_per_irrep = singlets_per_irrep
    if (not restricted) and do_triplets:
        raise ValidationError("Cannot compute triplets with an unrestricted reference")

    # validate calculation
    if restricted and wfn.functional().needs_xc() and do_triplets:
        raise ValidationError("Restricted Vx kernel only spin-adapted for singlets")

    not_lda = wfn.functional().is_gga() or wfn.functional().is_meta()
    if (not restricted) and not_lda:
        raise ValidationError("Unrestricted Kohn-Sham Vx kernel currently limited to SVWN functional")

    if guess.lower() != "denominators":
        raise ValidationError(f"Guess type {guess} is not valid")

    # which problem
    ptype = 'rpa'
    solve_function = solvers.hamiltonian_solver
    if tda:
        ptype = 'tda'
        solve_function = solvers.davidson_solver

    _print_tdscf_header(rtol=r_tol,
                        states=[(count, label) for count, label in zip(singlets_per_irrep,
                                                                       wfn.molecule().irrep_labels())],
                        guess_type=guess,
                        restricted=restricted,
                        triplet=do_triplets,
                        ptype=ptype)

    # construct the engine
    if restricted:
        engine = TDRSCFEngine(wfn, ptype=ptype, triplet=do_triplets)
    else:
        engine = TDUSCFEngine(wfn, ptype=ptype)

    _results = []
    for state_sym, nstates in enumerate(singlets_per_irrep):
        if nstates == 0:
            continue
        engine.reset_for_state_symm(state_sym)
        guess_ = engine.generate_guess(nstates * 2)

        vecs_per_root = max_ss_vec // nstates

        # ret = {"eigvals": ee, "eigvecs": (rvecs, rvecs), "stats": stats} (TDA)
        # ret = {"eigvals": ee, "eigvecs": (rvecs, lvecs), "stats": stats} (RPA)
        ret = solve_function(engine=engine,
                             nroot=nstates,
                             r_tol=r_tol,
                             max_vecs_per_root=vecs_per_root,
                             maxiter=maxiter,
                             guess=guess_,
                             verbose=print_lvl)

        if not ret["stats"][-1]["done"]:
            # prepare and raise error
            spin = "triplet" if do_triplets else "singlet"
            irrep_ES = wfn.molecule().irrep_labels()[state_sym]
            raise TDSCFConvergenceError(maxiter, wfn, f"{spin} excitations in irrep {irrep_ES}")

        # TODO move rescaling by np.sqrt(2.0) to the solver
        for root, (R, L) in enumerate(ret["eigvecs"]):
            R = engine.vector_scale(np.sqrt(2.0), R)
            L = engine.vector_scale(np.sqrt(2.0), L)
            ret["eigvecs"][root] = (R, L)
        # flatten dictionary: helps with sorting by energy
        # also append state symmetry to return value
        # TODO what to do with the stats?
        for e, (R, L) in zip(ret["eigvals"], ret["eigvecs"]):
            _results.append((e, R, L, state_sym))

    # sort by energy, symmetry is just meta data
    _results = sorted(_results, key=lambda x: x[0])

    # print excitation energies
    core.print_out("\n\nFinal Summary:\n")
    core.print_out("        " + (" " * 20) + " " + "Excitation Energy".center(31) + f" {'Total Energy':^15}" +
                   "Oscillator Strength".center(31) + "\n")
    core.print_out(
        f"    {'#':^4} {'Sym: GS->ES (Trans)':^20} {'au':^15} {'eV':^15} {'au':^15} {'au (length)':^15} {'au (velocity)':^15}\n"
    )
    core.print_out(f"    {'-':->4} {'-':->20} {'-':->15} {'-':->15} {'-':->15} {'-':->15} {'-':->15}\n")

    # compute some spectroscopic observables
    # TODO generalize to UHF
    # Get integrals
    Ca_left = wfn.Ca_subset("SO", "OCC")
    Ca_right = wfn.Ca_subset("SO", "VIR")
    mints = core.MintsHelper(wfn.basisset())

    def compute_ints(C_L, C_R, so_computer):
        return [core.triplet(C_L, x, C_R, True, False, False) for x in so_computer()]

    property_integrals = {
        "length gauge electric dipole": compute_ints(Ca_left, Ca_right, mints.so_dipole),
        "velocity gauge electric dipole": compute_ints(Ca_left, Ca_right, mints.so_nabla),
        "magnetic dipole": compute_ints(Ca_left, Ca_right, mints.so_angular_momentum)
    }

    irrep_GS = wfn.molecule().irrep_labels()[engine.G_gs]
    # collect results into ExcitationData and return as List[ExcitationData]
    solver_results = []
    for i, (E_ex_au, R, L, final_sym) in enumerate(_results):
        irrep_ES = wfn.molecule().irrep_labels()[final_sym]
        irrep_trans = wfn.molecule().irrep_labels()[engine.G_gs ^ final_sym]
        sym_descr = f"{irrep_GS}->{irrep_ES} ({irrep_trans})"
        solver_results.append({"EXCITATION ENERGY": E_ex_au, "SYMMETRY": irrep_trans})

        E_ex_ev = constants.conversion_factor('hartree', 'eV') * E_ex_au

        E_tot_au = wfn.energy() + E_ex_au

        wfn.set_variable(f"TD-{ssuper_name} ROOT {i+1} TOTAL ENERGY - {irrep_ES} SYMMETRY", E_tot_au)
        wfn.set_variable(f"TD-{ssuper_name} ROOT 0 -> ROOT {i+1} EXCITATION ENERGY - {irrep_ES} SYMMETRY", E_ex_au)

        # length-gauge electric dipole transition moment
        edtm_length = np.array([R.vector_dot(prop) for prop in property_integrals["length gauge electric dipole"]])
        # lenght-gauge oscillator strength
        f_length = 2 / 3 * E_ex_au * np.sum(edtm_length**2)
        # velocity-gauge electric dipole transition moment
        edtm_velocity = np.array([L.vector_dot(prop) for prop in property_integrals["velocity gauge electric dipole"]])
        # velocity-gauge oscillator strength
        f_velocity = 2 / 3 * np.sum(edtm_velocity**2) / E_ex_au
        # length gauge magnetic dipole transition moment
        # 1/2 is the Bohr magneton in atomic units
        mdtm = 0.5 * np.array([L.vector_dot(prop) for prop in property_integrals["magnetic dipole"]])
        # NOTE The signs for rotatory strengths are opposite WRT the cited paper.
        # This is becasue Psi4 defines length-gauge dipole integral to include the electron charge (-1.0)
        # velocity gauge rotatory strength
        R_velocity = -np.einsum("i,i", edtm_velocity, mdtm) / E_ex_au
        # length gauge rotatory strength
        R_length = np.einsum("i,i", edtm_length, mdtm)

        core.print_out(
            f"    {i+1:^4} {sym_descr:^20} {E_ex_au:< 15.5f} {E_ex_ev:< 15.5f} {E_tot_au:< 15.5f} {f_length:< 15.5f} {f_velocity:< 15.5f}\n"
        )

    core.print_out("\n")

    #TODO: output table

    #TODO: check/handle convergence failures

    return solver_results
