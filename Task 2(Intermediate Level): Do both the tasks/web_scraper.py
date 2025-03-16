import requests
from bs4 import BeautifulSoup

url = 'https://realpython.com/tutorials/'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    tutorials = soup.find_all('a', class_='card')
    for idx, tutorial in enumerate(tutorials, 1):
        title = tutorial.find('h2', class_='card-title').text.strip()
        link = 'https://realpython.com' + tutorial.get('href')
        print(f"{idx}. {title}\n   URL: {link}\n")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
