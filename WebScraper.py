import requests
from bs4 import BeautifulSoup

# URL of the web page you want to scrape
url = "https://nicholasgannon.io/"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the article titles on the page
article_titles = soup.find_all("h1")

# Print the titles of the articles
for title in article_titles:
    print(title.text)
