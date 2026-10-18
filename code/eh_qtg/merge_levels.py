"""Merge two anisotropic runs of the same physical problem (same B, k, h_s) that differ in v_1 by a multiple of h_s: the s grids are shifted by (v_1' - v_1)/... and the rays coincide to 1e-7 in U.
Keeps the common sample range v = 20..min(vq_max).  usage: merge_levels.py out.json a.json b.json"""
import sys, json
out,fa,fb=sys.argv[1:4]; A=json.load(open(fa)); Bj=json.load(open(fb))
for k in ('B','k','model','L2'): assert A[k]==Bj[k],k
assert all(abs(a-b)<1e-6*a for a,b in zip(A['Uq'],Bj['Uq'])), (A['Uq'],Bj['Uq'])
n=min(len(A['vq']),len(Bj['vq'])); data={}
for D in (A,Bj):
    for h,dd in D['data'].items():
        data[h]={k:([row[:n] for row in v] if isinstance(v,list) and v and isinstance(v[0],list) else v) for k,v in dd.items()}
M=dict(A); M['vq']=A['vq'][:n]; M['data']=data; M['v1']=(A['v1'],Bj['v1']); json.dump(M,open(out,'w'))
print('merged levels',sorted(data,key=float,reverse=True),'n samples',n,'v range',M['vq'][0],M['vq'][-1])
