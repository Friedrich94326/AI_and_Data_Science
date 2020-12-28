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
