import sys,re
def tx(x,d=2):
    s='%.*e'%(d,float(x)); m,e=s.split('e'); e=int(e); return '$%s\\!\\times\\!10^{%d}$'%(m,e)
fn=sys.argv[1]; step=int(sys.argv[2]) if len(sys.argv)>2 else 20; vmax=int(sys.argv[3]) if len(sys.argv)>3 else 10**9
out=[]
for l in open(fn).read().splitlines()[2:]:
    p=l.split()
    if len(p)<12: continue
    v=int(p[0])
    if v%step or v>vmax: continue
    # v K sigma err Gk vsig z errz m dm dmc Kr
    out.append('%d & %s & %s & %s & %s & %s & %s & %s & %s\\\\'%(v,p[2].replace('-','$-$'),tx(p[3],0),p[4].replace('-','$-$'),p[5].replace('-','$-$'),tx(p[6],2),p[9],p[10],tx(p[11],1)))
print('\n'.join(out))
