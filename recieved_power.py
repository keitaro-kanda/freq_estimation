import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize

#地表面パラメータ
epsilon_1 = 5.7
epsilon_0 = 1
losstangent = 0.01
radarcrosssection = 30.0
#レーダーパラメータ
P_t = 800 #[W]
P_min = 1e-12 #[W]
G_t = 1.64
#周波数
f1 = 10
f2 = 30
f3 = 50
f4 = 100

#光速
c = 299792458 #[m/s]
#探査深度
R = np.arange(1, 100, 0.1)


#反射係数・透過係数
reflection = (np.sqrt(epsilon_1) - np.sqrt(epsilon_0))**2 / (np.sqrt(epsilon_1) + np.sqrt(epsilon_0))**2
through = 1-reflection
print('反射係数', reflection)
print('投下係数', through)


#--------

def freq_depth_power():
    #meshの作成
    freq = np.arange(1, 201, 0.5)
    depth = np.arange(1, 51, 0.5)
    f, d = np.meshgrid(freq, depth)
    #ノイズレベル
    noise = 1e-12 #[W]
    #減衰率
    attenuation = 10**(-0.091*np.sqrt(epsilon_1)*losstangent*f*d/5)
    #パワーの計算
    power = P_t*G_t**2*(c/f*10**6)**2/(4*np.pi)**3/d**4 * radarcrosssection ** through**4 *reflection * attenuation**(2*d)
    power_dB = 10*np.log10(power/noise)

    #描画
    plt.pcolormesh(f, d, power_dB, cmap='coolwarm', norm=Normalize(vmin=-100, vmax=100))
    #カラーバー
    pp = plt.colorbar(orientation='vertical')
    pp.set_label('Echo Power to Noise Level [dB]', fontsize=15)
    #グラフの体裁
    plt.grid(linestyle='--', color='grey')
    plt.title('Echo from Tube Floor', fontsize=20)
    plt.xlabel('Frequency [MHz]', fontsize=15)
    plt.ylabel('Detecsion Depth [m]', fontsize=15)
    plt.savefig('fig/Echo_from_Tube_Floor.png')
    plt.show()


freq_depth_power()


def depth_power():
    #ノイズレベル
    noise = 1e-12 + R*0

    #減衰率
    attenuation_1 = 10**(-0.091*np.sqrt(epsilon_1)*losstangent*f1*R/5)
    attenuation_2 = 10**(-0.091*np.sqrt(epsilon_1)*losstangent*f2*R/5)
    attenuation_3 = 10**(-0.091*np.sqrt(epsilon_1)*losstangent*f3*R/5)
    attenuation_4 = 10**(-0.091*np.sqrt(epsilon_1)*losstangent*f4*R/5)

    #----天井----
    #反射
    P_r1 = P_t*G_t**2*(c/f1*10**6)**2/(4*np.pi)**3/R**4 * RCS ** through**2 *reflection * attenuation_1**(2*R)
    P_r2 = P_t*G_t**2*(c/f2*10**6)**2/(4*np.pi)**3/R**4 * RCS ** through**2 *reflection * attenuation_2**(2*R)
    P_r3 = P_t*G_t**2*(c/f3*10**6)**2/(4*np.pi)**3/R**4 * RCS ** through**2 *reflection * attenuation_3**(2*R)
    P_r4 = P_t*G_t**2*(c/f4*10**6)**2/(4*np.pi)**3/R**4 * RCS ** through**2 *reflection * attenuation_3**(2*R)


    #----床----
    #反射
    P_f1 = P_t*G_t**2*(c/f1*10**6)**2/(4*np.pi)**3/R**4 * RCS ** through**4 *reflection * attenuation_1**(2*R)
    P_f2 = P_t*G_t**2*(c/f2*10**6)**2/(4*np.pi)**3/R**4 * RCS ** through**4 *reflection * attenuation_2**(2*R)
    P_f3 = P_t*G_t**2*(c/f3*10**6)**2/(4*np.pi)**3/R**4 * RCS ** through**4 *reflection * attenuation_3**(2*R)
    P_f4 = P_t*G_t**2*(c/f4*10**6)**2/(4*np.pi)**3/R**4 * RCS ** through**4 *reflection * attenuation_4**(2*R)


    plt.figure(figsize=(14, 7))
    #天井のプロット
    plt.subplot(1, 2, 1, title='echo from tube roof')
    plt.plot(R, P_r1, label='freq='+str(f1)+'[MHz]')
    plt.plot(R, P_r2, label='freq='+str(f2)+'[MHz]')
    plt.plot(R, P_r3, label='freq='+str(f3)+'[MHz]')
    plt.plot(R, P_r4, label='freq='+str(f4)+'[MHz]')
    plt.plot(R, noise, label='noise level')
    #グラフの体裁
    plt.ylim(10**(-13), 1)
    plt.yscale('log')
    plt.xlabel('detection depth [m]', fontsize=15)
    plt.ylabel('recieved power [W]', fontsize=15)
    plt.legend(fontsize = 12)
    plt.grid()

    #床のプロット
    plt.subplot(1, 2, 2, title='echo from tube floor')
    plt.plot(R, P_f1, label='freq='+str(f1)+'[MHz]')
    plt.plot(R, P_f2, label='freq='+str(f2)+'[MHz]')
    plt.plot(R, P_f3, label='freq='+str(f3)+'[MHz]')
    plt.plot(R, P_f4, label='freq='+str(f4)+'[MHz]')
    plt.plot(R, noise, label='noise level')
    #グラフの体裁
    plt.ylim(10**(-13), 1)
    plt.yscale('log')
    plt.xlabel('detection depth [m]', fontsize=15)
    plt.ylabel('recieved power [W]', fontsize=15)
    plt.legend(fontsize = 12)
    plt.grid()


    plt.show()

#depth_power()