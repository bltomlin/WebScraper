"""
Grabs a URL and evaluates it to see if it has movie data from IMBD.
"""

import requests

from bs4 import BeautifulSoup

url = input()  # Grabs URL from user input
response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})  # Requested data comes in English
soup = BeautifulSoup(response.content, 'html.parser')  # Tool to scrape HTML off webpage
h1 = soup.find('h1')  # Looks for the title of the movie
if h1 is None:  # Evaluates if there is a title
    print('Invalid movie page!')
    quit()
span = soup.find('span', {'data-testid': 'plot-l'})  # Looks for the description of the movie
if span is None:  # Evaluates if there is a description
    print('Invalid movie page!')
    quit()
dictionary = {'title': h1.text, 'description': span.text}  # parses data to dictionary
print(dictionary)  # prints resulting dictionary

