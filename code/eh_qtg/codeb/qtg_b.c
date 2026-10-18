// Second implementation (code B) of the event-horizon-regular double-null evolution in 4D quasi-topological gravity (Paper F).
// Independent of code A (qtg_dn.c): different primary variables, different discretisation (method of lines, RK4 in v; RK4 with cubic interpolation along s).
//   Row variables (null coordinate s, spacing hs):  r, sg=ln W, p=phi_s, y=-r_s/W, q=-r_v/W.
//   v-derivatives:  r_v=-qW ;  q_v=4 pi r c1 phi_v^2/W ;  y_v=rQ/4-y sg_v ;  p_v=(y W phi_v+q W p)/r ;  sg_v and phi_v by integrating along s from the horizon column
//     (sg_v)_s = W psi/2 - W c2 - 8 pi c1 p phi_v + 64 pi^2 c3 p^2 phi_v^2/W ,   (phi_v)_s = (y W phi_v + q W p)/r ,   psi=(1+4 y q W)/r^2.
//   Coefficients from h(psi): Q=3h/h'-2psi, c1=1/h', c2=9h^2h''/(4h'^3), c3=h''/h'^3  (model 0: h=psi; 1: psi/(1-L2 psi); 2: psi/sqrt(1-L2 psi^2)).
//   proj=1: in every RK stage y is recomputed from the constraint  y_s=4 pi r c1 p^2/W, y(0)=1/2.
#include <math.h>
#include <stdlib.h>
#include <string.h>
static int model=1; static double L2=1.0;
static inline void coefB(double psi,double *Q,double *c1,double *c2,double *c3){
  double h,hp,hpp;
  if(model==0){h=psi;hp=1;hpp=0;}
  else if(model==1){double z=1-L2*psi; h=psi/z; hp=1/(z*z); hpp=2*L2/(z*z*z);}
  else {double s=sqrt(1-L2*psi*psi); h=psi/s; hp=1/(s*s*s); hpp=3*L2*psi/(s*s*s*s*s);}
  *Q=3*h/hp-2*psi; *c1=1/hp; *c2=9*h*h*hpp/(4*hp*hp*hp); *c3=hpp/(hp*hp*hp);
}
typedef struct { double r,sg,p,y,q; } D5;
static inline double midv(const double *x,int i,int nu){
  if(i==0) return (5*x[0]+15*x[1]-5*x[2]+x[3])/16;
  if(i==nu-2) return (x[nu-4]-5*x[nu-3]+15*x[nu-2]+5*x[nu-1])/16;
  return (-x[i-1]+9*x[i]+9*x[i+1]-x[i+2])/16;
}
static inline D5 midD(const double *X,int i,int nu){ D5 m; m.r=midv(X,i,nu); m.sg=midv(X+nu,i,nu); m.p=midv(X+2*nu,i,nu); m.y=midv(X+3*nu,i,nu); m.q=midv(X+4*nu,i,nu); return m; }
static inline D5 nodeD(const double *X,int i,int nu){ D5 m={X[i],X[nu+i],X[2*nu+i],X[3*nu+i],X[4*nu+i]}; return m; }
static inline void fsw(const D5 *d,double pv,double *fs,double *fp){
  double W=exp(d->sg), psi=(1+4*d->y*d->q*W)/(d->r*d->r), Q,c1,c2,c3; coefB(psi,&Q,&c1,&c2,&c3);
  *fs=0.5*W*psi-W*c2-8*M_PI*c1*d->p*pv+64*M_PI*M_PI*c3*d->p*d->p*pv*pv/W;
  *fp=(d->y*W*pv+d->q*W*d->p)/d->r;
}
static inline double gy(const D5 *d,double y){
  double W=exp(d->sg), psi=(1+4*y*d->q*W)/(d->r*d->r), Q,c1,c2,c3; coefB(psi,&Q,&c1,&c2,&c3);
  return 4*M_PI*d->r*c1*d->p*d->p/W;
}
static void projy(double *X,int nu,double hs){
  double y=0.5; X[3*nu]=y;
  for(int i=0;i<nu-1;i++){
    D5 a=nodeD(X,i,nu), b=nodeD(X,i+1,nu), m=midD(X,i,nu);
    double k1=gy(&a,y), k2=gy(&m,y+0.5*hs*k1), k3=gy(&m,y+0.5*hs*k2), k4=gy(&b,y+hs*k3);
    y+=hs/6*(k1+2*k2+2*k3+k4); X[3*nu+i+1]=y;
  }
}
static void sweep(const double *X,int nu,double hs,double sv0,double pv0,double *SV,double *PV){
  double sv=sv0,pv=pv0; SV[0]=sv; PV[0]=pv;
  for(int i=0;i<nu-1;i++){
    D5 a=nodeD(X,i,nu), b=nodeD(X,i+1,nu), m=midD(X,i,nu);
    double fs1,fp1,fs2,fp2,fs3,fp3,fs4,fp4;
    fsw(&a,pv,&fs1,&fp1); fsw(&m,pv+0.5*hs*fp1,&fs2,&fp2); fsw(&m,pv+0.5*hs*fp2,&fs3,&fp3); fsw(&b,pv+hs*fp3,&fs4,&fp4);
    sv+=hs/6*(fs1+2*fs2+2*fs3+fs4); pv+=hs/6*(fp1+2*fp2+2*fp3+fp4); SV[i+1]=sv; PV[i+1]=pv;
  }
}
// column data at time index jj (half-step grid): col[f*ncolt+jj], f: 0 R,1 SG,2 RU,3 RV,4 SU,5 SV,6 PU,7 PV
static void setbc(double *X,int nu,const double *col,int ncolt,int jj){
  double sg=col[1*ncolt+jj], W=exp(sg);
  X[0]=col[0*ncolt+jj]; X[nu]=sg; X[2*nu]=col[6*ncolt+jj]; X[3*nu]=-col[2*ncolt+jj]/W; X[4*nu]=-col[3*ncolt+jj]/W;
}
static void rhs(double *X,int nu,double hs,const double *col,int ncolt,int jj,int proj,double *dX,double *SV,double *PV){
  setbc(X,nu,col,ncolt,jj);
  if(proj) projy(X,nu,hs);
  sweep(X,nu,hs,col[5*ncolt+jj],col[7*ncolt+jj],SV,PV);
  for(int i=0;i<nu;i++){
    D5 d=nodeD(X,i,nu); double W=exp(d.sg), psi=(1+4*d.y*d.q*W)/(d.r*d.r), Q,c1,c2,c3; coefB(psi,&Q,&c1,&c2,&c3);
    dX[i]=-d.q*W; dX[nu+i]=SV[i]; dX[2*nu+i]=(d.y*W*PV[i]+d.q*W*d.p)/d.r;
    dX[3*nu+i]=0.25*d.r*Q-d.y*SV[i]; dX[4*nu+i]=4*M_PI*d.r*c1*PV[i]*PV[i]/W;
  }
}
// main entry: row0[8][nu] at v=0; col[8][ncolt] with ncolt=2*(nv-1)+1 (half steps); out[ncol][nv][8] = r,sg,r_s,r_v,sg_s(NaN),sg_v,phi_s,phi_v at columns cols
void evolve_B(int nu,int nv,double hs,double hv,int model_,double L2_,const double *row0,const double *col,int ncolt,int ncol,const int *cols,double *out,int proj,int nmon,double *mon)
{
  model=model_; L2=L2_;
  size_t N5=(size_t)5*nu;
  double *X=malloc(sizeof(double)*N5), *Xs=malloc(sizeof(double)*N5), *K1=malloc(sizeof(double)*N5),*K2=malloc(sizeof(double)*N5),*K3=malloc(sizeof(double)*N5),*K4=malloc(sizeof(double)*N5);
  double *SV=malloc(sizeof(double)*nu),*PV=malloc(sizeof(double)*nu);
  for(int i=0;i<nu;i++){ double W=exp(row0[nu+i]); X[i]=row0[i]; X[nu+i]=row0[nu+i]; X[2*nu+i]=row0[6*nu+i]; X[3*nu+i]=-row0[2*nu+i]/W; X[4*nu+i]=-row0[3*nu+i]/W; }
  #define EMIT(j,PVarr,SVarr) for(int c=0;c<ncol;c++){ int i=cols[c]; double W=exp(X[nu+i]); double *o=out+((size_t)c*nv+(j))*8; \
     o[0]=X[i];o[1]=X[nu+i];o[2]=-X[3*nu+i]*W;o[3]=-X[4*nu+i]*W;o[4]=NAN;o[5]=(SVarr)[i];o[6]=X[2*nu+i];o[7]=(PVarr)[i]; }
  // initial row: sigma_v, phi_v from the data row0
  for(int i=0;i<nu;i++){SV[i]=row0[5*nu+i];PV[i]=row0[7*nu+i];}
  EMIT(0,PV,SV)
  for(int j=0;j<nv-1;j++){
    int j0=2*j,jh=2*j+1,j1=2*j+2;
    memcpy(Xs,X,sizeof(double)*N5); rhs(Xs,nu,hs,col,ncolt,j0,proj,K1,SV,PV);
    for(size_t k=0;k<N5;k++) Xs[k]=X[k]+0.5*hv*K1[k];
    rhs(Xs,nu,hs,col,ncolt,jh,proj,K2,SV,PV);
    for(size_t k=0;k<N5;k++) Xs[k]=X[k]+0.5*hv*K2[k];
    rhs(Xs,nu,hs,col,ncolt,jh,proj,K3,SV,PV);
    for(size_t k=0;k<N5;k++) Xs[k]=X[k]+hv*K3[k];
    rhs(Xs,nu,hs,col,ncolt,j1,proj,K4,SV,PV);
    for(size_t k=0;k<N5;k++) X[k]+=hv/6*(K1[k]+2*K2[k]+2*K3[k]+K4[k]);
    setbc(X,nu,col,ncolt,j1);
    // sigma_v, phi_v at the new time (for output): sweep on the new row (y as evolved, or projected)
    if(proj) projy(X,nu,hs);
    sweep(X,nu,hs,col[5*ncolt+j1],col[7*ncolt+j1],SV,PV);
    EMIT(j+1,PV,SV)
    if(nmon>0 && mon){ // monitor (NOT used in the paper: it is dominated by columns where y*W is tiny): max over columns of |r_s+yW|/|yW| by finite difference
      double e=0; for(int i=2;i<nu-2;i+=1){ double W=exp(X[nu+i]); double rs=(X[i-2]-8*X[i-1]+8*X[i+1]-X[i+2])/(12*hs); double d=fabs(rs+X[3*nu+i]*W)/(fabs(X[3*nu+i]*W)+1e-300); if(d>e)e=d; }
      mon[j+1]=e; }
    int bad=0; for(int i=0;i<nu;i++) if(!isfinite(X[i])||!isfinite(X[nu+i])){bad=1;break;}
    if(bad){ for(int jj=j+2;jj<nv;jj++) for(int c=0;c<ncol;c++){ double *o=out+((size_t)c*nv+jj)*8; for(int f=0;f<8;f++)o[f]=NAN; } break; }
  }
  free(X);free(Xs);free(K1);free(K2);free(K3);free(K4);free(SV);free(PV);
}
