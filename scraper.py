import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = [h2.text for h2 in soup.find_all('h2')]
    return titles

if __name__ == "__main__":
    url = "https://ejemplo-blog.com"
    titles = scrape_website(url)
    print(titles)