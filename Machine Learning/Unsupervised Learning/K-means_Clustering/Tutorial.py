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


""" Observe Iris dataset """

# Store iris.data
samples = iris.data

# Create x and y
x = samples[:, 0] # 
y = samples[:, 1]

# Plot x and y
plt.scatter(x, y, alpha = .5)

# Show the plot
plt.show()


""" Step 1: Place k random centroids for the initial clusters """

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


""" Step 2: Assign samples to nearest centroid  """

# Distance formula
def distance(a, b):
  dist = 0
  for i in range(len(a)):
    dist += (a[i] - b[i]) ** 2
  return dist ** 0.5

# To store the value of centroids when it updates
centroids_old = np.zeros(centroids.shape)

# Cluster labels for each point (either 0, 1, or 2)
labels = np.zeros(len(samples))

# Distances to each centroid (k distances)
distances = np.zeros(k)


# Assign to the closest centroid
for i in range(len(samples)):
  for j in range(k):
    distances = distance(sepal_length_width[j], centroids[j])

  cluster = np.argmin(distances)
  labels[i] = cluster

# Print labels
print(labels)


""" Step 3: Update centroids """

# Store previous centroids 
centroids_old = deepcopy(centroids)


for i in range(k):
  # Calculate the mean of the points that have the same cluster label
  points = [sepal_length_width[j] for j in range(len(samples)) if labels[j] == i]

  # Update K means
  centroids[i] = np.mean(points, axis = 0)


print(centroids_old)
print(centroids)


""" Step 4: Repeat Steps 2 and 3 until convergence """

while error.all() != 0:
  # Step 2: Assign samples to nearest centroid
  for i in range(len(samples)):
    for j in range(k):
      distances = distance(sepal_length_width[j], centroids[j])
    cluster = np.argmin(distances)
    labels[i] = cluster

  # Step 3: Update centroids
  centroids_old = deepcopy(centroids)
  for i in range(k):
    points = [sepal_length_width[j] for j in range(len(sepal_length_width)) if labels[j] == i]
    centroids[i] = np.mean(points, axis = 0)

  # Update error
  for j in range(k):
    error[j] = distance(centroids[j], centroids_old[j])


# Visualise results
colours = ['r', 'g', 'b']

for i in range(k):
  points = np.array([sepal_length_width[j] for j in range(len(samples)) if labels[j] == i])
  plt.scatter(points[:, 0], points[:, 1], c = colours[i], alpha=0.5)

plt.scatter(centroids[:, 0], centroids[:, 1], marker = 'D', s = 150)

plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')

plt.show()


