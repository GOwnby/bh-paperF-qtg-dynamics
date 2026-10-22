"""Figure of the k=2 (non-compact data) collapse tail.  usage: QTG_CODE=<code dir> python3 fig_collapse_k2.py  (needs npdata/, nplin_*.npz, ce/*.json or data/)"""
import sys,os,numpy as np
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
sys.path.insert(0,os.environ['QTG_CODE']); sys.argv=['x']
from front import load
C1,C2,C3,C4='#2a6fb0','#c8501e','#6a6a6a','#2a8a4a'
plt.rcParams.update({'font.size':8.5,'axes.spines.top':False,'axes.spines.right':False,'lines.linewidth':1.2})
fig,ax=plt.subplots(1,3,figsize=(11,3.4))
a=ax[0]
for fn,c,lab in (('nplin_m0_M5_h0.2.npz',C3,'linear, Schwarzschild'),('npdata/np_m0_b1.0_h1.npz',C4,'collapse, Einstein'),('npdata/np_m1_b1.0_h1.npz',C1,'collapse, Hayward')):
    d=np.load(fn); t=d['t']; y=d['phiH']*t**2/(-4*float(d['b'])); m=t>150; a.semilogx(t[m],y[m],color=c,label=lab,ls='--' if 'linear' in lab else '-')
a.axhline(1,color='k',lw=0.6,ls=':'); a.set_ylim(0.2,1.25); a.set_xlabel(r'$v-v_{\rm start}$'); a.set_ylabel(r'$\phi_H\,(v-v_{\rm start})^{2}/(4I_0)$'); a.legend(frameon=False,loc='lower right')
a.set_title(r'(a) horizon field, $I_0=-b$',fontsize=9,loc='left')
b=ax[1]
for fn,c,lab in (('npdata/np_m1_b0.5_h1.npz',C3,r'$b=0.5$'),('npdata/np_m1_b1.0_h1.npz',C1,r'$b=1$'),('npdata/np_m1_b2.0_h1.npz',C2,r'$b=2$')):
    d=np.load(fn); t=d['t']; f=d['phiH']; xs=[];out=[]
    for T in np.geomspace(300,11000,60):
        j1=np.searchsorted(t,T*0.93); j2=np.searchsorted(t,T*1.07); out.append(-(np.log(abs(f[j2]))-np.log(abs(f[j1])))/(np.log(t[j2])-np.log(t[j1]))); xs.append(T)
    b.semilogx(xs,out,color=c,label=lab)
b.axhline(2,color='k',lw=0.6,ls=':'); b.set_ylim(1.7,2.1); b.set_xlabel(r'$v-v_{\rm start}$'); b.set_ylabel(r'$-{\rm d}\ln\phi_H/{\rm d}\ln(v-v_{\rm start})$'); b.legend(frameon=False,loc='lower right'); b.set_title('(b) local power index (Hayward)',fontsize=9,loc='left')
c=ax[2]; fn=[('ce/genc_np1_hs0.2_hv0.2_v1500.json',C1,r'$b=1$'),('ce/genc_np01_hs0.2_hv0.2_v1500.json',C2,r'$b=0.1$')]
for f,col,lab in fn:
    d,v,A=load(f,2); dv=v[1]-v[0]; K=A['K']; vv=[];sl=[];pl=[]
    for V in np.arange(700,1440,20):
        i=np.argmin(abs(v-V)); a_,b_=i-10,i+10; s=np.log(K[b_]/K[a_])/np.log(v[b_]/v[a_]); dm=(A['m'][i+5]-A['m'][i-5])/(10*dv); v0=v[i]-A['m'][i]/dm; vs=v[i]*A['sV'][i]
        vv.append(V); sl.append(s); pl.append(s+6*v0/(v[i]-v0)-2*(abs(vs)-6))
    c.plot(vv,sl,color=col,label='slope of $K$, '+lab); c.plot(vv,pl,color=col,ls='--',lw=0.9)
d,v,A=load(fn[0][0],2); mm=(v>700)&(v<1440); c.plot(v[mm],-v[mm]*A['sV'][mm],color=C3,label=r'$-v\sigma_v$ ($b=1$)')
c.axhline(6,color='k',lw=0.6,ls=':'); c.text(1430,6.08,r'$4k-2=2k+2=6$',ha='right',fontsize=8)
c.set_ylim(3.5,6.6); c.set_xlabel(r'$v$'); c.legend(frameon=False,loc='lower right',fontsize=7.5); c.set_title(r'(c) code E, $k=2$ (dashed: + two $1/v$ terms)',fontsize=9,loc='left')
plt.tight_layout(); plt.savefig(os.path.join(os.environ.get('FIG_OUT','.'),'fig_collapse_k2.png'),dpi=200); print('ok')
