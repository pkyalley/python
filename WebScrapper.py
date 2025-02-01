import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
try:
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful
except requests.exceptions.RequestException as e:
    print(f"Error fetching the URL: {e}")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all("a", class_="storylink")

if not titles:
    print("No titles found.")
else:
    for index, title in enumerate(titles[:5]):
        print(f"{index+1}. {title.text}")