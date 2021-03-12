#
# @BEGIN LICENSE
#
# Psi4: an open-source quantum chemistry software package
#
# Copyright (c) 2007-2021 The Psi4 Developers.
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
"""Module with property-related helper functions."""

import qcelemental as qcel

import psi4
from psi4 import core
from . import optproc


def free_atom_volumes(wfn, **kwargs):
    """ 

    """

    # the level of theory
    module = wfn.module()

    # print level
    print_level = core.get_global_option("PRINT")

    # if we're doing dft, grab the functional
    if module.lower() == 'scf':
        module = wfn.functional().name()
    # list of reference number of unpaired electrons.
    # Note that this is not the same as the 
    # total spin of the ground state atom
    reference_S = [ 0,
                    1,                                                                                           0,
                    1, 0,                                                                         1, 2, 3, 2, 1, 0,
                    1, 0,                                                                         1, 2, 3, 2, 1, 0,
                    1, 0,                                           1, 2, 3, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 2, 1, 0,
                    1, 0,                                           1, 2, 5, 6, 5, 4, 3, 0, 1, 0, 1, 2, 3, 2, 1, 0,
                    1, 0, 1, 0, 3, 4, 5, 6, 7, 8, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 2, 1, 0 ]


    # the parent molecule and reference type
    mol = wfn.molecule()
    user_ref = core.get_global_option('REFERENCE')

    # Get unique atoms by input symbol,
    # Be to handle different basis sets
    atom_ids = {}
    for atom in range(mol.natom()):
        symbol = mol.symbol(atom)
        Z = int(mol.Z(atom))
        basis = mol.basis_on_atom(atom)
    
        for a, info in atom_ids.items():
            if a == atom:
                continue
            if info['symbol'] == symbol:
                continue
            if info['basis'] == basis:
                continue
        atom_ids[atom] = {'symbol':symbol,'Z':Z,'basis':basis}

    core.print_out(f"  Running {len(atom_ids)} free-atom UHF computations")

    for label, info  in atom_ids.items():

        a_z = info['Z']
        basis = info['basis']
        a_sym = info['symbol']

        geom = f"""
0 {int(1+reference_S[a_z])} 
{a_sym} 0.0 0.0 0.0
symmetry c1
"""
        
        optstash = optproc.OptionsState(['REFERENCE'])

        # make sure we do UHF/UKS if we're not a singlet
        if reference_S[a_z] != 0:
            core.set_global_option("REFERENCE", "UHF") 
        else:
            core.set_global_option("REFERENCE", "RHF") 

        # Set the molecule, here just an atom
        molrec = qcel.molparse.from_string(geom, enable_qm=True, 
            missing_enabled_return_qm='minimal', enable_efp=True, missing_enabled_return_efp='none')
        a_mol = core.Molecule.from_dict(molrec['qm'])
        a_mol.update_geometry() 
        psi4.molutil.activate(a_mol)

        method = module+"/"+basis

        # Supress printing
        if print_level <= 1:
            core.be_quiet()

        # Get the atomic wfn
        at_e, at_wfn = psi4.energy(method, return_wfn=True)

        # Now, re-run mbis for the atomic density, grabbing only the volume 
        psi4.oeprop(at_wfn, 'MBIS_CHARGES', title=a_sym + " " + method , free_atom=True) 

        if print_level <= 1:
            core.reopen_outfile()

        vw = at_wfn.array_variable('MBIS RADIAL MOMENTS <R^3>')
        vw = vw.get(0,0) 

        # set the atomic widths as wfn variables
        wfn.set_variable("MBIS FREE ATOM " + a_sym + " VOLUME", vw)


    # reset mol and reference to original
    core.set_global_option("REFERENCE",user_ref)

    optstash.restore()
    mol.update_geometry()

