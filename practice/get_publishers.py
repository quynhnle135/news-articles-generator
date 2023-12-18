from api_key import header
import requests


response = requests.request(method="GET", url="https://newsapi.org/v2/top-headlines/sources?language=en&country=us", headers=header).json()
print(response["sources"])
sources = response["sources"]
for s in sources:
    print(s["category"])