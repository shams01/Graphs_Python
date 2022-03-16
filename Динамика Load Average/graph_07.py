import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
pd.plotting.register_matplotlib_converters()

df = pd.read_excel('graphs_sheikh.xlsx', sheet_name='Динамика Load Average')
x = df['Время']
y = df['за 1 минуту']
y1 = df['за 5 минут']
y2 = df['за 15 минут']
ax1 = plt.axes()
ax1.set_ylim([0, 3])
line_01 = ax1.plot(x, y, color='blue', label='за 1 минуту')
line_02 = ax1.plot(x, y1, color='green', label='за 5 минут')
line_03 = ax1.plot(x, y2, color='red', label='за 15 минут')
ax1.set_xlabel('Продолжительность теста ч:мм')
ax1.set_ylabel('Динамика Load Average')
ax1.set_title('Динамика Load Average')
ax1.legend(loc='lower right')
plt.savefig('graph_07')
plt.show()
