import sys; sys.path.insert(0,'.')
from pipeline import *
from collapse_lib import np_tail
TAIL=(1.0,25.3,1.8)
A=tune_A(0,1.0,5.0,tail=TAIL); h=0.05; hL=0.05
# N to 150, row at 150
uN,vN,snapN,outN,ahN=stageN(0,1.0,A,h,150.0,tail=TAIL)
R,SG,RU,RV,SU,SV,PU,PV=snapN[0]; ok=np.isfinite(R)&np.isfinite(PU)
bg=Static(0,5.0)
# L from the 70-row, final row at v_e equal to N's 150-row
uN7,vN7,snap7,_,_=stageN(0,1.0,A,h,70.0,tail=TAIL)
x0_70=bg.rstar_y(np.log(snap7[0][0][0]-bg.rp)); x0_150=bg.rstar_y(np.log(R[0]-bg.rp))
vrel=2*(x0_150-x0_70); vrel=round(vrel/hL)*hL
bg,t,phiH,x0,xmin=stageL(0,1.0,5.0,uN7,snap7,hL,vrel,tail=TAIL)
xrow,last=stageL.last; xrow=xrow+vrel/2
phi=CubicSpline(uN[ok],PU[ok]).antiderivative()(uN[ok])+np_tail(*TAIL)[0](R[ok][0]); Rok=R[ok]; ex=Rok>bg.rp*(1+1e-9)
xN=bg.rstar_y(np.log(Rok[ex]-bg.rp)); psiN=Rok[ex]*phi[ex]
print('vrel',vrel,'x0 diff',x0_150-x0_70,' (matching row v_e) ')
for xx in (35,30,20,10,0,-10,-20,-30):
    iN=np.argmin(abs(xN-xx)); iL=np.argmin(abs(xrow-xN[iN]))
    # interpolate L to xN[iN]
    pL=np.interp(xN[iN],xrow[::-1],last[::-1])
    print('x=%7.3f psi_N=%+.6e psi_L=%+.6e  rel diff %.2e'%(xN[iN],psiN[iN],pL,(psiN[iN]-pL)/abs(psiN[iN])))
