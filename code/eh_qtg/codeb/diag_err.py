"""Diagnostic: full-row numerical error of code B (hs=0.05) at hv=0.2,0.1 vs hv=0.05; saves rows every 5 units of v.  python diag_err.py outfile.npz v1"""
import os,sys,time,numpy as np,warnings
warnings.filterwarnings('ignore')
sys.path.insert(0,'..')
from gen_b import *
out_file=sys.argv[1]; v1=float(sys.argv[2]); B=3e-3;k=1.5;model=1;L2=1.0;hs=0.05
S=StaticU(5.0); U1=1.5; c=0.2*np.exp(-S.kp*v1)
res={}
for hv in [0.2,0.1,0.05]:
    t=time.time(); d=build_eh_q(S,model,L2,U1,v1,hs,hv/2,B,k=k,c=c,vH=v1+300)
    nu=d['nu']; cols=np.arange(nu)
    o,_=run_B(model,L2,d['row0'],d['col0'],hs,hv,cols,1)   # (nu,nv,8)
    vs=np.arange(0,v1+1e-9,5.0); ii=[int(round(x/hv)) for x in vs if round(x/hv)<o.shape[1]]
    res['o%g'%hv]=o[:,ii,:]; res['U']=d['U']; res['s']=d['s']; res['v']=vs[:len(ii)]; res['col']=d['col0']; res['colv']=d['v']
    print(hv,nu,o.shape,time.time()-t,np.isnan(o).sum(),flush=True)
np.savez(out_file,**res)
