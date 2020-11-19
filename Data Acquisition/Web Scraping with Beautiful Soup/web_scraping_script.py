""" Requests """

import requests  # import the requests library

# My request to the URL
webpage_response = requests.get('https://content.codecademy.com/courses/beautifulsoup/shellter.html')
print(webpage_response.text)

# See the content of this HTML
webpage = webpage_response.content
print(webpage)


""" BeautifulSoup is a Python library that makes it easy for us to traverse an HTML page and pull out the parts we’re interested in """
from bs4 import BeautifulSoup

# convert the HTML document to a BeautifulSoup object
soup = BeautifulSoup(webpage, "html.parser")  # html.parser as an indicated parser
# print(type(soup))
print(soup)

"""  Accessing Tags from a BeautifulSoup object """
# get the first <p> tag of that type on the requested page (<p> defines a paragraph)
print(soup.p)

# the string associated with the first p tage on the requested page
print(soup.p.string)


""" Navigating Tags: HTML Parent-Child Relationship """

# Print out all of the parents of the first <div>
print("all of the parents of the first <div>:\n")
for parent in soup.div.parents:
  print(parent)
  

# Print out all of the children of the first <div>- HEAD and BODY are child nodes of the HTML element.
print("all of the children of the first <div>:\n")
for child in soup.div.children: # Tag <div> defines a section in a document
  print(child)
  
  
  





