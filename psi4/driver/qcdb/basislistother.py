#
# @BEGIN LICENSE
#
# Psi4: an open-source quantum chemistry software package
#
# Copyright (c) 2007-2017 The Psi4 Developers.
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

"""Module with commands building :py:class:`~basislist.BasisFamily` objects
for Pople and other non-Dunning orbital basis sets. Some
plausible fitting basis sets are supplied as defaults.

"""
from __future__ import absolute_import
from __future__ import print_function
from .basislist import *


def load_basfam_other():

    # Pople
    basis_sto3g = BasisFamily('STO-3G', zeta=1)
    basis_321g = BasisFamily('3-21G', zeta=1)

    basisfamily_list.append(basis_sto3g)
    basisfamily_list.append(basis_321g)

    basis_631g = BasisFamily('6-31G', zeta=2)
    basis_631g_d_ = BasisFamily('6-31G(d)', zeta=2)
    basis_631g_d_p_ = BasisFamily('6-31G(d,p)', zeta=2)
    basis_631gs = BasisFamily('6-31G*', '6-31g_d_', zeta=2)
    basis_631gss = BasisFamily('6-31G**', '6-31g_d_p_', zeta=2)
    basis_631pg = BasisFamily('6-31+G', zeta=2)
    basis_631pg_d_ = BasisFamily('6-31+G(d)', zeta=2)
    basis_631pg_d_p_ = BasisFamily('6-31+G(d,p)', zeta=2)
    basis_631pgs = BasisFamily('6-31+G*', '6-31pg_d_', zeta=2)
    basis_631pgss = BasisFamily('6-31+G**', '6-31pg_d_p_', zeta=2)
    basis_631ppg = BasisFamily('6-31++G', zeta=2)
    basis_631ppg_d_ = BasisFamily('6-31++G(d)', zeta=2)
    basis_631ppg_d_p_ = BasisFamily('6-31++G(d,p)', zeta=2)
    basis_631ppgs = BasisFamily('6-31++G*', '6-31ppg_d_', zeta=2)
    basis_631ppgss = BasisFamily('6-31++G**', '6-31ppg_d_p_', zeta=2)

    basisfamily_list.append(basis_631g)
    basisfamily_list.append(basis_631g_d_)
    basisfamily_list.append(basis_631g_d_p_)
    basisfamily_list.append(basis_631gs)
    basisfamily_list.append(basis_631gss)
    basisfamily_list.append(basis_631pg)
    basisfamily_list.append(basis_631pg_d_)
    basisfamily_list.append(basis_631pg_d_p_)
    basisfamily_list.append(basis_631pgs)
    basisfamily_list.append(basis_631pgss)
    basisfamily_list.append(basis_631ppg)
    basisfamily_list.append(basis_631ppg_d_)
    basisfamily_list.append(basis_631ppg_d_p_)
    basisfamily_list.append(basis_631ppgs)
    basisfamily_list.append(basis_631ppgss)

    basis_6311g = BasisFamily('6-311G', zeta=3)
    basis_6311g_d_ = BasisFamily('6-311G(d)', zeta=3)
    basis_6311g_d_p_ = BasisFamily('6-311G(d,p)', zeta=3)
    basis_6311gs = BasisFamily('6-311G*', '6-311g_d_', zeta=3)
    basis_6311gss = BasisFamily('6-311G**', '6-311g_d_p_', zeta=3)
    basis_6311g_2d_ = BasisFamily('6-311G(2d)', zeta=3)
    basis_6311g_2d_p_ = BasisFamily('6-311G(2d,p)', zeta=3)
    basis_6311g_2d_2p_ = BasisFamily('6-311G(2d,2p)', zeta=3)
    basis_6311g_2df_ = BasisFamily('6-311G(2df)', zeta=3)
    basis_6311g_2df_p_ = BasisFamily('6-311G(2df,p)', zeta=3)
    basis_6311g_2df_2p_ = BasisFamily('6-311G(2df,2p)', zeta=3)
    basis_6311g_2df_2pd_ = BasisFamily('6-311G(2df,2pd)', zeta=3)
    basis_6311g_3df_ = BasisFamily('6-311G(3df)', zeta=3)
    basis_6311g_3df_p_ = BasisFamily('6-311G(3df,p)', zeta=3)
    basis_6311g_3df_2p_ = BasisFamily('6-311G(3df,2p)', zeta=3)
    basis_6311g_3df_2pd_ = BasisFamily('6-311G(3df,2pd)', zeta=3)
    basis_6311g_3df_3pd_ = BasisFamily('6-311G(3df,3pd)', zeta=3)

    basisfamily_list.append(basis_6311g)
    basisfamily_list.append(basis_6311g_d_)
    basisfamily_list.append(basis_6311g_d_p_)
    basisfamily_list.append(basis_6311gs)
    basisfamily_list.append(basis_6311gss)
    basisfamily_list.append(basis_6311g_2d_)
    basisfamily_list.append(basis_6311g_2d_p_)
    basisfamily_list.append(basis_6311g_2d_2p_)
    basisfamily_list.append(basis_6311g_2df_)
    basisfamily_list.append(basis_6311g_2df_p_)
    basisfamily_list.append(basis_6311g_2df_2p_)
    basisfamily_list.append(basis_6311g_2df_2pd_)
    basisfamily_list.append(basis_6311g_3df_)
    basisfamily_list.append(basis_6311g_3df_p_)
    basisfamily_list.append(basis_6311g_3df_2p_)
    basisfamily_list.append(basis_6311g_3df_2pd_)
    basisfamily_list.append(basis_6311g_3df_3pd_)

    basis_6311pg = BasisFamily('6-311+G', zeta=3)
    basis_6311pg_d_ = BasisFamily('6-311+G(d)', zeta=3)
    basis_6311pg_d_p_ = BasisFamily('6-311+G(d,p)', zeta=3)
    basis_6311pgs = BasisFamily('6-311+G*', '6-311pg_d_', zeta=3)
    basis_6311pgss = BasisFamily('6-311+G**', '6-311pg_d_p_', zeta=3)
    basis_6311pg_2d_ = BasisFamily('6-311+G(2d)', zeta=3)
    basis_6311pg_2d_p_ = BasisFamily('6-311+G(2d,p)', zeta=3)
    basis_6311pg_2d_2p_ = BasisFamily('6-311+G(2d,2p)', zeta=3)
    basis_6311pg_2df_ = BasisFamily('6-311+G(2df)', zeta=3)
    basis_6311pg_2df_p_ = BasisFamily('6-311+G(2df,p)', zeta=3)
    basis_6311pg_2df_2p_ = BasisFamily('6-311+G(2df,2p)', zeta=3)
    basis_6311pg_2df_2pd_ = BasisFamily('6-311+G(2df,2pd)', zeta=3)
    basis_6311pg_3df_ = BasisFamily('6-311+G(3df)', zeta=3)
    basis_6311pg_3df_p_ = BasisFamily('6-311+G(3df,p)', zeta=3)
    basis_6311pg_3df_2p_ = BasisFamily('6-311+G(3df,2p)', zeta=3)
    basis_6311pg_3df_2pd_ = BasisFamily('6-311+G(3df,2pd)', zeta=3)
    basis_6311pg_3df_3pd_ = BasisFamily('6-311+G(3df,3pd)', zeta=3)

    basisfamily_list.append(basis_6311pg)
    basisfamily_list.append(basis_6311pg_d_)
    basisfamily_list.append(basis_6311pg_d_p_)
    basisfamily_list.append(basis_6311pgs)
    basisfamily_list.append(basis_6311pgss)
    basisfamily_list.append(basis_6311pg_2d_)
    basisfamily_list.append(basis_6311pg_2d_p_)
    basisfamily_list.append(basis_6311pg_2d_2p_)
    basisfamily_list.append(basis_6311pg_2df_)
    basisfamily_list.append(basis_6311pg_2df_p_)
    basisfamily_list.append(basis_6311pg_2df_2p_)
    basisfamily_list.append(basis_6311pg_2df_2pd_)
    basisfamily_list.append(basis_6311pg_3df_)
    basisfamily_list.append(basis_6311pg_3df_p_)
    basisfamily_list.append(basis_6311pg_3df_2p_)
    basisfamily_list.append(basis_6311pg_3df_2pd_)
    basisfamily_list.append(basis_6311pg_3df_3pd_)

    basis_6311ppg = BasisFamily('6-311++G', zeta=3)
    basis_6311ppg_d_ = BasisFamily('6-311++G(d)', zeta=3)
    basis_6311ppg_d_p_ = BasisFamily('6-311++G(d,p)', zeta=3)
    basis_6311ppgs = BasisFamily('6-311++G*', '6-311ppg_d_', zeta=3)
    basis_6311ppgss = BasisFamily('6-311++G**', '6-311ppg_d_p_', zeta=3)
    basis_6311ppg_2d_ = BasisFamily('6-311++G(2d)', zeta=3)
    basis_6311ppg_2d_p_ = BasisFamily('6-311++G(2d,p)', zeta=3)
    basis_6311ppg_2d_2p_ = BasisFamily('6-311++G(2d,2p)', zeta=3)
    basis_6311ppg_2df_ = BasisFamily('6-311++G(2df)', zeta=3)
    basis_6311ppg_2df_p_ = BasisFamily('6-311++G(2df,p)', zeta=3)
    basis_6311ppg_2df_2p_ = BasisFamily('6-311++G(2df,2p)', zeta=3)
    basis_6311ppg_2df_2pd_ = BasisFamily('6-311++G(2df,2pd)', zeta=3)
    basis_6311ppg_3df_ = BasisFamily('6-311++G(3df)', zeta=3)
    basis_6311ppg_3df_p_ = BasisFamily('6-311++G(3df,p)', zeta=3)
    basis_6311ppg_3df_2p_ = BasisFamily('6-311++G(3df,2p)', zeta=3)
    basis_6311ppg_3df_2pd_ = BasisFamily('6-311++G(3df,2pd)', zeta=3)
    basis_6311ppg_3df_3pd_ = BasisFamily('6-311++G(3df,3pd)', zeta=3)

    basisfamily_list.append(basis_6311ppg)
    basisfamily_list.append(basis_6311ppg_d_)
    basisfamily_list.append(basis_6311ppg_d_p_)
    basisfamily_list.append(basis_6311ppgs)
    basisfamily_list.append(basis_6311ppgss)
    basisfamily_list.append(basis_6311ppg_2d_)
    basisfamily_list.append(basis_6311ppg_2d_p_)
    basisfamily_list.append(basis_6311ppg_2d_2p_)
    basisfamily_list.append(basis_6311ppg_2df_)
    basisfamily_list.append(basis_6311ppg_2df_p_)
    basisfamily_list.append(basis_6311ppg_2df_2p_)
    basisfamily_list.append(basis_6311ppg_2df_2pd_)
    basisfamily_list.append(basis_6311ppg_3df_)
    basisfamily_list.append(basis_6311ppg_3df_p_)
    basisfamily_list.append(basis_6311ppg_3df_2p_)
    basisfamily_list.append(basis_6311ppg_3df_2pd_)
    basisfamily_list.append(basis_6311ppg_3df_3pd_)

    # Ahlrichs
    basis_def2sv_p_ = BasisFamily('def2-SV(P)', zeta=2)
    basis_def2svp = BasisFamily('def2-SVP', zeta=2)
    basis_def2svpd = BasisFamily('def2-SVPD', zeta=2)
    basis_def2tzvp = BasisFamily('def2-TZVP', zeta=3)
    basis_def2tzvpd = BasisFamily('def2-TZVPD', zeta=3)
    basis_def2tzvpp = BasisFamily('def2-TZVPP', zeta=3)
    basis_def2tzvppd = BasisFamily('def2-TZVPPD', zeta=3)
    basis_def2qzvp = BasisFamily('def2-QZVP', zeta=4)
    basis_def2qzvpd = BasisFamily('def2-QZVPD', zeta=4)
    basis_def2qzvpp = BasisFamily('def2-QZVPP', zeta=4)
    basis_def2qzvppd = BasisFamily('def2-QZVPPD', zeta=4)

    basis_def2sv_p_.add_jfit('def2-SV(P)-JFIT')
    basis_def2svp.add_jfit('def2-SVP-JFIT')
    basis_def2svpd.add_jfit('def2-SVP-JFIT')
    basis_def2tzvp.add_jfit('def2-TZVP-JFIT')
    basis_def2tzvpd.add_jfit('def2-TZVP-JFIT')
    basis_def2tzvpp.add_jfit('def2-TZVPP-JFIT')
    basis_def2tzvppd.add_jfit('def2-TZVPP-JFIT')
    basis_def2qzvp.add_jfit('def2-QZVP-JFIT')
    basis_def2qzvpd.add_jfit('def2-QZVP-JFIT')
    basis_def2qzvpp.add_jfit('def2-QZVPP-JFIT')
    basis_def2qzvppd.add_jfit('def2-QZVPP-JFIT')

    basis_def2sv_p_.add_jkfit('def2-SV(P)-JKFIT')
    basis_def2svp.add_jkfit('def2-SVP-JKFIT')
    basis_def2svpd.add_jkfit('def2-SVP-JKFIT')
    basis_def2tzvp.add_jkfit('def2-TZVP-JKFIT')
    basis_def2tzvpd.add_jkfit('def2-TZVP-JKFIT')
    basis_def2tzvpp.add_jkfit('def2-TZVPP-JKFIT')
    basis_def2tzvppd.add_jkfit('def2-TZVPP-JKFIT')
    basis_def2qzvp.add_jkfit('def2-QZVP-JKFIT')
    basis_def2qzvpd.add_jkfit('def2-QZVP-JKFIT')
    basis_def2qzvpp.add_jkfit('def2-QZVPP-JKFIT')
    basis_def2qzvppd.add_jkfit('def2-QZVPP-JKFIT')

    basis_def2sv_p_.add_rifit('def2-SV(P)-RI')
    basis_def2svp.add_rifit('def2-SVP-RI')
    basis_def2svpd.add_rifit('def2-SVPD-RI')
    basis_def2tzvp.add_rifit('def2-TZVP-RI')
    basis_def2tzvpd.add_rifit('def2-TZVPD-RI')
    basis_def2tzvpp.add_rifit('def2-TZVPP-RI')
    basis_def2tzvppd.add_rifit('def2-TZVPPD-RI')
    basis_def2qzvp.add_rifit('def2-QZVP-RI')
    basis_def2qzvpp.add_rifit('def2-QZVPP-RI')
    basis_def2qzvppd.add_rifit('def2-QZVPPD-RI')

    basisfamily_list.append(basis_def2sv_p_)
    basisfamily_list.append(basis_def2svp)
    basisfamily_list.append(basis_def2svpd)
    basisfamily_list.append(basis_def2tzvp)
    basisfamily_list.append(basis_def2tzvpd)
    basisfamily_list.append(basis_def2tzvpp)
    basisfamily_list.append(basis_def2tzvppd)
    basisfamily_list.append(basis_def2qzvp)
    basisfamily_list.append(basis_def2qzvpd)
    basisfamily_list.append(basis_def2qzvpp)
    basisfamily_list.append(basis_def2qzvppd)

    # Jensen
    basis_augpcseg0 = BasisFamily('aug-pcseg-0', zeta=1)
    basis_augpcseg1 = BasisFamily('aug-pcseg-1', zeta=2)
    basis_augpcseg2 = BasisFamily('aug-pcseg-2', zeta=3)
    basis_augpcseg3 = BasisFamily('aug-pcseg-3', zeta=4)
    basis_augpcseg4 = BasisFamily('aug-pcseg-4', zeta=5)
    basis_augpcsseg0 = BasisFamily('aug-pcSseg-0', zeta=1)
    basis_augpcsseg1 = BasisFamily('aug-pcSseg-1', zeta=2)
    basis_augpcsseg2 = BasisFamily('aug-pcSseg-2', zeta=3)
    basis_augpcsseg3 = BasisFamily('aug-pcSseg-3', zeta=4)
    basis_augpcsseg4 = BasisFamily('aug-pcSseg-4', zeta=5)
    basis_pcseg0 = BasisFamily('pcseg-0', zeta=1)
    basis_pcseg1 = BasisFamily('pcseg-1', zeta=2)
    basis_pcseg2 = BasisFamily('pcseg-2', zeta=3)
    basis_pcseg3 = BasisFamily('pcseg-3', zeta=4)
    basis_pcseg4 = BasisFamily('pcseg-4', zeta=5)
    basis_pcsseg0 = BasisFamily('pcSseg-0', zeta=1)
    basis_pcsseg1 = BasisFamily('pcSseg-1', zeta=2)
    basis_pcsseg2 = BasisFamily('pcSseg-2', zeta=3)
    basis_pcsseg3 = BasisFamily('pcSseg-3', zeta=4)
    basis_pcsseg4 = BasisFamily('pcSseg-4', zeta=5)

    # Here lie practical (non-validated) fitting bases for
    # Jensen orbital basis sets

    basis_augpcseg0.add_jkfit('def2-SV(P)-JKFIT')
    basis_augpcseg1.add_jkfit('def2-SVP-JKFIT')
    basis_augpcseg2.add_jkfit('def2-TZVPP-JKFIT')
    basis_augpcseg3.add_jkfit('def2-QZVPP-JKFIT')
    basis_augpcseg4.add_jkfit('aug-cc-pV5Z-JKFIT')
    basis_augpcsseg0.add_jkfit('def2-SV(P)-JKFIT')
    basis_augpcsseg1.add_jkfit('def2-SVP-JKFIT')
    basis_augpcsseg2.add_jkfit('def2-TZVPP-JKFIT')
    basis_augpcsseg3.add_jkfit('def2-QZVPP-JKFIT')
    basis_augpcsseg4.add_jkfit('aug-cc-pV5Z-JKFIT')
    basis_pcseg0.add_jkfit('def2-SV(P)-JKFIT')
    basis_pcseg1.add_jkfit('def2-SVP-JKFIT')
    basis_pcseg2.add_jkfit('def2-TZVPP-JKFIT')
    basis_pcseg3.add_jkfit('def2-QZVPP-JKFIT')
    basis_pcseg4.add_jkfit('cc-pV5Z-JKFIT')
    basis_pcsseg0.add_jkfit('def2-SV(P)-JKFIT')
    basis_pcsseg1.add_jkfit('def2-SVP-JKFIT')
    basis_pcsseg2.add_jkfit('def2-TZVPP-JKFIT')
    basis_pcsseg3.add_jkfit('def2-QZVPP-JKFIT')
    basis_pcsseg4.add_jkfit('cc-pV5Z-JKFIT')

    basis_augpcseg0.add_rifit('def2-SV(P)-RI')
    basis_augpcseg1.add_rifit('def2-SVPD-RI')
    basis_augpcseg2.add_rifit('def2-TZVPPD-RI')
    basis_augpcseg3.add_rifit('def2-QZVPPD-RI')
    basis_augpcseg4.add_rifit('aug-cc-pV5Z-RI')
    basis_augpcsseg0.add_rifit('def2-SV(P)-RI')
    basis_augpcsseg1.add_rifit('def2-SVPD-RI')
    basis_augpcsseg2.add_rifit('def2-TZVPPD-RI')
    basis_augpcsseg3.add_rifit('def2-QZVPPD-RI')
    basis_augpcsseg4.add_rifit('aug-cc-pwCV5Z-RI')
    basis_pcseg0.add_rifit('def2-SV(P)-RI')
    basis_pcseg1.add_rifit('def2-SVP-RI')
    basis_pcseg2.add_rifit('def2-TZVPP-RI')
    basis_pcseg3.add_rifit('def2-QZVPP-RI')
    basis_pcseg4.add_rifit('cc-pV5Z-RI')
    basis_pcsseg0.add_rifit('def2-SV(P)-RI')
    basis_pcsseg1.add_rifit('def2-SVP-RI')
    basis_pcsseg2.add_rifit('def2-TZVPP-RI')
    basis_pcsseg3.add_rifit('def2-QZVPP-RI')
    basis_pcsseg4.add_rifit('cc-pwCV5Z-RI')

    basisfamily_list.append(basis_augpcseg0)
    basisfamily_list.append(basis_augpcseg1)
    basisfamily_list.append(basis_augpcseg2)
    basisfamily_list.append(basis_augpcseg3)
    basisfamily_list.append(basis_augpcseg4)
    basisfamily_list.append(basis_augpcsseg0)
    basisfamily_list.append(basis_augpcsseg1)
    basisfamily_list.append(basis_augpcsseg2)
    basisfamily_list.append(basis_augpcsseg3)
    basisfamily_list.append(basis_augpcsseg4)
    basisfamily_list.append(basis_pcseg0)
    basisfamily_list.append(basis_pcseg1)
    basisfamily_list.append(basis_pcseg2)
    basisfamily_list.append(basis_pcseg3)
    basisfamily_list.append(basis_pcseg4)
    basisfamily_list.append(basis_pcsseg0)
    basisfamily_list.append(basis_pcsseg1)
    basisfamily_list.append(basis_pcsseg2)
    basisfamily_list.append(basis_pcsseg3)
    basisfamily_list.append(basis_pcsseg4)

    # Others
    basis_dz = BasisFamily('DZ')
    basis_dzp = BasisFamily('DZP')
    basis_dzvp = BasisFamily('DZVP')
    basis_psi3dzp = BasisFamily('psi3-DZP')
    basis_psi3tz2p = BasisFamily('psi3-TZ2P')
    basis_psi3tz2pf = BasisFamily('psi3-TZ2PF')
    basis_sadlejlpoldl = BasisFamily('sadlej-lpol-dl')
    basis_sadlejlpolds = BasisFamily('sadlej-lpol-ds')
    basis_sadlejlpolfl = BasisFamily('sadlej-lpol-fl')
    basis_sadlejlpolfs = BasisFamily('sadlej-lpol-fs')

    basisfamily_list.append(basis_dz)
    basisfamily_list.append(basis_dzp)
    basisfamily_list.append(basis_dzvp)
    basisfamily_list.append(basis_psi3dzp)
    basisfamily_list.append(basis_psi3tz2p)
    basisfamily_list.append(basis_psi3tz2pf)
    basisfamily_list.append(basis_sadlejlpoldl)
    basisfamily_list.append(basis_sadlejlpolds)
    basisfamily_list.append(basis_sadlejlpolfl)
    basisfamily_list.append(basis_sadlejlpolfs)

    # Here lie practical (non-validated) fitting bases for
    # Pople orbital basis sets

    basis_sto3g.add_jkfit('def2-SVP-JKFIT')
    basis_sto3g.add_rifit('def2-SVP-RIFIT')
    basis_321g.add_jkfit('def2-SVP-JKFIT')
    basis_321g.add_rifit('def2-SVP-RIFIT')

    basis_631g.add_jkfit('cc-pvdz-jkfit')
    basis_631g_d_.add_jkfit('cc-pvdz-jkfit')
    basis_631g_d_p_.add_jkfit('cc-pvdz-jkfit')
    basis_631gs.add_jkfit('cc-pvdz-jkfit')
    basis_631gss.add_jkfit('cc-pvdz-jkfit')
    basis_631g.add_rifit('cc-pvdz-ri')
    basis_631g_d_.add_rifit('cc-pvdz-ri')
    basis_631g_d_p_.add_rifit('cc-pvdz-ri')
    basis_631gs.add_rifit('cc-pvdz-ri')
    basis_631gss.add_rifit('cc-pvdz-ri')

    basis_631pg.add_jkfit('heavy-aug-cc-pvdz-jkfit')
    basis_631pg_d_.add_jkfit('heavy-aug-cc-pvdz-jkfit')
    basis_631pg_d_p_.add_jkfit('heavy-aug-cc-pvdz-jkfit')
    basis_631pgs.add_jkfit('heavy-aug-cc-pvdz-jkfit')
    basis_631pgss.add_jkfit('heavy-aug-cc-pvdz-jkfit')
    basis_631pg.add_rifit('heavy-aug-cc-pvdz-ri')
    basis_631pg_d_.add_rifit('heavy-aug-cc-pvdz-ri')
    basis_631pg_d_p_.add_rifit('heavy-aug-cc-pvdz-ri')
    basis_631pgs.add_rifit('heavy-aug-cc-pvdz-ri')
    basis_631pgss.add_rifit('heavy-aug-cc-pvdz-ri')

    basis_631ppg.add_jkfit('aug-cc-pvdz-jkfit')
    basis_631ppg_d_.add_jkfit('aug-cc-pvdz-jkfit')
    basis_631ppg_d_p_.add_jkfit('aug-cc-pvdz-jkfit')
    basis_631ppgs.add_jkfit('aug-cc-pvdz-jkfit')
    basis_631ppgss.add_jkfit('aug-cc-pvdz-jkfit')
    basis_631ppg.add_rifit('aug-cc-pvdz-ri')
    basis_631ppg_d_.add_rifit('aug-cc-pvdz-ri')
    basis_631ppg_d_p_.add_rifit('aug-cc-pvdz-ri')
    basis_631ppgs.add_rifit('aug-cc-pvdz-ri')
    basis_631ppgss.add_rifit('aug-cc-pvdz-ri')

    basis_6311g.add_jkfit('cc-pvtz-jkfit')
    basis_6311g_d_.add_jkfit('cc-pvtz-jkfit')
    basis_6311g_d_p_.add_jkfit('cc-pvtz-jkfit')
    basis_6311gs.add_jkfit('cc-pvtz-jkfit')
    basis_6311gss.add_jkfit('cc-pvtz-jkfit')
    basis_6311g_2d_.add_jkfit('cc-pvtz-jkfit')
    basis_6311g_2d_p_.add_jkfit('cc-pvtz-jkfit')
    basis_6311g_2d_2p_.add_jkfit('cc-pvtz-jkfit')
    basis_6311g_2df_.add_jkfit('cc-pvtz-jkfit')
    basis_6311g_2df_p_.add_jkfit('cc-pvtz-jkfit')
    basis_6311g_2df_2p_.add_jkfit('cc-pvtz-jkfit')
    basis_6311g_2df_2pd_.add_jkfit('cc-pvtz-jkfit')
    basis_6311g_3df_.add_jkfit('cc-pvtz-jkfit')
    basis_6311g_3df_p_.add_jkfit('cc-pvtz-jkfit')
    basis_6311g_3df_2p_.add_jkfit('cc-pvtz-jkfit')
    basis_6311g_3df_2pd_.add_jkfit('cc-pvtz-jkfit')
    basis_6311g_3df_3pd_.add_jkfit('cc-pvtz-jkfit')

    basis_6311g.add_rifit('cc-pvtz-ri')
    basis_6311g_d_.add_rifit('cc-pvtz-ri')
    basis_6311g_d_p_.add_rifit('cc-pvtz-ri')
    basis_6311gs.add_rifit('cc-pvtz-ri')
    basis_6311gss.add_rifit('cc-pvtz-ri')
    basis_6311g_2d_.add_rifit('cc-pvtz-ri')
    basis_6311g_2d_p_.add_rifit('cc-pvtz-ri')
    basis_6311g_2d_2p_.add_rifit('cc-pvtz-ri')
    basis_6311g_2df_.add_rifit('cc-pvtz-ri')
    basis_6311g_2df_p_.add_rifit('cc-pvtz-ri')
    basis_6311g_2df_2p_.add_rifit('cc-pvtz-ri')
    basis_6311g_2df_2pd_.add_rifit('cc-pvtz-ri')
    basis_6311g_3df_.add_rifit('cc-pvtz-ri')
    basis_6311g_3df_p_.add_rifit('cc-pvtz-ri')
    basis_6311g_3df_2p_.add_rifit('cc-pvtz-ri')
    basis_6311g_3df_2pd_.add_rifit('cc-pvtz-ri')
    basis_6311g_3df_3pd_.add_rifit('cc-pvtz-ri')

    basis_6311pg.add_jkfit('heavy-aug-cc-pvtz-jkfit')
    basis_6311pg_d_.add_jkfit('heavy-aug-cc-pvtz-jkfit')
    basis_6311pg_d_p_.add_jkfit('heavy-aug-cc-pvtz-jkfit')
    basis_6311pgs.add_jkfit('heavy-aug-cc-pvtz-jkfit')
    basis_6311pgss.add_jkfit('heavy-aug-cc-pvtz-jkfit')
    basis_6311pg_2d_.add_jkfit('heavy-aug-cc-pvtz-jkfit')
    basis_6311pg_2d_p_.add_jkfit('heavy-aug-cc-pvtz-jkfit')
    basis_6311pg_2d_2p_.add_jkfit('heavy-aug-cc-pvtz-jkfit')
    basis_6311pg_2df_.add_jkfit('heavy-aug-cc-pvtz-jkfit')
    basis_6311pg_2df_p_.add_jkfit('heavy-aug-cc-pvtz-jkfit')
    basis_6311pg_2df_2p_.add_jkfit('heavy-aug-cc-pvtz-jkfit')
    basis_6311pg_2df_2pd_.add_jkfit('heavy-aug-cc-pvtz-jkfit')
    basis_6311pg_3df_.add_jkfit('heavy-aug-cc-pvtz-jkfit')
    basis_6311pg_3df_p_.add_jkfit('heavy-aug-cc-pvtz-jkfit')
    basis_6311pg_3df_2p_.add_jkfit('heavy-aug-cc-pvtz-jkfit')
    basis_6311pg_3df_2pd_.add_jkfit('heavy-aug-cc-pvtz-jkfit')
    basis_6311pg_3df_3pd_.add_jkfit('heavy-aug-cc-pvtz-jkfit')

    basis_6311pg.add_rifit('heavy-aug-cc-pvtz-ri')
    basis_6311pg_d_.add_rifit('heavy-aug-cc-pvtz-ri')
    basis_6311pg_d_p_.add_rifit('heavy-aug-cc-pvtz-ri')
    basis_6311pgs.add_rifit('heavy-aug-cc-pvtz-ri')
    basis_6311pgss.add_rifit('heavy-aug-cc-pvtz-ri')
    basis_6311pg_2d_.add_rifit('heavy-aug-cc-pvtz-ri')
    basis_6311pg_2d_p_.add_rifit('heavy-aug-cc-pvtz-ri')
    basis_6311pg_2d_2p_.add_rifit('heavy-aug-cc-pvtz-ri')
    basis_6311pg_2df_.add_rifit('heavy-aug-cc-pvtz-ri')
    basis_6311pg_2df_p_.add_rifit('heavy-aug-cc-pvtz-ri')
    basis_6311pg_2df_2p_.add_rifit('heavy-aug-cc-pvtz-ri')
    basis_6311pg_2df_2pd_.add_rifit('heavy-aug-cc-pvtz-ri')
    basis_6311pg_3df_.add_rifit('heavy-aug-cc-pvtz-ri')
    basis_6311pg_3df_p_.add_rifit('heavy-aug-cc-pvtz-ri')
    basis_6311pg_3df_2p_.add_rifit('heavy-aug-cc-pvtz-ri')
    basis_6311pg_3df_2pd_.add_rifit('heavy-aug-cc-pvtz-ri')
    basis_6311pg_3df_3pd_.add_rifit('heavy-aug-cc-pvtz-ri')

    basis_6311ppg.add_jkfit('aug-cc-pvtz-jkfit')
    basis_6311ppg_d_.add_jkfit('aug-cc-pvtz-jkfit')
    basis_6311ppg_d_p_.add_jkfit('aug-cc-pvtz-jkfit')
    basis_6311ppgs.add_jkfit('aug-cc-pvtz-jkfit')
    basis_6311ppgss.add_jkfit('aug-cc-pvtz-jkfit')
    basis_6311ppg_2d_.add_jkfit('aug-cc-pvtz-jkfit')
    basis_6311ppg_2d_p_.add_jkfit('aug-cc-pvtz-jkfit')
    basis_6311ppg_2d_2p_.add_jkfit('aug-cc-pvtz-jkfit')
    basis_6311ppg_2df_.add_jkfit('aug-cc-pvtz-jkfit')
    basis_6311ppg_2df_p_.add_jkfit('aug-cc-pvtz-jkfit')
    basis_6311ppg_2df_2p_.add_jkfit('aug-cc-pvtz-jkfit')
    basis_6311ppg_2df_2pd_.add_jkfit('aug-cc-pvtz-jkfit')
    basis_6311ppg_3df_.add_jkfit('aug-cc-pvtz-jkfit')
    basis_6311ppg_3df_p_.add_jkfit('aug-cc-pvtz-jkfit')
    basis_6311ppg_3df_2p_.add_jkfit('aug-cc-pvtz-jkfit')
    basis_6311ppg_3df_2pd_.add_jkfit('aug-cc-pvtz-jkfit')
    basis_6311ppg_3df_3pd_.add_jkfit('aug-cc-pvtz-jkfit')

    basis_6311ppg.add_rifit('aug-cc-pvtz-ri')
    basis_6311ppg_d_.add_rifit('aug-cc-pvtz-ri')
    basis_6311ppg_d_p_.add_rifit('aug-cc-pvtz-ri')
    basis_6311ppgs.add_rifit('aug-cc-pvtz-ri')
    basis_6311ppgss.add_rifit('aug-cc-pvtz-ri')
    basis_6311ppg_2d_.add_rifit('aug-cc-pvtz-ri')
    basis_6311ppg_2d_p_.add_rifit('aug-cc-pvtz-ri')
    basis_6311ppg_2d_2p_.add_rifit('aug-cc-pvtz-ri')
    basis_6311ppg_2df_.add_rifit('aug-cc-pvtz-ri')
    basis_6311ppg_2df_p_.add_rifit('aug-cc-pvtz-ri')
    basis_6311ppg_2df_2p_.add_rifit('aug-cc-pvtz-ri')
    basis_6311ppg_2df_2pd_.add_rifit('aug-cc-pvtz-ri')
    basis_6311ppg_3df_.add_rifit('aug-cc-pvtz-ri')
    basis_6311ppg_3df_p_.add_rifit('aug-cc-pvtz-ri')
    basis_6311ppg_3df_2p_.add_rifit('aug-cc-pvtz-ri')
    basis_6311ppg_3df_2pd_.add_rifit('aug-cc-pvtz-ri')
    basis_6311ppg_3df_3pd_.add_rifit('aug-cc-pvtz-ri')
