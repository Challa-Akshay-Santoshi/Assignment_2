 # C. Akshay Santoshi
 # CS21BTECH11012
 # To find regression line
 
 # SIMPLER WAY TO FIND REGRESSION LINE IS IN 'figure.py' FILE
 
 import pandas as pd
 
 # Reads the data from excel and prints it.
 df= pd.read_excel(r'C:\Users\aksha\Documents\Book1.xlsx')
 print(df)
 
 # To calculate sigma x, we add the data from the column "x"
 x = []
 x = list(df['x'])
 print(x)
 sigma_x = sum(x)
 
 # To calculate sigma y, we add the data from column "y"
 y = []
 y = list(df['y'])
 print(y)
 sigma_y = sum(y)
 
 # To calculate sigma xy, we have to multiply column "x" and column "y" and define it in a seperate column
 df["xy"] = df["x"] * df["y"]
 print(df)
 xy = list(df['xy'])
 print(xy)
 sigma_xy = sum(xy)
 
 # To calculate sigma x^2
 df["x^2"] = df["x"] * df["x"]
 print(df)
 x_square = list(df['x^2'])
 print(x_square)
 sigma_x_square = sum(x_square)
 
 # Let regression line be y= A + Bx
 # To calulate B
 n = len(x)
 B = ((n * sigma_xy) - (sigma_x*sigma_y))/((n * sigma_x_square) - (sigma_x * sigma_x))
 
 # To calculate A
 A = sigma_y/n - (B * (sigma_x/n))
 
 print("Regression line of y on x is y = " + A " + " + B " x.")
 
 # To calaculate y_value when x_value is 14.
 x_value = 14
 y_value = A + (B * x_value)
 
 print(" The estimated value of y when x = " + x_value " is " + y_value ".")