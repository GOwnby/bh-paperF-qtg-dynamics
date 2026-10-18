"""Romberg (h^2) extrapolation of the constrained-y/rho QTG runs and derived quantities.  usage: analyze_q.py genq_*.json"""
import os, json, sys, numpy as np
d=json.load(open(sys.argv[1])); hl=sorted((float(h) for h in d['data']),reverse=True); names=['r','sg','rs','rv','sgs','sV','Ps','PV']; v=np.array(d['vq'])
def romb(arrs):
    T=[arrs]
    for lev in range(1,len(arrs)): T.append([(4**lev*T[-1][i+1]-T[-1][i])/(4**lev-1) for i in range(len(T[-1])-1)])
    return T          # T[lev][i]
F={}                  # F[name] -> list over levels of array (nray,nv)
for nm in names:
    arrs=[np.array(d['data'][str(h) if str(h) in d['data'] else repr(h)][nm]) for h in hl]
    T=romb(arrs); F[nm]=[t[0] for t in T]; F[nm+'_top']=T[-1][0]
def derived(lev):
    r,sg,rs,rv=[F[n][lev] for n in ('r','sg','rs','rv')]; y=-rs*np.exp(-sg); rho=-rv; psi=(1+4*y*rho)/r**2
    return dict(r=r,y=y,rho=rho,psi=psi,sV=F['sV'][lev],PV=F['PV'][lev],m=0.5*r**3*psi/(1-psi),M=0.5*r**3*psi)
L=len(hl)-1; top=derived(L); prev=derived(L-1)
if __name__=='__main__':
    print('B=%g k=%g grids %s; rays U=%s'%(d['B'],d['k'],hl,['%.3f'%u for u in d['Uq']]))
    for n,U in enumerate(d['Uq']):
        print('--- ray U=%.3f'%U)
        print(' v     r        y          rho        psi       1-psi      m          sigma_v    phi_v      |psi(L)-psi(L-1)|')
        for vv in (20,30,40,50,60,70,80,90,100,108):
            if vv>v[-1]: continue
            i=int(np.argmin(abs(v-vv)))
            print('%4d %.6f %.4e %.3e %.6f %.3e %.4e %+.5f %+.4e %.1e'%(v[i],top['r'][n,i],top['y'][n,i],top['rho'][n,i],top['psi'][n,i],1-top['psi'][n,i],top['m'][n,i],top['sV'][n,i],top['PV'][n,i],abs(top['psi'][n,i]-prev['psi'][n,i])))
