import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
import numpy as np
pd.plotting.register_matplotlib_converters()

df = pd.read_excel('graphs_sheikh.xlsx', sheet_name='Очередь дисковой подсистемы')
pd.pivot_table(df, index='Время',
               values='Очередь дисковой подсистемы',
               aggfunc=np.sum,
               fill_value=0).plot()
plt.title("Очередь дисковой подсистемы")
plt.xlabel('Продолжительность теста ч:мм')
plt.ylabel("Очередь дисковой подсистемы")
plt.savefig('graph_04')
plt.show()
