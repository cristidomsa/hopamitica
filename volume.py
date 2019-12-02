import math

R1 = 2.0
R2 = 1.0
Rc = 0.5

x1 = 0.5
x2 = 0.5
xG = 2.5
h = 4.0

G_mic = 0.33
G_mare = 0.7

RTT1 = math.sqrt(x2*(2*R2-x2))
RBT1 = math.sqrt(x1*(2*R1-x1))
VT1 = (3.14*h*(RBT1**2 + RTT1**2 + RBT1*RTT1))/3
VS1 = (4*3.14*R1**3 - 3.14*x1**2*(3*R1 - x1))/3
VS2 = (4*3.14*R2**3 - 3.14*x2**2*(3*R2 - x2))/3

VSG = (3.14*xG**2*(3*R1 - xG))/3

VS_mare = (4*3.14*R1**3)/3
VS_mica = (4*3.14*R2**3)/3

VCg = 3.14*Rc**2*(h+R2+R1)
VT1 = VT1-VCg

print("Volum trunchi de con: ", VT1)
print("Volum cilindru scos: ", VCg)
print("Volum sfera mare (fara calota): ", VS1)
print("Volum sfera mica (fara calota): ", VS2)
print("Volum sfera mare: ", VS_mare)
print("Volum sfera mica: ", VS_mica)

print("Volum calota grea: ", VSG)
print("Greutate calota grea: ", VSG*G_mare)

print("Volum tot: ", VS1+VS2+VT1)

G_T = h - (RBT1 * h)/(RBT1+RTT1)
G_total_usor = (VS2 + VT1 + VS1 - VSG) * G_mic
G_total_greu = (VSG) * G_mare

print("Volum greu: {} --- Volum usor: {} --- Raport: {}".format(VSG, (VS2 + VT1 + VS1 - VSG), VSG/(VS2 + VT1 + VS1 - VSG)))
print("Greutate mare: {} --- Greutate mica: {} --- Raport: {}".format(G_total_greu, G_total_usor, G_total_greu/(G_total_usor+G_total_greu)))

GS1_usor = (VS1-VSG)*G_mic

print("Centru greutate T: ", G_T)
print("Centru greutate S2: ", R2)
print("Centru greutate S1: ", R1 - R1*G_total_greu/(G_total_greu+GS1_usor))

