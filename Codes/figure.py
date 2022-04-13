import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df= pd.read_excel(r'C:\Users\aksha\Documents\Book1.xlsx')

x_list = list(df['x'])
x = np.array(x_list)

y_list = list(df['y'])
y = np.array(y_list)

plt.plot(x, y, 'o')

m, b = np.polyfit(x, y, 1) # For getting regression line

plt.plot(x, m*x + b, label = '4x-3y+10=0')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()
plt.show()