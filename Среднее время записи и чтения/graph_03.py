import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
import numpy as np

pd.plotting.register_matplotlib_converters()
df = pd.read_excel('graphs_sheikh.xlsx', sheet_name='Среднее время записи и чтения(у')
pd.pivot_table(df, index=["Время"],
               values=["Среднее время выполнения чтения/записи", "Среднее время обслуживания чтения/записи"],
               aggfunc=[np.sum],
               fill_value=0).plot()
plt.title("Среднее время чтение/записи (устройство)")
plt.ylabel("Время, мс")
plt.savefig('graph_03')
plt.show()


