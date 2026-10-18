"""First non-finite advanced time of each level in a gen_b / gen_e JSON file (ray index 2, step 1 in v).  usage: python3 first_nonfinite.py file.json ..."""
import sys,json,numpy as np
for f in sys.argv[1:]:
    d=json.load(open(f)); v=np.array(d['vq'])
    for hv in d['data']:
        n=2 if len(d['data'][hv]['sV'])>2 else 0; s=np.array(d['data'][hv]['sV'][n]); bad=np.where(~np.isfinite(s))[0]
        print(f.split('/')[-1],'hv=%s'%hv,'first non-finite v =',v[bad[0]] if len(bad) else 'none to v=%g'%v[-1])
