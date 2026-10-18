"""Slope law of K for a code-E run driven by a collapse tail (Paper F, Sec. collapse).  usage: python3 an_k.py file.json k [ray]
dlnK/dlnv = (4k-2) - 6 v0/(v-v0) + 2(|v sigma_v| - (2k+2)),  v0 = v - m/(dm/dv) (origin of the linear growth of m)."""
import sys,os,numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from front import load
fn=sys.argv[1]; k=float(sys.argv[2]); n=int(sys.argv[3]) if len(sys.argv)>3 else 2
d,v,A=load(fn,n); dv=v[1]-v[0]
print(fn,'ray',n,'U=%.4f'%d['Uq'][n]); print('   v      zm       dm/dv     v0     v*sV     slope    formula  slope+terms')
for V in (300,400,500,650,800,1000,1200,1400):
    j=np.argmin(abs(v-V)); a,b=j-50,j+50
    slope=np.log(A['K'][b]/A['K'][a])/np.log(v[b]/v[a]); dm=(A['m'][j+5]-A['m'][j-5])/(10*dv); v0=v[j]-A['m'][j]/dm; vs=v[j]*A['sV'][j]
    form=(4*k-2)-6*v0/(v[j]-v0)+2*(abs(vs)-(2*k+2)); plus=slope+6*v0/(v[j]-v0)-2*(abs(vs)-(2*k+2))
    print('%6.0f  %.5f  %.4f  %6.1f  %7.3f  %7.3f  %7.3f  %7.3f'%(v[j],A['z'][j]*A['m'][j],dm,v0,vs,slope,form,plus))
