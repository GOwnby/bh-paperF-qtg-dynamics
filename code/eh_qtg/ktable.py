"""Table of sigma_v (PDE, h_s=0.05) against the kernel prediction G for k = 1/2, 3/2, 3 (B=3e-3) and B=3e-4, 3e-2 at k=3/2, from endpoint_*.log (for k=3/2, B=3e-3 the merged file of eight levels, endpoint_B0.003_merged.log, which reaches v=290).  usage: ktable.py"""
import re
logs=[('k=0.5, B=3e-3','endpoint_k0.5.log'),('k=1.5, B=3e-4','endpoint_B0.0003.log'),('k=1.5, B=3e-3','endpoint_B0.003_merged.log'),('k=1.5, B=3e-2','endpoint_B0.03.log'),('k=3, B=3e-3','endpoint_k3.log')]
rows={}
for name,fn in logs:
    try: L=open(fn).read().splitlines()
    except Exception as e: print('missing',fn); continue
    for l in L[2:]:
        p=l.split()
        if len(p)<8: continue
        v=int(p[0]); rows.setdefault(v,{})[name]=(float(p[2]),float(p[3]),float(p[4]))   # sigma_v, err, G_kernel
print('v     '+'   '.join('%-34s'%n for n,_ in logs))
for v in (100,120,150,170,200,230,250,270,290):
    s='%4d  '%v
    for n,_ in logs:
        r=rows.get(v,{}).get(n)
        s+=('%+.5f %+.5f %+.1e  '%(r[0],r[2],r[0]-r[2]) if r else '   --                              ')
    print(s)
