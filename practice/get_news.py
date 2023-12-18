from api_key import header, API_KEY
import requests


url_one = "https://newsapi.org/v2/everything?qInTitle=python&from=2023-12-10&to=2023-12-16&language=en&sortBy=popularity&domain=medium.com"
response = requests.request(method="GET", url=url_one, headers=header).json()
print(response["articles"][0].keys())
print(response["articles"][0]["publishedAt"])
print(type(response["articles"][0]["publishedAt"]))


url = f"https://newsapi.org/v2/everything?domains=freecodecamp.org&apiKey={API_KEY}"
response_django = requests.request(method="GET", url=url, headers=header).json()
print(response_django)