import requests
from datetime import date, timedelta

API_KEY = "b939e78e924b4e949331cc38cab93a95"

header = {
    "X-Api-Key": API_KEY
}


def get_technology_top_headlines():
    url = "https://newsapi.org/v2/top-headlines?category=technology&language=en"
    response = requests.request(method="GET", url=url, headers=header).json()
    print(response)
    articles = response["articles"][:20]
    count = 1
    for item in articles:
        print(f"{count}. {item['title']}\n"
              f"Written by: {item['author']}\n"
              f"Description: {item['description']}\n"
              f"Read the full article at: {item['url']}\n")
        count += 1
    return response


def get_top_headlines_publishers():
    url = "https://newsapi.org/v2/top-headlines/sources"
    response = requests.request(method="GET", url=url, headers=header).json()
    print(response['sources'][0].keys())
    publishers = response["sources"][:20]
    count = 1
    for p in publishers:
        print(f"{count}. {p['name']}\n"
              f"Description: {p['description']}\n"
              f"Check their website at: {p['url']}\n")
        count += 1


def get_this_week_openai_articles():
    today = date.today()
    start_date = today - timedelta(days=today.weekday())
    end_date = start_date + timedelta(days=6)
    formatted_start_date = date.strftime(start_date, "%Y-%m-%d")
    formatted_end_date = date.strftime(end_date, "%Y-%m-%d")
    url = f"https://newsapi.org/v2/everything?qInTitle=OpenAI&from={formatted_start_date}&to={formatted_end_date}&sortBy=popularity&language=en"
    response = requests.request(method="GET", url=url, headers=header).json()
    articles = response["articles"][:20]
    count = 1
    for item in articles:
        print(f"{count}. {item['title']}\n"
              f"Written by: {item['author']}\n"
              f"Description: {item['description']}\n"
              f"Read the full article at: {item['url']}\n")
        count += 1


def get_article_based_on_keyword(keyword: str):
    url = f"https://newsapi.org/v2/everything?qInTitle={keyword}&language=en&sortBy=popularity"
    response = requests.request(method="GET", url=url, headers=header).json()
    articles = response["articles"][:20]
    count = 1
    for item in articles:
        print(f"{count}. {item['title']}\n"
              f"Written by: {item['author']}\n"
              f"Description: {item['description']}\n"
              f"Read the full article at: {item['url']}\n")
        count += 1


def get_articles_based_on_domain(domain: str):
    url = f"https://newsapi.org/v2/everything?domains={domain}&sortBy=popularity&language=en"
    response = requests.request(method="GET", url=url, headers=header).json()
    print(response)
    articles = response["articles"][:20]
    count = 1
    for item in articles:
        print(f"{count}. {item['title']}\n"
              f"Written by: {item['author']}\n"
              f"Description: {item['description']}\n"
              f"Read the full article at: {item['url']}\n")
        count += 1


get_articles_based_on_domain(domain="medium.com")






