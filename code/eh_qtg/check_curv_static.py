"""Check of the double-null Kretschmann formula K=(4 Sigma)^2+8 H_ab H^ab/r^2+4 psi^2 on the static Hayward and bounded interiors (g=0):
Sigma=psi/2-c2, H_abH^ab/r^2=Q^2/2, against K=f''^2+4 f'^2/r^2+4(1-f)^2/r^4 of the metric -f dt^2+dr^2/f+r^2 dOmega^2 (finite differences of the exact f).  Einstein: 48 M^2/r^6."""
import os, sys, numpy as np
sys.path.insert(0,os.environ.get('QTG_CODE',os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')))
from qtg_lib import coef
from static_gen import hayward, bounded
def K_formula(model,L2,f,r):
    psi=(1-f)/r**2; Q,c1,c2,c3=[float(x) for x in coef(model,L2,psi)]; Sig=psi/2-c2
    return (4*Sig)**2+8*Q**2/2+4*psi**2
for name,model,L2,(fm,fn,fpn) in (('Hayward m=5',1,1.0,hayward(5.0,1.0)),('bounded m=1.5 alpha=1',2,1.0,bounded(1.5,1.0))):
    worst=0
    for r in ([1.1,1.5,2.5,4.0,7.0,9.0] if model==1 else [1.05,1.3,1.8,2.5,2.9]):
        e=1e-4; f=fn(r); f1=(fn(r+e)-fn(r-e))/(2*e); f2=(fn(r+e)-2*fn(r)+fn(r-e))/e**2
        Kx=f2**2+4*f1**2/r**2+4*(1-f)**2/r**4; Kf=K_formula(model,L2,f,r); worst=max(worst,abs(Kf-Kx)/abs(Kx))
    print('%s: max relative difference over radii = %.1e'%(name,worst))
M=2.0; r=7.0; psi=2*M/r**3; print('Einstein h=psi: K=%.10e, 48 M^2/r^6=%.10e'%(((4*(psi/2))**2+8*psi**2/2+4*psi**2),48*M**2/r**6))
