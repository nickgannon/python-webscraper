import requests
from bs4 import BeautifulSoup

# Prompt the user for the URL to be scraped
url = input("Enter the URL to be scraped: ")

# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the article titles on the page
article_titles = soup.find_all("div")

# Print the titles of the articles
for title in article_titles:
    print(title.text)
