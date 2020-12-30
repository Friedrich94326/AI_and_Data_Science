
# Supervised Learning

from texts import text_counter, text_training
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# intercepted_text = "This hot dog was awful!"
#intercepted_text = "I love my government."
intercepted_text = "I feel super tired today."


text_counts = text_counter.transform([intercepted_text])

text_classifier = MultinomialNB()

text_labels = [0] * 1000 + [1] * 1000

text_classifier.fit(text_training, text_labels)

final_pos = text_classifier.predict_proba(text_counts)[0][1]

final_neg = text_classifier.predict_proba(text_counts)[0][0]

if final_pos > final_neg:
  print("The text is positive.")
else:
  print("The text is negative.")
  
  
  


# Unsupervised Learning

import codecademylib3_seaborn
import matplotlib.pyplot as plt
import numpy as np 

from os.path import join, dirname, abspath
from mpl_toolkits.mplot3d import Axes3D

from sklearn.cluster import KMeans
from sklearn import datasets

iris = datasets.load_iris()

x = iris.data
y = iris.target

fignum = 1

# Plot the ground truth

fig = plt.figure(fignum, figsize=(4, 3))

ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

for name, label in [('Robots', 0),
                    ('Cyborgs', 1),
                    ('Humans', 2)]:
    ax.text3D(x[y == label, 3].mean(),
              x[y == label, 0].mean(),
              x[y == label, 2].mean() + 2, name,
              horizontalalignment='center',
              bbox=dict(alpha=.2, edgecolor='w', facecolor='w'))

# Reorder the labels to have colors matching the cluster results

y = np.choose(y, [1, 2, 0]).astype(np.float)
ax.scatter(x[:, 3], x[:, 0], x[:, 2], c=y, edgecolor='k')

ax.w_xaxis.set_ticklabels([])
ax.w_yaxis.set_ticklabels([])
ax.w_zaxis.set_ticklabels([])

ax.set_xlabel('Time to Heal')
ax.set_ylabel('Reading Speed')
ax.set_zlabel('EQ')

ax.set_title('')
ax.dist = 12

plt.show()
  
  
  
 
 
