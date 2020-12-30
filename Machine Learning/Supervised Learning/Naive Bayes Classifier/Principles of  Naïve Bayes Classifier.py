# A Naive Bayes classifier is a supervised machine learning algorithm that leverages Bayes’ Theorem to make predictions and classifications. 
# Naive Bayes classifiers are often used for text classification


# Bayes' Theorem for classifying a review of a product
from reviews import neg_counter, pos_counter

review = "This crib was amazing"

percent_pos = 0.5
percent_neg = 0.5

# total number of words in all positive reviews
total_pos = sum(pos_counter.values())
total_neg = sum(neg_counter.values())

pos_probability = 1
neg_probability = 1

review_words = review.split()
print(review_words)

for word in review_words:
  word_in_pos = pos_counter[word]
  word_in_neg = neg_counter[word]
  # each word in review is conditionally independent
  pos_probability *= word_in_pos / total_pos
  neg_probability *= word_in_neg / total_neg
  
 
# Smoothing- If an unclassified review has a typo in it, the entire probability will be 0

# typo in this review 
review = "This cribb was amazing"


# In the following block is SMOOTHING implemented 
for word in review_words:
  word_in_pos = pos_counter[word]
  word_in_neg = neg_counter[word]
  
  pos_probability *= (word_in_pos + 1) / (total_pos + len(pos_counter))
  neg_probability *= (word_in_neg + 1) / (total_neg + len(neg_counter))
  
 
# Classify!
# calculate P(review|positive)*P(positive) & P(review|negative)*P(negative)
final_pos = pos_probability * percent_pos
final_neg = neg_probability * percent_neg

print(final_pos)
print(final_neg)

if final_pos > final_neg:
  print("The review is positive")
elif final_pos < final_neg:
  print("This review is negative")
else:
  print("It's a die!")


