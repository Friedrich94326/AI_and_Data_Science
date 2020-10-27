# Spam Filters

import numpy as np

a = 'spam'
b = 'enhancement'

p_spam = .2
p_enhancement_given_spam = .05
p_enhancment_given_nonspam = .001

p_enhancement = p_enhancement_given_spam * p_spam + p_enhancment_given_nonspam * (1 - p_spam)

# According to Bayes' theorem, we're able to evaluate the prob that the email is spam given that it contains 'enhancement'
p_spam_enhancement = p_enhancement_given_spam * p_spam / p_enhancement
print(p_spam_enhancement)
print("If we block all emails that contain 'enhancement', then we will block %.2f%% of non-spam email out of them." %((1 - p_spam_enhancement)*100) )
