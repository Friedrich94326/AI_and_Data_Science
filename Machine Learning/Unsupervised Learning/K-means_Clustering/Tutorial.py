""" Iris Dataset """

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()

print(type(iris)) # <class 'sklearn.utils.Bunch'>
print(iris.data)

# ground truth for the Iris dataset
print(iris.target)

# descriptoins of the data
print(iris.DESCR)


""" Visualise Iris data """

# Store iris.data
samples = iris.data

# Create x and y
x = samples[:, 0] # 
y = samples[:, 1]

# Plot x and y
plt.scatter(x, y, alpha = .5)

# Show the plot
plt.show()


""" Step 1: Place k random centroids for the initial clusters"""

# Number of clusters
k = 3

# Create x coordinates of k random centroids
centroids_x = np.random.uniform(min(x), max(x), size = k)

# Create y coordinates of k random centroids
centroids_y = np.random.uniform(min(y), max(y), size = k)

# Create centroids array
centroids = np.array(list(zip(centroids_x, centroids_y)))
print(centroids)


fig, ax = plt.subplots(2, 1, figsize = (10, 10))
# Make a scatter plot of x, y
ax[0].scatter(x, y)
ax[0].set_xlabel('sepal length (cm)')
ax[0].set_ylabel('sepal width (cm)')
ax[0].set_title('Raw Data')

# Make a scatter plot of the centroids
ax[1].scatter(centroids_x, centroids_y)
ax[1].set_xlabel('sepal length (cm)')
ax[1].set_ylabel('sepal width (cm)')
ax[1].set_title('Centroids')

# Display plot
plt.tight_layout()
plt.show()

