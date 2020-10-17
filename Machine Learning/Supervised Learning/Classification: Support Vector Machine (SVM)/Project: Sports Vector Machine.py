# In this project, we will use an SVM trained using a baseball dataset to find the decision boundary of the strike zone.

import codecademylib3_seaborn
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from svm_visualization import draw_boundary
from players import aaron_judge, jose_altuve, david_ortiz

fig, ax = plt.subplots()
print(aaron_judge.columns)
print(aaron_judge.description.unique())
print(aaron_judge.type.unique())

aaron_judge["type"].replace({'S': 1, 'B': 0}, inplace = True)
print(aaron_judge.type)

# Plotting the pitches

# plate_x measures how far left or right the pitch is from the center of home plate
# plate_z measures how high off the ground the pitch was
print(aaron_judge['plate_x'])
print(aaron_judge)

# remove every row that has a NaN in those 3 columns
aaron_judge.dropna(subset = ['plate_x', 'plate_z', 'type'])

plt.scatter(x = aaron_judge["plate_x"], y = aaron_judge["plate_z"], c = aaron_judge["type"], cmap = plt.cm.coolwarm, alpha = .25)
plt.show()
