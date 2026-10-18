// Collapse driver (Paper F, tails): same free-evolution arithmetic as evolve_stream_qtg (qtg_dn.c, included verbatim), plus
//   * full-row snapshots at requested v-indices,
//   * per-row apparent-horizon tracker: ah[j] = fractional u-index where r_v changes sign (first sign change from small u), -1 if none.
#include "../../qtg_dn.c"
void evolve_col(int nu,int nv,double hu,double hv,int model_,double L2_,const double *row0,const double *col0,int ncol,const int *cols,double *out,int niter,int nrow,const int *rows,double *snap,double *ah)
{
  model=model_; L2=L2_;
  double *buf=(double*)malloc(sizeof(double)*8*nu*2);
  double *P[8],*C[8]; for(int f=0;f<8;f++){P[f]=buf+f*nu; C[f]=buf+(8+f)*nu; memcpy(P[f],row0+(size_t)f*nu,sizeof(double)*nu);}
  for(int j=0;j<nv;j++){
    if(j>0){
      for(int f=0;f<8;f++) C[f][0]=col0[(size_t)f*nv+j];
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
      for(int f=0;f<8;f++){double *t=P[f];P[f]=C[f];C[f]=t;}
    }
    // P now holds row j
    for(int c=0;c<ncol;c++) for(int f=0;f<8;f++) out[((size_t)c*nv+j)*8+f]=P[f][cols[c]];
    for(int k=0;k<nrow;k++) if(rows[k]==j) for(int f=0;f<8;f++) memcpy(snap+((size_t)k*8+f)*nu,P[f],sizeof(double)*nu);
    ah[j]=-1; for(int i=0;i<nu-1;i++) if(P[3][i]>0 && P[3][i+1]<=0){ ah[j]=i+P[3][i]/(P[3][i]-P[3][i+1]); break; }
  }
  free(buf);
}
