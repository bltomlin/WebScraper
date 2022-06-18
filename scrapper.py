"""
User inputs URL. If the URL is good, it saves the HTML to a file.
"""

url = input()  # Grabs URL from user input
response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})  # Requested data comes in English
if response:  # If return 200, it saves html to file
    page_content = requests.get(url).content
    file = open('source.html', 'wb')
    file.write(page_content)
    file.close()
    print('Content saved.')
else:
    print("The URL returned", response)
