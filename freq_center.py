from cProfile import label

import matplotlib.pyplot as plt
import numpy as np

#地表面パラメータ
epsilon_1 = 4.0
epsilon_0 = 1
losstangent = 0.01
RCS = 1.0
#レーダーパラメータ
P_t = 800 #[W]
P_min = 1e-12 #[W]
G_t = 1.64
f = np.arange(0, 2000, 1)
#光速
c = 299792458 #[m/s]
#最大探査深度
R1 = 10
R2 = 15
R3 = 20
R4 = 25
R5 = 30
R6 = 35
R7 = 40


#反射係数・透過係数
reflection = (np.sqrt(epsilon_1) - np.sqrt(epsilon_0))**2 / (np.sqrt(epsilon_1) + np.sqrt(epsilon_0))**2
through = 1-reflection


#----計算----
#左辺
#天井
roof_l1 = f*10**6/10**(-0.091*np.sqrt(epsilon_1)*losstangent*R1/5*f)
roof_l2 = f*10**6/10**(-0.091*np.sqrt(epsilon_1)*losstangent*R2/5*f)
roof_l3 = f*10**6/10**(-0.091*np.sqrt(epsilon_1)*losstangent*R3/5*f)
roof_l4 = f*10**6/10**(-0.091*np.sqrt(epsilon_1)*losstangent*R4/5*f)
roof_l5 = f*10**6/10**(-0.091*np.sqrt(epsilon_1)*losstangent*R5/5*f)

#床
floor_l1 = f*10**6/10**(-0.091*np.sqrt(epsilon_1)*losstangent*R3/5*f)
floor_l2 = f*10**6/10**(-0.091*np.sqrt(epsilon_1)*losstangent*R4/5*f)
floor_l3 = f*10**6/10**(-0.091*np.sqrt(epsilon_1)*losstangent*R5/5*f)
floor_l4 = f*10**6/10**(-0.091*np.sqrt(epsilon_1)*losstangent*R6/5*f)
floor_l5 = f*10**6/10**(-0.091*np.sqrt(epsilon_1)*losstangent*R7/5*f)


#右辺
#天井
roof_r1 = P_t/P_min * (G_t**2 * c * RCS)/((4*np.pi)**3 * R1**4) * through**2 * reflection + f*0
roof_r2 = P_t/P_min * (G_t**2 * c * RCS)/((4*np.pi)**3 * R2**4) * through**2 * reflection + f*0
roof_r3 = P_t/P_min * (G_t**2 * c * RCS)/((4*np.pi)**3 * R3**4) * through**2 * reflection + f*0
roof_r4 = P_t/P_min * (G_t**2 * c * RCS)/((4*np.pi)**3 * R4**4) * through**2 * reflection + f*0
roof_r5 = P_t/P_min * (G_t**2 * c * RCS)/((4*np.pi)**3 * R5**4) * through**2 * reflection + f*0
#床
floor_r1 = P_t/P_min * (G_t**2 * c * RCS)/((4*np.pi)**3 * R3**4) * through**4 * reflection + f*0
floor_r2 = P_t/P_min * (G_t**2 * c * RCS)/((4*np.pi)**3 * R4**4) * through**4 * reflection + f*0
floor_r3 = P_t/P_min * (G_t**2 * c * RCS)/((4*np.pi)**3 * R5**4) * through**4 * reflection + f*0
floor_r4 = P_t/P_min * (G_t**2 * c * RCS)/((4*np.pi)**3 * R6**4) * through**4 * reflection + f*0
floor_r5 = P_t/P_min * (G_t**2 * c * RCS)/((4*np.pi)**3 * R7**4) * through**4 * reflection + f*0


#----描画----
plt.figure(figsize=(16, 8))
#----天井のプロット----
plt.subplot(121, title='roof')
plt.plot(f, roof_l1, color='b', label='roof_l side, R=10' ) #左辺
plt.plot(f, roof_r1, color='b',linestyle='--', label='roof_r side, R=10' ) #右辺

plt.plot(f, roof_l2, color='r', label='roof_l side, R=15' )
plt.plot(f, roof_r2, color='r',linestyle='--', label='roof_r side, R=15' )

plt.plot(f, roof_l3, color='g', label='roof_l side, R=20' )
plt.plot(f, roof_r3, color='g',linestyle='--', label='roof_r side, R=20' )

plt.plot(f, roof_l4, color='k', label='roof_l side, R=25' )
plt.plot(f, roof_r4, color='k',linestyle='--', label='roof_r side, R=25' )

plt.plot(f, roof_l5, color='orange', label='roof_l side, R=30' )
plt.plot(f, roof_r5, color='orange',linestyle='--', label='roof_r side, R=30' )

#グラフの体裁
plt.ylim(10**13, 10**16)
plt.yscale('log')
plt.xlabel('frequency[MHz]')
plt.legend(fontsize = 8)

plt.grid()

#----床のプロット----
plt.subplot(122, title='floor')
plt.plot(f, floor_l1, color='b', label='floor_l side, R=20' ) #左辺
plt.plot(f, floor_r1, color='b',linestyle='--', label='roof_r side, R=20' ) #右辺

plt.plot(f, floor_l2, color='r', label='roof_l side, R=25' )
plt.plot(f, floor_r2, color='r',linestyle='--', label='roof_r side, R=25' )

plt.plot(f, floor_l3, color='g', label='roof_l side, R=30' )
plt.plot(f, floor_r3, color='g',linestyle='--', label='roof_r side, R=30' )

plt.plot(f, floor_l4, color='k', label='roof_l side, R=35' )
plt.plot(f, floor_r4, color='k',linestyle='--', label='roof_r side, R=35' )

plt.plot(f, floor_l5, color='orange', label='roof_l side, R=40' )
plt.plot(f, floor_r5, color='orange',linestyle='--', label='roof_r side, R=40' )

#グラフの体裁
plt.ylim(10**13, 10**16)
plt.yscale('log')
plt.xlabel('frequency[MHz]')
plt.legend(fontsize = 8)

plt.grid()


plt.show()