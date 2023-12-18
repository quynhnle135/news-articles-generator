import requests
from datetime import date, timedelta
from api_key import header


def get_publishers(args):
    base_url = "https://newsapi.org/v2/top-headlines/sources"
    params = {}

    # Adding provided arguments to the parameters
    if args.category:
        params["category"] = args.category.lower()
    if args.language:
        params["language"] = args.language.lower()
    if args.country:
        params["country"] = args.country.lower()

    # Fetching data from the API
    try:
        response = requests.request(method="GET", url=base_url, headers=header, params=params).json()
        sources = response["sources"][:10]

        # Displaying each source with detail
        for count, source in enumerate(sources, start=1):
            print(f"{count}. {source['name']}\n"
                  f"Description: {source['description']}\n"
                  f"Check their website: {source['url']}\n")
        return response
    except requests.RequestException as e:
        print(f"An error occurred: {e}")


def get_latest_articles(args):
    base_url = "https://newsapi.org/v2/everything"
    params = {
        "q": "technology", # Default query
        "language": "en",  # Default language
        "sortBy": "popularity"  # Default sorting
    }

    # Adding provided arguments to the parameters
    if args.keyword:
        params["qInTitle"] = args.keyword
    if args.sortby:
        params["sortBy"] = args.sortby
    if args.domain:
        params["domains"] = args.domain
    if args.category:
        params["category"] = args.category
    if args.language:
        params["language"] = args.language

    try:
        response = requests.request(method="GET", url=base_url, headers=header, params=params).json()
        articles = response["articles"][:10]
        for count, article in enumerate(articles, start=1):
            print(f"{count}. {article['title']}\n"
                  f"Written by: {article['author']}\n"
                  f"Description: {article['description']}\n"
                  f"Read the full article at: {article['url']}\n")
        return response
    except requests.RequestException as e:
        print(f"An error occurred: {e}")


def get_this_week_articles(args):
    today = date.today()
    start_date = today - timedelta(days=today.weekday())
    end_date = start_date + timedelta(days=6)
    formatted_start_date = date.strftime(start_date, "%Y-%m-%d")
    formatted_end_date = date.strftime(end_date, "%Y-%m-%d")
    base_url = f"https://newsapi.org/v2/everything"
    params = {
        "from": formatted_start_date,
        "to": formatted_end_date,
        "q": "technology",
        "sortBy": "popularity",
        "language": "en"
    }

    # Adding provided arguments to the parameters
    if args.keyword:
        params["qInTitle"] = args.keyword
    if args.sortby:
        params["sortBy"] = args.sortby
    if args.domain:
        params["domains"] = args.domain
    if args.category:
        params["category"] = args.category
    if args.language:
        params["language"] = args.language

    try:
        response = requests.request(method="GET", url=base_url, headers=header, params=params).json()
        articles = response["articles"][:10]
        for count, article in enumerate(articles, start=1):
            print(f"{count}. {article['title']}\n"
                  f"Written by: {article['author']}\n"
                  f"Description: {article['description']}\n"
                  f"Read the full article at: {article['url']}\n")
        return response
    except requests.RequestException as e:
        print(f"An error occurred: {e}")






