# K-Means Clustering Algorithm

K-Means is the most popular and well-known clustering algorithm, and it tries to address these two questions:
- How many groups do we choose?
- How do we define similarity?

## Parameters Concerned:
- The “K” refers to the number of clusters (groups) we expect to find in a dataset.
- The “Means” refers to the average distance of data to each cluster centre, also known as the **centroid**, which we are trying to minimise.

## Workflow of Algorithm:
- Step 1: Place k random centroids for the initial clusters. 
- Step 2: Assign data samples to the nearest centroid. 
- Step 3: Update centroids based on the above-assigned data samples. 
- Step 4: Repeat Steps 2 and 3 until convergence (when points don’t move between clusters and centroids stabilise).

## Optimal Number of Clusters K:
Q: How to define what is a good cluster?

Good clustering results in tight clusters, meaning that the samples in each cluster are bunched together. How spread out the clusters are is measured by inertia. Inertia is the distance from each sample to the centroid of its cluster. The lower the inertia is, the better our model has done.

*Elbow method*



## K-Means v.s. K-Means++
![](https://github.com/Friedrich94326/AI_and_Data_Science/blob/Python/Machine%20Learning/Unsupervised%20Learning/K-means_Clustering/Custom_Initialisation.png)
![](https://github.com/Friedrich94326/AI_and_Data_Science/blob/Python/Machine%20Learning/Unsupervised%20Learning/K-means_Clustering/K-Means%2B%2B_Initialisation.png)
