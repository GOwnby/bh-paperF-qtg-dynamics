"""Stage N to v1+Dv against stage L started at the row v1 (strong-pulse start, strong.py): psi=r*phi on the later row at several r*.  usage: overlap_h.py model m0 mt h0f hLf [Dv_rel=80]"""
import sys; sys.path.insert(0,'.')
from strong import *
from pipeline import stageL
model=int(sys.argv[1]); m0=float(sys.argv[2]); mt=float(sys.argv[3]); h0=float(sys.argv[4]); hLf=float(sys.argv[5]); Dv=float(sys.argv[6]) if len(sys.argv)>6 else 80.0
g=geom(m0,mt); s=g['s']; A=tune_A_m(model,m0,g,mt,0.03); h=h0*s; hL=hLf*s
u1,v1_,r0_,c0_,snap1,ah1=stageN_h(model,m0,g,A,h)
g2=dict(g); g2['v1']=g['v1']+Dv*s
u2,v2_,r02,c02,snap2,ah2=stageN_h(model,m0,g2,A,h)
mf=float(ms_mass(model,L2,c0_[0][-1],c0_[1][-1],c0_[2][-1],c0_[3][-1])); bg=Static(model,mf,L2)
R1=snap1[0][0]; R2,SG2,RU2,RV2,SU2,SV2,PU2,PV2=snap2[0]
ok=np.isfinite(R2)&np.isfinite(PU2)
x0_1=bg.rstar_y(np.log(R1[0]-bg.rp)); x0_2=bg.rstar_y(np.log(R2[0]-bg.rp))
vrel=round(2*(x0_2-x0_1)/hL)*hL
bgx,t,phiH,x0,xmin=stageL(model,L2,mf,u1,snap1,hL,vrel)
xrow,last=stageL.last; xrow=xrow+vrel/2
phi=CubicSpline(u2[ok],PU2[ok]).antiderivative()(u2[ok]); Rok=R2[ok]; ex=Rok>bg.rp*(1+1e-9)
xN=bg.rstar_y(np.log(Rok[ex]-bg.rp)); psiN=Rok[ex]*phi[ex]
print('model %d m0=%g mt=%g s=%.2f rp=%.3f vrel=%.2f  (x0 diff %.3f)'%(model,m0,mt,s,bg.rp,vrel,x0_2-x0_1))
scale=1.0/bg.kp/(4*5.0) if False else 1.0
for xx in (35*s,20*s,10*s,0,-10*s,-20*s):
    iN=np.argmin(abs(xN-xx)); pL=np.interp(xN[iN],xrow[::-1],last[::-1])
    print('r*=%8.3f  psi_N=%+.6e psi_L=%+.6e  rel diff %.2e'%(xN[iN],psiN[iN],pL,(psiN[iN]-pL)/abs(psiN[iN])))
