"""Profiles across x = U e^{kappa_+ v} at v = 100, 150, 200 (Paper F, 'Behind the front'), from the snapshots prof2_{U,snap}.npy of prof2.py (B=3e-3, h_s=0.05, h_v=0.0125, not extrapolated).
Raychaudhuri: rho_v = sigma_v rho + S, S = 4 pi r c1(psi) phi_v^2  (rho=-r_v), i.e.  rho_v/rho = sigma_v + S/rho  at every point.  If rho(v) is independent of u this combination is independent of x."""
import os, sys, numpy as np
sys.path.insert(0,os.environ.get('QTG_CODE','..')); from qtg_lib import coef
U=np.load('prof2_U.npy'); snap=np.load('prof2_snap.npy'); kp=0.04896874
for k,vv in enumerate((100,150,200)):
    r,sg,rs,rv,sgs,sV,Ps,PV=snap[k]; W=np.exp(sg); y=-rs/W; rho=-rv; psi=(1+4*y*rho)/r**2
    c1=np.array([float(coef(1,1.0,p)[1]) for p in psi]); S=4*np.pi*r*c1*PV**2; x=U*np.exp(kp*vv)
    print('v=%d   (x = U e^{kappa_+ v})'%vv)
    print('     x        rho          phi_v        sigma_v     S/rho      rho_v/rho = sigma_v+S/rho     z=1-psi')
    last=-1
    for xx in (6,10,20,25,30,40,60,80,100,150,300,1000,3000,10000):
        i=int(np.argmin(abs(x-xx)))
        if i==last: continue
        last=i; print('  %7.0f  %.4e  %+.5e  %+.5f  %+.5f   %+.5f              %.3e'%(x[i],rho[i],PV[i],sV[i],S[i]/rho[i],sV[i]+S[i]/rho[i],1-psi[i]))
