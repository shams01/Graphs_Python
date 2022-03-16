import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
import numpy as np
pd.plotting.register_matplotlib_converters()

df = pd.read_excel('graphs_sheikh.xlsx', sheet_name='Утилиз Сет интерфейса')
pd.pivot_table(df, index=['Время'],
               values=['Принимаемые данные', 'Передаваемые данные'],
               aggfunc=np.sum,
               fill_value=0).plot()
plt.title('Утилизация сетевого интерфейса (интерфейс)')
plt.xlabel('Продолжительность теста ч:мм')
plt.ylabel('Утилизация сетевого интерфейса , Кбит/с')
plt.savefig('graph_06')
plt.show()