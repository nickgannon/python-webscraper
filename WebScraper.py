import requests
from bs4 import BeautifulSoup

try:
    # Prompt the user for the URL to be scraped
    url = input("Enter the URL to be scraped: ")

    # Send an HTTP GET request to the URL with a user-agent header
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    response.raise_for_status()

    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the article titles on the page (h1, h2, h3, and div)
    h1_titles = soup.find_all("h1")
    h2_titles = soup.find_all("h2")
    h3_titles = soup.find_all("h3")
    div_elements = soup.find_all("div")

    # Print the titles of the articles in separate sections
    print("""---------
|ALL H1:|
---------""")
    if h1_titles:
        for title in h1_titles:
            print(title.text)
    else:
        print("**THERE ARE NO H1**")

    print("""\n---------
|ALL H2:|
---------""")
    if h2_titles:
        for title in h2_titles:
            print(title.text)
    else:
        print("**THERE ARE NO H2**")

    print("""\n---------
|ALL H3:|
---------""")
    if h3_titles:
        for title in h3_titles:
            print(title.text)
    else:
        print("**THERE ARE NO H3**")

    print("""\n---------
|ALL div:|
---------""")
    if div_elements:
        for element in div_elements:
            print(element.text)
    else:
        print("**THERE ARE NO DIV**")

    # Provide a message if none of the specified elements were found
    if not h1_titles and not h2_titles and not h3_titles and not div_elements:
        print("No <h1>, <h2>, <h3>, or <div> elements found on the page.")

except requests.exceptions.RequestException as e:
    print("Error: Unable to connect to the URL or invalid URL.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
