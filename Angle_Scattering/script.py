import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def read_data(csv,nth_degree):
    df = pd.read_csv(csv,header=None)

    curve = np.polyfit(df[0],df[1],nth_degree) #polynomial to the 3rd degree with its coefficients
    poly = np.poly1d(curve)
    
    x_fit = np.linspace(df[0].iloc[0],df[0].iloc[-1])
    y_fit = poly(x_fit) #plugs in our values as a function of x

    
    plt.plot(df[0],df[1],'.',x_fit,y_fit)
    plt.show()


read_data('clark2010_75.csv')
