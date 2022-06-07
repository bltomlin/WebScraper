import requests

url = input()
response = requests.get(url)
text = response.json()
content = False
for i in text:
    if i == 'content':
        content = True
        phrase = text[i]
if content:
    print(phrase)
else:
    print("Invalid quote resource!")