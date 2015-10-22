# writing a python script that calls different directories
A = ['1E4', '1E5', '5E5', '7E5', '1E6', '1.05E6', '1.1E6', '1.2E6', '1.5E6', '2E6']
for a in A:
   inputdir = "../../../COMBI_Output/Noise Studies/{} Macro Particles/10KT_{}MP_IP1hoN0.0025/".format(a)
