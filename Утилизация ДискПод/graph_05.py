import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
import numpy as np
pd.plotting.register_matplotlib_converters()

df = pd.read_excel('graphs_sheikh.xlsx', sheet_name='Утилизация ДискПод')
pd.pivot_table(df, index='Время',
               values='Утилизация CPU дисковой подсистемой',
               aggfunc=np.sum,
               fill_value=0).plot()
plt.title("Утилизация CPU дисковой подсистемы (устройство)")
plt.xlabel('Продолжительность теста ч:мм')
plt.ylabel("Утилизация CPU дисковой подсистемы")
plt.savefig('graph_05')
plt.show()