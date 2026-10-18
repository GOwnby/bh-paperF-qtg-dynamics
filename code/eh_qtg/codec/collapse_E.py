"""Code E on the collapse tail against the prescribed k=3 run (Paper F, Sec. collapse).  usage: QTG_CODE=<code dir> python3 collapse_E.py > logs/collapse_E.log
Reads data/collapseE_*.json (4 rays) and the shipped prescribed-tail data ../codee/data (B=3e-3, k=3, ray U=0.9968)."""
import sys,os,json,numpy as np
here=os.path.dirname(os.path.abspath(__file__)); sys.argv=['x']; sys.path.insert(0,here)
from front import load
D=os.path.join(here,'data'); P=os.path.join(here,'..','codee','data','gene_p1_hs0.2_m1_B0.003_k3_v1200_ray2.json')
def stats(fn,n):
    d,v,A=load(fn,n); zs=A['z'][np.argmin(abs(v-45))]; vf=v[np.argmax(A['z']<0.5*zs)]; return d,v,A,vf
def at(v,A,V,k=50):
    j=np.argmin(abs(v-V)); a,b=j-k,j+k; return dict(vsV=v[j]*A['sV'][j],K=A['K'][j],slope=np.log(A['K'][b]/A['K'][a])/np.log(v[b]/v[a]),m=A['m'][j],dm=(A['m'][j+5]-A['m'][j-5])/10,zm=A['z'][j]*A['m'][j])
print('closed form z m -> r_-^3/2 = 0.59126')
for fn in ('collapseE_profile_hv0.1.json','collapseE_profile_hv0.2.json','collapseE_zeroPU0_hv0.2.json'):
    for n in range(4):
        d,v,A,vf=stats(os.path.join(D,fn),n)
        for V in (1100,1400):
            s=at(v,A,V); print('%-32s ray %d U=%.3f front v=%3.0f  v=%d: v*sV=%+.3f K=%.3e slope=%.3f m=%.1f dm/dv=%.4f zm=%.5f'%(fn,n,d['Uq'][n],vf,V,s['vsV'],s['K'],s['slope'],s['m'],s['dm'],s['zm']))
if os.path.exists(P):
    d,v,A,vf=stats(P,0); s=at(v,A,1100); print('prescribed B=3e-3 k=3 U=0.9968: front v=%.0f v=1100: v*sV=%+.3f K=%.3e slope=%.3f m=%.1f dm/dv=%.4f zm=%.5f'%(vf,s['vsV'],s['K'],s['slope'],s['m'],s['dm'],s['zm']))
d,v,A,_=stats(os.path.join(D,'collapseE_profile_hv0.2.json'),2); d0,v0,B0,_=stats(os.path.join(D,'collapseE_zeroPU0_hv0.2.json'),2)
print('row-profile sensitivity (U=0.9968, v=1200): K ratio %.3f, Ps ratio per ray:'%(A['K'][np.argmin(abs(v-1200))]/B0['K'][np.argmin(abs(v-1200))]),[ '%.3f'%(load(os.path.join(D,'collapseE_profile_hv0.2.json'),n)[2]['Ps'][np.argmin(abs(v-1200))]/load(os.path.join(D,'collapseE_zeroPU0_hv0.2.json'),n)[2]['Ps'][np.argmin(abs(v-1200))]) for n in range(4)])
