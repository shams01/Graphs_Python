import pandas as pd
import openpyxl
import matplotlib.pyplot as plt

pd.plotting.register_matplotlib_converters()

df = pd.read_excel('graphs_sheikh.xlsx', sheet_name='Утилизация CPU')
x = df['Время']
y = df['Утилизация CPU']
y1 = df['Длина очереди']
fig, ax1 = plt.subplots(nrows=1, ncols=1, figsize=(30, 20), dpi=100)
ax1.plot(x, y, color='Red', label='Утилизация CPU', linewidth=5)
ax2 = ax1.twinx()
ax2.plot(x, y1, color='Blue', label='Длина очереди', linewidth=5)
ax1.set_xlim(['9:10', '12:37'])
ax1.set_ylim([0, 100])
ax2.set_ylim([0, 8])
ax1.set_title('Утилизация CPU', fontsize=20)
ax1.set_xlabel('Продолжительность теста ч:мм', fontsize=10)
ax1.set_ylabel('Утилизация CPU %')
ax2.set_ylabel('Длина очереди шт')
ax1.legend(loc='lower right', fontsize=10)
ax2.legend(loc='right', fontsize=10)
fig.savefig('graph_02', transparent=False, dpi=100, bbox_inches="tight")
plt.show()