from sklearn.cluster import DBSCAN
import scripts.data_handler as data
import matplotlib.pyplot as plt

X, mean, std = data.get_total_data('DECEL_020G_15KMH_30KMH')

db = DBSCAN(eps=0.4, min_samples=5)
db.fit(X)

y_pred = db.fit_predict(X)

X = X*std
X = X + mean

plt.figure(figsize=(10,6))
plt.scatter(X[:,0], X[:,1],c=y_pred, cmap='Paired')
plt.title("Clusters determined by DBSCAN")

dangerous = y_pred == -1

x = X[dangerous]

plt.figure(figsize=(10,6))
plt.scatter(x[:,0], x[:,1], cmap='Paired')
plt.title("Dangerous locations")
plt.show()

ax = data.plot_3D(X,y_pred)

