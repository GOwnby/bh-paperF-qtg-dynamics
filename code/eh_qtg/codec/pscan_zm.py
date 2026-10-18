"""zm = r^3 psi/2 at v=900*VS and the mean dm/dv over 800*VS<=v<=900*VS (env VS, default 1) on the ray, against zm=r_inf^3/2 and the closed form
dm/dv = 2 r beta kappa_-/c1^II (beta=(r^2-1)/4, c1^II=(1-1/r^2)^2, kappa_-=r|Q|/2, Q=psi(1-3 psi), psi=1/r^2) at r=r_inf.   usage: pscan_zm.py json... (codec/sc)"""
import sys,os,json,numpy as np
VS=float(os.environ.get('VS','1'))
print('%-8s %8s %9s %9s %9s %9s %7s'%('run','r_inf','zm(900)','r^3/2','dm/dv','closed','ratio'))
for f in sys.argv[1:]:
    d=json.load(open(f)); v=np.array(d['vq']); F={a:np.array(b[2],float) for a,b in list(d['data'].values())[-1].items() if a not in('nan','mon')}
    r=F['r']; W=np.exp(F['sg']); y=-F['rs']/W; z=(r**2-1-4*y*(-F['rv']))/r**2; m=r**3*(1-z)/(2*z)
    i=int(np.argmin(abs(v-900*VS))); j=int(np.argmin(abs(v-800*VS))); ri=r[-1]
    psi=1/ri**2; kap=ri*abs(psi*(1-3*psi))/2; beta=(ri*ri-1)/4; c1=(1-1/ri**2)**2; cl=2*ri*beta*kap/c1; dm=(m[i]-m[j])/(v[i]-v[j])
    print('%-8s %8.5f %9.5f %9.5f %9.3f %9.3f %7.3f'%(f.split('_')[1],ri,z[i]*m[i],ri**3/2,dm,cl,dm/cl))
