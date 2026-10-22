"""Code-level check: the QTG code with model 0 (h=psi, i.e. GR without regulator) must reproduce the Paper-E double-null code with m_N=0 to round-off on arbitrary smooth
characteristic data (only the evolution equations are compared; the data need not satisfy the constraints).  Uses dn2lib.py and libdouble_null.so from vendor_E/ (build with build.sh)."""
import sys,os,numpy as np
here=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,here); sys.path.insert(0,os.path.join(here,'vendor_E')); sys.path.insert(0,os.path.join(here,'..'))
import qtg_lib as Q, dn2lib as D
nu,nv=60,70; hu=hv=0.02
def mk():
    A=[np.zeros((nv,nu)) for _ in range(8)]; u=np.arange(nu)*hu; v=np.arange(nv)*hv
    A[0][0,:]=3+0.3*np.sin(u); A[0][:,0]=3+0.3*np.sin(v); A[1][0,:]=0.2*np.cos(u); A[1][:,0]=0.2*np.cos(v)
    A[2][0,:]=0.3*np.cos(u); A[2][:,0]=-0.4+0.05*v; A[3][0,:]=-0.6+0.1*np.cos(u); A[3][:,0]=0.3*np.cos(v)
    A[4][0,:]=0.1*np.sin(u); A[4][:,0]=0.1*np.cos(v); A[5][0,:]=0.05*np.cos(u); A[5][:,0]=0.05*np.sin(v)
    A[6][0,:]=0.2*np.sin(u); A[6][:,0]=0.1*np.cos(v); A[7][0,:]=0.1*np.cos(u); A[7][:,0]=0.2*np.sin(v)
    return A
A1=mk(); A2=mk(); Q.run(0,1.0,A1,hu,hv)
p=lambda a:a.ctypes.data_as(D.dp); D.lib2.evolve2(nu,nv,hu,hv,0.0,10.0,*[p(a) for a in A2],3)
print('finite:',all(np.isfinite(a).all() for a in A1),' max|QTG(model 0)-PaperE(m_N=0)| = %.2e  (field scale %.2f)'%(max(np.max(np.abs(a-b)) for a,b in zip(A1,A2)),max(np.max(np.abs(a)) for a in A1)))
