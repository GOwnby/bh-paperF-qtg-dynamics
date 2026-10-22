"""Figures of Paper F.  Needs: ray_blowup.json (ray_blowup.py), conv_B2e-4_h*.npz (run_conv.py).  Model-2 curves are recomputed here (h=0.02)."""
import sys,os,json,numpy as np,warnings
warnings.filterwarnings('ignore'); sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from qtg_lib import *
plt.rcParams.update({'font.size':9,'axes.grid':True,'grid.alpha':0.25,'axes.spines.top':False,'axes.spines.right':False})
fig,ax=plt.subplots(1,3,figsize=(11,3.2))
# (a) v_*(B)
r=json.load(open('ray_blowup.json')); B=np.array([x[0] for x in r]); vs=np.array([x[1] for x in r]); m=B<=2e-2
p=np.polyfit(np.log10(1/B[m]),vs[m],1)
ax[0].plot(np.log10(1/B[m]),vs[m],'o',color='#1f4e79'); x=np.linspace(1.5,7,10); ax[0].plot(x,np.polyval(p,x),'-',color='#999999',lw=1)
ax[0].set_xlabel(r'$\log_{10}(1/B)$'); ax[0].set_ylabel(r'$v_*$'); ax[0].set_title('(a) singular time of the data ray')
ax[0].text(0.05,0.85,'slope %.1f per decade'%p[0],transform=ax[0].transAxes)
# (b) convergence at u=0
cols=['#c8d6e5','#8fb3d9','#4f8fc6','#2a6aa8','#0b3d6e']
for h,c in zip(('0.01','0.005','0.0025','0.00125','0.000625'),cols):
    d=np.load('conv_B2e-4_h%s.npz'%h); v=d['v']; o=d['out']; R,SG,RU,RV,SU,SV,PU,PV=[o[0,:,f] for f in range(8)]; psi=psi_of(R,SG,RU,RV)
    ax[1].plot(v,psi,color=c,label='h=%s'%h,lw=1.3)
ax[1].axhline(1.0,color='#b03a2e',lw=1,ls='--'); ax[1].text(41,1.001,r'pole $1/\ell^2$',color='#b03a2e',fontsize=8)
ax[1].set_xlim(40,70); ax[1].set_ylim(0.88,1.01); ax[1].set_xlabel('v'); ax[1].set_ylabel(r'$\psi$'); ax[1].set_title(r'(b) $\psi(v)$ at $u=0$, five meshes'); ax[1].legend(fontsize=7,loc='lower right',frameon=False)
# (c) model 2, bounded h
h=0.02; vmax=76; bg=Bg2(1.0,1.0)
u,v,arrs,_=build(bg,2,1.0,-6,8,0,vmax,h,h,0.02,0.002); run(2,1.0,arrs,h,h)
R,SG,RU,RV,SU,SV,PU,PV=arrs; psi=psi_of(R,SG,RU,RV); W=np.exp(SG)
for uu,c in ((-6,'#8e44ad'),(-1,'#2a6aa8'),(2,'#1e8449')):
    i=int(round((uu+6)/h)); ax[2].plot(v,psi[:,i],color=c,label='u=%g'%uu,lw=1.3)
ax[2].axhline(1.0,color='#b03a2e',lw=1,ls='--'); ax[2].axhline(-1.0,color='#b03a2e',lw=1,ls='--'); ax[2].set_ylim(-1.1,1.1)
ax[2].set_xlabel('v'); ax[2].set_ylabel(r'$\psi$'); ax[2].set_title(r'(c) bounded $h$: walls $\pm1/\alpha$ (m=1, B=0.002)'); ax[2].legend(fontsize=7,loc='center right',frameon=False)
plt.tight_layout(); _o=os.environ.get('FIG_OUT','.'); plt.savefig(os.path.join(_o,'fig_qtg.pdf')); plt.savefig(os.path.join(_o,'fig_qtg.png'),dpi=160)
print('slope per decade %.3f'%p[0]); print('model2 range',np.nanmin(psi),np.nanmax(psi),'finite',np.isfinite(psi).all())
for uu in (-6,-3,-1,0,2,4,6):
    i=int(round((uu+6)/h)); print(' u=%2g psi(v=20,40,60,76): %s | sigma_v %s | y(vmax) %+.2e'%(uu,' '.join('%.5f'%psi[int(round(x/h)),i] for x in (20,40,60,76)),' '.join('%+.3f'%SV[int(round(x/h)),i] for x in (20,40,60,76)),-RU[-1,i]/W[-1,i]))
