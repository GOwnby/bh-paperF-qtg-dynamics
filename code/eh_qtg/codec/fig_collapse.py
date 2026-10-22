import sys,os,json,numpy as np
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
sys.path.insert(0,os.environ['QTG_CODE']); sys.argv=['x']
from front import load
C1,C2,C3='#2a6fb0','#c8501e','#6a6a6a'
plt.rcParams.update({'font.size':8.5,'axes.spines.top':False,'axes.spines.right':False,'lines.linewidth':1.2})
H=np.load('tail_m1_v60_h05.npz'); G=np.load('tail_m0_v60_h05.npz')
fig,ax=plt.subplots(1,3,figsize=(11,3.4))
# (a) horizon field
t=H['t']; f=H['phiH']; vs=23.23; B=25.4474
a=ax[0]; m=t>1
a.loglog(t[m],np.abs(f[m]),color=C1,label=r'$|\phi_H|$ (Hayward collapse)')
tt=t[t>200]; a.loglog(tt,B/(tt-vs)**3,'--',color=C2,label=r'$B\,(v-v_s)^{-3}$, $B=25.45$')
a.set_xlabel(r'$v-v_{\rm start}$'); a.set_ylabel(r'$|\phi_H|$'); a.legend(frameon=False,loc='lower left')
a.set_title('(a) horizon field after the collapse',fontsize=9,loc='left')
# (b) local index
b=ax[1]
for D,c,lab,v0 in ((H,C1,'Hayward',23.23),(G,C3,'Einstein (GR)',23.79)):
    t=D['t']; f=D['phiH']; w=int(0.1)  # +-10%
    out=[];xs=[]
    for T in np.geomspace(700,2300,50):
        j1=np.searchsorted(t,T*0.93); j2=np.searchsorted(t,T*1.07)
        out.append(-(np.log(abs(f[j2]))-np.log(abs(f[j1])))/(np.log(t[j2]-v0)-np.log(t[j1]-v0))); xs.append(T)
    b.semilogx(xs,out,color=c,label=lab)
b.axhline(3,color='k',lw=0.6,ls=':'); b.set_ylim(2.8,3.2); b.set_xlabel(r'$v-v_{\rm start}$'); b.set_ylabel(r'$-{\rm d}\ln\phi_H/{\rm d}\ln(v-v_s)$'); b.legend(frameon=False)
b.set_title('(b) local power index',fontsize=9,loc='left')
# (c) K slope and v sigma_v with collapse tail
c=ax[2]
d,v,A=load('genc_prof_hs0.2_hv0.2_v1500.json',2); K=A['K']
sl=[];vv=[]
for V in np.arange(700,1440,20):
    i=np.argmin(abs(v-V)); a_,b_=i-10,i+10; sl.append(np.log(K[b_]/K[a_])/np.log(v[b_]/v[a_])); vv.append(V)
c.plot(vv,sl,color=C1,label=r'local slope of $K$, collapse tail')
c.plot(v[v>700],-v[v>700]*A["sV"][v>700],color=C2,label=r'$-v\,\sigma_v$')
c.axhline(10,color='k',lw=0.6,ls=':'); c.axhline(8,color='k',lw=0.6,ls=':')
c.text(1450,10.15,r'$4k-2=10$',ha='right',fontsize=8); c.text(1450,7.6,r'$2k+2=8$',ha='right',fontsize=8)
c.set_ylim(6,11.5); c.set_xlabel(r'$v$'); c.legend(frameon=False,loc='lower right'); c.set_title('(c) code E driven by the collapse tail',fontsize=9,loc='left')
plt.tight_layout(); plt.savefig(os.path.join(os.environ.get('FIG_OUT','.'),'fig_collapse.png'),dpi=200); print('ok')
