"""Weak-limit analytics for 1-F = Q_abs/Q_0 (Paper F, Eq. qabs): linearise the Vaidya-like horizon about the final hole,
 dr_H/dv = f(r_H, m(v))/2,  r_H = 2 m_f + delta :  delta' = kappa (delta + 2 (m_f - m(v))),  kappa = 1/(4 m_f),  delta(v1)=0,
so  rdot_H = kappa delta + 2 kappa (m_f - m(v)),  Q_abs = -2 int psi rdot_H dv  (psi = r phi on u0, eikonal),  Q_0 = -int psi f dv  (exact on u0).
Printed: the measured 1-F_abs (log), the linearised estimate, the 'thin pulse' estimate int psi (m_f-m) dv /(m_f int psi f dv) and the
leading closed form  Delta m /(2 m_f <f>_psi).   usage: weak_limit.py PULSE_A PULSE_B PULSE_V1 tables..."""
import sys,os,numpy as np
os.environ['PULSE_A'],os.environ['PULSE_B'],os.environ['PULSE_V1']=sys.argv[1:4]
from strong import *
Fabs={}
for ln in open('sp/horizon_ray.log' if os.path.exists('sp/horizon_ray.log') else 'horizon_ray.log'):
    t=ln.split()
    if len(t)>=12 and t[0].endswith('.npz') and 'invalid' not in ln:
        try: Fabs[t[0]]=float(t[9])
        except ValueError: pass
print('%-22s %5s %5s %9s | %9s %9s %9s %9s | %6s %6s'%('table','m0','m_f','1-F_abs','lin','thin','closed','data(f)','<f>','dm/mf'))
for fn in sys.argv[4:]:
    d=np.load(fn); model=int(d['model']); m0=float(d['m0']); mt=float(d['mt']); A=float(d['A']); mf=float(d['mf']); g=geom(m0,mt); s=g['s']; hN=0.1*s
    u,v,row0,col0,ph=rays(model,L2,g['u0'],g['uend'],g['v0'],g['v1'],hN,hN,A,g['va'],g['vb'],m0=m0)
    rc=np.asarray(col0[0]); pv=np.asarray(col0[7]); phi=np.concatenate([[0],np.cumsum(0.5*(pv[1:]+pv[:-1])*np.diff(v))]); psi=rc*phi
    mv=np.array([ms_mass(model,L2,rc[i],np.asarray(col0[1])[i],np.asarray(col0[2])[i],np.asarray(col0[3])[i]) for i in range(len(v))])
    kap=1/(4*mf); n=len(v); delta=np.zeros(n)
    for i in range(n-1,0,-1):                      # backwards from delta(v1)=0 (trapezoid, implicit-explicit)
        h=v[i]-v[i-1]; a=kap*(delta[i]+2*(mf-mv[i])); b0=2*kap*(mf-mv[i-1])
        delta[i-1]=(delta[i]-h*0.5*a-h*0.5*b0)/(1+0.5*h*kap)*1.0 if False else (delta[i]-0.5*h*(a+b0))/(1+0.5*h*kap)
    rdot=kap*delta+2*kap*(mf-mv)
    Q0=float(d['Q']); Qabs=-2*np.trapezoid(psi*rdot,v)
    # 'f' on u0 from the data: f = 2 r_v (r_v = f/2 on the ingoing->outgoing u0 ray)
    f=2*np.asarray(col0[3])
    Q0d=-np.trapezoid(psi*f,v)
    thin=np.trapezoid(psi*(mf-mv),v)/(mf*np.trapezoid(psi*f,v))
    fbar=np.trapezoid(psi*f,v)/np.trapezoid(psi,v); dm=mf-m0
    closed=dm/(2*mf*fbar)
    base=os.path.basename(fn)
    print('%-22s %5.2f %5.2f %9.4f | %9.4f %9.4f %9.4f %9.4f | %6.3f %6.4f'%(base[:22],m0,mf,1-Fabs.get(base,np.nan),Qabs/Q0,thin,closed,Q0d/Q0,fbar,dm/mf))
