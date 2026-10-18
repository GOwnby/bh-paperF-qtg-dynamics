"""Figure of the strong-pulse collapse tables: F=B/(8 m_f|Q|) and B/m_f^3 against m0/m_f (Hayward filled, Einstein open; 5 -> m_f, 2.5 -> m_f, 7.5/10 -> ...).  usage: QTG_CODE=<code dir> python3 fig_strong.py  (run from codec/, needs sp/*.npz)"""
import sys,os,glob,numpy as np
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
sys.path.insert(0,os.environ['QTG_CODE']); sys.argv=['x']
from fit1 import fitwin
C1,C2,C3='#2a6fb0','#c8501e','#6a6a6a'
plt.rcParams.update({'font.size':8.5,'axes.spines.top':False,'axes.spines.right':False,'lines.linewidth':1.2})
rows=[]
for fn in sorted(glob.glob('sp/t*_m*_mt*.npz')):
    d=np.load(fn); mf=float(d['mf']); s2=mf/5; ve=float(d['v1e'])+d['t']
    B=fitwin(ve,d['phiH'],1000*s2,2900*s2,3.0)[0]; Q=abs(float(d['Q'])); model=int(d['model']); m0=float(d['m0'])
    rows.append((model,m0/mf,B/(8*mf*Q),B/mf**3,mf))
rows=np.array(rows)
fig,ax=plt.subplots(1,3,figsize=(10.4,3.2))
for a,col,lab in ((ax[0],2,r'$B/(8m_f|Q|)$'),(ax[1],3,r'$B/m_f^{3}$')):
    for model,mk,fc,c,l in ((1,'o',C1,C1,'Hayward'),(0,'s','none',C2,'Einstein')):
        k=rows[:,0]==model
        a.plot(rows[k,1],rows[k,col],mk,mfc=fc,mec=c,color=c,ms=6,label=l,ls='none')
    a.set_xlabel(r'$m_0/m_f$'); a.set_ylabel(lab)
ax[0].plot([0,1],[0,1],color=C3,lw=0.8,ls=':'); ax[0].text(0.62,0.5,'$m_0/m_f$',color=C3,fontsize=8,rotation=33)
ax[0].legend(frameon=False,loc='lower right'); ax[0].set_title('(a) effective charge factor',fontsize=9,loc='left'); ax[1].set_title('(b) amplitude in units of $m_f^{3}$',fontsize=9,loc='left')
# panel (c): F from the horizon-absorbed charge (horizon_ray.py, sp/horizon_ray.log) against the measured F
import re
pts=[]
for ln in open('sp/horizon_ray.log'):
    t=ln.split()
    if len(t)>=12 and t[0].endswith('.npz') and 'invalid' not in ln:
        try: pts.append((t[0],float(t[1]),float(t[2]),float(t[9]),float(t[10])))
        except ValueError: pass
for nm,m0,mf,Fh,Fm in pts:
    sh='narrow' in nm or 'wide' in nm; mk='s' if nm.startswith('t0_') else ('^' if sh else 'o'); col=C2 if nm.startswith('t0_') else (C3 if sh else C1)
    ax[2].plot(Fh,Fm,mk,mfc='none' if mk=='s' else col,mec=col,color=col,ms=5,ls='none')
ax[2].plot([0.3,1.02],[0.3,1.02],color=C3,lw=0.8,ls=':'); ax[2].set_xlabel(r'$1-Q_{\rm abs}/Q_0$ (horizon charge)'); ax[2].set_ylabel(r'$B/(8m_f|Q_0|)$ (measured)')
ax[2].set_title('(c) measured against horizon charge',fontsize=9,loc='left')
ax[2].plot([],[],'o',color=C1,label='Hayward'); ax[2].plot([],[],'s',mfc='none',color=C2,label='Einstein'); ax[2].plot([],[],'^',color=C3,label='other widths'); ax[2].legend(frameon=False,loc='lower right',fontsize=7.5)
fig.tight_layout(); fig.savefig('fig_strong.png',dpi=200); print('saved',len(rows))
