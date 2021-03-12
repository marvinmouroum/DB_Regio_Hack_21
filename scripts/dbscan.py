from sklearn.cluster import DBSCAN
import scripts.data_handler as data
import matplotlib.pyplot as plt

X = data.get_total_data('DECEL')[0:1000]

plt.figure(figsize=(10,6))

db = DBSCAN(eps=0.4, min_samples=20)
db.fit(X)

y_pred = db.fit_predict(X)
plt.figure(figsize=(10,6))
plt.scatter(X[:,0], X[:,1],c=y_pred, cmap='Paired')
plt.title("Clusters determined by DBSCAN")
#plt.show()

data.plot_3D(X,y_pred)
