"""Validation of the QTG double-null code: (1) static Hayward interior (A=B=0) convergence; (2) convergence of the modified Raychaudhuri residual
   r_uu - s_u r_u + (4 pi r/h') phi_u^2 (and u<->v) for a pulse -- the constraints are not used by the evolution, so their convergence at order 2 tests the
   derived r_uv, s_uv equations (a wrong s_uv would leave an O(1) residual)."""
import sys,os,numpy as np,json,warnings
warnings.filterwarnings('ignore'); sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from qtg_lib import *
model=int(os.environ.get('MODEL','1')); L2=float(os.environ.get('L2','1.0')); bg=Bg() if model!=2 else Bg2(float(os.environ.get("MASS","1.0")),L2**0.5); out={}
print('model',model,'L2',L2)
# (1) static
errs=[]
for h in (0.08,0.04,0.02,0.01):
    u,v,arrs,_=build(bg,model,L2,-6,6,0,30,h,h,0.0,0.0); run(model,L2,arrs,h,h)
    yb=bg.y((u[None,:]+v[:,None])/2); rb=bg.rm+yb
    errs.append(float(np.max(np.abs(arrs[0]-rb)/rb)))
print('static max rel err in r:',['%.2e'%e for e in errs],' orders',['%.2f'%np.log2(errs[i]/errs[i+1]) for i in range(3)])
out['static']=errs
# (2) residuals
def resid(arrs,h,vmax,vmin):
    R,SG,RU,RV,SU,SV,PU,PV=arrs; psi=psi_of(R,SG,RU,RV); c1=coef(model,L2,psi)[1]
    Ruu=(RU[:,2:]-RU[:,:-2])/(2*h); Rvv=(RV[2:,:]-RV[:-2,:])/(2*h)
    ru=Ruu-SU[:,1:-1]*RU[:,1:-1]+4*np.pi*R[:,1:-1]*c1[:,1:-1]*PU[:,1:-1]**2
    rv=Rvv-SV[1:-1,:]*RV[1:-1,:]+4*np.pi*R[1:-1,:]*c1[1:-1,:]*PV[1:-1,:]**2
    j0,j1=int(round(vmin/h)),int(round(vmax/h))
    nu_=np.linalg.norm(ru[j0:j1])/np.linalg.norm(Ruu[j0:j1]); nv_=np.linalg.norm(rv[j0:j1,:])/np.linalg.norm(Rvv[j0:j1,:])
    return nu_,nv_
out['resid']={}
W2=float(os.environ.get('VMAX2','55'))
for (A,B,vmin,vmax) in [(0.02,0.002,0,20),(0.02,0.002,20,W2)]:
    rows=[]
    for h in (0.08,0.04,0.02):
        u,v,arrs,_=build(bg,model,L2,-6,8,0,vmax,h,h,A,B); run(model,L2,arrs,h,h); rows.append((h,)+resid(arrs,h,vmax,vmin))
    print('A=%g B=%g v in [%g,%g]:'%(A,B,vmin,vmax),' '.join('h=%g: u %.2e v %.2e'%r for r in rows),'| orders u %.2f %.2f, v %.2f %.2f'%(np.log2(rows[0][1]/rows[1][1]),np.log2(rows[1][1]/rows[2][1]),np.log2(rows[0][2]/rows[1][2]),np.log2(rows[1][2]/rows[2][2])))
    out['resid']['A=%g,B=%g,v=[%g,%g]'%(A,B,vmin,vmax)]=rows
json.dump(out,open('validate_model%d.json'%model,'w'),indent=1)
