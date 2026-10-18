"""hv-convergence of code E on the collapse tail (hs=0.2): usage conv_c.py coarse.json fine.json"""
import sys,numpy as np
sys.argv=sys.argv[:3]; fa,fb=sys.argv[1:3]
from front import load
for n in range(4):
    d,v,A=load(fa,n); d2,v2,B=load(fb,n)
    out=[]
    for V in (100,200,400,800,1200,1400):
        i=np.argmin(abs(v-V)); out.append('v=%d: dlnK=%.1e dsV=%.1e dr/r=%.1e dlnm=%.1e dPV/PV=%.1e'%(V,abs(np.log(A['K'][i]/B['K'][i])),abs(A['sV'][i]-B['sV'][i]),abs(A['r'][i]/B['r'][i]-1),abs(np.log(A['m'][i]/B['m'][i])),abs(A['PV'][i]/B['PV'][i]-1)))
    print('ray',n,'U=%.3f'%d['Uq'][n]); print('\n'.join('  '+o for o in out))
