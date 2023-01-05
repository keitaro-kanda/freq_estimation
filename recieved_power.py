import wave
from cProfile import label
from turtle import title

import matplotlib.pyplot as plt
import numpy as np

#地表面パラメータ
epsilon_r1 = 4.0
epsilon_r2 = 1
losstangent = 0.01
RCS = 1.0
#レーダーパラメータ
P_t = 800 #[W]
P_min = 1e-12 #[W]
G_t = 1.64
f = np.arange(1, 1000, 1)
#光速
c = 299792458 #[m/s]
#波長
wavelength=c/f
#最大探査深度
R1 = 10
R2 = 15
R3 = 20
R4 = 25
R5 = 30
R6 = 35
R7 = 40


#反射係数・透過係数
reflection = (np.sqrt(epsilon_r1) - np.sqrt(epsilon_r2))**2 / (np.sqrt(epsilon_r1) + np.sqrt(epsilon_r2))**2
through = 1-reflection

#ノイズレベル
noise = 1e-12 + f*0
#----天井----
#減衰率
attenuation_r1 = 10**(-0.091*np.sqrt(epsilon_r1)*losstangent*f*R1/10)
attenuation_r2 = 10**(-0.091*np.sqrt(epsilon_r1)*losstangent*f*R2/10)
attenuation_r3 = 10**(-0.091*np.sqrt(epsilon_r1)*losstangent*f*R3/10)
attenuation_r4 = 10**(-0.091*np.sqrt(epsilon_r1)*losstangent*f*R4/10)
attenuation_r5 = 10**(-0.091*np.sqrt(epsilon_r1)*losstangent*f*R5/10)
#反射
attenuation_1 = 10**(-0.091*np.sqrt(epsilon_r1)*losstangent*f*R1/5)
P_r1 = P_t*G_t**2*(wavelength)**2/(4*np.pi)**3/R1**4 * RCS ** through**2 *reflection * attenuation_r1**(2*R1)

attenuation_1 = 10**(-0.091*np.sqrt(epsilon_r1)*losstangent*f*R2/5)
P_r2 = P_t*G_t**2*(wavelength)**2/(4*np.pi)**3/R2**4 * RCS ** through**2 *reflection * attenuation_r2**(2*R2)

attenuation_1 = 10**(-0.091*np.sqrt(epsilon_r1)*losstangent*f*R3/5)
P_r3 = P_t*G_t**2*(wavelength)**2/(4*np.pi)**3/R3**4 * RCS ** through**2 *reflection * attenuation_r3**(2*R3)

attenuation_1 = 10**(-0.091*np.sqrt(epsilon_r1)*losstangent*f*R4/5)
P_r4 = P_t*G_t**2*(wavelength)**2/(4*np.pi)**3/R4**4 * RCS ** through**2 *reflection * attenuation_r4**(2*R4)

attenuation_1 = 10**(-0.091*np.sqrt(epsilon_r1)*losstangent*f*R5/5)
P_r5 = P_t*G_t**2*(wavelength)**2/(4*np.pi)**3/R5**4 * RCS ** through**2 *reflection * attenuation_r5**(2*R5)


#----床----
#減衰率
attenuation_r1 = 10**(-0.091*np.sqrt(epsilon_r1)*losstangent*f*R3/10)
attenuation_r2 = 10**(-0.091*np.sqrt(epsilon_r1)*losstangent*f*R4/10)
attenuation_r3 = 10**(-0.091*np.sqrt(epsilon_r1)*losstangent*f*R5/10)
attenuation_r4 = 10**(-0.091*np.sqrt(epsilon_r1)*losstangent*f*R6/10)
attenuation_r5 = 10**(-0.091*np.sqrt(epsilon_r1)*losstangent*f*R7/10)
#反射
attenuation_1 = 10**(-0.091*np.sqrt(epsilon_r1)*losstangent*f*R3/5)
P_f1 = P_t*G_t**2*(wavelength)**2/(4*np.pi)**3/R3**4 * RCS ** through**4 *reflection * attenuation_r1**(2*R3)

attenuation_1 = 10**(-0.091*np.sqrt(epsilon_r1)*losstangent*f*R4/5)
P_f2 = P_t*G_t**2*(wavelength)**2/(4*np.pi)**3/R4**4 * RCS ** through**4 *reflection * attenuation_r2**(2*R4)

attenuation_1 = 10**(-0.091*np.sqrt(epsilon_r1)*losstangent*f*R5/5)
P_f3 = P_t*G_t**2*(wavelength)**2/(4*np.pi)**3/R5**4 * RCS ** through**4 *reflection * attenuation_r3**(2*R5)

attenuation_1 = 10**(-0.091*np.sqrt(epsilon_r1)*losstangent*f*R6/5)
P_f4 = P_t*G_t**2*(wavelength)**2/(4*np.pi)**3/R6**4 * RCS ** through**4 *reflection * attenuation_r4**(2*R6)

attenuation_1 = 10**(-0.091*np.sqrt(epsilon_r1)*losstangent*f*R7/5)
P_f5 = P_t*G_t**2*(wavelength)**2/(4*np.pi)**3/R7**4 * RCS ** through**4 *reflection * attenuation_r5**(2*R7)


plt.figure(figsize=(16, 8))

plt.subplot(1, 2, 1, title='roof')
plt.plot(f, P_r1, label='depth='+str(R1)+'[m]')
plt.plot(f, P_r2, label='depth='+str(R2)+'[m]')
plt.plot(f, P_r3, label='depth='+str(R3)+'[m]')
plt.plot(f, P_r4, label='depth='+str(R4)+'[m]')
plt.plot(f, P_r5, label='depth='+str(R5)+'[m]')
plt.plot(f, noise, label='noise level')
#グラフの体裁
plt.ylim(10**(-13), 1)
plt.yscale('log')
plt.xlabel('frequency[MHz]')
plt.ylabel('recieved power[W]')
plt.legend(fontsize = 12)
plt.grid()

plt.subplot(1, 2, 2, title='floor')
plt.plot(f, P_f1, label='depth='+str(R3)+'[m]')
plt.plot(f, P_f2, label='depth='+str(R4)+'[m]')
plt.plot(f, P_f3, label='depth='+str(R5)+'[m]')
plt.plot(f, P_f4, label='depth='+str(R6)+'[m]')
plt.plot(f, P_f5, label='depth='+str(R7)+'[m]')
plt.plot(f, noise, label='noise level')
#グラフの体裁
plt.ylim(10**(-13), 1)
plt.yscale('log')
plt.xlabel('frequency[MHz]')
plt.ylabel('recieved power[W]')
plt.legend(fontsize = 12)
plt.grid()


plt.show()