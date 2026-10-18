"""Action-level check of the null-coordinate equations of Paper F from the LITERATURE action.
Reduced 2D Horndeski action of 4D quasi-topological gravity (Bueno, Cano, Hennigar, Murcia, arXiv:2509.19016, Eqs. (22)-(26)):
   S_2d = (1/2G) int d^2x sqrt(-g) L2d,  L2d = G2 - box(r) G3 + G4 R + (-2 G4_X)[(box r)^2 - r_ab r^ab],  X=(grad r)^2, psi=(1-X)/r^2,
   G2 = r^2 [3h - 2 psi h'],  G3 = 2 r h'(psi),  G4 = -(1/2) r^2 psi int dpsi psi^-2 h'(psi)       (h has no psi^2 term in D=4).
plus the massless scalar, S_m = -2 pi int d^2x sqrt(-g) r^2 (grad phi)^2 (G=1).  Double-null gauge ds^2=-W du dv, W=e^sigma.
We compute the Euler-Lagrange expressions E_W, E_r by automatic differentiation of L with respect to the jet variables (dual numbers over exact rational
bivariate Taylor jets), at random points, with h a random polynomial. Tests:
  A  the action of the static reduction (action_check.py) and the literature action give identical E_W and E_r (off shell);
  B  E_W = 0 is Paper F's r_uv equation; E_r = 0 (with the Raychaudhuri constraints) is Paper F's sigma_uv equation including the c3 term;
  C  controls: a wrong Raychaudhuri coefficient is detected.
usage: action_check2.py nseeds"""
import sys, random
from fractions import Fraction as Fr
import action_check as A1
from action_check import J, PI, pmul, padd, pscale, dX, dr, mulX, mulr, ppow, pev
A1.N=5
N=6
J.__init__.__defaults__=(N,)
class D:
    """dual number: value J and tangents {slot: J}"""
    __slots__=('v','t')
    def __init__(s,v,t=None): s.v=v; s.t=t or {}
    def _c(o,ref): return o if isinstance(o,D) else D(J.const(o,ref.v.n) if not isinstance(o,J) else o)
    def __add__(a,b):
        b=D._c(b,a); t=dict(a.t)
        for k,x in b.t.items(): t[k]=t[k]+x if k in t else x
        return D(a.v+b.v,t)
    __radd__=__add__
    def __neg__(a): return D(-a.v,{k:-x for k,x in a.t.items()})
    def __sub__(a,b): return a+(-D._c(b,a))
    def __rsub__(a,b): return (-a)+b
    def __mul__(a,b):
        b=D._c(b,a); t={}
        for k,x in a.t.items(): t[k]=x*b.v
        for k,x in b.t.items(): t[k]=t[k]+a.v*x if k in t else a.v*x
        return D(a.v*b.v,t)
    __rmul__=__mul__
    def inv(a):
        iv=a.v.inv(); m=-(iv*iv)
        return D(iv,{k:x*m for k,x in a.t.items()})
    def __truediv__(a,b):
        b=D._c(b,a); return a*b.inv()
    def __rtruediv__(a,b): return D._c(b,a)*a.inv()
    def __pow__(a,m):
        if m<0: return (a.inv())**(-m)
        o=D(J.const(1,a.v.n))
        for _ in range(m): o=o*a
        return o
def pevD(a,X,r):
    out=None
    for (i,j),v in a.items():
        t=(X**i)*(r**j)*v
        out=t if out is None else out+t
    return out
def lit_G(acoef):
    """G2,G3,G4 of the literature as Laurent polynomials in (X,r); a_2 must vanish (Gauss-Bonnet is topological in D=4)."""
    assert acoef.get(2,0)==0
    psi={(0,-2):Fr(1),(1,-2):Fr(-1)}
    h={}; hp={}
    for k,a in acoef.items():
        h=padd(h,pscale(ppow(psi,k),a)); hp=padd(hp,pscale(ppow(psi,k-1),a*k))
    G2=mulr(padd(pscale(h,3),pscale(pmul(psi,hp),2),-1),2)          # r^2 (3h - 2 psi h')
    G3=pscale(mulr(hp,1),2)                                          # 2 r h'
    # G4 = -(1/2) r^2 psi [ int psi^-2 h' dpsi ],  h' = sum k a_k psi^(k-1):  int = -a_1/psi + sum_{k>=3} k a_k psi^(k-2)/(k-2)
    I={}
    for k,a in acoef.items():
        if k==1: I=padd(I,pscale(ppow(psi,-1) if False else {},0))
    inner={}
    for k,a in acoef.items():
        if k>=3: inner=padd(inner,pscale(ppow(psi,k-2),a*Fr(k,k-2)))
    # psi * int = -a_1 + psi * inner
    pint=padd({(0,0):-acoef[1]},pmul(psi,inner))
    G4=pscale(mulr(pint,2),Fr(-1,2))
    return dict(G2=G2,G3=G3,G4=G4,G4X=dX(G4))
SLOTS=['r','ru','rv','ruu','ruv','rvv','W','Wu','Wv','Wuv','phu','phv']
def build_L(kind,P,Lc,fields):
    r,W,ph=fields
    ru0,rv0=r.du(),r.dv()
    vals={'r':r,'ru':ru0,'rv':rv0,'ruu':ru0.du(),'ruv':ru0.dv(),'rvv':rv0.dv(),'W':W,'Wu':W.du(),'Wv':W.dv(),'Wuv':W.du().dv(),'phu':ph.du(),'phv':ph.dv()}
    V={k:D(vals[k],{k:J.const(1,vals[k].n)}) for k in SLOTS}
    rr,ru,rv,ruu,ruv,rvv,Wd,Wu,Wv,Wuv,phu,phv=[V[k] for k in SLOTS]
    X=-4*ru*rv/Wd
    suv=Wuv/Wd-Wu*Wv/(Wd*Wd)
    boxr=-4*ruv/Wd; Rc=4*suv/Wd
    rayu=ruu-Wu/Wd*ru; rayv=rvv-Wv/Wd*rv
    sq=Fr(8)*(ruv*ruv-rayu*rayv)/(Wd*Wd)          # (box r)^2 - r_ab r^ab
    if kind=='lit':
        G2=pevD(P['G2'],X,rr); G3=pevD(P['G3'],X,rr); G4=pevD(P['G4'],X,rr); G4X=pevD(P['G4X'],X,rr)
        Lg=Fr(1,2)*(Wd*Fr(1,2))*(G2-boxr*G3+G4*Rc-2*G4X*sq)       # (1/2G) sqrt(-g) L2d,  sqrt(-g)=W/2
    else:   # action derived from the static reduction (action_check.py): L = (W/2)G2 - 2 G3 r_uv + 2 F sigma_uv
        G2=pevD(P['G2'],X,rr); G3=pevD(P['G3'],X,rr); Fp=None
        Lg=(Wd*Fr(1,2))*(G2+G3*boxr)+2*pevD(P['F'],{},rr)*suv if False else (Wd*Fr(1,2))*(G2+G3*boxr)+2*Fcall(P,rr)*suv
    Lm=4*PI*rr*rr*phu*phv
    return Lg+Lm
def Fcall(P,rr):
    # F(r) = int F' dr  (Laurent in r, no log: a_2=0 means no 1/r term in F')
    F={ (0,j+1):v/(j+1) for (i,j),v in P['Fp'].items()}
    assert all(j!=-1 for (_,j) in P['Fp'])
    return pevD(F,rr,rr) if False else pevD(F,D(J.const(0,rr.v.n)),rr)
def EL(Ld):
    t=Ld.t
    g=lambda k: t.get(k,J.const(0,N-2))
    Er=g('r')-g('ru').du()-g('rv').dv()+g('ruu').du().du()+g('ruv').du().dv()+g('rvv').dv().dv()
    EW=g('W')-g('Wu').du()-g('Wv').dv()+g('Wuv').du().dv()
    return Er.v0(),EW.v0()
def setup_fields(seed,acoef,Kscale,PHI,alpha,P_h):
    rnd=random.Random(seed); R=lambda a,b: Fr(rnd.randint(-a,a),b)
    def rand_jet(c0,amp=Fr(1,3)):
        c={(0,0):Fr(c0)}
        for i in range(N+1):
            for j in range(N+1-i):
                if (i,j)!=(0,0): c[(i,j)]=R(5,10)*amp/(1+i+j)
        return c
    rc=rand_jet(Fr(11,10)); rc[(1,0)]=R(8,10)+Fr(1,5); rc[(0,1)]=-abs(R(8,10))-Fr(1,4)
    Wc=rand_jet(Fr(7,5)); phc=rand_jet(0)
    for k in list(phc):
        if sum(k)<=2: phc[k]*=PHI
    for k in ((1,0),(0,1)):
        if phc[k]==0: phc[k]=Fr(1,3)*PHI
    return rc,Wc,phc
def h_funcs(acoef):
    psi={(0,-2):Fr(1),(1,-2):Fr(-1)}
    h={}; hp={}
    for k,a in acoef.items():
        h=padd(h,pscale(ppow(psi,k),a)); hp=padd(hp,pscale(ppow(psi,k-1),a*k))
    return h,hp
def run(seed,acoef,Kscale=Fr(1),PHI=Fr(1),alpha=Fr(0)):
    Plit=lit_G(acoef); Pmine=A1.build(acoef); h,hp_=h_funcs(acoef)
    rc,Wc,phc=setup_fields(seed,acoef,Kscale,PHI,alpha,None)
    def fields(w11=None,extra=None):
        r=J(dict(rc),N); W=J(dict(Wc),N); ph=J(dict(phc),N)
        if w11 is not None: W.c[(1,1)]=w11
        return r,W,ph
    def derived(r,W):
        ru,rv=r.du(),r.dv(); X=-4*ru*rv/W; psi=(1+4*ru*rv/W)/(r*r)
        return ru,rv,X,pev(h,X,r),pev(hp_,X,r),psi
    # constraints at the point
    r,W,ph=fields(Wc[(1,1)]); ru,rv,X,hh,hp,psi=derived(r,W)
    c0=(Kscale*(1+alpha*psi)*4*PI/hp).v0()
    rc[(2,0)]=(W.du().v0()/W.v0()*ru.v0()-c0*r.v0()*ph.du().v0()**2)/2
    rc[(0,2)]=(W.dv().v0()/W.v0()*rv.v0()-c0*r.v0()*ph.dv().v0()**2)/2
    # r_uv equation to second order in the jet:  r_uv = -W r Q/4,  Q=3h/h'-2psi
    for m in range(0,3):
        r,W,ph=fields(Wc[(1,1)]); ru,rv,X,hh,hp,psi=derived(r,W)
        S=-(W*r*(3*hh/hp-2*psi))*Fr(1,4)
        for i in range(m+1):
            j=m-i; rc[(i+1,j+1)]=S.c.get((i,j),Fr(0))/((i+1)*(j+1))
    out={}
    def ELs(kind,w11):
        P=Plit if kind=='lit' else Pmine
        Ld=build_L(kind,P,None,fields(w11))
        return EL(Ld)
    # A: identical Euler-Lagrange expressions (off shell: perturb r_uv, r_uu, r_uuu)
    save=dict(rc)
    rc[(1,1)]+=Fr(1,7); rc[(2,0)]+=Fr(1,5); rc[(3,0)]+=Fr(1,9); rc[(1,2)]+=Fr(1,11)
    EL_l=ELs('lit',Wc[(1,1)]); EL_m=ELs('mine',Wc[(1,1)])
    out['A_Er_off_shell_diff']=EL_l[0]-EL_m[0]; out['A_EW_off_shell_diff']=EL_l[1]-EL_m[1]
    out['A_Er_value']=EL_l[0]
    rc.clear(); rc.update(save)
    # B: E_W on shell, and sigma_uv from E_r = 0
    out['B_EW_on_shell']=ELs('lit',Wc[(1,1)])[1]
    e0=ELs('lit',Fr(0))[0]; e1=ELs('lit',Fr(1))[0]; w11=-e0/(e1-e0)
    r,W,ph=fields(w11); ru,rv,X,hh,hp,psi=derived(r,W)
    suv=(W.du().dv()/W-W.du()*W.dv()/(W*W)).v0()
    phu,phv=ph.du().v0(),ph.dv().v0(); psi0=psi.v0(); h0=hh.v0(); hp0=hp.v0(); W0=W.v0()
    hpp0=sum(a*k*(k-1)*psi0**(k-2) for k,a in acoef.items() if k>=2)
    c2=9*h0**2*hpp0/(4*hp0**3); c3=hpp0/hp0**3
    paper=W0*psi0/2-W0*c2-8*PI/hp0*phu*phv+64*PI**2*c3/W0*phu**2*phv**2
    out['B_suv_diff']=suv-paper; out['c3_term']=64*PI**2*c3/W0*phu**2*phv**2
    out['B_diff_if_c3_dropped']=suv-(paper-out['c3_term'])
    # E_r independent of r_uuu (third derivative) -> second-order equation
    rc[(3,0)]+=Fr(1,3); e0b=ELs('lit',Fr(0))[0]; rc[(3,0)]-=Fr(1,3)
    out['B_Er_indep_of_r_uuu']=e0b-e0
    return out
if __name__=='__main__':
    ns=int(sys.argv[1]) if len(sys.argv)>1 else 4
    for seed in range(1,ns+1):
        rnd=random.Random(2000+seed); deg=4+(seed%2)
        acoef={1:Fr(1),2:Fr(0)}
        for k in range(3,deg+1): acoef[k]=Fr(rnd.randint(-3,3),7+2*k)
        acoef[deg]=abs(acoef[deg])+Fr(1,17)
        print('seed %d  h = psi + sum_{k>=3} a_k psi^k, degree %d,'%(seed,deg),{k:str(v) for k,v in acoef.items() if k>2})
        for K,PHI,al in ((Fr(1),Fr(1),0),(Fr(1),Fr(6),0),(Fr(11,10),Fr(6),0),(Fr(1),Fr(6),Fr(1,5))):
            o=run(seed,acoef,K,PHI,al)
            z=lambda x:'0 (exact)' if x==0 else '%.3e'%float(x)
            tag='c=4pi/h' if (K==1 and al==0) else '[CONTROL c*%s*(1+%s psi)]'%(K,al)
            print('  PHI=%-2s %-28s A: E_r(lit)-E_r(static-red.)=%s  E_W: %s | B: E_W on shell=%s  sigma_uv(action)-sigma_uv(paper)=%s  (c3 term %.2e; if dropped: %.2e)  E_r indep. of r_uuu: %s'%(
                PHI,tag,z(o['A_Er_off_shell_diff']),z(o['A_EW_off_shell_diff']),z(o['B_EW_on_shell']),z(o['B_suv_diff']),float(o['c3_term']),float(o['B_diff_if_c3_dropped']),z(o['B_Er_indep_of_r_uuu'])))
