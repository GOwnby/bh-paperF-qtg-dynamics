import sys; sys.path.insert(0,'.')
from runL import *
from scipy.optimize import least_squares
def fitwin(ve,phi,a,b,k=None):
    m=(ve>=a)&(ve<=b); x=ve[m]; y=phi[m]
    if k is None:
        f=lambda p:(np.log(np.abs(y))-(np.log(p[0])-p[2]*np.log(x-p[1])))
        s=least_squares(f,[30.,0.,3.0],x_scale=[10,50,1]); return s.x
    f=lambda p:(np.log(np.abs(y))-(np.log(p[0])-k*np.log(x-p[1])))
    s=least_squares(f,[30.,0.],x_scale=[10,50]); return np.r_[s.x,k]
if __name__=='__main__':
    model=int(sys.argv[1]); mf=float(sys.argv[2]); v1=float(sys.argv[3])
    A,bg,ve,phi=go(model,mf,0.1,v1,0.1,vmax=3000.)
    print('A',A)
    for a,b in ((400,800),(800,1600),(1600,3000),(500,3000)):
        print((a,b),'free k: B=%.4f vs=%.2f k=%.4f'%tuple(fitwin(ve,phi,a,b)),'  fixed k=3: B=%.4f vs=%.2f'%tuple(fitwin(ve,phi,a,b,3.0)[:2]))
