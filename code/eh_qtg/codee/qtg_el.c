// Code E (Paper F): code B in variables measured from the exact horizon column, with all horizon-subtracted sources evaluated in difference form.
//   Row variables:  Dl = r-r_H(v),  sg = ln W,  p = phi_s,  Dq = r_v - r_v^H(v).   Derived at every stage by integration along s from the horizon column (RK4, cubic mid-point values):
//     dy = y-1/2 (y_s = 4 pi r c1(psi) p^2/W),  ds = sigma_v - sigma_v^H,  dp = phi_v - phi_v^H  (increments of the sweep of code B), psi = (1-4 y r_v)/r^2.
//   Evolution (exact): Dl_v = Dq ;  Dq_v = sigma_v Dq + ds r_v^H - (S-S_H),  S = 4 pi r c1(psi) phi_v^2 ;  sg_v = sigma_v ;  p_v = (y W phi_v - r_v p)/r.
//   S-S_H = 4 pi [ Dl c1 phi_v^2 + r_H (c1-c1_H) phi_v^2 + r_H c1_H dp (phi_v+phi_v^H) ],  psi-psi_H = (1-2 r_v^H)(1/r^2-1/r_H^2) - (2 Dq + 4 dy r_v)/r^2,
//   c1-c1_H = (z+z_H)(z-z_H) with z=1-L2 psi (Hayward h; other h: direct difference).  No difference of two nearly equal numbers is formed near the horizon.
#include <math.h>
#include <stdlib.h>
#include <string.h>
typedef long double real;
static int model=1; static real L2=1.0;
static inline void coefB(real psi,real *Q,real *c1,real *c2,real *c3){
  real h,hp,hpp;
  if(model==0){h=psi;hp=1;hpp=0;}
  else if(model==1){real z=1-L2*psi; h=psi/z; hp=1/(z*z); hpp=2*L2/(z*z*z);}
  else {real s=sqrtl(1-L2*psi*psi); h=psi/s; hp=1/(s*s*s); hpp=3*L2*psi/(s*s*s*s*s);}
  *Q=3*h/hp-2*psi; *c1=1/hp; *c2=9*h*h*hpp/(4*hp*hp*hp); *c3=hpp/(hp*hp*hp);
}
static inline real midv(const real *x,int i,int nu){
  if(i==0) return (5*x[0]+15*x[1]-5*x[2]+x[3])/16;
  if(i==nu-2) return (x[nu-4]-5*x[nu-3]+15*x[nu-2]+5*x[nu-1])/16;
  return (-x[i-1]+9*x[i]+9*x[i+1]-x[i+2])/16;
}
// row arrays (absolute): r, sg, p, y, q ; plus dy
typedef struct { real r,sg,p,y,q; } D5;
static inline D5 nodeA(const real *A,int i,int nu){ D5 m={A[i],A[nu+i],A[2*nu+i],A[3*nu+i],A[4*nu+i]}; return m; }
static inline D5 midA(const real *A,int i,int nu){ D5 m; m.r=midv(A,i,nu); m.sg=midv(A+nu,i,nu); m.p=midv(A+2*nu,i,nu); m.y=midv(A+3*nu,i,nu); m.q=midv(A+4*nu,i,nu); return m; }
static inline void fsw(const D5 *d,real pv,real *fs,real *fp){
  real W=expl(d->sg), psi=(1+4*d->y*d->q*W)/(d->r*d->r), Q,c1,c2,c3; coefB(psi,&Q,&c1,&c2,&c3);
  *fs=0.5*W*psi-W*c2-8*M_PI*c1*d->p*pv+64*M_PI*M_PI*c3*d->p*d->p*pv*pv/W;
  *fp=(d->y*W*pv+d->q*W*d->p)/d->r;
}
static inline real gy(const D5 *d,real dy){
  real W=expl(d->sg), psi=(1+4*(0.5+dy)*d->q*W)/(d->r*d->r), Q,c1,c2,c3; coefB(psi,&Q,&c1,&c2,&c3);
  return 4*M_PI*d->r*c1*d->p*d->p/W;
}
// A = [r, sg, p, y, q] absolute row arrays (y filled here), DY increments y-1/2
static void projy(real *A,real *DY,int nu,real hs){
  real dy=0; DY[0]=0; A[3*nu]=0.5;
  for(int i=0;i<nu-1;i++){
    D5 a=nodeA(A,i,nu), b=nodeA(A,i+1,nu), m=midA(A,i,nu);
    real k1=gy(&a,dy), k2=gy(&m,dy+0.5*hs*k1), k3=gy(&m,dy+0.5*hs*k2), k4=gy(&b,dy+hs*k3);
    dy+=hs/6*(k1+2*k2+2*k3+k4); DY[i+1]=dy; A[3*nu+i+1]=0.5+dy;
  }
}
// increments ds=sigma_v-sigma_H, dp=phi_v-phi_H, with phi_v^H = pvh
static void sweep(const real *A,int nu,real hs,real pvh,real *DS,real *DP){
  real ds=0,dp=0; DS[0]=0; DP[0]=0;
  for(int i=0;i<nu-1;i++){
    D5 a=nodeA(A,i,nu), b=nodeA(A,i+1,nu), m=midA(A,i,nu);
    real fs1,fp1,fs2,fp2,fs3,fp3,fs4,fp4;
    fsw(&a,pvh+dp,&fs1,&fp1); fsw(&m,pvh+dp+0.5*hs*fp1,&fs2,&fp2); fsw(&m,pvh+dp+0.5*hs*fp2,&fs3,&fp3); fsw(&b,pvh+dp+hs*fp3,&fs4,&fp4);
    ds+=hs/6*(fs1+2*fs2+2*fs3+fs4); dp+=hs/6*(fp1+2*fp2+2*fp3+fp4); DS[i+1]=ds; DP[i+1]=dp;
  }
}
typedef struct { real *A,*DY,*DS,*DP; } Work;
static void buildA(const real *X,Work *w,int nu,const real *col,int ncolt,int jj){
  real RH=col[0*ncolt+jj],RVH=col[3*ncolt+jj],SGH=col[1*ncolt+jj],PUH=col[6*ncolt+jj];
  real *A=w->A;
  for(int i=0;i<nu;i++){ real W=expl(X[nu+i]); A[i]=RH+X[i]; A[nu+i]=X[nu+i]; A[2*nu+i]=X[2*nu+i]; A[4*nu+i]=-(RVH+X[4*nu+i])/W; }
  A[nu]=SGH; A[2*nu]=PUH; A[0]=RH; A[4*nu]=-RVH/expl(SGH);
}
// evaluate row: fills A (y), DY, DS, DP and the time derivative dX
static void rhs(real *X,Work *w,int nu,real hs,const real *col,int ncolt,int jj,real *dX){
  X[nu]=col[1*ncolt+jj]; X[0]=0.0; X[2*nu]=col[6*ncolt+jj]; X[4*nu]=0.0;
  buildA(X,w,nu,col,ncolt,jj);
  real RH=col[0*ncolt+jj],RVH=col[3*ncolt+jj],SVH=col[5*ncolt+jj],PVH=col[7*ncolt+jj];
  projy(w->A,w->DY,nu,hs);
  sweep(w->A,nu,hs,PVH,w->DS,w->DP);
  real psiH=(1-2*RVH)/(RH*RH),QH,c1H,c2H,c3H; coefB(psiH,&QH,&c1H,&c2H,&c3H); real zH=1-L2*psiH;
  for(int i=0;i<nu;i++){
    D5 d=nodeA(w->A,i,nu); real W=expl(d.sg), Dl=X[i], Dq=X[4*nu+i], rv=RVH+Dq, dy=w->DY[i], ds=w->DS[i], dp=w->DP[i];
    real pv=PVH+dp, sv=SVH+ds;
    real psi=(1-4*d.y*rv)/(d.r*d.r), Q,c1,c2,c3; coefB(psi,&Q,&c1,&c2,&c3);
    real dpsi=(1-2*RVH)*(-Dl*(2*RH+Dl)/(d.r*d.r*RH*RH))-(2*Dq+4*dy*rv)/(d.r*d.r);
    real dc1;
    if(model==1){ real z=1-L2*psi; dc1=(z+zH)*(-L2*dpsi); } else dc1=c1-c1H;
    real SmSH=4*M_PI*(Dl*c1*pv*pv+RH*dc1*pv*pv+RH*c1H*dp*(pv+PVH));
    dX[i]=Dq; dX[nu+i]=sv; dX[2*nu+i]=(d.y*W*pv-rv*d.p)/d.r; dX[3*nu+i]=0.0;
    dX[4*nu+i]=sv*Dq+ds*RVH-SmSH;
  }
}
void evolve_E(int nu,int nv,double hs_,double hv_,int model_,double L2_,const double *row0_,const double *col_,int ncolt,int ncol,const int *cols,double *out)
{
  real hs=hs_,hv=hv_; real *row0=malloc(sizeof(real)*sizeof(real)*nu),*col=malloc(sizeof(real)*8*ncolt); for(int k=0;k<sizeof(real)*nu;k++)row0[k]=row0_[k]; for(int k=0;k<8*ncolt;k++)col[k]=col_[k];
  model=model_; L2=L2_;
  size_t N5=(size_t)5*nu;
  real *X=malloc(sizeof(real)*N5),*Xs=malloc(sizeof(real)*N5),*K1=malloc(sizeof(real)*N5),*K2=malloc(sizeof(real)*N5),*K3=malloc(sizeof(real)*N5),*K4=malloc(sizeof(real)*N5);
  Work w; w.A=malloc(sizeof(real)*N5); w.DY=malloc(sizeof(real)*nu); w.DS=malloc(sizeof(real)*nu); w.DP=malloc(sizeof(real)*nu);
  for(int i=0;i<nu;i++){ X[i]=row0[i]; X[nu+i]=row0[nu+i]; X[2*nu+i]=row0[6*nu+i]; X[3*nu+i]=0.0; X[4*nu+i]=row0[3*nu+i]; }
  #define EMITE(jj) { real RVH_=col[3*ncolt+(jj)],SVH_=col[5*ncolt+(jj)],PVH_=col[7*ncolt+(jj)]; \
     for(int c=0;c<ncol;c++){ int i=cols[c]; real W=expl(w.A[nu+i]); double *o=out+((size_t)c*nv+(jjx))*8; \
     o[0]=w.A[i];o[1]=w.A[nu+i];o[2]=-w.A[3*nu+i]*W;o[3]=RVH_+X[4*nu+i];o[4]=NAN;o[5]=SVH_+w.DS[i];o[6]=w.A[2*nu+i];o[7]=PVH_+w.DP[i]; } }
  { real *tmp=malloc(sizeof(real)*N5); memcpy(Xs,X,sizeof(real)*N5); rhs(Xs,&w,nu,hs,col,ncolt,0,tmp); free(tmp); }
  { int jjx=0; EMITE(0) }
  for(int j=0;j<nv-1;j++){
    int j0=2*j,jh=2*j+1,j1=2*j+2;
    memcpy(Xs,X,sizeof(real)*N5); rhs(Xs,&w,nu,hs,col,ncolt,j0,K1);
    for(size_t k=0;k<N5;k++) Xs[k]=X[k]+0.5*hv*K1[k];
    rhs(Xs,&w,nu,hs,col,ncolt,jh,K2);
    for(size_t k=0;k<N5;k++) Xs[k]=X[k]+0.5*hv*K2[k];
    rhs(Xs,&w,nu,hs,col,ncolt,jh,K3);
    for(size_t k=0;k<N5;k++) Xs[k]=X[k]+hv*K3[k];
    rhs(Xs,&w,nu,hs,col,ncolt,j1,K4);
    for(size_t k=0;k<N5;k++) X[k]+=hv/6*(K1[k]+2*K2[k]+2*K3[k]+K4[k]);
    memcpy(Xs,X,sizeof(real)*N5); rhs(Xs,&w,nu,hs,col,ncolt,j1,K1);
    { int jjx=j+1; EMITE(j1) }
    int bad=0; for(int i=0;i<nu;i++) if(!isfinite(X[i])||!isfinite(X[nu+i])||!isfinite(X[4*nu+i])){bad=1;break;}
    if(bad){ for(int jj=j+2;jj<nv;jj++) for(int c=0;c<ncol;c++){ double *o=out+((size_t)c*nv+jj)*8; for(int f=0;f<8;f++)o[f]=NAN; } break; }
  }
  free(X);free(Xs);free(K1);free(K2);free(K3);free(K4);free(w.A);free(w.DY);free(w.DS);free(w.DP);free(row0);free(col);
}
