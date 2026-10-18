// Double-null evolution of a massless scalar in spherically symmetric quasi-topological ("single-function") gravity with characteristic
// function h(psi),  psi = (1-(grad r)^2)/r^2 = (1+4 r_u r_v/W)/r^2,  generalized mass m = r^3 h(psi)/2.   G=1, ds^2=-W du dv + r^2 dOmega^2.
// Field equations (Bueno et al 2509.19016 eqs 36-38 translated to double-null gauge, see Paper E Sec. qtg):
//   r_uu - s_u r_u = -(4 pi r/h') phi_u^2 ,  r_vv - s_v r_v = -(4 pi r/h') phi_v^2        (constraints; not used by the evolution)
//   r_uv   = -(W r/4) (3h/h' - 2 psi)
//   s_uv   = W psi/2 - (9W/4) h^2 h''/h'^3 - (8 pi/h') phi_u phi_v + 64 pi^2 (h''/h'^3) phi_u^2 phi_v^2 / W
//   phi_uv = -(r_u phi_v + r_v phi_u)/r
// models: 0 h=psi (GR, no regulator); 1 Hayward h=psi/(1-L2 psi); 2 h=psi/sqrt(1-L2 psi^2) (2509.19016 eq. 51, L2=alpha^2)
// Scheme identical to Paper E double_null.c (diamond + trapezoidal first derivatives, predictor-corrector).
#include <math.h>
#include <stdlib.h>
#include <string.h>
static int model=1; static double L2=1.0;
void coef(double psi,double *Q,double *c1,double *c2,double *c3){
  if(model==0){*Q=psi;*c1=1;*c2=0;*c3=0;}
  else if(model==1){double z=1-L2*psi; *Q=psi*(1-3*L2*psi); *c1=z*z; *c2=4.5*L2*psi*psi*z; *c3=2*L2*z*z*z;}
  else {double s2=1-L2*psi*psi; if(s2<1e-30) s2=1e-30; double s=sqrt(s2); *Q=3*psi*s2-2*psi; *c1=s*s2; *c2=6.75*L2*psi*psi*psi*s2; *c3=3*L2*psi*s2*s2;}
}
static inline void F(double r,double sg,double ru,double rv,double pu,double pv,double *fr,double *fs,double *fp){
  double W=exp(sg), X=ru*rv/W, psi=(1+4*X)/(r*r), Q,c1,c2,c3; coef(psi,&Q,&c1,&c2,&c3);
  *fr=-0.25*W*r*Q;
  *fs=0.5*W*psi-W*c2-8*M_PI*c1*pu*pv+64*M_PI*M_PI*c3*pu*pu*pv*pv/W;
  *fp=-(ru*pv+rv*pu)/r;
}
void evolve_qtg(int nu,int nv,double hu,double hv,int model_,double L2_,double *R,double *SG,double *RU,double *RV,double *SU,double *SV,double *PU,double *PV,int niter)
{
  model=model_; L2=L2_;
  for(int j=0;j<nv-1;j++) for(int i=0;i<nu-1;i++){
    int S=j*nu+i,E=j*nu+i+1,Wn=(j+1)*nu+i,N=(j+1)*nu+i+1;
    double fS[3],fE[3],fW[3],fN[3],fC[3];
    F(R[S],SG[S],RU[S],RV[S],PU[S],PV[S],&fS[0],&fS[1],&fS[2]);
    F(R[E],SG[E],RU[E],RV[E],PU[E],PV[E],&fE[0],&fE[1],&fE[2]);
    F(R[Wn],SG[Wn],RU[Wn],RV[Wn],PU[Wn],PV[Wn],&fW[0],&fW[1],&fW[2]);
    double rN=R[E]+R[Wn]-R[S]+hu*hv*fS[0], sN=SG[E]+SG[Wn]-SG[S]+hu*hv*fS[1];
    double ruN=RU[E]+hv*fE[0], rvN=RV[Wn]+hu*fW[0], suN=SU[E]+hv*fE[1], svN=SV[Wn]+hu*fW[1], puN=PU[E]+hv*fE[2], pvN=PV[Wn]+hu*fW[2];
    for(int it=0;it<niter;it++){
      F(rN,sN,ruN,rvN,puN,pvN,&fN[0],&fN[1],&fN[2]);
      double rc=0.25*(R[S]+R[E]+R[Wn]+rN), sc=0.25*(SG[S]+SG[E]+SG[Wn]+sN);
      double ruc=0.25*(RU[S]+RU[E]+RU[Wn]+ruN), rvc=0.25*(RV[S]+RV[E]+RV[Wn]+rvN);
      double puc=0.25*(PU[S]+PU[E]+PU[Wn]+puN), pvc=0.25*(PV[S]+PV[E]+PV[Wn]+pvN);
      F(rc,sc,ruc,rvc,puc,pvc,&fC[0],&fC[1],&fC[2]);
      rN=R[E]+R[Wn]-R[S]+hu*hv*fC[0]; sN=SG[E]+SG[Wn]-SG[S]+hu*hv*fC[1];
      ruN=RU[E]+0.5*hv*(fE[0]+fN[0]); rvN=RV[Wn]+0.5*hu*(fW[0]+fN[0]);
      suN=SU[E]+0.5*hv*(fE[1]+fN[1]); svN=SV[Wn]+0.5*hu*(fW[1]+fN[1]);
      puN=PU[E]+0.5*hv*(fE[2]+fN[2]); pvN=PV[Wn]+0.5*hu*(fW[2]+fN[2]);
    }
    R[N]=rN;SG[N]=sN;RU[N]=ruN;RV[N]=rvN;SU[N]=suN;SV[N]=svN;PU[N]=puN;PV[N]=pvN;
  }
}

// Streaming version: keeps two rows only (memory O(nu)); out[ncol][nv][8] = fields at u-index cols[c] for every v-row.  Same arithmetic as evolve_qtg.
void evolve_stream_qtg(int nu,int nv,double hu,double hv,int model_,double L2_,const double *row0,const double *col0,int ncol,const int *cols,double *out,int niter)
{
  model=model_; L2=L2_;
  double *buf=(double*)malloc(sizeof(double)*8*nu*2);
  double *P[8],*C[8]; for(int f=0;f<8;f++){P[f]=buf+f*nu; C[f]=buf+(8+f)*nu; memcpy(P[f],row0+(size_t)f*nu,sizeof(double)*nu);}
  for(int c=0;c<ncol;c++) for(int f=0;f<8;f++) out[((size_t)c*nv+0)*8+f]=P[f][cols[c]];
  for(int j=0;j<nv-1;j++){
    for(int f=0;f<8;f++) C[f][0]=col0[(size_t)f*nv+(j+1)];
    for(int i=0;i<nu-1;i++){
      double fS[3],fE[3],fW[3],fN[3],fC[3];
      F(P[0][i],P[1][i],P[2][i],P[3][i],P[6][i],P[7][i],&fS[0],&fS[1],&fS[2]);
      F(P[0][i+1],P[1][i+1],P[2][i+1],P[3][i+1],P[6][i+1],P[7][i+1],&fE[0],&fE[1],&fE[2]);
      F(C[0][i],C[1][i],C[2][i],C[3][i],C[6][i],C[7][i],&fW[0],&fW[1],&fW[2]);
      double Rs=P[0][i],Re=P[0][i+1],Rw=C[0][i],Ss=P[1][i],Se=P[1][i+1],Sw=C[1][i];
      double rN=Re+Rw-Rs+hu*hv*fS[0], sN=Se+Sw-Ss+hu*hv*fS[1];
      double ruN=P[2][i+1]+hv*fE[0], rvN=C[3][i]+hu*fW[0], suN=P[4][i+1]+hv*fE[1], svN=C[5][i]+hu*fW[1], puN=P[6][i+1]+hv*fE[2], pvN=C[7][i]+hu*fW[2];
      for(int it=0;it<niter;it++){
        F(rN,sN,ruN,rvN,puN,pvN,&fN[0],&fN[1],&fN[2]);
        double rc=0.25*(Rs+Re+Rw+rN), sc=0.25*(Ss+Se+Sw+sN);
        double ruc=0.25*(P[2][i]+P[2][i+1]+C[2][i]+ruN), rvc=0.25*(P[3][i]+P[3][i+1]+C[3][i]+rvN);
        double puc=0.25*(P[6][i]+P[6][i+1]+C[6][i]+puN), pvc=0.25*(P[7][i]+P[7][i+1]+C[7][i]+pvN);
        F(rc,sc,ruc,rvc,puc,pvc,&fC[0],&fC[1],&fC[2]);
        rN=Re+Rw-Rs+hu*hv*fC[0]; sN=Se+Sw-Ss+hu*hv*fC[1];
        ruN=P[2][i+1]+0.5*hv*(fE[0]+fN[0]); rvN=C[3][i]+0.5*hu*(fW[0]+fN[0]);
        suN=P[4][i+1]+0.5*hv*(fE[1]+fN[1]); svN=C[5][i]+0.5*hu*(fW[1]+fN[1]);
        puN=P[6][i+1]+0.5*hv*(fE[2]+fN[2]); pvN=C[7][i]+0.5*hu*(fW[2]+fN[2]);
      }
      C[0][i+1]=rN;C[1][i+1]=sN;C[2][i+1]=ruN;C[3][i+1]=rvN;C[4][i+1]=suN;C[5][i+1]=svN;C[6][i+1]=puN;C[7][i+1]=pvN;
    }
    for(int c=0;c<ncol;c++) for(int f=0;f<8;f++) out[((size_t)c*nv+(j+1))*8+f]=C[f][cols[c]];
    for(int f=0;f<8;f++){double *t=P[f];P[f]=C[f];C[f]=t;}
  }
  free(buf);
}

// Constrained streaming version (Paper F, event-horizon-regular data).  Same diamond/trapezoid scheme as evolve_stream_qtg for r, sigma, sigma_u, sigma_v, phi_u, phi_v,
// but r_u and (mode 2) r_v are not evolved: they are replaced, at every new point and inside the corrector iterations, by the integrals of the two Raychaudhuri
// constraints (Eq. (ray) of Paper F with c1 = 1/h'(psi)), written for  y = -r_u/W  and  q = -r_v/W :
//    y(s,v) = y_0 + int_0^s 4 pi r c1 phi_s^2 /W ds' ,     y_0 = 1/2 on the horizon column (EF gauge),
//    q(s,v) = q(s,0) + int_0^v 4 pi r c1 phi_v^2 /W dv' ,  (since (r_v/W)_v = sigma_v-independent: r_vv - sigma_v r_v = -4 pi r c1 phi_v^2)
// cumulative trapezoid rules on the grid, with a fixed-point iteration because c1 depends on psi = (1+4 y q W)/r^2 at the new point.  Both integrands are
// positive.  The free evolution of r_u and r_v is unstable in the interior: r_u/W is blue-shifted like e^{kappa_- v} and r_v = r_v(horizon)+int r_uv du is a
// cancellation of O(1) terms down to a value ~ W; the constraint form has neither problem.   mode 1: project r_u only; mode 2: project r_u and r_v; mode 3: as 2 and r from r_v = -rho along each column (the r_uv equation is then not used for r).
void evolve_stream_qtg_cy(int nu,int nv,double hu,double hv,int model_,double L2_,const double *row0,const double *col0,int ncol,const int *cols,double *out,int niter,double y0,int mode,int nrow,const int *rows,double *snap)
{
  model=model_; L2=L2_;
  double *buf=(double*)malloc(sizeof(double)*8*nu*2);
  double *qc=(double*)malloc(sizeof(double)*nu), *gc=(double*)malloc(sizeof(double)*nu);
  double *P[8],*C[8]; for(int f=0;f<8;f++){P[f]=buf+f*nu; C[f]=buf+(8+f)*nu; memcpy(P[f],row0+(size_t)f*nu,sizeof(double)*nu);}
  for(int c=0;c<ncol;c++) for(int f=0;f<8;f++) out[((size_t)c*nv+0)*8+f]=P[f][cols[c]];
  for(int k=0;k<nrow;k++) if(rows[k]==0) for(int f=0;f<8;f++) memcpy(snap+((size_t)k*8+f)*nu,P[f],sizeof(double)*nu);
  for(int i=0;i<nu;i++){ double W=exp(P[1][i]), rho=-P[3][i], y=-P[2][i]/W, psi=(1+4*y*rho)/(P[0][i]*P[0][i]),Q,c1,c2,c3; coef(psi,&Q,&c1,&c2,&c3);
                          qc[i]=rho/W; gc[i]=4*M_PI*P[0][i]*c1*P[7][i]*P[7][i]/W; }
  for(int j=0;j<nv-1;j++){
    for(int f=0;f<8;f++) C[f][0]=col0[(size_t)f*nv+(j+1)];
    double W0=exp(C[1][0]); C[2][0]=-y0*W0; qc[0]=-C[3][0]/W0;
    double yprev=y0, gprev; { double rho0=-C[3][0], psi0=(1+4*yprev*rho0)/(C[0][0]*C[0][0]), Q,c1,c2,c3; coef(psi0,&Q,&c1,&c2,&c3); gprev=4*M_PI*C[0][0]*c1*C[6][0]*C[6][0]/W0; }
    { double rho0=-C[3][0], psi0=(1+4*y0*rho0)/(C[0][0]*C[0][0]), Q,c1,c2,c3; coef(psi0,&Q,&c1,&c2,&c3); gc[0]=4*M_PI*C[0][0]*c1*C[7][0]*C[7][0]/W0; }
    for(int i=0;i<nu-1;i++){
      double fS[3],fE[3],fW[3],fN[3],fC[3];
      F(P[0][i],P[1][i],P[2][i],P[3][i],P[6][i],P[7][i],&fS[0],&fS[1],&fS[2]);
      F(P[0][i+1],P[1][i+1],P[2][i+1],P[3][i+1],P[6][i+1],P[7][i+1],&fE[0],&fE[1],&fE[2]);
      F(C[0][i],C[1][i],C[2][i],C[3][i],C[6][i],C[7][i],&fW[0],&fW[1],&fW[2]);
      double Rs=P[0][i],Re=P[0][i+1],Rw=C[0][i],Ss=P[1][i],Se=P[1][i+1],Sw=C[1][i];
      double rN=Re+Rw-Rs+hu*hv*fS[0], sN=Se+Sw-Ss+hu*hv*fS[1];
      double ruN=P[2][i+1]+hv*fE[0], rvN=C[3][i]+hu*fW[0], suN=P[4][i+1]+hv*fE[1], svN=C[5][i]+hu*fW[1], puN=P[6][i+1]+hv*fE[2], pvN=C[7][i]+hu*fW[2];
      double yN=yprev, gN=gprev, qN=qc[i+1], gvN=gc[i+1], qold=qc[i+1], gvold=gc[i+1];
      for(int it=0;it<niter+1;it++){
        { double W=exp(sN), r=rN, yy=yN, qq=qN, rho;
          for(int k=0;k<4;k++){
            rho=(mode>=2)? qq*W : -rvN; double psi=(1+4*yy*rho)/(r*r),Q,c1,c2,c3; coef(psi,&Q,&c1,&c2,&c3);
            gN=4*M_PI*r*c1*puN*puN/W; yy=yprev+0.5*hu*(gprev+gN);
            gvN=4*M_PI*r*c1*pvN*pvN/W; if(mode>=2) qq=qold+0.5*hv*(gvold+gvN);
          }
          yN=yy; ruN=-yN*W; if(mode>=2){ qN=qq; rvN=-qN*W; } }
        if(mode==3) rN=P[0][i+1]+0.5*hv*(P[3][i+1]+rvN);      // r from r_v = -rho along the column (trapezoid), data r(s,0) exact
        if(it==niter) break;
        F(rN,sN,ruN,rvN,puN,pvN,&fN[0],&fN[1],&fN[2]);
        double rc=0.25*(Rs+Re+Rw+rN), sc=0.25*(Ss+Se+Sw+sN);
        double ruc=0.25*(P[2][i]+P[2][i+1]+C[2][i]+ruN), rvc=0.25*(P[3][i]+P[3][i+1]+C[3][i]+rvN);
        double puc=0.25*(P[6][i]+P[6][i+1]+C[6][i]+puN), pvc=0.25*(P[7][i]+P[7][i+1]+C[7][i]+pvN);
        F(rc,sc,ruc,rvc,puc,pvc,&fC[0],&fC[1],&fC[2]);
        if(mode<3) rN=Re+Rw-Rs+hu*hv*fC[0];
        sN=Se+Sw-Ss+hu*hv*fC[1];
        if(mode<2) rvN=C[3][i]+0.5*hu*(fW[0]+fN[0]);
        suN=P[4][i+1]+0.5*hv*(fE[1]+fN[1]); svN=C[5][i]+0.5*hu*(fW[1]+fN[1]);
        puN=P[6][i+1]+0.5*hv*(fE[2]+fN[2]); pvN=C[7][i]+0.5*hu*(fW[2]+fN[2]);
      }
      yprev=yN; gprev=gN; qc[i+1]=(mode>=2)?qN:-rvN/exp(sN); gc[i+1]=gvN;
      C[0][i+1]=rN;C[1][i+1]=sN;C[2][i+1]=ruN;C[3][i+1]=rvN;C[4][i+1]=suN;C[5][i+1]=svN;C[6][i+1]=puN;C[7][i+1]=pvN;
    }
    for(int c=0;c<ncol;c++) for(int f=0;f<8;f++) out[((size_t)c*nv+(j+1))*8+f]=C[f][cols[c]];
    for(int k=0;k<nrow;k++) if(rows[k]==j+1) for(int f=0;f<8;f++) memcpy(snap+((size_t)k*8+f)*nu,C[f],sizeof(double)*nu);
    for(int f=0;f<8;f++){double *t=P[f];P[f]=C[f];C[f]=t;}
  }
  free(buf); free(qc); free(gc);
}
