// IIRCoeffs : coefficients (b0, b1, b2, a0, a1, a2) for N_SOS_SECTIONS cascaded SOS sections
#define IIR_QXY_RES_NBITS 13 // Q2.13
#define N_SOS_SECTIONS 4
int32_t IIRCoeffs[N_SOS_SECTIONS][6] = {
  {6936, -13193, 6936, 8192, -15063, 7798},
  {8192, -15587, 8192, 8192, -15393, 7858},                                         
  {8192, -15578, 8192, 8192, -15440, 8146},
  {8192, -15591, 8192, 8192, -15635, 8151}
};
int32_t IIRu[N_SOS_SECTIONS] = {0}, IIRv[N_SOS_SECTIONS] = {0};
