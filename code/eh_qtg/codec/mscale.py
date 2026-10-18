import sys; sys.path.insert(0,'.')
import pipeline as P
from runL import *
from fit1 import fitwin
for model,ms in ((0,(3.,5.,10.)),(1,(3.,5.,10.))):
    for m in ms:
        s=m/5.
        P.U0,P.UEND,P.V0,P.VA,P.VB=0.0,(29.5 if model==0 else 37.)*s,40.*s,44.*s,52.*s
        A=tune_A(model,1.0,m,A0=0.03*5/m*0.9*1.0+0.0) if False else tune_A(model,1.0,m,A0=0.03)
        v1=60.*s; h=0.1*s if s>1 else 0.1
        u,v,snap,out,ah=stageN(model,1.0,A,h,v1)
        bg,t,phiH,x0,xmin=stageL(model,1.0,m,u,snap,0.1*max(s,1.),2500.*s*0+3000.*s)
        ve=2*x0+t
        a,b=1000*s*0+ (1000.+0*s)*s,2900.*s
        B,vs,k=fitwin(ve,phiH,a,b,3.0)[:3]; kk=fitwin(ve,phiH,a,b)[2]
        print('model %d m=%4.1f A=%.5f B=%.4f B/m^3=%.4f (vs-v1e)/m=%.3f free k=%.4f'%(model,m,A,B,B/m**3,(vs-2*x0)/m,kk),flush=True)
