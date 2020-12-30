import codecademylib3_seaborn
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from copy import deepcopy
from sklearn.cluster import KMeans 

x = [1, 1, 4, 4]
y = [1, 3, 1, 3]

values = np.array(list(zip(x, y)))

centroids_x = [2.5, 2.5]
centroids_y = [1, 3]

centroids = np.array(list(zip(centroids_x, centroids_y)))

""" Original K-Means """
model_1 = KMeans(init = 'random', n_clusters = 2)

# Initial centroids
plt.scatter(centroids[:, 0], centroids[:, 1], marker = 'D', s = 100)

results_1 = model_1.fit_predict(values)

plt.scatter(x, y, c = results_1, alpha = 1)

# Cluster centers
plt.scatter(model_1.cluster_centers_[:, 0], model_1.cluster_centers_[:, 1], marker = 'v', s = 100)

""" K-Means++ """
model_2 = KMeans(init = 'k-means++', n_clusters = 2)

# Initial centroids
#plt.scatter(centroids[:, 0], centroids[:, 1], marker = 'D', s = 100)

results_2 = model_2.fit_predict(values)



# Cluster centers




fig, ax = plt.subplots(2, 1)
ax[0].scatter(x, y, c = results_1, alpha = 1)
ax[0].scatter(model_1.cluster_centers_[:, 0], model_1.cluster_centers_[:, 1], marker = 'v', s = 100)
ax[0].set_xticks([0, 1, 2, 3, 4, 5])
ax[0].set_yticks([0, 1, 2, 3, 4])
ax[0].set_title('Original K-Means Initialization')


ax[1].scatter(x, y, c = results_2, alpha = 1)
ax[1].scatter(model_2.cluster_centers_[:, 0], model_2.cluster_centers_[:, 1], marker = 'v', s = 100)
ax[1].set_xticks([0, 1, 2, 3, 4, 5])
ax[1].set_yticks([0, 1, 2, 3, 4])
ax[1].set_title('K-Means++ Initialization')
plt.tight_layout()
plt.show()


print("The model's inertia is " + str(model_1.inertia_))
print("The model's inertia is " + str(model_2.inertia_))
