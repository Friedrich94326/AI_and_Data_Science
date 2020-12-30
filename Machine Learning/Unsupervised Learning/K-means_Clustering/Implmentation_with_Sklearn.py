# Implementing K-Means Clustering by Scikit-Learn

import codecademylib3_seaborn
import matplotlib.pyplot as plt
from sklearn import datasets


""" Training """

iris = datasets.load_iris()

samples = iris.data


# From sklearn.cluster, import KMeans class
from sklearn.cluster import KMeans

# Use KMeans() to create a model that finds 3 clusters
model = KMeans(n_clusters = 3)

# Use .fit() to fit the model to samples
model.fit(samples)

# Use .predict() to determine the labels of samples 
labels = model.predict(samples)

# Print the labels: All the 0‘s are Iris-setosa, All the 1‘s are Iris-versicolor, All the 2‘s are Iris-virginica
print(labels)



""" Prediction on New Data """
# Store the new Iris measurements
new_samples = np.array(
  [[5.7, 4.4, 1.5, 0.4],
   [6.5, 3. , 5.5, 0.4],
   [5.8, 2.7, 5.1, 1.9]])

print(new_samples)

# Predict labels for the new_samples
new_labels = model.predict(new_samples)
print(new_labels)


""" Visualisation of Clustering Result """
# Convert integers to RGB colours (for K = 3)
def int2RGB(n):
  if (n == 0):
    c = 'r'
  elif (n == 1):
    c = 'g'
  else:
    c = 'b'
  return c

# Make a scatter plot of x and y and using labels to define the colors
x = samples[:, 0]
y = samples[:, 1]

c_labels = [int2RGB(label) for label in labels ]

print(c_labels)


fig, ax = plt.subplots(figsize = (10, 10))
ax.scatter(x, y, c = c_labels, alpha = .5)
ax.set_xlabel('sepal length (cm)')
ax.set_ylabel('sepal width (cm)')
ax.set_title('K-Means Clustering: Iris Dataset')
plt.show()


""" Evaluation of Model by Cross-Tabulation """
species = np.chararray(target.shape, itemsize = 150)

for i in range(len(samples)):
  if target[i] == 0:
    species[i] = 'setosa'
  elif target[i] == 1:
    species[i] = 'versicolor'
  else:
    species[i] = 'virginica'

df = pd.DataFrame({'labels' : labels, 'species' : species})

print(df)

# Perform cross-tabulation
ct = pd.crosstab(df['labels'], df['species'])
print(ct)


""" Choose optimal number of clusters """

num_clusters = list(range(1, 9))
inertias = []

for k in num_clusters:
  model = KMeans(n_clusters = k)
  model.fit(samples)
  inertias.append(model.inertia_)

fig, ax = plt.subplots(figsize = (8, 6))
ax.plot(num_clusters, inertias, '-o') 
ax.set_xlabel('Number of Clusters (k)')
ax.set_ylabel('Inertia')
ax.set_title('Optimal Number of Clusters', fontsize = 15, fontweight = 'bold')
plt.show()



