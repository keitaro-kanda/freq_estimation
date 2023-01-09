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


#--------

def freq_depth_power(epsilon):
    #meshの作成
    freq = np.arange(1, 201, 0.5)
    depth = np.arange(1, 51, 0.5)
    f, d = np.meshgrid(freq, depth)

    #ノイズレベル
    noise = 1e-12 #[W]
    #減衰率
    attenuation = 10**(-0.091*np.sqrt(epsilon)*losstangent*f*d/5)
    #反射係数・透過係数
    reflection = (np.sqrt(epsilon) - np.sqrt(epsilon_0))**2 / (np.sqrt(epsilon) + np.sqrt(epsilon_0))**2
    through = 1-reflection
    print('反射係数', reflection)
    print('投下係数', through)
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
    plt.savefig('fig/epsilon='+str(epsilon)+'.png')
    plt.show()


freq_depth_power(5.7)