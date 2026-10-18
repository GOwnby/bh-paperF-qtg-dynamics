"""Same as action_check2.py but for h WITH a psi^2 term (a_2 != 0, e.g. the Hayward h = psi/(1-l^2 psi) = psi + l^2 psi^2 + ...).
The literature G4 (arXiv:2509.19016 Eq. 26) then contains  -a_2 r^2 psi ln psi  (and G4_X contains a_2 (ln psi + 1)); the static-reduction action has no logarithm of psi (only ln r in F).
Arithmetic is exact rational except for the logarithms (float64), so 'exact zero' becomes ~1e-13."""
import sys, random, math
from fractions import Fraction as Fr
import action_check as A1
import action_check2 as A2
from action_check import J, PI
from action_check2 import D, N, pevD, EL, SLOTS, lit_G, h_funcs, setup_fields
def Jlog(a):
    c0=a.c[(0,0)]; x=(a-c0)*(1/c0); out=J({(0,0):math.log(float(c0))},a.n); p=J.const(1,a.n)
    for k in range(1,a.n+1):
        p=p*x; out=out+p*(Fr((-1)**(k+1),k))
    return out
def Dlog(d):
    lv=Jlog(d.v); iv=d.v.inv()
    return D(lv,{k:x*iv for k,x in d.t.items()})
def lit_G2(acoef):
    a2=acoef.get(2,Fr(0)); ac=dict(acoef); ac[2]=Fr(0)
    P=lit_G(ac); P['a2']=a2
    # G2 and G3 contain the psi^2 term of h as well: rebuild with the full h
    psi={(0,-2):Fr(1),(1,-2):Fr(-1)}
    h={}; hp={}
    for k,a in acoef.items():
        h=A1.padd(h,A1.pscale(A1.ppow(psi,k),a)); hp=A1.padd(hp,A1.pscale(A1.ppow(psi,k-1),a*k))
    P['G2']=A1.mulr(A1.padd(A1.pscale(h,3),A1.pscale(A1.pmul(psi,hp),2),-1),2)
    P['G3']=A1.pscale(A1.mulr(hp,1),2)
    return P
def build_L(kind,P,fields,acoef):
    r,W,ph=fields
    ru0,rv0=r.du(),r.dv()
    vals={'r':r,'ru':ru0,'rv':rv0,'ruu':ru0.du(),'ruv':ru0.dv(),'rvv':rv0.dv(),'W':W,'Wu':W.du(),'Wv':W.dv(),'Wuv':W.du().dv(),'phu':ph.du(),'phv':ph.dv()}
    V={k:D(vals[k],{k:J.const(1,vals[k].n)}) for k in SLOTS}
    rr,ru,rv,ruu,ruv,rvv,Wd,Wu,Wv,Wuv,phu,phv=[V[k] for k in SLOTS]
    X=-4*ru*rv/Wd; suv=Wuv/Wd-Wu*Wv/(Wd*Wd); boxr=-4*ruv/Wd; Rc=4*suv/Wd
    rayu=ruu-Wu/Wd*ru; rayv=rvv-Wv/Wd*rv; sq=Fr(8)*(ruv*ruv-rayu*rayv)/(Wd*Wd)
    G2=pevD(P['G2'],X,rr); G3=pevD(P['G3'],X,rr)
    if kind=='lit':
        a2=P['a2']; psi=(1-X)/(rr*rr); lp=Dlog(psi)
        G4=pevD(P['G4'],X,rr)-a2*rr*rr*psi*lp
        G4X=pevD(P['G4X'],X,rr)+a2*(lp+1)
        Lg=Fr(1,2)*(Wd*Fr(1,2))*(G2-boxr*G3+G4*Rc-2*G4X*sq)
    else:
        # F(r)=int F' dr : F' = kappa r h'(1/r^2) = (1/2)(r + 2 a2/r + ...): the 1/r term integrates to ln r
        Fp=P['Fp']; Fd={}
        for (i,j),v in Fp.items():
            if j!=-1: Fd[(0,j+1)]=v/(j+1)
        F=pevD(Fd,D(J.const(0,rr.v.n)),rr)+Fp.get((0,-1),Fr(0))*Dlog(rr)
        Lg=(Wd*Fr(1,2))*(G2+G3*boxr)+2*F*suv
    return Lg+4*PI*rr*rr*phu*phv
def run(seed,acoef,Kscale=Fr(1),PHI=Fr(1),alpha=Fr(0)):
    Plit=lit_G2(acoef); Pmine=A1.build(acoef); h,hp_=h_funcs(acoef)
    rc,Wc,phc=setup_fields(seed,acoef,Kscale,PHI,alpha,None)
    Wc[(0,0)]=Fr(6)
    def fields(w11=None):
        r=J(dict(rc),N); W=J(dict(Wc),N); ph=J(dict(phc),N)
        if w11 is not None: W.c[(1,1)]=w11
        return r,W,ph
    def derived(r,W):
        ru,rv=r.du(),r.dv(); X=-4*ru*rv/W; psi=(1+4*ru*rv/W)/(r*r)
        return ru,rv,X,A1.pev(h,X,r),A1.pev(hp_,X,r),psi
    r,W,ph=fields(Wc[(1,1)]); ru,rv,X,hh,hp,psi=derived(r,W)
    assert psi.v0()>0
    c0=(Kscale*(1+alpha*psi)*4*PI/hp).v0()
    rc[(2,0)]=(W.du().v0()/W.v0()*ru.v0()-c0*r.v0()*ph.du().v0()**2)/2
    rc[(0,2)]=(W.dv().v0()/W.v0()*rv.v0()-c0*r.v0()*ph.dv().v0()**2)/2
    for m in range(0,3):
        r,W,ph=fields(Wc[(1,1)]); ru,rv,X,hh,hp,psi=derived(r,W)
        S=-(W*r*(3*hh/hp-2*psi))*Fr(1,4)
        for i in range(m+1):
            j=m-i; rc[(i+1,j+1)]=S.c.get((i,j),Fr(0))/((i+1)*(j+1))
    out={}
    def ELs(kind,w11):
        P=Plit if kind=='lit' else Pmine
        return EL(build_L(kind,P,fields(w11),acoef))
    save=dict(rc)
    rc[(1,1)]+=Fr(1,7); rc[(2,0)]+=Fr(1,5); rc[(3,0)]+=Fr(1,9); rc[(1,2)]+=Fr(1,11)
    a=ELs('lit',Wc[(1,1)]); b=ELs('mine',Wc[(1,1)])
    out['A_Er']=float(a[0]-b[0]); out['A_EW']=float(a[1]-b[1]); out['A_scale']=abs(float(a[0]))+abs(float(a[1]))
    rc.clear(); rc.update(save)
    out['B_EW']=float(ELs('lit',Wc[(1,1)])[1])
    e0=ELs('lit',Fr(0))[0]; e1=ELs('lit',Fr(1))[0]; w11=-e0/(e1-e0)
    r,W,ph=fields(w11); ru,rv,X,hh,hp,psi=derived(r,W)
    suv=float((W.du().dv()/W-W.du()*W.dv()/(W*W)).v0())
    phu,phv=ph.du().v0(),ph.dv().v0(); psi0=psi.v0(); h0=hh.v0(); hp0=hp.v0(); W0=W.v0()
    hpp0=sum(a*k*(k-1)*psi0**(k-2) for k,a in acoef.items() if k>=2)
    c2=9*h0**2*hpp0/(4*hp0**3); c3=hpp0/hp0**3
    c3t=64*PI**2*c3/W0*phu**2*phv**2
    paper=float(W0*psi0/2-W0*c2-8*PI/hp0*phu*phv+c3t)
    out['B_suv_diff']=suv-paper; out['c3_term']=float(c3t); out['B_diff_if_c3_dropped']=suv-(paper-float(c3t)); out['suv']=suv
    return out
if __name__=='__main__':
    ns=int(sys.argv[1]) if len(sys.argv)>1 else 3
    for seed in range(1,ns+1):
        rnd=random.Random(3000+seed); deg=4
        acoef={1:Fr(1)}
        for k in range(2,deg+1): acoef[k]=Fr(rnd.randint(-3,3),7+2*k)
        acoef[2]=abs(acoef[2])+Fr(1,5)       # Hayward-like: positive psi^2 coefficient
        acoef[deg]=abs(acoef[deg])+Fr(1,17)
        print('seed %d  h = psi + sum a_k psi^k (a_2 != 0),'%seed,{k:str(v) for k,v in acoef.items() if k>1})
        for K,PHI,al in ((Fr(1),Fr(1),0),(Fr(1),Fr(6),0),(Fr(11,10),Fr(6),0)):
            o=run(seed,acoef,K,PHI,al)
            tag='c=4pi/h' if (K==1 and al==0) else '[CONTROL c*%s]'%K
            print('  PHI=%-2s %-16s A: |E_r(lit)-E_r(static-red.)|=%.1e |E_W diff|=%.1e (scale %.1e) | B: E_W on shell=%.1e  sigma_uv(action)-sigma_uv(paper)=%.2e  (c3 term %.2e; if dropped: %.2e)'%(
                PHI,tag,abs(o['A_Er']),abs(o['A_EW']),o['A_scale'],o['B_EW'],o['B_suv_diff'],o['c3_term'],o['B_diff_if_c3_dropped']))
