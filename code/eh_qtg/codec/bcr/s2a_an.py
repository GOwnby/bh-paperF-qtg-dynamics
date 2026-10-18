"""Stage 2a: strong-field dispersing data (no horizon).  Test of the exact (all-order) form of the Bondi-mass-weighted tail law
   C(eps) = -8 Int M_B(u) a(u) du,   a = (r phi)|scri,  M_B = Bondi mass,   phi(t, r fixed) -> C t^-3
using the full nonlinear run at each eps: M_B(u) and a(u) from m(t,R_obs), r phi(t,R_obs) (R_obs = 100,200,300; Int M_B a du = Int m(t) psi(t) dt at fixed R_obs),
and the tail from phi_NL = [phi_eps - (eps/eps0) phi_eps0] / (1 - (eps0/eps)^2)   (removes the O(eps) part, scheme-exactly; eps0=0.01).
h -> 0 by Richardson (2nd order, h=0.1,0.05); tail by fit c + a/t + b/t^2 over t in [100,300].   usage: s2a_an.py"""
import numpy as np
eps0=0.01
def L(h,e): d=np.load('s2a/h%s_%s.npz'%(h,e)); return d
def stuff(h,e):
    d=L(h,e); d0=L(h,'0.01'); ef=float(e)
    phi=(d['phi']-ef/eps0*d0['phi'])/(1-(eps0/ef)**2)
    t=d['t']; dt=t[1]-t[0]
    c=[-8*np.trapezoid(d['mfar'][:,k]*d['psifar'][:,k],dx=dt) for k in (0,1)]        # R_obs = 100, 200
    naive=-8*d['mfar'][0,1]*np.trapezoid(d['psifar'][:,1],dx=dt)                      # -8 M_ADM Int a du  (R_obs=200)
    return t,phi,np.array(c+[naive])
print('C(eps) = lim t^3 phi_NL at fixed r  vs  -8 Int M_B a du  (Bondi mass and a(u) from the same nonlinear run; R_obs -> inf by 1/R extrapolation of 100,200)')
print('eps   M_ADM  |  C_pred(100) C_pred(200) C_pred(inf) | C_meas r=5  r=10  r=20 | meas/pred(inf) | naive -8 M_ADM Int a du | eps^3 BCR (-116 eps^3)')
for e in ('0.04','0.06','0.08','0.10'):
    t1,p1,c1=stuff('0.1',e); t2,p2,c2=stuff('0.05',e)
    ph=p2+(p2-p1)/3; cp=c2+(c2-c1)/3
    cinf=cp[1]+(cp[1]-cp[0])                      # C = Cinf + k/R : Cinf = C200 - (C100 - C200)
    m=(t1>=100)&(t1<=300); res=[]
    for k in range(3):
        y=t1**3*ph[:,k]; A=np.vstack([np.ones(m.sum()),1/t1[m],1/t1[m]**2]).T
        res.append(np.linalg.lstsq(A,y[m],rcond=None)[0][0])
    d=L('0.05',e); madm=d['mfar'][0,0]
    print('%s %.4f | %9.4f %9.4f %9.4f | %8.4f %8.4f %8.4f | %.4f | %9.4f | %8.4f'%(e,madm,cp[0],cp[1],cinf,res[0],res[1],res[2],res[0]/cinf,cp[2],-116.0*float(e)**3))
