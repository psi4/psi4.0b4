#
# @BEGIN LICENSE
#
# Psi4: an open-source quantum chemistry software package
#
# Copyright (c) 2007-2016 The Psi4 Developers.
#
# The copyrights for code used from other parties are included in
# the corresponding files.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# @END LICENSE
#

"""
| Database of Pulay corannulene structures. Subsumed into CFLOW.

- **cp**  ``'off'`` || ``'on'``

- **rlxd** ``'off'``

"""
import re
import qcdb

# <<< CORE Database Module >>>
# Geometries and Reference energies from.
dbse = 'CORE'

# <<< Database Members >>>
HRXN = ['dimer3_54', 'dimer3_64', 'dimer3_73', 'dimer3_74', 'dimer3_84', ]
HRXN_SM = []
HRXN_LG = []

# <<< Chemical Systems Involved >>>
RXNM = {}     # reaction matrix of reagent contributions per reaction
ACTV = {}     # order of active reagents per reaction
ACTV_CP = {}  # order of active reagents per counterpoise-corrected reaction
ACTV_SA = {}  # order of active reagents for non-supermolecular calculations
for rxn in HRXN:

    RXNM[   '%s-%s' % (dbse, rxn)] = {'%s-%s-dimer'      % (dbse, rxn) : +1,
                                      '%s-%s-monoA-CP'   % (dbse, rxn) : -1,
                                      '%s-%s-monoB-CP'   % (dbse, rxn) : -1,
                                      '%s-%s-monoA-unCP' % (dbse, rxn) : -1,
                                      '%s-%s-monoB-unCP' % (dbse, rxn) : -1 }

    ACTV_SA['%s-%s' % (dbse, rxn)] = ['%s-%s-dimer'      % (dbse, rxn) ]

    ACTV_CP['%s-%s' % (dbse, rxn)] = ['%s-%s-dimer'      % (dbse, rxn),
                                      '%s-%s-monoA-CP'   % (dbse, rxn),
                                      '%s-%s-monoB-CP'   % (dbse, rxn) ]

    ACTV[   '%s-%s' % (dbse, rxn)] = ['%s-%s-dimer'      % (dbse, rxn),
                                      '%s-%s-monoA-unCP' % (dbse, rxn),
                                      '%s-%s-monoB-unCP' % (dbse, rxn) ]

# <<< Reference Values [kcal/mol] >>>
# Taken from
BIND = {}
BIND['%s-%s'            % (dbse, 'dimer3_54'             )] =    -14.8000
BIND['%s-%s'            % (dbse, 'dimer3_64'             )] =    -15.4000
BIND['%s-%s'            % (dbse, 'dimer3_73'             )] =    -15.6000  # Bootstrapped, Pulay does not report
BIND['%s-%s'            % (dbse, 'dimer3_74'             )] =    -15.4000
BIND['%s-%s'            % (dbse, 'dimer3_84'             )] =    -15.0000

# <<< Comment Lines >>>
TAGL = {}
TAGL['%s-%s'            % (dbse, 'dimer3_54'             )] = """ """
TAGL['%s-%s-dimer'      % (dbse, 'dimer3_54'             )] = """Dimer from  """
TAGL['%s-%s-monoA-CP'   % (dbse, 'dimer3_54'             )] = """Monomer A from  """
TAGL['%s-%s-monoB-CP'   % (dbse, 'dimer3_54'             )] = """Monomer B from  """
TAGL['%s-%s-monoA-unCP' % (dbse, 'dimer3_54'             )] = """Monomer A from  """
TAGL['%s-%s-monoB-unCP' % (dbse, 'dimer3_54'             )] = """Monomer B from  """
TAGL['%s-%s'            % (dbse, 'dimer3_64'             )] = """ """
TAGL['%s-%s-dimer'      % (dbse, 'dimer3_64'             )] = """Dimer from  """
TAGL['%s-%s-monoA-CP'   % (dbse, 'dimer3_64'             )] = """Monomer A from  """
TAGL['%s-%s-monoB-CP'   % (dbse, 'dimer3_64'             )] = """Monomer B from  """
TAGL['%s-%s-monoA-unCP' % (dbse, 'dimer3_64'             )] = """Monomer A from  """
TAGL['%s-%s-monoB-unCP' % (dbse, 'dimer3_64'             )] = """Monomer B from  """
TAGL['%s-%s'            % (dbse, 'dimer3_73'             )] = """ """
TAGL['%s-%s-dimer'      % (dbse, 'dimer3_73'             )] = """Dimer from  """
TAGL['%s-%s-monoA-CP'   % (dbse, 'dimer3_73'             )] = """Monomer A from  """
TAGL['%s-%s-monoB-CP'   % (dbse, 'dimer3_73'             )] = """Monomer B from  """
TAGL['%s-%s-monoA-unCP' % (dbse, 'dimer3_73'             )] = """Monomer A from  """
TAGL['%s-%s-monoB-unCP' % (dbse, 'dimer3_73'             )] = """Monomer B from  """
TAGL['%s-%s'            % (dbse, 'dimer3_74'             )] = """ """
TAGL['%s-%s-dimer'      % (dbse, 'dimer3_74'             )] = """Dimer from  """
TAGL['%s-%s-monoA-CP'   % (dbse, 'dimer3_74'             )] = """Monomer A from  """
TAGL['%s-%s-monoB-CP'   % (dbse, 'dimer3_74'             )] = """Monomer B from  """
TAGL['%s-%s-monoA-unCP' % (dbse, 'dimer3_74'             )] = """Monomer A from  """
TAGL['%s-%s-monoB-unCP' % (dbse, 'dimer3_74'             )] = """Monomer B from  """
TAGL['%s-%s'            % (dbse, 'dimer3_84'             )] = """ """
TAGL['%s-%s-dimer'      % (dbse, 'dimer3_84'             )] = """Dimer from  """
TAGL['%s-%s-monoA-CP'   % (dbse, 'dimer3_84'             )] = """Monomer A from  """
TAGL['%s-%s-monoB-CP'   % (dbse, 'dimer3_84'             )] = """Monomer B from  """
TAGL['%s-%s-monoA-unCP' % (dbse, 'dimer3_84'             )] = """Monomer A from  """
TAGL['%s-%s-monoB-unCP' % (dbse, 'dimer3_84'             )] = """Monomer B from  """

# <<< Geometry Specification Strings >>>
GEOS = {}

GEOS['%s-%s-dimer' % (dbse, 'dimer3_54')] = qcdb.Molecule("""
0 1
C        0.70622800     0.97211978     0.61694803
C       -0.70622800     0.97211978     0.61694803
C       -1.14280400    -0.37137722     0.61681203
C        0.00000000    -1.20165922     0.61659503
C        1.14280400    -0.37137722     0.61681203
C        1.45779000     2.00650178     0.09413403
C       -1.45779000     2.00650178     0.09413403
C       -2.35873800    -0.76639722     0.09397203
C        0.00000000    -2.48004022     0.09366903
C        2.35873800    -0.76639722     0.09397203
C        0.69261800     3.17923978    -0.25321497
C       -0.69261800     3.17923978    -0.25321497
C       -2.80958100     1.64119778    -0.25292797
C       -3.23765700     0.32373778    -0.25303797
C       -2.42918200    -2.16498922    -0.25302597
C       -1.30841500    -2.97916822    -0.25327697
C        1.30841500    -2.97916822    -0.25327697
C        2.42918200    -2.16498922    -0.25302597
C        3.23765700     0.32373778    -0.25303797
C        2.80958100     1.64119778    -0.25292797
H        1.20851300     4.06642078    -0.61418797
H       -1.20851300     4.06642078    -0.61418797
H       -3.49401500     2.40602178    -0.61367197
H       -4.24094400     0.10729578    -0.61373997
H       -3.36816400    -2.57958822    -0.61350597
H       -1.41248600    -4.00024222    -0.61397997
H        1.41248600    -4.00024222    -0.61397997
H        3.36816400    -2.57958822    -0.61350597
H        4.24094400     0.10729578    -0.61373997
H        3.49401500     2.40602178    -0.61367197
--
0 1
C        0.70622800     0.97211978     4.15694803
C       -0.70622800     0.97211978     4.15694803
C       -1.14280400    -0.37137722     4.15681203
C        0.00000000    -1.20165922     4.15659503
C        1.14280400    -0.37137722     4.15681203
C        1.45779000     2.00650178     3.63413403
C       -1.45779000     2.00650178     3.63413403
C       -2.35873800    -0.76639722     3.63397203
C        0.00000000    -2.48004022     3.63366903
C        2.35873800    -0.76639722     3.63397203
C        0.69261800     3.17923978     3.28678503
C       -0.69261800     3.17923978     3.28678503
C       -2.80958100     1.64119778     3.28707203
C       -3.23765700     0.32373778     3.28696203
C       -2.42918200    -2.16498922     3.28697403
C       -1.30841500    -2.97916822     3.28672303
C        1.30841500    -2.97916822     3.28672303
C        2.42918200    -2.16498922     3.28697403
C        3.23765700     0.32373778     3.28696203
C        2.80958100     1.64119778     3.28707203
H        1.20851300     4.06642078     2.92581203
H       -1.20851300     4.06642078     2.92581203
H       -3.49401500     2.40602178     2.92632803
H       -4.24094400     0.10729578     2.92626003
H       -3.36816400    -2.57958822     2.92649403
H       -1.41248600    -4.00024222     2.92602003
H        1.41248600    -4.00024222     2.92602003
H        3.36816400    -2.57958822     2.92649403
H        4.24094400     0.10729578     2.92626003
H        3.49401500     2.40602178     2.92632803
units angstrom
""")

GEOS['%s-%s-dimer' % (dbse, 'dimer3_64')] = qcdb.Molecule("""
0 1
C        0.70622800     0.97211978     0.61694803
C       -0.70622800     0.97211978     0.61694803
C       -1.14280400    -0.37137722     0.61681203
C        0.00000000    -1.20165922     0.61659503
C        1.14280400    -0.37137722     0.61681203
C        1.45779000     2.00650178     0.09413403
C       -1.45779000     2.00650178     0.09413403
C       -2.35873800    -0.76639722     0.09397203
C        0.00000000    -2.48004022     0.09366903
C        2.35873800    -0.76639722     0.09397203
C        0.69261800     3.17923978    -0.25321497
C       -0.69261800     3.17923978    -0.25321497
C       -2.80958100     1.64119778    -0.25292797
C       -3.23765700     0.32373778    -0.25303797
C       -2.42918200    -2.16498922    -0.25302597
C       -1.30841500    -2.97916822    -0.25327697
C        1.30841500    -2.97916822    -0.25327697
C        2.42918200    -2.16498922    -0.25302597
C        3.23765700     0.32373778    -0.25303797
C        2.80958100     1.64119778    -0.25292797
H        1.20851300     4.06642078    -0.61418797
H       -1.20851300     4.06642078    -0.61418797
H       -3.49401500     2.40602178    -0.61367197
H       -4.24094400     0.10729578    -0.61373997
H       -3.36816400    -2.57958822    -0.61350597
H       -1.41248600    -4.00024222    -0.61397997
H        1.41248600    -4.00024222    -0.61397997
H        3.36816400    -2.57958822    -0.61350597
H        4.24094400     0.10729578    -0.61373997
H        3.49401500     2.40602178    -0.61367197
--
0 1
C        0.70622800     0.97211978     4.25694803
C       -0.70622800     0.97211978     4.25694803
C       -1.14280400    -0.37137722     4.25681203
C        0.00000000    -1.20165922     4.25659503
C        1.14280400    -0.37137722     4.25681203
C        1.45779000     2.00650178     3.73413403
C       -1.45779000     2.00650178     3.73413403
C       -2.35873800    -0.76639722     3.73397203
C        0.00000000    -2.48004022     3.73366903
C        2.35873800    -0.76639722     3.73397203
C        0.69261800     3.17923978     3.38678503
C       -0.69261800     3.17923978     3.38678503
C       -2.80958100     1.64119778     3.38707203
C       -3.23765700     0.32373778     3.38696203
C       -2.42918200    -2.16498922     3.38697403
C       -1.30841500    -2.97916822     3.38672303
C        1.30841500    -2.97916822     3.38672303
C        2.42918200    -2.16498922     3.38697403
C        3.23765700     0.32373778     3.38696203
C        2.80958100     1.64119778     3.38707203
H        1.20851300     4.06642078     3.02581203
H       -1.20851300     4.06642078     3.02581203
H       -3.49401500     2.40602178     3.02632803
H       -4.24094400     0.10729578     3.02626003
H       -3.36816400    -2.57958822     3.02649403
H       -1.41248600    -4.00024222     3.02602003
H        1.41248600    -4.00024222     3.02602003
H        3.36816400    -2.57958822     3.02649403
H        4.24094400     0.10729578     3.02626003
H        3.49401500     2.40602178     3.02632803
units angstrom
""")

GEOS['%s-%s-dimer' % (dbse, 'dimer3_73')] = qcdb.Molecule("""
0 1
C        0.70622800     0.97211978     0.61694803
C       -0.70622800     0.97211978     0.61694803
C       -1.14280400    -0.37137722     0.61681203
C        0.00000000    -1.20165922     0.61659503
C        1.14280400    -0.37137722     0.61681203
C        1.45779000     2.00650178     0.09413403
C       -1.45779000     2.00650178     0.09413403
C       -2.35873800    -0.76639722     0.09397203
C        0.00000000    -2.48004022     0.09366903
C        2.35873800    -0.76639722     0.09397203
C        0.69261800     3.17923978    -0.25321497
C       -0.69261800     3.17923978    -0.25321497
C       -2.80958100     1.64119778    -0.25292797
C       -3.23765700     0.32373778    -0.25303797
C       -2.42918200    -2.16498922    -0.25302597
C       -1.30841500    -2.97916822    -0.25327697
C        1.30841500    -2.97916822    -0.25327697
C        2.42918200    -2.16498922    -0.25302597
C        3.23765700     0.32373778    -0.25303797
C        2.80958100     1.64119778    -0.25292797
H        1.20851300     4.06642078    -0.61418797
H       -1.20851300     4.06642078    -0.61418797
H       -3.49401500     2.40602178    -0.61367197
H       -4.24094400     0.10729578    -0.61373997
H       -3.36816400    -2.57958822    -0.61350597
H       -1.41248600    -4.00024222    -0.61397997
H        1.41248600    -4.00024222    -0.61397997
H        3.36816400    -2.57958822    -0.61350597
H        4.24094400     0.10729578    -0.61373997
H        3.49401500     2.40602178    -0.61367197
--
0 1
C        0.70622800     0.97211978     4.34694803
C       -0.70622800     0.97211978     4.34694803
C       -1.14280400    -0.37137722     4.34681203
C        0.00000000    -1.20165922     4.34659503
C        1.14280400    -0.37137722     4.34681203
C        1.45779000     2.00650178     3.82413403
C       -1.45779000     2.00650178     3.82413403
C       -2.35873800    -0.76639722     3.82397203
C        0.00000000    -2.48004022     3.82366903
C        2.35873800    -0.76639722     3.82397203
C        0.69261800     3.17923978     3.47678503
C       -0.69261800     3.17923978     3.47678503
C       -2.80958100     1.64119778     3.47707203
C       -3.23765700     0.32373778     3.47696203
C       -2.42918200    -2.16498922     3.47697403
C       -1.30841500    -2.97916822     3.47672303
C        1.30841500    -2.97916822     3.47672303
C        2.42918200    -2.16498922     3.47697403
C        3.23765700     0.32373778     3.47696203
C        2.80958100     1.64119778     3.47707203
H        1.20851300     4.06642078     3.11581203
H       -1.20851300     4.06642078     3.11581203
H       -3.49401500     2.40602178     3.11632803
H       -4.24094400     0.10729578     3.11626003
H       -3.36816400    -2.57958822     3.11649403
H       -1.41248600    -4.00024222     3.11602003
H        1.41248600    -4.00024222     3.11602003
H        3.36816400    -2.57958822     3.11649403
H        4.24094400     0.10729578     3.11626003
H        3.49401500     2.40602178     3.11632803
units angstrom
""")

GEOS['%s-%s-dimer' % (dbse, 'dimer3_74')] = qcdb.Molecule("""
0 1
C        0.70622800     0.97211978     0.61694803
C       -0.70622800     0.97211978     0.61694803
C       -1.14280400    -0.37137722     0.61681203
C        0.00000000    -1.20165922     0.61659503
C        1.14280400    -0.37137722     0.61681203
C        1.45779000     2.00650178     0.09413403
C       -1.45779000     2.00650178     0.09413403
C       -2.35873800    -0.76639722     0.09397203
C        0.00000000    -2.48004022     0.09366903
C        2.35873800    -0.76639722     0.09397203
C        0.69261800     3.17923978    -0.25321497
C       -0.69261800     3.17923978    -0.25321497
C       -2.80958100     1.64119778    -0.25292797
C       -3.23765700     0.32373778    -0.25303797
C       -2.42918200    -2.16498922    -0.25302597
C       -1.30841500    -2.97916822    -0.25327697
C        1.30841500    -2.97916822    -0.25327697
C        2.42918200    -2.16498922    -0.25302597
C        3.23765700     0.32373778    -0.25303797
C        2.80958100     1.64119778    -0.25292797
H        1.20851300     4.06642078    -0.61418797
H       -1.20851300     4.06642078    -0.61418797
H       -3.49401500     2.40602178    -0.61367197
H       -4.24094400     0.10729578    -0.61373997
H       -3.36816400    -2.57958822    -0.61350597
H       -1.41248600    -4.00024222    -0.61397997
H        1.41248600    -4.00024222    -0.61397997
H        3.36816400    -2.57958822    -0.61350597
H        4.24094400     0.10729578    -0.61373997
H        3.49401500     2.40602178    -0.61367197
--
0 1
C        0.70622800     0.97211978     4.35694803
C       -0.70622800     0.97211978     4.35694803
C       -1.14280400    -0.37137722     4.35681203
C        0.00000000    -1.20165922     4.35659503
C        1.14280400    -0.37137722     4.35681203
C        1.45779000     2.00650178     3.83413403
C       -1.45779000     2.00650178     3.83413403
C       -2.35873800    -0.76639722     3.83397203
C        0.00000000    -2.48004022     3.83366903
C        2.35873800    -0.76639722     3.83397203
C        0.69261800     3.17923978     3.48678503
C       -0.69261800     3.17923978     3.48678503
C       -2.80958100     1.64119778     3.48707203
C       -3.23765700     0.32373778     3.48696203
C       -2.42918200    -2.16498922     3.48697403
C       -1.30841500    -2.97916822     3.48672303
C        1.30841500    -2.97916822     3.48672303
C        2.42918200    -2.16498922     3.48697403
C        3.23765700     0.32373778     3.48696203
C        2.80958100     1.64119778     3.48707203
H        1.20851300     4.06642078     3.12581203
H       -1.20851300     4.06642078     3.12581203
H       -3.49401500     2.40602178     3.12632803
H       -4.24094400     0.10729578     3.12626003
H       -3.36816400    -2.57958822     3.12649403
H       -1.41248600    -4.00024222     3.12602003
H        1.41248600    -4.00024222     3.12602003
H        3.36816400    -2.57958822     3.12649403
H        4.24094400     0.10729578     3.12626003
H        3.49401500     2.40602178     3.12632803
units angstrom
""")

GEOS['%s-%s-dimer' % (dbse, 'dimer3_84')] = qcdb.Molecule("""
0 1
C        0.70622800     0.97211978     0.61694803
C       -0.70622800     0.97211978     0.61694803
C       -1.14280400    -0.37137722     0.61681203
C        0.00000000    -1.20165922     0.61659503
C        1.14280400    -0.37137722     0.61681203
C        1.45779000     2.00650178     0.09413403
C       -1.45779000     2.00650178     0.09413403
C       -2.35873800    -0.76639722     0.09397203
C        0.00000000    -2.48004022     0.09366903
C        2.35873800    -0.76639722     0.09397203
C        0.69261800     3.17923978    -0.25321497
C       -0.69261800     3.17923978    -0.25321497
C       -2.80958100     1.64119778    -0.25292797
C       -3.23765700     0.32373778    -0.25303797
C       -2.42918200    -2.16498922    -0.25302597
C       -1.30841500    -2.97916822    -0.25327697
C        1.30841500    -2.97916822    -0.25327697
C        2.42918200    -2.16498922    -0.25302597
C        3.23765700     0.32373778    -0.25303797
C        2.80958100     1.64119778    -0.25292797
H        1.20851300     4.06642078    -0.61418797
H       -1.20851300     4.06642078    -0.61418797
H       -3.49401500     2.40602178    -0.61367197
H       -4.24094400     0.10729578    -0.61373997
H       -3.36816400    -2.57958822    -0.61350597
H       -1.41248600    -4.00024222    -0.61397997
H        1.41248600    -4.00024222    -0.61397997
H        3.36816400    -2.57958822    -0.61350597
H        4.24094400     0.10729578    -0.61373997
H        3.49401500     2.40602178    -0.61367197
--
0 1
C        0.70622800     0.97211978     4.45694803
C       -0.70622800     0.97211978     4.45694803
C       -1.14280400    -0.37137722     4.45681203
C        0.00000000    -1.20165922     4.45659503
C        1.14280400    -0.37137722     4.45681203
C        1.45779000     2.00650178     3.93413403
C       -1.45779000     2.00650178     3.93413403
C       -2.35873800    -0.76639722     3.93397203
C        0.00000000    -2.48004022     3.93366903
C        2.35873800    -0.76639722     3.93397203
C        0.69261800     3.17923978     3.58678503
C       -0.69261800     3.17923978     3.58678503
C       -2.80958100     1.64119778     3.58707203
C       -3.23765700     0.32373778     3.58696203
C       -2.42918200    -2.16498922     3.58697403
C       -1.30841500    -2.97916822     3.58672303
C        1.30841500    -2.97916822     3.58672303
C        2.42918200    -2.16498922     3.58697403
C        3.23765700     0.32373778     3.58696203
C        2.80958100     1.64119778     3.58707203
H        1.20851300     4.06642078     3.22581203
H       -1.20851300     4.06642078     3.22581203
H       -3.49401500     2.40602178     3.22632803
H       -4.24094400     0.10729578     3.22626003
H       -3.36816400    -2.57958822     3.22649403
H       -1.41248600    -4.00024222     3.22602003
H        1.41248600    -4.00024222     3.22602003
H        3.36816400    -2.57958822     3.22649403
H        4.24094400     0.10729578     3.22626003
H        3.49401500     2.40602178     3.22632803
units angstrom
""")

# <<< Derived Geometry Strings >>>
for rxn in HRXN:
    GEOS['%s-%s-monoA-unCP' % (dbse, rxn)] = GEOS['%s-%s-dimer' % (dbse, rxn)].extract_fragments(1)
    GEOS['%s-%s-monoB-unCP' % (dbse, rxn)] = GEOS['%s-%s-dimer' % (dbse, rxn)].extract_fragments(2)
    GEOS['%s-%s-monoA-CP'   % (dbse, rxn)] = GEOS['%s-%s-dimer' % (dbse, rxn)].extract_fragments(1, 2)
    GEOS['%s-%s-monoB-CP'   % (dbse, rxn)] = GEOS['%s-%s-dimer' % (dbse, rxn)].extract_fragments(2, 1)

#########################################################################

# <<< Supplementary Quantum Chemical Results >>>
DATA = {}

DATA['NUCLEAR REPULSION ENERGY'] = {}
DATA['NUCLEAR REPULSION ENERGY']['CORE-dimer3_54-dimer'           ] =    4584.11459289
DATA['NUCLEAR REPULSION ENERGY']['CORE-dimer3_54-monoA-unCP'      ] =    1387.77369315
DATA['NUCLEAR REPULSION ENERGY']['CORE-dimer3_54-monoB-unCP'      ] =    1387.77369315
DATA['NUCLEAR REPULSION ENERGY']['CORE-dimer3_64-dimer'           ] =    4555.01239979
DATA['NUCLEAR REPULSION ENERGY']['CORE-dimer3_64-monoA-unCP'      ] =    1387.77369315
DATA['NUCLEAR REPULSION ENERGY']['CORE-dimer3_64-monoB-unCP'      ] =    1387.77369315
DATA['NUCLEAR REPULSION ENERGY']['CORE-dimer3_73-dimer'           ] =    4529.48976988
DATA['NUCLEAR REPULSION ENERGY']['CORE-dimer3_73-monoA-unCP'      ] =    1387.77369315
DATA['NUCLEAR REPULSION ENERGY']['CORE-dimer3_73-monoB-unCP'      ] =    1387.77369315
DATA['NUCLEAR REPULSION ENERGY']['CORE-dimer3_74-dimer'           ] =    4526.69216135
DATA['NUCLEAR REPULSION ENERGY']['CORE-dimer3_74-monoA-unCP'      ] =    1387.77369315
DATA['NUCLEAR REPULSION ENERGY']['CORE-dimer3_74-monoB-unCP'      ] =    1387.77369315
DATA['NUCLEAR REPULSION ENERGY']['CORE-dimer3_84-dimer'           ] =    4499.12706628
DATA['NUCLEAR REPULSION ENERGY']['CORE-dimer3_84-monoA-unCP'      ] =    1387.77369315
DATA['NUCLEAR REPULSION ENERGY']['CORE-dimer3_84-monoB-unCP'      ] =    1387.77369315
DATA['NUCLEAR REPULSION ENERGY']['CORE-dimer3_54-monoA-CP'        ] =    1387.77369315
DATA['NUCLEAR REPULSION ENERGY']['CORE-dimer3_54-monoB-CP'        ] =    1387.77369315
DATA['NUCLEAR REPULSION ENERGY']['CORE-dimer3_64-monoA-CP'        ] =    1387.77369315
DATA['NUCLEAR REPULSION ENERGY']['CORE-dimer3_64-monoB-CP'        ] =    1387.77369315
DATA['NUCLEAR REPULSION ENERGY']['CORE-dimer3_73-monoA-CP'        ] =    1387.77369315
DATA['NUCLEAR REPULSION ENERGY']['CORE-dimer3_73-monoB-CP'        ] =    1387.77369315
DATA['NUCLEAR REPULSION ENERGY']['CORE-dimer3_74-monoA-CP'        ] =    1387.77369315
DATA['NUCLEAR REPULSION ENERGY']['CORE-dimer3_74-monoB-CP'        ] =    1387.77369315
DATA['NUCLEAR REPULSION ENERGY']['CORE-dimer3_84-monoA-CP'        ] =    1387.77369315
DATA['NUCLEAR REPULSION ENERGY']['CORE-dimer3_84-monoB-CP'        ] =    1387.77369315
