import requests
from api_key import header
from datetime import date


def get_publishers(args):
    base_url = "https://newsapi.org/v2/top-headlines/sources"
    params = {}

    # Adding provided arguments to the parameters
    if args.category:
        params["category"] = args.category
    if args.language:
        params["language"] = args.language
    if args.country:
        params["country"] = args.country

    # Fetching data from the API
    try:
        response = requests.request(method="GET", url=base_url, headers=header, params=params).json()
        sources = response["sources"][:10]

        # Displaying each source with detail
        for count, source in enumerate(sources, start=1):
            print(f"{count}. {source['name']}\n"
                  f"Description: {source['description']}\n"
                  f"Check their website: {source['url']}\n\n")
        return response
    except requests.RequestException as e:
        print(f"An error occurred: {e}")


def get_latest_articles(args):
    base_url = "https://newsapi.org/v2/everything"
    params = {
        "qInTitle": "technology",  # Default query
        "language": "en",  # Default language
        "sortBy": "popularity"  # Default sorting
    }

    # Adding provided arguments to the parameters
    if args.query:
        params["q"] = args.query
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
    if args.fromdate:
        params["from"] = args.fromdate
    if args.todate:
        params["to"] = args.todate

    try:
        response = requests.request(method="GET", url=base_url, headers=header, params=params).json()
        articles = response["articles"][:10]
        if not articles:
            print("No articles based on provided arguments.")
            return

        for count, article in enumerate(articles, start=1):
            title = article.get("title", "No Title")
            author = article.get("author", "Unknown Author")
            published_at = article.get("publishedAt", "N/A")
            url = article.get("url", "No URL")

            print(f"{count}. {title}\n"
                  f"Written by: {author}\n"
                  f"Published at: {published_at}\n"
                  f"Read the full article at: {url}\n\n")
        return response
    except requests.RequestException as e:
        print(f"An error occurred: {e}")


def append_articles_to_file(file_path, args):
    response = get_latest_articles(args)
    articles = response["articles"][:10]
    if not articles:
        print("No articles to append.")
        return

    try:
        with open(file_path, "a") as file:
            for count, article in enumerate(articles, start=1):
                title = article.get("title", "No Title")
                author = article.get("author", "Unknown Author")
                published_at = article.get("publishedAt", "N/A")
                url = article.get("url", "No URL")

                file.write(
                      "---\n"
                      f"{count}. {title}\n"
                      f"Written by: {author}\n"
                      f"Published at: {published_at}\n"
                      f"Read the full article at: {url}\n\n"
                )
    except IOError as e:
        print(f"An error occurred while opening the file: {e}")


def generate_files_with_articles(directory, args):
    today = date.today()
    file_name = f"{today.strftime('%Y%m%d')}.md"
    file_path = f"{directory}/{file_name}"

    response = get_latest_articles(args)
    articles = response["articles"][:20]
    if not articles:
        print("No articles to generate.")
        return

    try:
        with open(file_path, "a") as file:
            file.write(f"# To Read List {today.strftime('%Y%m%d')}\n")

            for article in articles:
                title = article.get("title", "No Title")
                author = article.get("author", "Unknown Author")
                published_at = article.get("publishedAt", "N/A")
                url = article.get("url", "No URL")

                file.write(
                    f"- [ ] <b>{title}</b> </br>"
                    f"Written by: {author} </br>"
                    f"Published at: {published_at} </br>"
                    f"Read the full article at: {url} </br> "
                    f"</br>"
                    f"\n\n"
                )
    except IOError as e:
        print(f"An error occurred when opening a file: {e}")