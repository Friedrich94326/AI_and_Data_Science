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
soup = BeautifulSoup(webpage, "html.parser")
# print(type(soup))
print(soup)


