import json,numpy as np,sys
def L(f,hv='0.05'):
    d=json.load(open(f)); return d,{k:np.array(v,float) for k,v in d['data'][hv].items() if k not in('nan','mon')}
d1,a=L('data/genb_hs0.05_v360_hv.json'); d2,b=L('data/genb_hs0.025_v360.json'); d3,c=L('data/genb_hs0.0125_v360.json')
vq=np.array(d1['vq']); print('sq',d1['sq'],d2['sq'])
ray=2
print('relative change of the solution with h_s (h_v=0.05, ray 2):  |0.05-0.025| ; |0.05-0.0125| ; |0.025-0.0125| ; ratio err(0.05)/err(0.025) taking 0.0125 as reference')
for nm in ['r','sV','PV','Ps','rs','rv']:
    out=[]
    for v in (40,60,80,100,150,200,250,300):
        i=np.argmin(abs(vq-v)); x,y,z=a[nm][ray][i],b[nm][ray][i],c[nm][ray][i]
        out.append('%g: %.1e;%.1e;%.1e;%.1f'%(v,abs(x-y)/abs(z),abs(x-z)/abs(z),abs(y-z)/abs(z),abs(x-z)/max(abs(y-z),1e-300)))
    print(nm,'  '.join(out))
