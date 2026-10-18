"""Exact charge balance of the collapse pulse: Q_0=int r^2 phi_v dv on u0 (conserved Noether charge of phi->phi+c); Q_S=int r^2 phi_u du over the row v=v1 from u=0 to r=r_+(m_f)
(the whole late slice outside the final horizon).  Test of B = 8 m_f |Q_S|  (time-inverted NP constant of the final static exterior), against the measured B/(8 m_f |Q_0|).
usage: charge_row.py PULSE_A PULSE_B PULSE_V1 table.npz ..."""
import sys,os,numpy as np
os.environ['PULSE_A'],os.environ['PULSE_B'],os.environ['PULSE_V1']=sys.argv[1:4]
from strong import *
from fit1 import fitwin
print('%-26s %4s %6s %9s %9s %9s %9s %8s %7s'%('table','m0','m_f','Q_0','Q_S','r+^2phiH','F_pred','F_meas','ratio'))
for fn in sys.argv[4:]:
    d=np.load(fn); model=int(d['model']); m0=float(d['m0']); mt=float(d['mt']); A=float(d['A']); mf=float(d['mf']); g=geom(m0,mt); s=g['s']; hN=0.1*s
    u,v,row0,col0,ph=rays(model,L2,g['u0'],g['uend'],g['v0'],g['v1'],hN,hN,A,g['va'],g['vb'],m0=m0)
    out,snap,ah=run(model,L2,row0,col0,hN,hN,[0],rows=[len(v)-1])
    R,SG,RU,RV,SU,SV,PU,PV=[np.asarray(x) for x in snap[0]]
    bg=Static(model,mf,L2)
    ok=np.isfinite(R)&np.isfinite(PU); nb=np.where(~(np.diff(R)<0))[0]
    n=nb[0]+1 if len(nb) else len(R)
    sel=np.zeros(len(R),bool); sel[:n]=True; sel&=ok&(R>bg.rp)
    uu=u[sel]; f=(R**2*PU)[sel]
    QS=np.trapezoid(f,uu)
    phr=np.concatenate([[0],np.cumsum(0.5*(PU[sel][1:]+PU[sel][:-1])*np.diff(uu))])   # phi(u,v1) from phi(0,v1)=0 (u0 ray beyond the pulse)
    # quadratic extrapolation of r^2 phi_u and phi to r=r_+ : integrate to the exact cut by linear interpolation of R
    rr=R[sel]; j=len(rr)-1; fr=(rr[j]-bg.rp)/(rr[j-1]-rr[j])   # fraction of a cell beyond the last selected cell (outside r_+ cut)
    phH=phr[-1]-fr*(phr[-1]-phr[-2]); QSh=QS-0.0
    horizon=bg.rp**2*phH; phH0=float(d['phiH'][0]); h0=bg.rp**2*phH0
    # boundary piece to r=r_+ (small): extend linearly one cell
    s2=mf/5.0; ve=float(d['v1e'])+d['t']; B=fitwin(ve,d['phiH'],1000*s2,2900*s2,3.0)[0]
    Q0=float(d['Q'])
    Fm=B/(8*mf*abs(Q0)); Fp=(QS+h0)/Q0
    print('%-26s %4g %6.2f %9.4f %9.4f %9.4f %9.4f %8.4f %7.4f'%(os.path.basename(fn)[:26],m0,mf,Q0,QS,h0,Fp,Fm,Fm/Fp))
