"""Sensitivity of code E to its input data (Paper F): perturb row0[PROW] (0: Delta, 1: sigma, 2: phi_s, 3: D) or the horizon column field PCOL (0: r_H, 3: r_v^H, 5: sigma_v^H, 7: phi_v^H) by the relative amount PERT (constant bias) and compare sigma_v with the unperturbed run.
usage: PROW=3 PERT=1e-12 python3 noise_tests.py v1 hs hv stride out.npz  (v1=800 hs=0.2 hv=0.1 stride=5).  Result (logs/noise_tests.log): the response is linear (~10 eps) and flat in v, no e^{kappa v} growth."""
import sys,os,numpy as np,warnings
warnings.filterwarnings('ignore')
src=open('gen_e.py').read().split("if __name__")[0]; exec(src)
model=1;L2=1.0;B=3e-3;k=1.5;v1=float(sys.argv[1]);hs=float(sys.argv[2]);hv=float(sys.argv[3]); stride=int(sys.argv[4])
S=StaticU(5.0); c=0.2*np.exp(-S.kp*v1)
d=build_eh_q(S,model,L2,1.5,v1,hs,hv/2,B,k=k,c=c,vH=v1+300)
row0=d['row0'].copy(); Ux=d['U']; zz=np.where(Ux<1.0,-Ux*S.w(Ux),row0[0]-S.rp); row0[0]=zz+(S.rp-d['col0'][0,0])
hz=d['hz']; r0h,rv0=hz.sol(0); sQ=lambda r,rv: r*float(coef(model,L2,(1-2*rv)/r**2)[0])/2; sgv0=sQ(r0h,rv0); phv=lambda t:PHVF(k,B,t)
def rhsD(t,Y):
    r,sg,rU,_,sUt,_=[a[0] for a in S.fields(np.array([t]),0.0)]
    a,b,c_=Fq(model,L2,r,sg,rU,rv0+Y[0],0.0,Y[2]); return [float(a),float(b),float(c_)]
sD=solve_ivp(rhsD,[0,d['U'][-1]],[0.0,sgv0,phv(0)],t_eval=d['U'],method='DOP853',rtol=1e-13,atol=[1e-26,1e-14,1e-300]); row0[3]=sD.y[0]
pc=int(os.environ.get('PCOL','-1'))
if pc>=0:
    cc=d['col0'].copy(); cc[pc]=cc[pc]*(1+float(os.environ["PERT"])); d['col0']=cc
pr=int(os.environ.get('PROW','-1'))
if pr>=0: row0[pr]=row0[pr]*(1+float(os.environ['PERT']))
nu=d['nu']; cols=np.arange(0,nu,stride)
out,_=run_B(model,L2,row0,d['col0'],hs,hv,cols,1)
vs=np.arange(0,v1+1e-9,10.0); ii=[int(round(x/hv)) for x in vs if int(round(x/hv))<out.shape[1]]
np.savez(sys.argv[5],o=out[::10][:,ii,:],s=d['s'][cols],U=d['U'][cols],v=vs[:len(ii)],col=d['col0'][:, ::int(round(10/(hv/2)))])
print('done',out.shape)
