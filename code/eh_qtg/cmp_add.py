import os, json, numpy as np
import os, analyze_q as A
import sys
Btag=sys.argv[2]
import os
a=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'data','gen3_B%s_k1.5_v110.json'%Btag))); hl=sorted((float(h) for h in a['data']),reverse=True)
print('additive grids',hl,' Uq additive',[round(u,4) for u in a['Uq']],' QTG',[round(u,4) for u in A.d['Uq']])
def romb(arrs):
    T=[arrs]
    for lev in range(1,len(arrs)): T.append([(4**lev*T[-1][i+1]-T[-1][i])/(4**lev-1) for i in range(len(T[-1])-1)])
    return T[-1][0]
add={nm:romb([np.array(a['data'][str(h)][nm]) for h in hl]) for nm in ('PV','sV','r')}
v=np.array(a['vq']); assert np.allclose(v,A.v)
print('v: rel diff of phi_v (QTG/add-1) and sigma_v diff (QTG-add), per ray')
for n in range(4):
    row=[]
    for vv in (20,30,40,50,60,70,80):
        i=int(np.argmin(abs(v-vv))); row.append('v=%d: %+.1e %+.1e'%(vv,A.top['PV'][n,i]/add['PV'][n,i]-1,A.top['sV'][n,i]-add['sV'][n,i]))
    print(' ray',n,' | '.join(row))
