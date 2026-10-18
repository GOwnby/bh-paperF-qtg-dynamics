"""Endpoint diagnostics of a Hayward run (Romberg top level and its difference from the next-lower level): sigma_v, 1-psi, m, dm/dv, (1-psi)*m, y*phi_v^2 on each ray.  usage: endpoint_q.py json"""
import sys, numpy as np
import analyze_q as A
v=A.v; L=len(A.hl)-1
def lev(l):
    r=A.F['r'][l]; sg=A.F['sg'][l]; rs=A.F['rs'][l]; rv=A.F['rv'][l]; W=np.exp(sg); y=-rs/W; psi=(1+4*y*(-rv))/r**2
    z=1-psi; m=0.5*r**3*psi/z; return dict(r=r,y=y,psi=psi,z=z,m=m,sV=A.F['sV'][l],PV=A.F['PV'][l])
T=lev(L); P=lev(L-1)
print('B=%g grids %s; Romberg top level, difference to the next-lower level in parentheses'%(A.d['B'],A.hl))
for n,U in enumerate(A.d['Uq']):
    print('--- U=%.3f   v   sigma_v (dlev)   1-psi (dlev)   m   dm/dv   (1-psi)*m   y*phi_v^2'%U)
    for vv in range(80,int(v[-1])+1,10):
        i=int(np.argmin(abs(v-vv)))
        if not np.isfinite(T['sV'][n,i]): continue
        dm=(T['m'][n,min(i+5,len(v)-1)]-T['m'][n,i-5])/(v[min(i+5,len(v)-1)]-v[i-5])
        print('  %5.0f  %+.5f (%.1e)  %.4e (%.1e)  %.4e  %.3f  %.4f  %.4f'%(v[i],T['sV'][n,i],abs(T['sV'][n,i]-P['sV'][n,i]),T['z'][n,i],abs(T['z'][n,i]-P['z'][n,i])/T['z'][n,i],T['m'][n,i],dm,T['z'][n,i]*T['m'][n,i],T['y'][n,i]*T['PV'][n,i]**2))
