"""Action-level derivation check (Paper F): 2D reduced action of quasi-topological gravity + massless scalar, double-null gauge.
 S = int du dv [ (W/2) G2(r,X) - 2 G3(r,X) r_uv + 2 F(r) sigma_uv + 4 pi r^2 phi_u phi_v ],  W=e^sigma, X=-4 r_u r_v/W,
 i.e. the covariant L = G2(r,X) + G3(r,X) box r + F(r) R  (sqrt(-g)=W/2, box r=-4 r_uv/W, R=4 sigma_uv/W)  with G2,G3,F fixed ONLY by the static
 reduction  L_static = (1/2) N d/dr[r^3 h(psi)]  (Lagrangian reduction property of QTG, Bueno-Cano-Hennigar 2019) and analyticity in X at X=0.
 We evaluate the Euler-Lagrange expressions E_sigma, E_r, E_phi exactly (rational arithmetic, bivariate truncated Taylor jets) at random points and compare
 with the equations of Paper F: r_uv eq, sigma_uv eq (incl. the c3 term), propagation of the Raychaudhuri constraints.  h = polynomial of degree 4 with random coefficients (h''' != 0).
 usage: action_check.py [seed]"""
import sys, random
from fractions import Fraction as Fr
N=5   # jet order (total degree)
PI=Fr(22,7)   # formal stand-in for pi: the identities are algebraic in pi
class J:
    __slots__=('c','n')
    def __init__(s,c,n=N): s.c=c; s.n=n
    @staticmethod
    def const(a,n=N): return J({(0,0):Fr(a)},n)
    def __add__(a,b):
        if not isinstance(b,J): b=J.const(b,a.n)
        n=min(a.n,b.n); c=dict(a.c)
        for k,v in b.c.items(): c[k]=c.get(k,0)+v
        return J({k:v for k,v in c.items() if sum(k)<=n},n)
    __radd__=__add__
    def __neg__(a): return J({k:-v for k,v in a.c.items()},a.n)
    def __sub__(a,b): return a+(-b if isinstance(b,J) else -Fr(b))
    def __rsub__(a,b): return (-a)+b
    def __mul__(a,b):
        if not isinstance(b,J): return J({k:v*Fr(b) for k,v in a.c.items()},a.n)
        n=min(a.n,b.n); c={}
        for (i,j),x in a.c.items():
            for (k,l),y in b.c.items():
                if i+j+k+l<=n: c[(i+k,j+l)]=c.get((i+k,j+l),0)+x*y
        return J(c,n)
    __rmul__=__mul__
    def inv(a):
        a0=a.c.get((0,0),0); assert a0!=0
        x=(a-a0)*(1/a0); out=J.const(1,a.n); p=J.const(1,a.n)
        for k in range(1,a.n+1):
            p=p*(-x); out=out+p
        return out*(1/a0)
    def __truediv__(a,b): return a*(b.inv() if isinstance(b,J) else Fr(1)/Fr(b))
    def __rtruediv__(a,b): return a.inv()*b
    def __pow__(a,m):
        if m<0: return (a.inv())**(-m)
        out=J.const(1,a.n)
        for _ in range(m): out=out*a
        return out
    def du(a): return J({(i-1,j):v*i for (i,j),v in a.c.items() if i>0},a.n-1)
    def dv(a): return J({(i,j-1):v*j for (i,j),v in a.c.items() if j>0},a.n-1)
    def v0(a): return a.c.get((0,0),Fr(0))
# ---------- Laurent polynomials in (X, r): dict {(i,j): c} = c X^i r^j
def pmul(a,b):
    o={}
    for (i,j),x in a.items():
        for (k,l),y in b.items(): o[(i+k,j+l)]=o.get((i+k,j+l),0)+x*y
    return o
def padd(a,b,s=1):
    o=dict(a)
    for k,v in b.items(): o[k]=o.get(k,0)+s*v
    return {k:v for k,v in o.items() if v!=0}
def pscale(a,s): return {k:v*s for k,v in a.items()}
def dX(a): return {(i-1,j):v*i for (i,j),v in a.items() if i!=0}
def dr(a): return {(i,j-1):v*j for (i,j),v in a.items() if j!=0}
def mulX(a): return {(i+1,j):v for (i,j),v in a.items()}
def mulr(a,m=1): return {(i,j+m):v for (i,j),v in a.items()}
def ppow(a,m):
    o={(0,0):Fr(1)}
    for _ in range(m): o=pmul(o,a)
    return o
def pev(a,X,r):
    out=None
    for (i,j),v in a.items():
        t=(X**i if i>=0 else (X**(-i)).inv())*(r**j)*v
        out=t if out is None else out+t
    return out if out is not None else J.const(0,X.n)
def build(acoef,kappa=Fr(1,2)):
    """acoef = {k: a_k} for h(psi)=sum_k a_k psi^k (a_1=1).  Returns the Laurent polynomials G2,G3,Fp (= dF/dr) fixed by the static reduction."""
    psi={(0,-2):Fr(1),(1,-2):Fr(-1)}          # (1-X)/r^2
    h={}; hp={}
    for k,a in acoef.items():
        h=padd(h,pscale(ppow(psi,k),a)); hp=padd(hp,pscale(ppow(psi,k-1),a*k))
    A=pscale(mulr(padd(pscale(h,3),pmul(psi,hp),-2) if False else padd(pscale(h,3),pscale(pmul(psi,hp),2),-1),2),kappa)   # kappa r^2 (3h-2 psi h')
    B=pscale(mulr(hp,1),-kappa)               # -kappa r h'
    Fp={k:v for k,v in pscale(B,-1).items() if k[0]==0}   # F' = -B(r,X=0)
    S=padd(B,Fp)                              # B+F' has no X^0 term
    assert all(k[0]>=1 for k in S)
    G3X=pscale({(i-1,j):v for (i,j),v in S.items()},-1)   # G3_X = -(B+F')/X
    G3={(i+1,j):v/(i+1) for (i,j),v in G3X.items()}
    G3r=dr(G3); Fpp={(0,j-1):v*j for (i,j),v in Fp.items()}
    G2=padd(padd(A,mulX(G3r)),pscale(mulX(Fpp),2))        # A + X G3_r + 2 X F''
    return dict(h=h,hp=hp,A=A,B=B,Fp=Fp,Fpp=Fpp,G3=G3,G3X=G3X,G3r=G3r,G2=G2,G2X=dX(G2),G2r=dr(G2))
def run(seed,acoef,Kscale=Fr(1),PHI=Fr(1),alpha=Fr(0)):
    rnd=random.Random(seed)
    R=lambda a,b: Fr(rnd.randint(-a,a),b)
    P=build(acoef)
    # fields as polynomials of degree N in (s,t) = (u-u0, v-v0); W and r positive
    def rand_jet(c0,amp=Fr(1,3)):
        c={(0,0):Fr(c0)}
        for i in range(N+1):
            for j in range(N+1-i):
                if (i,j)!=(0,0): c[(i,j)]=R(5,10)*amp/(1+i+j)
        return c
    rc=rand_jet(Fr(11,10)); rc[(1,0)]=R(8,10); rc[(0,1)]=-abs(R(8,10))-Fr(1,4)    # r_u r_v<0 (interior of a trapped region)
    Wc=rand_jet(Fr(7,5)); phc=rand_jet(0)
    for k in list(phc):
        if sum(k)<=2: phc[k]*=PHI
    for k in ((1,0),(0,1)):
        if phc[k]==0: phc[k]=Fr(1,3)*PHI
    def fields(w11=None):
        r=J(dict(rc)); W=J(dict(Wc)); ph=J(dict(phc))
        if w11 is not None: W.c[(1,1)]=w11
        return r,W,ph
    # --- impose (i) r_uv equation at the point and to first order (r_21,r_12), (ii) the two Raychaudhuri constraints at the point
    def derived(r,W,ph):
        ru,rv=r.du(),r.dv(); ruv=ru.dv()
        X=-4*ru*rv/W; psi=(1+4*ru*rv/W)/(r*r)
        hh=pev(P['h'],X,r); hp=pev(P['hp'],X,r)
        return ru,rv,ruv,X,psi,hh,hp
    # step 1: Raychaudhuri constraints at the point (r_20, r_02)
    r,W,ph=fields(Wc[(1,1)]); ru,rv,ruv,X,psi,hh,hp=derived(r,W,ph)
    ph_u=ph.du(); ph_v=ph.dv()
    cc=Kscale*(1+alpha*psi)*4*PI/hp; c0=cc.v0()
    Wu0=W.du().v0(); Wv0=W.dv().v0(); W0=W.v0()
    rc[(2,0)]=(Wu0/W0*ru.v0()-c0*r.v0()*ph_u.v0()**2)/2      # r_uu - sigma_u r_u = -c r phi_u^2
    rc[(0,2)]=(Wv0/W0*rv.v0()-c0*r.v0()*ph_v.v0()**2)/2
    # step 2: r_uv equation at the point and to first order (r_11, r_21, r_12)
    r,W,ph=fields(Wc[(1,1)]); ru,rv,ruv,X,psi,hh,hp=derived(r,W,ph)
    Q=3*hh/hp-2*psi
    S=-(W*r*Q)*Fr(1,4)
    rc[(1,1)]=S.c[(0,0)]
    r,W,ph=fields(Wc[(1,1)]); ru,rv,ruv,X,psi,hh,hp=derived(r,W,ph)      # psi_u contains r_uv: rebuild with r_11 in place
    Q=3*hh/hp-2*psi; S=-(W*r*Q)*Fr(1,4)
    rc[(2,1)]=S.c[(1,0)]/2; rc[(1,2)]=S.c[(0,1)]/2
    def E_r(w11):
        r,W,ph=fields(w11); ru,rv,ruv,X,psi,hh,hp=derived(r,W,ph)
        Wu,Wv=W.du(),W.dv(); suv=W.du().dv()/W-Wu*Wv/(W*W)
        phu,phv=ph.du(),ph.dv()
        G2r=pev(P['G2r'],X,r); G2X=pev(P['G2X'],X,r); G3r=pev(P['G3r'],X,r); Y=pev(P['G3X'],X,r); G3=pev(P['G3'],X,r); Fp=pev(P['Fp'],X,r)
        Pr=W*G2r*Fr(1,2)-2*G3r*ruv+2*Fp*suv+8*PI*r*phu*phv
        Pru=-2*rv*G2X+8*rv*Y*ruv/W
        Prv=-2*ru*G2X+8*ru*Y*ruv/W
        Pruv=-2*G3
        return (Pr-Pru.du()-Prv.dv()+Pruv.du().dv()).v0()
    def E_sig():
        r,W,ph=fields(Wc[(1,1)]); ru,rv,ruv,X,psi,hh,hp=derived(r,W,ph)
        G2=pev(P['G2'],X,r); G2X=pev(P['G2X'],X,r); Y=pev(P['G3X'],X,r); Fp=pev(P['Fp'],X,r); Fpp=pev(P['Fpp'],X,r)
        return (W*(G2-X*G2X)*Fr(1,2)+2*X*Y*ruv+2*(Fpp*ru*rv+Fp*ruv)).v0()
    out={}
    # (T1) sigma-equation: E_sigma = 2 kappa r h' (r_uv + W r Q/4) for arbitrary jets (here r_uv is on shell -> 0); test also off-shell
    rc2=dict(rc); rc2[(1,1)]=rc[(1,1)]+Fr(1,3)
    save=rc; rc=rc2
    r,W,ph=fields(Wc[(1,1)]); ru,rv,ruv,X,psi,hh,hp=derived(r,W,ph); Q=3*hh/hp-2*psi
    out['T1_off_shell']=E_sig()-(2*Fr(1,2)*r*hp*(ruv+W*r*Q*Fr(1,4))).v0()
    rc=save
    out['T1_on_shell']=E_sig()
    # (T2) sigma_uv from E_r = 0
    e0=E_r(Fr(0)); e1=E_r(Fr(1)); w11=-e0/(e1-e0)
    r,W,ph=fields(w11); ru,rv,ruv,X,psi,hh,hp=derived(r,W,ph)
    Wu,Wv=W.du(),W.dv(); suv=(W.du().dv()/W-Wu*Wv/(W*W)).v0()
    phu,phv=ph.du().v0(),ph.dv().v0()
    hpp=pev(dX({}),X,r) if False else None
    # h'' from the polynomial (derivative of hp with respect to psi): sum k(k-1) a_k psi^(k-2)
    psi0=psi.v0(); h0=hh.v0(); hp0=hp.v0()
    hpp0=sum(a*k*(k-1)*psi0**(k-2) for k,a in acoef.items() if k>=2)
    c2=9*h0**2*hpp0/(4*hp0**3); c3=hpp0/hp0**3; W0=W.v0()
    paper=W0*psi0/2-W0*c2-8*PI/hp0*phu*phv+64*PI**2*c3/W0*phu**2*phv**2*Kscale**2*0+64*PI**2*c3/W0*phu**2*phv**2
    out['T2_suv_action']=suv; out['T2_suv_paper']=paper; out['T2_diff']=suv-paper
    out['c3_term']=64*PI**2*c3/W0*phu**2*phv**2
    out['T2_diff_if_c3_dropped']=suv-(paper-out['c3_term'])
    # (T3) propagation of the u-Raychaudhuri constraint: d_v[ r_uu - sigma_u r_u + c r phi_u^2 ] = 0 on the constraint surface
    # d_v of  C_u = Ray_u + c r phi_u^2 with sigma_uv from E_r, r_uuv from the r_uv equation, phi_uv from E_phi
    r_,W_,ph_=fields(w11); ru,rv,ruv,X,psi,hh,hp=derived(r_,W_,ph_)
    Wu,Wv=W_.du(),W_.dv(); sig_u=Wu/W_; suvJ=W_.du().dv()/W_-Wu*Wv/(W_*W_)
    phu,phv=ph_.du(),ph_.dv()
    # phi_uv from the scalar equation, as a jet: need phi_uv jet to first order -> take the jet of the right-hand side
    phuv=-(ru*phv+rv*phu)/r_
    cJ=Kscale*(1+alpha*psi)*4*PI/hp
    Cu=ru.du()-sig_u*ru+cJ*r_*phu*phu
    Cu_v=(ru.du().dv()-sig_u.dv()*ru-sig_u*ruv)+cJ.dv()*r_*phu*phu+cJ*rv*phu*phu+2*cJ*r_*phu*phuv
    # sig_u.dv() = d_v(W_u/W) = W_uv/W - W_u W_v/W^2 = sigma_uv  (same as suvJ)
    out['T3_Cu']=Cu.v0(); out['T3_dvCu']=Cu_v.v0()
    return out
if __name__=='__main__':
    seeds=range(1,int(sys.argv[1])+1) if len(sys.argv)>1 else range(1,7)
    worst=0
    for seed in seeds:
        rnd=random.Random(1000+seed); deg=4 if seed%2 else 6
        acoef={1:Fr(1)}
        for k in range(2,deg+1): acoef[k]=Fr(rnd.randint(-3,3),7+2*k)
        acoef[deg]=abs(acoef[deg])+Fr(1,17)
        print('seed %d  h(psi)=sum a_k psi^k, degree %d, a ='%(seed,deg),{k:str(v) for k,v in acoef.items()})
        for K,PHI,al in ((Fr(1),Fr(1),0),(Fr(1),Fr(6),0),(Fr(1),Fr(25),0),(Fr(11,10),Fr(6),0),(Fr(1),Fr(6),Fr(1,5))):
            o=run(seed,acoef,K,PHI,al)
            tag='c=4pi/h'+('' if (K==1 and al==0) else "  [CONTROL: c multiplied by %s*(1+%s psi)]"%(K,al))
            print('  PHI=%-3s %-62s |E_sigma on shell|=%s  sigma_uv(action)-sigma_uv(paper)=%s  d_v C_u=%s  (c3 term=%.3e; without it the difference would be %.3e)'%(PHI,tag,o['T1_on_shell'],
                  '0 (exact)' if o['T2_diff']==0 else '%.3e'%float(o['T2_diff']), '0 (exact)' if o['T3_dvCu']==0 else '%.3e'%float(o['T3_dvCu']), float(o['c3_term']), float(o['T2_diff_if_c3_dropped'])))
            assert o['T1_off_shell']==0 and o['T3_Cu']==0
            if K==1 and al==0: worst=max(worst,abs(o['T2_diff']),abs(o['T3_dvCu']))
            else: assert o['T2_diff']!=0   # (a constant rescaling of c can leave d_v C_u = 0 at a special point; sigma_uv always detects it)
    print('max |difference| for c=4pi/h over all seeds: %s'%worst)
