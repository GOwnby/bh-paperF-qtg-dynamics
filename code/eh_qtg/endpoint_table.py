"""Endpoint table of Paper F (Section 'The endpoint'): sigma_v, z=1-l^2 psi, m, K, v*sigma_v on the ray U~1 from an anisotropic run (h_s fixed, h_v halved),
Richardson-Romberg in h_v^2 over the finest levels that are finite at v; error = |top - next-lower| of the T-table; kernel prediction G_pred (Paper G kernel, rho_v=-kappa_- rho+S).
usage: endpoint_table.py json B k kappa_minus [ray]   (QTG_CODE = code dir; kernel_lib on the path)"""
import os, sys, json, numpy as np
sys.path.insert(0,os.environ.get('QTG_CODE','..')); from qtg_lib import coef
fn=sys.argv[1]; B=float(sys.argv[2]); k=float(sys.argv[3]); kap=float(sys.argv[4]); n=int(sys.argv[5]) if len(sys.argv)>5 else 2
d=json.load(open(fn)); v=np.array(d['vq']); hl=sorted((float(h) for h in d['data']),reverse=True)
D={h:d['data'][repr(h) if repr(h) in d['data'] else str(h)] for h in hl}
def table(nm,K,j):
    lv=hl[-K:]; T=[[np.array(D[h][nm][n])[j] for h in lv]]   # j: index array
    for lev in range(1,K): T.append([(4**lev*T[-1][i+1]-T[-1][i])/(4**lev-1) for i in range(len(T[-1])-1)])
    return T
import math
def _vb(h):
    bad=np.where(~np.isfinite(np.array(D[h]['sV'][n])))[0]
    if len(bad): return v[bad[0]]
    return (205.25+2/0.04896874208903945*math.log(1.5e-4/(B*h))) if os.environ.get('VB_LAW') else 1e9   # VB_LAW=1: unobserved blow-up taken from Eq. (vb) (k=3/2 only)
vb={h:_vb(h) for h in hl}
MARGIN=30.0   # a level is used only while v <= v_b(h) - 30 (v_b: first non-finite sample; error ~ h_v^2 e^{kappa_+ v} grows by e^{kappa_+ 30}=4.3 per margin)
def best(nm,j,vv):
    for K in (4,3,2):
        lv=hl[-K:]
        if len(lv)==K and all(vb[h]>=vv+MARGIN for h in lv):
            T=table(nm,K,j); return T[-1][0], T[-2][1], K          # value, next-lower estimate from the K-1 finest levels, K
    return None
import kernel_lib as KL
vs=np.arange(20,3000.5,0.5); dv=0.5; Phi=np.array([KL.phi_v(float(x),k,B) for x in vs]); S=Phi**2
rho=np.zeros_like(vs); r_=0.0; e=np.exp(-kap*dv)
for i in range(1,len(vs)):
    a,b=S[i-1],S[i]; I=a*(1-e)/kap+(b-a)/dv*((dv-(1-e)/kap)/kap); r_=r_*e+I; rho[i]=r_
Gk=S/np.maximum(rho,1e-300)-kap
print('file %s  B=%g k=%g kappa_-=%g ray U=%.3f levels h_v=%s'%(fn,B,k,kap,d['Uq'][n],hl))
RM=1.057475; c1II=(1-1/RM**2)**2     # plateau c1 = z_II^2, psi_II = 1/r_-^2 (r_- of the static Hayward hole m=5)
print('   v   K   sigma_v      err      G_kernel    v*sigma_v   z          err_z/z   m        dm/dv   dm/dv(closed)  Kretschmann')
for vv in range(100,int(d['vq'][-1])-5,10):
    j=int(np.argmin(abs(v-vv))); jj=np.array([j-5,j,j+5]); res={}
    ok=True
    for nm in ('r','sg','rs','rv','sV'):
        b=best(nm,jj,vv)
        if b is None: ok=False;break
        res[nm]=b
    if not ok: continue
    K=res['r'][2]
    def fields(ix):   # ix: 0 top, 1 next-lower
        r,sg,rs,rv=[res[x][ix] for x in ('r','sg','rs','rv')]
        W=np.exp(sg)
        y=-rs/W; rho_=-rv; psi=(1+4*y*rho_)/r**2; return r,psi,y,rho_,W
    r,psi,y,rho_,W=fields(0); r2,psi2,_,_,_=fields(1)
    z=1-psi; z2=1-psi2; m=r**3*psi/(2*z)
    dm=(m[2]-m[0])/10.0 if True else 0
    # Kretschmann needs phi: use PV,Ps
    PsPV=[best('Ps',jj,vv),best('PV',jj,vv)]
    if PsPV[0] is None or PsPV[1] is None: continue
    g=PsPV[0][0][1]*PsPV[1][0][1]/W[1]
    Q,c1,c2,c3=[float(a) for a in coef(1,1.0,psi[1])]; Sig=psi[1]/2-c2-8*np.pi*c1*g+64*np.pi**2*c3*g**2
    Kr=(4*Sig)**2+8*(128*np.pi**2*c1**2*g**2+Q**2/2)+4*psi[1]**2
    sV=res['sV'][0][1]; err=abs(res['sV'][0][1]-res['sV'][1][1])
    beta=(psi[1]*r[1]**2-1)/4; dmc=2*r[1]*beta*(kap+sV)/c1II
    print('%5d  %d  %+.6f  %.0e   %+.6f   %+.3f   %.4e  %.0e   %.1f  %.3f   %.3f      %.4e'%(vv,K,sV,err,Gk[int(round((vv-20)/dv))],vv*sV,z[1],abs(z[1]-z2[1])/z[1],m[1],dm,dmc,Kr))
