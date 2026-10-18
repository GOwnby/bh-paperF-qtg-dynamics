"""Check sigma_v = dln(rho)/dv + (W-separability defect) on the extrapolated ray data (Paper F, slaving).  usage: rho_check.py json"""
import sys, json, numpy as np
d=json.load(open(sys.argv[1])); v=np.array(d['vq']); hl=sorted((float(h) for h in d['data']),reverse=True)
def romb(arrs):
    T=[arrs]
    for lev in range(1,len(arrs)): T.append([(4**lev*T[-1][i+1]-T[-1][i])/(4**lev-1) for i in range(len(T[-1])-1)])
    return T[-1][0]
get=lambda nm,n:romb([np.array(d['data'][repr(h) if repr(h) in d['data'] else str(h)][nm][n]) for h in hl[-4:]])
n=2
sV=get('sV',n); rv=get('rv',n)
lr=np.log(-rv)
print(' v     sigma_v      dln(rho)/dv   difference')
for vv in (100,120,140,160,180,200,220,240,250,260):
    j=int(np.argmin(abs(v-vv)))
    dl=(lr[j+1]-lr[j-1])/(v[j+1]-v[j-1])
    print('%4d  %+.6f   %+.6f   %+.2e'%(vv,sV[j],dl,sV[j]-dl))
# split the defect: d/dv ln(W/rho) = d/dv ln(-r_u) - d/dv ln(beta),  beta = y rho = (psi r^2 - 1)/4
rs=get('rs',n); sg=get('sg',n); r=get('r',n)
W=np.exp(sg); y=-rs/W; beta=y*(-rv)
dd=lambda a,j:(a[j+1]-a[j-1])/(v[j+1]-v[j-1])
print(' v    dln(-r_u)/dv   -dln(beta)/dv   sum        v*sum     r-r_-')
for vv in (100,140,180,200,220,240,250):
    j=int(np.argmin(abs(v-vv)))
    a=dd(np.log(-rs),j); b=-dd(np.log(beta),j)
    print('%4d  %+.3e   %+.3e   %+.3e  %+.4f  %+.2e'%(vv,a,b,a+b,(a+b)*vv,r[j]-1.057475))
print(' v   sigma_v(stored)  d sg/dv     dln(rho)/dv + dln(W/rho)/dv')
for vv in (100,140,180,200,220,240,250):
    j=int(np.argmin(abs(v-vv))); print('%4d %+.6f  %+.6f  %+.6f'%(vv,sV[j],dd(sg,j),dd(np.log(-rv),j)+dd(np.log(-rs),j)-dd(np.log(beta),j)))
print('early:')
for vv in (30,40,50,60,70,80,90):
    j=int(np.argmin(abs(v-vv))); print('%4d %+.8f  %+.8f  diff %+.2e  (rays n=0..3:'%(vv,sV[j],dd(sg,j),sV[j]-dd(sg,j)), ' '.join('%+.2e'%(get('sV',m)[j]-dd(get('sg',m),j)) for m in range(4)),')')
print(v[:5], v[-3:])
