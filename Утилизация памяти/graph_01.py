import pandas as pd
import openpyxl
import matplotlib.pyplot as plt

pd.plotting.register_matplotlib_converters()

df = pd.read_excel('graphs_sheikh.xlsx', sheet_name='Утилизация памяти', usecols=['Время', 'Утилизация памяти', 'Утилизация подкачки'])
x = df['Время']
y = df['Утилизация памяти']
y1 = df['Утилизация подкачки']
fig, ax1 = plt.subplots(nrows = 1, ncols = 1, figsize=(30, 20), dpi=200)
ax1.plot(x, y, color='Red', label='Утилизация памяти', linewidth=5)
ax2 = ax1.twinx()
ax2.plot(x, y1, color='Blue', label='Утилизация подкачки', linewidth=5)
ax1.set_xlim(['9:10', '12:37'])
ax1.set_ylim([0, 100])
ax2.set_ylim([0, 0.12])
ax1.set_title('Утилизация памяти', fontsize=20)
ax1.set_xlabel('Продолжительность теста ч:мм', fontsize=10)
ax1.set_ylabel('Утилизация памяти')
ax2.set_ylabel('Утилизация подкачки %')
ax1.legend(loc='right', fontsize=10)
ax2.legend(fontsize=10)
fig.savefig('graph_01', transparent=False, dpi=100, bbox_inches="tight")
plt.show()
