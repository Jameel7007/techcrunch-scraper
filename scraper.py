import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = "https://techcrunch.com"

# Send an HTTP request to the URL
response = requests.get(url)
print(f"HTTP Status Code: {response.status_code}")

if response.status_code == 200:
    print("Page fetched successfully")
    # Parse the content of the request with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all articles with the 'data-destinationlink' attribute
    articles = soup.find_all('a', attrs={'data-destinationlink': True})
    print(f"Found {len(articles)} articles with 'data-destinationlink' attribute")
    
    for article in articles:
        title = article.text.strip()
        url = article['href']
        if title:
            print(f"Title: {title}")
            print(f"URL: {url}")
            print('-' * 80)
else:
    print("Failed to fetch the page")
