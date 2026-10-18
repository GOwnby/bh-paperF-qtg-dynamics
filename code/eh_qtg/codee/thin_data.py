"""Thin a gen_e / gen_el JSON file to the single ray U=0.9968 (index 2) and 12 significant digits (Paper F, codee/data).  usage: thin.py in.json out.json [fields]"""
import sys,json
d=json.load(open(sys.argv[1])); keep=(sys.argv[3].split(',') if len(sys.argv)>3 else ['r','sg','rs','rv','sV','Ps','PV'])
r=lambda x:float('%.12g'%x) if x==x else None
o=dict(model=d['model'],L2=d['L2'],Uq=[d['Uq'][2]],sq=[d['sq'][2]],vq=d['vq'],B=d['B'],k=d['k'],v1=d['v1'],data={})
for hv,x in d['data'].items(): o['data'][hv]={f:[[r(t) for t in x[f][2]]] for f in keep}
json.dump(o,open(sys.argv[2],'w'),separators=(',',':'))
