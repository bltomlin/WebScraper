import requests
import os

from bs4 import BeautifulSoup


def getScrapper(url):
    response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})  # Requested data comes in English
    return BeautifulSoup(response.content, 'html.parser')  # Tool to scrape HTML off webpage


print('Enter the number of pages you wish to scrape:')
number_of_pages = int(input())
print('Enter the article type you would like results for:')
article_type = str(input())
url = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3'  # URL is static for legal purposes
response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})  # Requesting data
for num in range(number_of_pages):  # Iterates through each page
    
    # Creates a directory based on website page number.
    page_num = 'Page_' + str(num + 1)
    os.mkdir(page_num)
    os.chdir(page_num)
    
    # Main program
    page_num_string = 'page=' + str(num)
    soup = getScrapper(url + page_num_string)  # Concatenates page for accurate URL
    link = soup.find_all('article')  # All information needed to be scraped is in Article tag

    # Iterates through each article for article type and title
    for i in link:

        # If the article type matches it scrapes the paragraph data and writes it to a text file.
        if i.find_next('span', class_="c-meta__type").text == article_type:
            hrefs = (i.find("a").get("href"))
            title = "_".join(i.find('a').text.split())
            for char in title:
                if char == '?':
                    title = title.replace('?', '')
            web_request = 'https://www.nature.com' + hrefs
            soup = getScrapper(web_request)
            paragraph_text = soup.find_all('div', {'class': "c-article-body u-clearfix"})
            file = open(title + '.txt', 'wb')
            for paragraph in paragraph_text:
                file.write(bytes(paragraph.text, "utf-8"))
            file.close()
