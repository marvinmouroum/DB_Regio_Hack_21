import pandas as pd
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

def get_total_data():
    df = pd.read_csv('../data/Telematik_Events.csv', sep=';')
    # print(df)
    data = df[['lat','lon','dur']].dropna()

    arr = data.values
    mean = np.mean(arr,0)
    std = np.std(arr,0)

    arr_m = arr-mean
    arr_m_s = arr_m/std

    return arr_m_s

#t = get_total_data()
#print(t)

def plot_3D(X,pred_y):
    ax = plt.axes(projection='3d')
    ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=pred_y, cmap='viridis', linewidth=0.5);

    plt.show()