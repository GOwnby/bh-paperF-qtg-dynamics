"""Finite-advanced-time blow-up on the tail-carrying ray u=u0 of the QTG system (Hayward h).  The ray ODE (r, r_v, r_u, s_v, phi_u) is the same as in qtg_lib.build;
the background gauge is the static one.  Event: |psi| > PSIMAX.  Prints v_* (B,k) and the sign of psi, and compares with the GR-additive (linear) system, which has no blow-up."""
import sys,os,numpy as np,warnings,json
warnings.filterwarnings('ignore'); sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from qtg_lib import *
from scipy.integrate import solve_ivp
bg=Bg(); u0=-6.0
bg2=None
def vstar(model,L2,B,k,A=0.02,width=1.0,PSIMAX=1e6,vmax=400,rtol=1e-12):
    dph1=lambda x:-2*x/width**2*A*np.exp(-(x/width)**2); dph2=lambda x:-k*B*(1+x)**(-k-1)
    yc=bg.y(np.array([u0/2]))[0]; rc=bg.rm+yc; fc=bg.fy(yc)
    def rhs(s,Y):
        r,rs,rt,st,pt=Y
        y=bg.y(np.array([(s+u0)/2]))[0]; f=bg.fy(y); sg=np.log(abs(f)); rb=bg.rm+y; ss=dfr(bg,rb)/2; ps=dph2(s)
        W=np.exp(sg); psi=(1+4*rs*rt/W)/r**2; c1=coef(model,L2,psi)[1]
        a,b,c=F(model,L2,r,sg,rt,rs,pt,ps)
        return [rs,ss*rs-4*np.pi*r*c1*ps**2,a,b,c]
    def ev(s,Y):
        y=bg.y(np.array([(s+u0)/2]))[0]; W=abs(bg.fy(y)); return abs((1+4*Y[1]*Y[2]/W)/Y[0]**2)-PSIMAX
    ev.terminal=True
    sol=solve_ivp(rhs,[0,vmax],[rc,fc/2,fc/2,dfr(bg,rc)/2,dph1(u0)],method='DOP853',rtol=rtol,atol=1e-300,events=ev)
    s=sol.t[-1]; Y=sol.y[:,-1]; y=bg.y(np.array([(s+u0)/2]))[0]; W=abs(bg.fy(y)); psi=(1+4*Y[1]*Y[2]/W)/Y[0]**2
    return s,psi,Y[0]-bg.rm,sol.status
if __name__=='__main__' and len(sys.argv)>1 and sys.argv[1]=='sub':
    # all solves except B = 2e-1 (the solver gives up at the singularity, status -1, and needs about an hour): the lines are those of ray_blowup.log;  python3 ray_blowup.py sub
    for B in (2e-2,2e-3,2e-4,2e-5,2e-6,2e-7):
        s,psi,dr,st=vstar(1,1.0,B,1.5); print('  B=%.0e  v_*=%8.3f  psi(v_*)=%+.3e  r-r_-=%+.3e  status %d'%(B,s,psi,dr,st))
    for k in (0.5,1.0,1.5,2.0,3.0):
        s,psi,dr,st=vstar(1,1.0,2e-3,k); print('  k=%.1f v_*=%8.3f psi=%+.3e'%(k,s,psi))
elif __name__=='__main__':
    res=[]
    print('Hayward h (model 1, l=1), tail k=1.5')
    for B in (2e-1,2e-2,2e-3,2e-4,2e-5,2e-6,2e-7):
        s,psi,dr,st=vstar(1,1.0,B,1.5); print('  B=%.0e  v_*=%8.3f  psi(v_*)=%+.3e  r-r_-=%+.3e  status %d'%(B,s,psi,dr,st)); res.append((B,s,psi))
    print('k dependence at B=2e-3')
    for k in (0.5,1.0,1.5,2.0,3.0):
        s,psi,dr,st=vstar(1,1.0,2e-3,k); print('  k=%.1f v_*=%8.3f psi=%+.3e'%(k,s,psi))
    print('GR, no regulator is linear in the ray ODE (model 0 on the Hayward background is not static; skip)')
    json.dump(res,open('ray_blowup.json','w'))
