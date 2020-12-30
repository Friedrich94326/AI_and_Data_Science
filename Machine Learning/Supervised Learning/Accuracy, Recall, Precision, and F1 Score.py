from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score


# Accuracy

labels = [1, 0, 0, 1, 1, 1, 0, 1, 1, 1]
guesses = [0, 1, 1, 1, 1, 0, 1, 0, 1, 0]

true_positives = 0
true_negatives = 0
false_positives = 0
false_negatives = 0


for i in range(len(labels)):
  # true predictions
  if ( guesses[i] == labels[i] ):
    if (guesses[i] == 1):
      true_positives += 1
    else:
      true_negatives += 1
  # false predictions
  else:
    if ( guesses[i] == 1 ):
      false_positives += 1
    else:
      false_negatives += 1
  

# analysis of tp, tn, fp, fn
print("true positives = %d" %true_positives) # 3
print("true_negatives = %d" %true_negatives) # 0
print("false_positives = %d" %false_positives) # 3
print("false_negatives = %d\n" %false_negatives) # 4

# Accuracy measures how many classifications your algorithm got correct out of every classification it made
accuracy = (true_positives + true_negatives) / len(guesses)
print("accuracy: %.2f" %accuracy) # 0.3

# Recall measures the percentage of the relevant items your classifier was able to successfully find
recall = true_positives  / ( true_positives + false_negatives )
print("recall: %.2f" %recall) # 0.43

# Precision measures the percentage of items your classifier found that were actually relevant
precision = true_positives / ( true_positives + false_positives )
print("precision: %.2f" %precision) # 0.50

# F1 describes will be low if either precision or recall is low
f_1 = 2*precision*recall / (precision + recall)
print("F1 score: %.2f" %f_1) # 0.46



# They all take two parameters — a list of the true labels and a list of the predicted classifications

print("accuracy = %.2f" %accuracy_score(labels, guesses))
print("recall = %.2f" %recall_score(labels, guesses))
print("precision = %.2f" %precision_score(labels, guesses))
print("F1 score = %.2f" %f1_score(labels, guesses))

