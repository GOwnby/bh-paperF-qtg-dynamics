"""Mass taken up by the horizon after the start of stage L (row v1): dm = 4 pi r_+^2 Int (d phi_H/dt)^2 dt, from the stage-L horizon-column tables
(Einstein-type flux 4 pi r^2 T_vv with Killing time t; the Hayward factor y -> 1/2 on the horizon is of order 1).  usage: linbound.py sp/*.npz"""
import sys,numpy as np
print('%-26s %8s %9s %12s %12s'%('table','m_f','r_+','dm_H','dm_H/m_f'))
for fn in sys.argv[1:]:
    d=np.load(fn)
    if 'phiH' not in d.files: continue
    t=d['t']; f=d['phiH']; mf=float(d['mf']) if 'mf' in d.files else float(d['mt'])
    rp=float(d['rp']) if 'rp' in d.files else 2*mf
    ft=np.gradient(f,t); dm=4*np.pi*rp**2*np.trapezoid(ft**2,t)
    print('%-26s %8.3f %9.3f %12.3e %12.3e'%(fn.split('/')[-1],mf,rp,dm,dm/mf))
