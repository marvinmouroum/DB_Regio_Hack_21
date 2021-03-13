import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

from mpl_toolkits import mplot3d

import data_handler as data
import map_gen as mapper


def find_optimal_number_of_clusters():
    wcss = []
    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
        kmeans.fit(X)
        wcss.append(kmeans.inertia_)
    plt.plot(range(1, 11), wcss)
    plt.title('Elbow Method')
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS')
    plt.show()

X, mean, std = data.get_total_data('DECEL_020G_15KMH_30KMH')

a1 = 0
a2 = 1
a3 = 2

#X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)
#plt.scatter(X[:,a1], X[:,a2], X[:,a3])

#find_optimal_number_of_clusters()

kmeans = KMeans(n_clusters=20, init='k-means++', max_iter=300, n_init=10, random_state=0)
pred_y = kmeans.fit_predict(X)
plt.scatter(X[:,a1], X[:,a2], X[:,a3])
#plt.scatter(kmeans.cluster_centers_[:, a1], kmeans.cluster_centers_[:, a2], kmeans.cluster_centers_[:, a3], s=300, c='red')
plt.show()

data.plot_3D(X,pred_y)
