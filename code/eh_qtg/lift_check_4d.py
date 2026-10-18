"""R1 (Paper F, Sec. checks (g)): independent check that the covariant lifts P,H,T,K (BCHM 2509.19016 / Borissova-Carballo-Rubio 2602.16773 Eqs. 53-65) reduce on the warped product
g = q_ab dy^a dy^b + phi^2 dOmega^2 to psi=(1-chi)/phi^2, eta=box(phi)/phi, tau=(nabla nabla phi)^2/phi^2, calR.
The 4D Riemann tensor is computed FROM THE 4D METRIC by high-order finite differences (no use of warped-product curvature formulas).
Invariants (Zakhary-McIntosh as in that paper): I_R=R, I_R^2-hat, I_R^3-hat (traceless Ricci), I_C2=C^2, I_C3=C_{mn}^{rs}C_{rs}^{ab}C_{ab}^{mn}, I_R2C=R^{mn}R^{rs}C_{rmns}."""
import numpy as np, itertools, sys
rng=np.random.default_rng(int(sys.argv[1]) if len(sys.argv)>1 else 0)
cf=rng.normal(size=(12,))*0.3
def qab(u,v):
    a=0.3*np.sin(u+2*v)*cf[0]*3+0.2*cf[1]*u*v
    b=-(1+0.2*cf[2]*u*v+0.1*cf[3]*u**2+0.15*cf[4]*np.cos(v))
    c=0.2*np.cos(v-u)*cf[5]*3+0.1*cf[6]*v**2
    return np.array([[a,b],[b,c]])
def phi(u,v): return 1.5+0.3*cf[7]*3*u-0.2*cf[8]*3*v+0.1*cf[9]*3*u*v+0.1*cf[10]*3*np.sin(u)+0.05*cf[11]*3*v**2
def g4(x):
    u,v,th,ph=x; g=np.zeros((4,4)); g[:2,:2]=qab(u,v); p=phi(u,v); g[2,2]=p*p; g[3,3]=p*p*np.sin(th)**2; return g
def g2(x): return qab(*x)
x0=lambda n: np.array([0.3,-0.2,1.0,0.4])[:n]
def derivs(gf,x,h=2e-3):
    n=len(x); g0=gf(x); dg=np.zeros((n,)+g0.shape); ddg=np.zeros((n,n)+g0.shape)
    def sh(*s):
        y=x.copy()
        for i,c in s: y[i]+=c*h
        return gf(y)
    for i in range(n):
        dg[i]=(-sh((i,2))+8*sh((i,1))-8*sh((i,-1))+sh((i,-2)))/(12*h)
        ddg[i,i]=(-sh((i,2))+16*sh((i,1))-30*g0+16*sh((i,-1))-sh((i,-2)))/(12*h*h)
        for j in range(i):
            f=lambda a,b: sh((i,a),(j,b))
            # 4th-order mixed derivative via two-step Richardson
            def mixed(hh):
                y=lambda a,b:(lambda z:(z.__setitem__(i,z[i]+a*hh) or z.__setitem__(j,z[j]+b*hh) or gf(z)))(x.copy())
                return (y(1,1)-y(1,-1)-y(-1,1)+y(-1,-1))/(4*hh*hh)
            m1=mixed(h); m2=mixed(2*h); ddg[i,j]=ddg[j,i]=(4*m1-m2)/3
    return g0,dg,ddg
def curv(gf,x):
    n=len(x); g,dg,ddg=derivs(gf,x); gi=np.linalg.inv(g)
    # Gamma_{a,bc} lowered, d_e Gamma_{a,bc}
    G1=0.5*(np.einsum('cab->abc',dg)*0+0)  # placeholder
    Gl=np.zeros((n,n,n)); dGl=np.zeros((n,n,n,n))   # Gl[a,b,c]=Gamma_{a bc}; dGl[e,a,b,c]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                Gl[a,b,c]=0.5*(dg[b][a,c]+dg[c][a,b]-dg[a][b,c])
                for e in range(n):
                    dGl[e,a,b,c]=0.5*(ddg[e,b][a,c]+ddg[e,c][a,b]-ddg[e,a][b,c])
    dgi=-np.einsum('ij,ejk,kl->eil',gi,dg,gi)
    Gam=np.einsum('ad,dbc->abc',gi,Gl)                       # Gamma^a_{bc}
    dGam=np.einsum('ead,dbc->eabc',dgi,Gl)+np.einsum('ad,edbc->eabc',gi,dGl)  # d_e Gamma^a_{bc}
    # R^a_{bcd}=d_c Gam^a_{db}-d_d Gam^a_{cb}+Gam^a_{ce}Gam^e_{db}-Gam^a_{de}Gam^e_{cb}
    Rm=np.zeros((n,n,n,n))
    for a,b,c,d in itertools.product(range(n),repeat=4):
        Rm[a,b,c,d]=dGam[c,a,d,b]-dGam[d,a,c,b]+sum(Gam[a,c,e]*Gam[e,d,b]-Gam[a,d,e]*Gam[e,c,b] for e in range(n))
    return g,gi,Gam,dGam,Rm
# ---- 2D side
g,gi,Gam,dGam,Rm2=curv(g2,x0(2)); n=2
Ric2=np.einsum('abad->bd',Rm2); calR=np.einsum('bd,bd',gi,Ric2)
u0,v0=0.3,-0.2; h=1e-3
def dphi(f,i,hh=1e-3):
    def F(y): return f(*y)
    X=np.array([u0,v0]); d=np.zeros(2)
    for i in range(2):
        e=np.zeros(2); e[i]=hh; d[i]=(-F(X+2*e)+8*F(X+e)-8*F(X-e)+F(X-2*e))/(12*hh)
    return d
X=np.array([u0,v0]); P1=dphi(phi,0)
H2=np.zeros((2,2))
def F(y): return phi(*y)
hh=2e-3
for i in range(2):
    for j in range(2):
        if i==j:
            e=np.zeros(2); e[i]=hh; H2[i,j]=(-F(X+2*e)+16*F(X+e)-30*F(X)+16*F(X-e)-F(X-2*e))/(12*hh*hh)
        else:
            ei=np.zeros(2); ei[i]=hh; ej=np.zeros(2); ej[j]=hh
            def mx(s): return (F(X+s*ei+s*ej)-F(X+s*ei-s*ej)-F(X-s*ei+s*ej)+F(X-s*ei-s*ej))/(4*s*s*hh*hh/hh/hh)
            m=lambda s:(F(X+s*ei+s*ej)-F(X+s*ei-s*ej)-F(X-s*ei+s*ej)+F(X-s*ei-s*ej))/(4*(s*hh)**2)
            H2[i,j]=(4*m(1)-m(2))/3
nab=H2-np.einsum('aij,a->ij',Gam,P1)           # nabla_i nabla_j phi
p0=phi(u0,v0); chi=P1@gi@P1; box=np.einsum('ij,ij',gi,nab)
psi=(1-chi)/p0**2; eta=box/p0; tau=np.einsum('ik,jl,ij,kl',gi,gi,nab,nab)/p0**2
# ---- 4D side
g4m,g4i,Gam4,dGam4,Rm4=curv(g4,x0(4)); n=4
Rlow=np.einsum('ae,ebcd->abcd',g4m,Rm4)
Ric=np.einsum('abad->bd',Rm4); Rs=np.einsum('bd,bd',g4i,Ric)
Cw=Rlow-0.5*(np.einsum('ac,bd->abcd',g4m,Ric)-np.einsum('ad,bc->abcd',g4m,Ric)-np.einsum('bc,ad->abcd',g4m,Ric)+np.einsum('bd,ac->abcd',g4m,Ric))+Rs/6*(np.einsum('ac,bd->abcd',g4m,g4m)-np.einsum('ad,bc->abcd',g4m,g4m))
Cup=np.einsum('ai,bj,ck,dl,ijkl->abcd',g4i,g4i,g4i,g4i,Cw)
IC2=np.einsum('abcd,abcd',Cw,Cup)
Cmix=np.einsum('abcd,ce,df->abef',Cw,g4i,g4i)   # C_{ab}^{ef}
Cmix_up=np.einsum('ai,bj,ijef->abef',g4i,g4i,Cmix)  # C^{ab ef}
C_ab_ef=Cmix
IC3=np.einsum('mnrs,rsab,abmn->',np.einsum('mnrs->mnrs',np.einsum('mi,nj,ijrs->mnrs',np.eye(4),np.eye(4),Cw)*0+0,optimize=True) if False else Cmix,Cmix,Cmix) if False else None
# C_{mn}^{rs}: mixed with last two raised, then I_C3 = C_{mn}^{rs} C_{rs}^{ab} C_{ab}^{mn}
A=np.einsum('mnij,ir,js->mnrs',Cw,g4i,g4i)       # C_{mn}^{rs}
IC3=np.einsum('mnrs,rsab,abmn->',A,A,A)
Ricup=np.einsum('ai,bj,ij->ab',g4i,g4i,Ric)
Rhat=Ric-0.25*Rs*g4m; Rh_mix=np.einsum('ai,ib->ab',g4i,Rhat)
IRh2=np.einsum('ab,ba',Rh_mix,Rh_mix); IRh3=np.einsum('ab,bc,ca',Rh_mix,Rh_mix,Rh_mix)
IR2C=np.einsum('mn,rs,rmns->',Ricup,Ricup,Cw)
IR2C_alt=-np.einsum('mn,rs,rmsn->',Ricup,Ricup,Cw)
Om=calR+2*eta+2*psi; Sig=calR**2/4-calR*psi-2*eta**2+4*tau+psi**2
print('--- reduced (4D invariants vs warped-product formulas of 2602.16773)')
chk=lambda nm,a,b: print('%-8s 4D=%+.8f  pred=%+.8f  diff=%.1e'%(nm,a,b,abs(a-b)))
chk('R',Rs,calR-4*eta+2*psi); chk('IC2',IC2,Om**2/3); chk('IC3',IC3,Om**3/18); chk('IRh2',IRh2,Sig)
chk('IRh3',IRh3,-1.5*calR*eta**2+3*calR*tau+3*eta**2*psi-6*tau*psi)
chk('IR2C',IR2C,-Om*((eta**2-2*tau)+Sig/3)); print('   (alt index order IR2C =%+.8f)'%IR2C_alt)
# ---- lifts
Hh=-Rs/6+IC3/IC2
Tt=Rs**2/72+IRh2/6-Rs*IC3/(6*IC2)+0.5*(IC3/IC2)**2+IC2*IR2C/(12*IC3)
D=IC2*IR2C+2*IRh2*IC3
Pp=Rs/12+IC3/IC2-IRh3*IC3/D
Kk=(Rs*IC2*IR2C/6+Rs*IRh2*IC3/3+4*IRh2*IC3**2/IC2+2*IRh3*IC3+2*IC3*IR2C)/D   # Eq. 65 of arXiv:2602.16773 (TeX source: 4 I_Rh2 I_C3^2 / I_C2; the square is needed by dimensions)
print('--- lifts (Eqs. 55,63,64,65) vs 2D scalars')
chk('H=eta',Hh,eta); chk('T=tau',Tt,tau); chk('P=psi',Pp,psi); chk('K=calR',Kk,calR)
# negative control: with the first power of I_C3 in the 4th term of Eq. (65) the lift fails (dimensionally inconsistent)
Kk_bad=(Rs*IC2*IR2C/6+Rs*IRh2*IC3/3+4*IRh2*IC3/IC2+2*IRh3*IC3+2*IC3*IR2C)/D
chk('K, I_C3^1 (control, must fail)',Kk_bad,calR)

# a lift is exact if the printed differences are <~1e-9 (finite-difference Riemann, 4th order, step 2e-3)
# Einstein limit of the covariant density (H2=2P, H3=4, H4=1): 2P - 4H + K must equal the 4D Ricci scalar
chk('GR dens.',2*Pp-4*Hh+Kk,Rs)
# generic h (Hayward, ell=1): H2=3h-2 psi h', H3=2h', H4(psi)=-(psi/2) int h'/psi^2 : the density at the point equals the 2D Lagrangian
# G2-box(phi)G3+G4 R-2G4X(...) of Eq. (S2d) term by term because P,H,T,K equal psi,eta,tau,calR (checked above); the identification of the coefficients
# (G2=phi^2 H2, G3=phi H3, G4=phi^2 H4, G4,X=-H4') is algebraic and is done in the paper text.
