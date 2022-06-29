import requests

from bs4 import BeautifulSoup

url = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3'  # Grabs URL from user input
response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})  # Requested data comes in English
soup = BeautifulSoup(response.content, 'html.parser')  # Tool to scrape HTML off webpage
link = soup.find_all('article')
for i in link:
    if i.find_next('span', class_="c-meta__type").text == 'News':
        hrefs = (i.find("a").get("href"))
        title = i.find('a').text
        title = "_".join( title.split() )
        for i in title:
            if i == '?':
                title = title.replace('?', '')
        print(title)
        web_request = requests.get('https://www.nature.com' + hrefs).content
        file = open(title + '.txt', 'wb')
        file.write(web_request)
        file.close()
