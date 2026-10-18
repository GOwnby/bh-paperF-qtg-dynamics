// Linear massless scalar (l=0) on a static background in Eddington null coordinates, psi=r*phi, psi_uv=-(V/4) psi, V=f f'/r; V is tabulated vs (v-u)/2 on the uniform lattice.
// Standard Gundlach-Price-Pullin (1994) second-order scheme: psi_N=psi_E+psi_W-psi_S-(h^2/8) V_c (psi_E+psi_W), V_c = V at the cell centre.
// row0[nu]: psi on v=v_start, col0[nv]: psi on u=u_start; Vc[j][i] = Vt[j-i+off] ; diag[nv]: psi along lattice index i=j+di (the line r* = const) for every row.
#include <stdlib.h>
#include <string.h>
void evolve_L(int nu,int nv,double h,const double *row0,const double *col0,const double *Vt,int off,int di,double *diag,double *last)
{
  double *P=(double*)malloc(sizeof(double)*nu), *C=(double*)malloc(sizeof(double)*nu);
  memcpy(P,row0,sizeof(double)*nu);
  for(int j=0;j<nv;j++){
    if(j>0){
      C[0]=col0[j];
      for(int i=0;i<nu-1;i++){
        double Vc=Vt[j-1-i+off];       // centre of cell (i,j-1) -> (i+1,j): lattice index (j-1)-i  (x_c = x0 + ((j-1)-i) h/2 + h/2 -> table is defined at centres)
        C[i+1]=P[i+1]+C[i]-P[i]-(h*h/8)*Vc*(P[i+1]+C[i]);
      }
      double *t=P;P=C;C=t;
    }
    int i=j+di; diag[j]=(i>=0&&i<nu)?P[i]:0.0;
  }
  memcpy(last,P,sizeof(double)*nu);
  free(P);free(C);
}
