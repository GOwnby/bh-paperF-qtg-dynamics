"""Affine-parameter / tidal diagnostics along the ingoing radial null ray u=const (U~1) from code-B data.
usage: tidal.py json hv vmax_trust [json2 hv2]    (second dataset = coarser level for an error estimate)
Quantities (exact in spherical symmetry; W=e^sigma in the s-gauge; all invariant under u-reparametrisation):
  affine parameter  d lambda = W dv  (Gamma^v_vv = d_v ln W)    -> remaining affine distance  Dl(v) = int_v^inf W dv'
  r_lambda = r_v/W,   transverse tidal eigenvalue  T = -r_lambda_lambda / r = (4 pi/h') (phi_v/W)^2   (Raychaudhuri constraint, h'=1/c1)
  tidal integrals   I1(v)=int_v^inf T dlambda = int 4 pi c1 phi_v^2/W dv ,   I2 = int int T  (Tipler/Krolak weak-singularity test)
  K (Kretschmann-like scalar of Paper F Sec.), boost-invariant Sigma = sigma_uv/W."""
import sys,json,os,numpy as np
sys.path.insert(0,os.environ['QTG_CODE'])
from qtg_lib import coef
def load(fn,hv,n=2):
    d=json.load(open(fn)); F={k:np.array(x[n],float) for k,x in d['data'][hv].items() if k not in('nan','mon')}; return np.array(d['vq']),F
def derived(F):
    r,sg,rs,rv,Ps,PV,sV=[F[x] for x in ('r','sg','rs','rv','Ps','PV','sV')]
    W=np.exp(sg); y=-rs/W; rho=-rv; psi=(1+4*y*rho)/r**2; Q,c1,c2,c3=[np.array(a) for a in coef(1,1.0,psi)]; g=Ps*PV/W
    Sig=psi/2-c2-8*np.pi*c1*g+64*np.pi**2*c3*g**2; K=(4*Sig)**2+8*(128*np.pi**2*c1**2*g**2+Q**2/2)+4*psi**2
    return dict(r=r,W=W,y=y,rho=rho,psi=psi,z=1-psi,c1=c1,g=g,Sig=Sig,K=K,PV=PV,Ps=Ps,sV=sV,rl=rv/W,T=4*np.pi*c1*(PV/W)**2)
def tails(v,f,sV,k=1.5):
    """int_v^vend f dv (trapezoid) + analytic tail beyond vend assuming f ~ v^-a with local a (power) -> two bounds (exponential-local, power-law)"""
    seg=0.5*(f[1:]+f[:-1])*np.diff(v); inside=np.concatenate([np.cumsum(seg[::-1])[::-1],[0.0]])   # summed from the end (no cancellation)
    a=-(np.log(f[-1])-np.log(f[-11]))/(np.log(v[-1])-np.log(v[-11])); pw=f[-1]*v[-1]/(a-1) if a>1 else np.inf
    lam=-(np.log(f[-1])-np.log(f[-11]))/(v[-1]-v[-11]); ex=f[-1]/lam if lam>0 else np.inf
    return inside,pw,ex,a
fn,hv,vmax=sys.argv[1],sys.argv[2],float(sys.argv[3])
v,F=load(fn,hv); m=(v<=vmax); D=derived(F); v=v[m]; D={k:x[m] for k,x in D.items()}
if len(sys.argv)>4:
    v2,F2=load(sys.argv[4],sys.argv[5]); D2=derived(F2); m2=np.isin(v2,v); D2={k:x[m2] for k,x in D2.items()}
W=D['W']
inW,pwW,exW,aW=tails(v,W,D['sV'])
inT,pwT,exT,aT=tails(v,D['T']*W,D['sV'])          # int T dlambda = int T W dv
print('trust window v<=%g (hv=%s); local power index of W at the end: %.2f (expected 2k+2 = 5); of T*W: %.2f'%(vmax,hv,aW,aT))
print('  v     Dl(v)=remaining affine dist (power/exp tail)   T=-r_ll/r    int_v T dl (power/exp)   K     K*Dl      Dl*T')
for vv in range(100,int(vmax)+1,20):
    i=int(np.argmin(abs(v-vv)))
    Dl=inW[i]+pwW; Dle=inW[i]+exW; I1=inT[i]+pwT; I1e=inT[i]+exT
    print('%4d  %.3e (%.3e)   %.3e   %.3e (%.3e)  %.3e  %.3e  %.3e'%(vv,Dl,Dle,D['T'][i],I1,I1e,D['K'][i],D['K'][i]*Dl,Dl*D['T'][i]))
# local power laws vs Dl: K ~ Dl^-a_K, T ~ Dl^-a_T  (power-law tail version of Dl)
Dl=inW+pwW
def sl(f,i,w=10): return (np.log(abs(f[i+w]))-np.log(abs(f[i-w])))/(np.log(Dl[i+w])-np.log(Dl[i-w]))
print('local exponents with respect to remaining affine distance (K ~ Dl^e_K etc.); predictions for k=3/2: e_K=-(4k-2)/(2k+1)=-1, e_T=-2k/(2k+1)=-0.75')
for vv in range(120,int(vmax)-10,20):
    i=int(np.argmin(abs(v-vv))); print('%4d  e_K=%.2f  e_T=%.2f  e_Sigma=%.2f  e_rl=%.3f  e_PV/W=%.2f'%(vv,sl(D['K'],i),sl(D['T'],i),sl(D['Sig'],i),sl(D['rl'],i),sl(D['PV']/D['W'],i)))
if len(sys.argv)>4:
    print('error estimate: |K(hv)-K(2hv)|/K and |T| rel. diff (hv vs coarser)')
    for vv in range(100,int(vmax)+1,40):
        i=int(np.argmin(abs(v-vv))); print('%4d  K %.1e  T %.1e  W %.1e'%(vv,abs(D['K'][i]-D2['K'][i])/D['K'][i],abs(D['T'][i]-D2['T'][i])/D['T'][i],abs(W[i]-D2['W'][i])/W[i]))
# invariant tidal measures over the remaining affine range (independent of the normalisation of lambda): change of r, T*Dl^2, int int T dlambda^2
inT2,pwT2,exT2,aT2=tails(v,D['T']*W,D['sV']); I1=inT2+pwT2
inI2,pwI2,exI2,a2=tails(v,I1*W,D['sV']); I2=inI2+pwI2
print('\ninvariants over the remaining affine range (power-law tails: index of W %.2f, of T*W %.2f):'%(aW,aT2))
print('  v   |r_lambda| Dl   T Dl^2   I2=int int T dlambda dlambda')
for vv in range(100,int(vmax)+1,50):
    i=int(np.argmin(abs(v-vv))); print('%4d  %.2e   %.2e   %.2e'%(vv,abs(D['rl'][i])*Dl[i],Dl[i]**2*D['T'][i],I2[i]))
