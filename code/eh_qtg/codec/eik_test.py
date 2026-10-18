"""[eikonal estimate test] Charge absorbed by the event horizon of a collapse pulse.  The event horizon is the null ray u_H with r(u_H,v1)=r_+(m_f); its column is followed back from v1 to v0 in the nonlinear stage N.
Checks (i) conservation Q_0 = int_{0}^{u_H} r^2 phi_u du (row v1) + int_H r^2 phi_v dv; (ii) F = 1 - Q_abs/Q_0 with Q_abs = Q_H[v0,inf) = int_H r^2 phi_v dv - r_+^2 phi_H(v1) = -int 2 r r_v phi dv (r_H grows only up to v1).
usage: horizon_ray.py PULSE_A PULSE_B PULSE_V1 table.npz ..."""
import sys,os,numpy as np
os.environ['PULSE_A'],os.environ['PULSE_B'],os.environ['PULSE_V1']=sys.argv[1:4]
from strong import *
from fit1 import fitwin
print('%-24s %3s %5s %8s %8s %8s %8s %8s %8s %8s %8s  %s'%('table','m0','m_f','Q_0','Q_S','Q_H','cons.err','r_H(v0)','r_H(v1)','F(horizon)','F_meas','ratio'))
for fn in sys.argv[4:]:
    d=np.load(fn); model=int(d['model']); m0=float(d['m0']); mt=float(d['mt']); A=float(d['A']); mf=float(d['mf']); g=geom(m0,mt); s=g['s']; hN=float(os.environ.get('HNF','0.1'))*s
    u,v,row0,col0,ph=rays(model,L2,g['u0'],g['uend'],g['v0'],g['v1'],hN,hN,A,g['va'],g['vb'],m0=m0)
    out,snap,ah=run(model,L2,row0,col0,hN,hN,[0],rows=[len(v)-1])
    R,SG,RU,RV,SU,SV,PU,PV=[np.asarray(x) for x in snap[0]]
    bg=Static(model,mf,L2)
    nb=np.where(~(np.diff(R)<0))[0]; n=nb[0]+1 if len(nb) else len(R)
    # columns i0,i0+1 bracket r(u,v1)=r_+(m_f); linear interpolation in r(u,v1) gives the event-horizon ray
    if R[n-1]>bg.rp:
        print('%-24s %3g %5.2f  the event horizon is not in the domain at v1 (r(last)=%.3f > r_+=%.3f): slice invalid'%(os.path.basename(fn)[:24],m0,mf,R[n-1],bg.rp)); continue
    i0=int(np.where(R[:n]>bg.rp)[0][-1]); w=(R[i0]-bg.rp)/(R[i0]-R[i0+1])
    out,snap,ah=run(model,L2,row0,col0,hN,hN,[i0,i0+1],rows=[len(v)-1])
    def col(c):
        r=c[:,0]; pv=c[:,7]; phi=np.concatenate([[0],np.cumsum(0.5*(pv[1:]+pv[:-1])*np.diff(v))])
        return r,phi,np.trapezoid(r**2*pv,v)
    (ra,pa,QHa),(rb,pb,QHb)=col(out[0]),col(out[1])
    r=(1-w)*ra+w*rb; phi=(1-w)*pa+w*pb; QH=(1-w)*QHa+w*QHb
    QS=np.trapezoid((R**2*PU)[:i0+1],u[:i0+1])+w*0.5*((R**2*PU)[i0]+(R**2*PU)[i0+1])*(u[i0+1]-u[i0]); Q0=float(d['Q'])
    phH=phi[-1]; Qabs=QH-r[-1]**2*phH
    rc=np.asarray(col0[0]); pc=np.concatenate([[0],np.cumsum(0.5*(np.asarray(col0[7])[1:]+np.asarray(col0[7])[:-1])*np.diff(v))]); psi_in=rc*pc   # psi=r phi on u0
    psi_H=r*phi; rdot=np.gradient(r,v)
    Qe=-np.trapezoid(2*psi_in*rdot,v)          # eikonal: psi conserved along ingoing rays
    Qe2=-np.trapezoid(2*psi_H*rdot,v)          # same with the true horizon field (= Qabs2)
    # a priori (Vaidya-eikonal) estimate: m(v) along u0 from the data, EH from dr/dv=f(r,m(v))/2 backwards from r_+(m_f), psi_H=psi_in
    from collapse_lib import fstat
    mv=np.array([ms_mass(model,L2,rc[i],np.asarray(col0[1])[i],np.asarray(col0[2])[i],np.asarray(col0[3])[i]) for i in range(len(v))])
    rr=np.zeros(len(v)); rr[-1]=bg.rp
    for i in range(len(v)-1,0,-1):
        h_=v[i]-v[i-1]
        f1=fstat(model,L2,mv[i],rr[i])[0]*0.5
        rp_=rr[i]-h_*f1; f2=fstat(model,L2,mv[i-1],rp_)[0]*0.5
        rr[i-1]=rr[i]-0.5*h_*(f1+f2)
    rdv=np.gradient(rr,v)
    Qv=-np.trapezoid(2*psi_in*rdv,v); Qv0=-np.trapezoid(2*rc*np.gradient(rc,v)*pc,v)
    print('   Vaidya-eikonal: r_H(v0) %.3f (true %.3f); Qabs_V=%.4f (true %.4f) F_V=%.4f ; Q0 from data %.4f (table %.4f)'%(rr[0],r[0],Qv,Qabs,1-Qv/Q0,Qv0,Q0))
    pk=abs(psi_in).max(); pkH=abs(psi_H).max()
    print('   eikonal: Qabs_eik=%.4f (true %.4f) ratio %.3f ; max|psi_in|=%.4f max|psi_H|=%.4f ; F_eik=%.4f'%(Qe,Qabs,Qe/Qabs,pk,pkH,1-Qe/Q0))
    Qabs2=-np.trapezoid(2*r*np.gradient(r,v)*phi,v)   # same, from the horizon radius history
    s2=mf/5.0; ve=float(d['v1e'])+d['t']; B=fitwin(ve,d['phiH'],1000*s2,2900*s2,3.0)[0]; Fm=B/(8*mf*abs(Q0))
    Fh=(Q0-Qabs)/Q0
    print('%-24s %3g %5.2f %8.4f %8.4f %8.4f %8.1e %8.4f %8.4f %8.4f %8.4f  %6.4f   [Qabs=%.4f Qabs2=%.4f r(u_H,v1)=%.5f r_+=%.5f]'%(os.path.basename(fn)[:24],m0,mf,Q0,QS,QH,(Q0-QS-QH)/Q0,r[0],r[-1],Fh,Fm,Fm/Fh,Qabs,Qabs2,r[-1],bg.rp))
