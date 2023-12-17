import articles_generator
from articles_generator import *
import argparse


def main():
    parser = argparse.ArgumentParser(description="Tech News Generator")
    parser.add_argument("-t", "--topheadlines", nargs="?", help="Get Top Headlines technology news")
    parser.add_argument("-p", "--publishers", nargs="?",  help="Get Top Publishers")
    parser.add_argument("-k", "--keyword", type=str, help="Get top news based on given key words")
    parser.add_argument("-d", "--domain", help="Get top news in the given domain")

    args = parser.parse_args()

    if args.topheadlines:
        print("---20 Top Headlines in Technology---")
        articles_generator.get_technology_top_headlines()

    if args.publishers:
        print("---20 Top Publishers---")
        articles_generator.get_top_headlines_publishers()

    if args.keyword:
        print(f"---20 articles based on {args.keyword} keyword---")
        articles_generator.get_article_based_on_keyword(args.keyword)

    if args.domain:
        print(f"---20 articles from {args.domain} domain---")
        articles_generator.get_articles_based_on_domain(args.domain)


if __name__ == "__main__":
    main()
