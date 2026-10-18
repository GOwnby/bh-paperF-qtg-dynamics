import sys, numpy as np
import analyze_q as A
lo,hi=-0.72,-0.19   # 10% and 90% of the rise from -0.796 to ~-0.1
print('B=%g: advanced-time width of the rise of sigma_v from %g to %g'%(A.d['B'],lo,hi))
for n,U in enumerate(A.d['Uq']):
    s=A.top['sV'][n]; v=A.v; ok=np.isfinite(s)
    def cross(t):
        for i in range(len(v)-1):
            if ok[i] and ok[i+1] and s[i]<t<=s[i+1]: return v[i]+(t-s[i])/(s[i+1]-s[i])*(v[i+1]-v[i])
        return None
    a,b=cross(lo),cross(hi); print(' U=%.3f  v(%g)=%s  v(%g)=%s  width=%s'%(U,lo,a and '%.1f'%a,hi,b and '%.1f'%b,(a is not None and b is not None) and '%.1f'%(b-a) or 'n/a'))
