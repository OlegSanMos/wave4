import numpy as np
import matplotlib.pyplot as plot


def read(filename):
    with open(filename) as f:
        lines = f.readlines()

    duration = float(lines[2].split()[2])
    samples = np.asarray(lines[4:], dtype=int)
    
    return samples, duration, len(samples)


samples20, duration20, len20 = read('20mm.txt')
samples40, duration40, len40 = read('40mm.txt')
samples60, duration60, len60 = read('60mm.txt')
samples80, duration80, len80 = read('80mm.txt')
samples100, duration100, len100 = read('100mm.txt')
samples120, duration120, len120 = read('120mm.txt')

samples = np.hstack([samples20, samples40, samples60, samples80, samples100, samples120])
x = [20]*len20 + [40]*len40 + [60]*len60 + [80]*len80 + [100]*len100 + [120]*len120

x1 = [i/500 for i in range(10000, 60000)]
y = np.polyval(np.polyfit(x,samples,3), x1 )


fig, ax = plot.subplots(figsize = (16, 10), dpi = 400)
ax.plot(x1, y)

plt.xlabel("Время, с")
plt.title("Зависимость уровня воды от времени")
plt.ylabel("Уровень воды, мм")
plt.legend("h(t)")
plt.minorticks_on()

plt.grid(which='major', color='grey', linestyle='--', linewidth = 1)
plt.grid(which='minor', color='grey', linestyle='--', linewidth = 1)

ax.set_xlim([min(y), 1.1*max(y)])
ax.set_ylim([min(x1), 1.05*max(x1)])

plt.text(80, 2.5, "Экспериментально полученная скорость = ")
plt.text(80, 2.0, "Теоретически полученная скорость = ")


fig.savefig("wave_calibration.png")


value_of_waves, duration, len_of_waves = read('wave.txt')

for k in range(len_of_waves):
    i = 0
    while (y[i] < value_of_waves[k] ):
        i += 1
    value_of_waves[k] = x1[i]


step_of_time = duration/len_of_waves

time = []
for i in range(len_of_waves):
    time.append(step_of_time*i)

fig1, ax1 = plot.subplots(figsize = (16, 10), dpi = 400)
ax1.plot(time[:len(time)//2],value_of_waves[:len(value_of_waves)//2])
fig1.savefig("value_of_waves.png")
