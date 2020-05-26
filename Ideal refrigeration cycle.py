# Consider an ideal refrigeration cycle that uses R134a as the working fluid.
# The temperature of the refrigerant in the evaporator is −20C, and in the condenser it is 40C.
# The refrigerant is circulated at the rate of 0.03 kg/s.
# Determine the COP and the capacity of the plant in rate of refrigeration.

import pyromat as pm
pm.config["unit_pressure"] = "kPa"
pm.config["def_p"] = 100

mp_R134a = pm.get("mp.C2H2F4")

m_dot = 0.03 #kg/s <-- given
T1 = -20 + 273.15 # K <--given
T3 = 40 +273.15 # K <--given

h1 = mp_R134a.hs(T=T1)[1]
s1 = mp_R134a.ss(T=T1)[1]
p_g = mp_R134a.ps(T=T3)
print(f"Enthalpy after evaporator: {round(float(h1),1)} kJ/kg")
print(f"Entropy after evaporator: {round(float(s1),4)} kJ/kg")
print(f"Vapour pressure: {round(float(p_g),1)} kPa")

s2 = s1
T2 = mp_R134a.T_s(s=s2, p=p_g)
h2 = mp_R134a.h(T=T2, p=p_g)
print(f"Enthalpy after compressor: {round(float(h2),1)} kJ/kg")
print(f"Temperature after compressor: {round(float(T2),1)} K")
w_c = h2-h1
print(f"Work done by compressor: {round(float(w_c),1)} kJ/kg")

h3 = mp_R134a.hs(p=p_g)[0]
s3 = mp_R134a.ss(p=p_g)[0]

h4 = h3
q_L = h1 - h4
print(f"Heat added by the evaporator: {round(float(q_L),1)} kJ/kg")

beta = q_L/w_c
print(f"Coefficient of performance: {round(float(beta),3)}")
print(f"Refrigeration capacity is: {q_L*m_dot} kW")


# The system can also be used as a heat pump, in which case it is desired to maintain a
# space at a temperature T_3 above that of the ambient T_1.

q_H = h2 -h3
print(f"Heat ejected by the condenser: {round(float(q_H),1)} kJ/kg")

beta = q_H/w_c
print(f"Coefficient of performance: {round(float(beta),3)}")



