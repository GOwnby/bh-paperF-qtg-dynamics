"""A priori estimate of F with the linear transfer of the pulse through the hole: the horizon field phi_H(v) is that of the pulse (data on u0) as a test field on the static exterior of
mass m_f (stage L, tail_L.run_L), mapped to the label v by v_e=2 r_*(r(u0,v)); the horizon radius is the Vaidya-like outgoing ray dr/dv=f(r,m(v))/2 integrated backwards from r_+(m_f)
(m(v) the generalized mass on u0).  Q_abs=-int 2 r_H rdot_H phi_H dv, F=1-Q_abs/Q_0.   usage: eik2.py PULSE_A PULSE_B PULSE_V1 table.npz ... (env STRONG_DR)"""
import sys,os,numpy as np
os.environ['PULSE_A'],os.environ['PULSE_B'],os.environ['PULSE_V1']=sys.argv[1:4]
from strong import *
from scipy.interpolate import interp1d
import tail_L
print('%-26s %3s %6s %8s %8s %8s %8s %8s'%('table','m0','m_f','F_abs','F_psi','F_lin','Fi_V','max psiH_lin/psiin'))
Fabs={}
for ln in open('sp/horizon_ray.log') if os.path.exists('sp/horizon_ray.log') else open('horizon_ray.log'):
    t=ln.split()
    if len(t)>=12 and t[0].endswith('.npz') and 'invalid' not in ln:
        try: Fabs[t[0]]=float(t[9])
        except ValueError: pass
for fn in sys.argv[4:]:
    d=np.load(fn); model=int(d['model']); m0=float(d['m0']); mt=float(d['mt']); A=float(d['A']); mf=float(d['mf']); g=geom(m0,mt); s=g['s']; hN=0.1*s; Q0=float(d['Q'])
    u,v,row0,col0,ph=rays(model,L2,g['u0'],g['uend'],g['v0'],g['v0']+30*s,hN,hN,A,g['va'],g['vb'],m0=m0)
    r=np.asarray(col0[0]); rv_=np.asarray(col0[3]); pv=np.asarray(col0[7]); phi=np.concatenate([[0],np.cumsum(0.5*(pv[1:]+pv[:-1])*np.diff(v))])
    bg=Static(model,mf,L2); x=bg.rstar_y(np.log(r-bg.rp)); ve=2*x
    hL=hN; nv=int(round((ve[-1]-ve[0])/hL)); tl=ve[0]+hL*np.arange(nv)
    vof=interp1d(ve,v,kind='cubic'); phit=np.interp(tl,ve,phi); rt=np.interp(tl,ve,r); col=rt*phit
    x0=x[0]; Lh=9.5/bg.kp/2; di=int(round(2*(x0+Lh)/hL)); nu=di+nv+2; xrow=x0-hL/2*np.arange(nu)
    t_,phiH,last=tail_L.run_L(bg,xrow,np.zeros(nu),hL,hL*(nv-1),Lh,psi_col_val=col)
    phH_v=np.interp(ve,ve[0]+t_,phiH)                      # phi_H as a function of the label v
    # Vaidya-like horizon
    from collapse_lib import fstat
    mv=np.array([ms_mass(model,L2,r[i],col0[1][i],col0[2][i],col0[3][i]) for i in range(len(v))])
    rr=np.zeros(len(v)); rr[-1]=bg.rp
    for i in range(len(v)-1,0,-1):
        h_=v[i]-v[i-1]; f1=fstat(model,L2,mv[i],rr[i])[0]*0.5; rp_=rr[i]-h_*f1; f2=fstat(model,L2,mv[i-1],rp_)[0]*0.5; rr[i-1]=rr[i]-0.5*h_*(f1+f2)
    rdot=np.gradient(rr,v); sel=v<=g['v1']; 
    Ql=-np.trapezoid((2*rr*rdot*phH_v)[sel],v[sel]); psin=r*phi
    Qp=-np.trapezoid((2*rdot*psin)[sel],v[sel])
    print('%-26s %3g %6.2f %8.4f %8.4f %8.4f   %s'%(os.path.basename(fn)[:26],m0,mf,Fabs.get(os.path.basename(fn),np.nan),1-Qp/Q0,1-Ql/Q0,''))
