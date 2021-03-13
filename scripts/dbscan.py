from sklearn.cluster import DBSCAN
import scripts.data_handler as data
import matplotlib.pyplot as plt
import numpy as np
import scripts.map_gen as mapper

x0 = data.get_total_data('DECEL_020G_15KMH_30KMH')
x1 = data.get_total_data('DECEL_018G_30KMH_45KMH')
x2 = data.get_total_data('DECEL_016G_45KMH_60KMH')
x3 = data.get_total_data('DECEL_014G_60KMH_75KMH')
x4 = data.get_total_data('DECEL_012G_75KMH')

x_sum = np.concatenate((x0, x1), axis=0)
x_sum = np.concatenate((x_sum, x2), axis=0)
x_sum = np.concatenate((x_sum, x3), axis=0)
x_sum = np.concatenate((x_sum, x4), axis=0)

X, mean, std = data.zero_mean(x_sum)

db = DBSCAN(eps=0.5, min_samples=5)
db.fit(X)

y_pred = db.fit_predict(X)

X = X*std
X = X + mean

plt.figure(figsize=(10,6))
plt.scatter(X[:,0], X[:,1],c=y_pred, cmap='Paired')
plt.title("Clusters determined by DBSCAN")

dangerous = y_pred == -1

x = X[dangerous]

trip_info = data.get_bounding_data()
vin = trip_info[:,0]
bounding_boxes = [(trip_info[:,1],trip_info[:,3],(trip_info[:,2],trip_info[:,4]))]

plt.figure(figsize=(10,6))
plt.scatter(x[:,0], x[:,1], cmap='Paired')
plt.title("Dangerous locations")
plt.show()


#ax = data.plot_3D(x,y_pred)
ax = data.plot_3D_simple(x)
#boundingBox = [(lat,lon),(lat,lon)]

def inBox(box,point):
    if point[0] >= box[0][0] and point[1] >= box[0][1]:
        if point[1] <= box[1][0] and point[1] <= box[1][1]:
            return True

    return False


print("number of bounding boxes => ", len(trip_info))

for info in trip_info:
    point_list = []

    box = [(info[1],info[3]),(info[2],info[4])]
    counter = 0
    print("\nlooping through " + str(x.shape[0]) + " points")
    for point in x:
        if inBox(box,point):
            counter += 1
            print("appened a point ratio ", counter/x.shape[0])
            point_list.append(point)

    if len(point_list) > 5:
        x_new = np.array(point_list)
        mapper.gen_heat_map(x_new, "dbscan")
        break



