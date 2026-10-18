"""Figure for Paper F (event-horizon-regular data): reads data/*.json (Romberg in h^2 inside) and logs/kernel_ratio_B*.log.  usage: python3 fig_eh.py -> ../../fig_eh.pdf, fig_eh.png"""
import json, os, numpy as np
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
here=os.path.dirname(os.path.abspath(__file__)); D=os.path.join(here,'data'); L=os.path.join(here,'logs')
def load(fn):
    d=json.load(open(os.path.join(D,fn))); hl=sorted((float(h) for h in d['data']),reverse=True); out={}
    for nm in ('r','sg','rs','rv','sV','Ps','PV'):
        T=[np.array(d['data'][str(h) if str(h) in d['data'] else repr(h)][nm]) for h in hl]
        for lev in range(1,len(T)): T=[(4**lev*T[i+1]-T[i])/(4**lev-1) for i in range(len(T)-1)]
        out[nm]=T[0]
    W=np.exp(out['sg']); y=-out['rs']/W; rho=-out['rv']; out['psi']=(1+4*y*rho)/out['r']**2; out['v']=np.array(d['vq']); out['U']=d['Uq']; out['B']=d['B']; return out
plt.rcParams.update({'font.size':9,'axes.grid':True,'grid.alpha':0.25})
fig,ax=plt.subplots(2,2,figsize=(10,7.2))
cols=['#1b6ca8','#c0392b','#2e8b57','#8e44ad']
a=load('genq_m1_B0.003_k1.5_v200.json'); m=a['v']<=160
for n in range(4):
    i0=int(np.argmax(a['sV'][n]<-0.79)); mm=m&(np.arange(len(a['v']))>=i0)   # start after the static exterior-to-interior transition
    ax[0,0].plot(a['v'][mm],a['sV'][n][mm],color=cols[n],label='$U=%.1f$'%a['U'][n])
ax[0,0].axhline(-0.7956534,color='k',ls='--',lw=0.8); ax[0,0].axhline(0,color='k',lw=0.6)
ax[0,0].text(115,-0.76,r'$-\kappa_-(m_f)$',fontsize=8); ax[0,0].set_xlabel('$v$'); ax[0,0].set_ylabel(r'$\sigma_v$'); ax[0,0].legend(fontsize=8,loc='center right'); ax[0,0].set_title('(a) Hayward $h$, $B=3\\times10^{-3}$')
for B,c in (('0.0003',cols[0]),('0.003',cols[1]),('0.03',cols[2])):
    a=load('genq_m1_B%s_k1.5_v110.json'%B); m=a['v']<=108
    ax[0,1].semilogy(a['v'][m],1-a['psi'][2][m],color=c,label='$B=%s$'%B)
ax[0,1].set_xlabel('$v$'); ax[0,1].set_ylabel(r'$1-\ell^2\psi$ on $U\simeq1$'); ax[0,1].legend(fontsize=8); ax[0,1].set_title('(b) approach to the pole $\\psi=1/\\ell^2$')
for B,c,vmax in (('0.0003',cols[0],100),('0.003',cols[1],70)):
    a=load('genq_m2_a1_M1.5_B%s_k1.5_v110.json'%B); m=a['v']<=vmax
    for n,ls in ((2,'-'),(0,':')): ax[1,0].plot(a['v'][m],a['sV'][n][m],color=c,ls=ls,label='$B=%s$, $U=%.1f$'%(B,a['U'][n]))
ax[1,0].axhline(-0.7970077,color='k',ls='--',lw=0.8); ax[1,0].axhline(0,color='k',lw=0.6)
ax[1,0].set_xlabel('$v$'); ax[1,0].set_ylabel(r'$\sigma_v$'); ax[1,0].legend(fontsize=7,loc='center right'); ax[1,0].set_title(r'(c) bounded $h$ ($m=1.5,\ \alpha=1$)')
for B,c in (('0.0003',cols[0]),('0.003',cols[1]),('0.03',cols[2])):
    rows=[l.split() for l in open(os.path.join(L,'kernel_ratio_B%s.log'%B)).read().strip().split('\n')[2:]]
    v=np.array([float(r[0]) for r in rows]); ratio=np.array([float(r[3]) for r in rows]); ax[1,1].plot(v,ratio-1,'o-',color=c,ms=3,label='$B=%s$'%B)
ax[1,1].set_xlabel('$v$'); ax[1,1].set_ylabel(r'$\phi_v/\phi_v^{\rm kernel}-1$ on $U\simeq1$'); ax[1,1].legend(fontsize=8); ax[1,1].set_title('(d) flux against the linear kernel of Paper G')
plt.tight_layout(); fn=os.path.join(here,'..','..','fig_eh'); plt.savefig(fn+'.pdf'); plt.savefig(fn+'.png',dpi=150); print('ok')
