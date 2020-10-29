from sklearn.datasets import fetch_20newsgroups
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

emails = fetch_20newsgroups()

print(type(emails))
print(emails.target_names)

emails = fetch_20newsgroups( categories = [ 'rec.sport.baseball', 'rec.sport.hockey'] )

print(emails.data[5])
print(emails.target[5])

# Making training sets and test sets
train_emails = fetch_20newsgroups( categories = [ 'rec.sport.baseball', 'rec.sport.hockey'], subset = 'train', shuffle = True, random_state = 108)

test_emails = fetch_20newsgroups(categories = [ 'rec.sport.baseball', 'rec.sport.hockey'], subset = 'test', shuffle = True, random_state = 108)

# Counting words
counter = CountVectorizer()
counter.fit(test_emails.data + train_emails.data)
train_counts = counter.transform(train_emails.data)
test_counts = counter.transform(test_emails.data)

# Making a Naive Bayes Classifier
classifier = MultinomialNB()
classifier.fit(train_counts, train_emails.target)
accu = classifier.score(test_counts, test_emails.target)
print("test score = %.3f" %accu) # .972

# Testing Other Datasets
train_emails_2 = fetch_20newsgroups( categories = ['comp.sys.ibm.pc.hardware','rec.sport.hockey'], subset = 'train', shuffle = True, random_state = 108)

test_emails_2 = fetch_20newsgroups(categories = ['comp.sys.ibm.pc.hardware','rec.sport.hockey'], subset = 'test', shuffle = True, random_state = 108)

counter.fit(test_emails_2.data + train_emails_2.data)
train_counts_2 = counter.transform(train_emails_2.data)
test_counts_2 = counter.transform(test_emails_2.data)

classifier.fit(train_counts_2, train_emails_2.target)
accu_2 = classifier.score(test_counts_2, test_emails_2.target)
print("test score = %.3f" %accu_2) # .997


# Testing Other Datasets Again
train_emails_3 = fetch_20newsgroups( categories = ['alt.atheism', 'comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware', 'comp.sys.mac.hardware', 'comp.windows.x', 'misc.forsale', 'rec.autos', 'rec.motorcycles', 'rec.sport.baseball', 'rec.sport.hockey','sci.crypt', 'sci.electronics', 'sci.med', 'sci.space','soc.religion.christian', 'talk.politics.guns', 'talk.politics.mideast', 'talk.politics.misc', 'talk.religion.misc'], subset = 'train', shuffle = True, random_state = 108)

test_emails_3 = fetch_20newsgroups( categories = ['alt.atheism', 'comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware', 'comp.sys.mac.hardware', 'comp.windows.x', 'misc.forsale', 'rec.autos', 'rec.motorcycles', 'rec.sport.baseball', 'rec.sport.hockey','sci.crypt', 'sci.electronics', 'sci.med', 'sci.space','soc.religion.christian', 'talk.politics.guns', 'talk.politics.mideast', 'talk.politics.misc', 'talk.religion.misc'], subset = 'train', shuffle = True, random_state = 108)


counter.fit(test_emails_3.data + train_emails_3.data)
train_counts_3 = counter.transform(train_emails_3.data)
test_counts_3 = counter.transform(test_emails_3.data)

classifier.fit(train_counts_3, train_emails_3.target)
accu_3 = classifier.score(test_counts_3, test_emails_3.target)
print("test score = %.3f" %accu_3) # .925
