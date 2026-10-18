import sys,time; sys.path.insert(0,'.')
from pipeline import *
def go(model,mf,h,v1,hL,vmax=3000.,Lh=None,A=None):
    if A is None: A=tune_A(model,1.0,mf)
    u,v,snap,out,ah=stageN(model,1.0,A,h,v1)
    bg,t,phiH,x0,xmin=stageL(model,1.0,mf,u,snap,hL,vmax,Lh=Lh)
    ve=2*x0+t
    return A,bg,ve,phiH
def idx(ve,phi,v,rel=0.1):
    j1=np.searchsorted(ve,v*(1-rel)); j2=np.searchsorted(ve,v*(1+rel))
    return -(np.log(abs(phi[j2]))-np.log(abs(phi[j1])))/(np.log(ve[j2])-np.log(ve[j1]))
if __name__=='__main__':
    model=int(sys.argv[1]); h=float(sys.argv[2]); hL=float(sys.argv[3]); v1=float(sys.argv[4])
    A,bg,ve,phiH=go(model,5.0,h,v1,hL)
    print('A=%.6f'%A)
    for V in (200,300,500,800,1200,2000,2900):
        j=np.searchsorted(ve,V); print('v_e=%6.0f phi_H=%+.6e v^3 phi=%+.5f  index=%.4f'%(ve[j],phiH[j],ve[j]**3*phiH[j],idx(ve,phiH,V)))
