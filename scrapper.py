"""
Grabs a URL and evaluates it to see if it has movie data from IMBD.
"""

import requests

from bs4 import BeautifulSoup

url = input()
response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
soup = BeautifulSoup(response.content, 'html.parser')
h1 = soup.find('h1')
if h1 is None:
    print('Invalid movie page!')
    quit()
span = soup.find('span', {'data-testid': 'plot-l'})
if span is None:
    print('Invalid movie page!')
    quit()
dictionary = {'title': h1.text, 'description': span.text}
print(dictionary)
