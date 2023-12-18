import articles_generator
import argparse


def main():
    parser = argparse.ArgumentParser(description="Tech News Generator")
    parser.add_argument("-p", "--publishers", action="store_true",
                        help="Retrieve a list of top news publishers. Can be filtered by category, country, and language.")
    parser.add_argument("-a", "--articles", action="store_true",
                        help="Fetch the latest news articles. Filters like keyword, sortby, domain, category, country, and language can be applied.")
    parser.add_argument("-w", "--weekly", action="store_true", help="Fetch the latest news articles of this week. Filters like keyword, sortby, domain, category, country, and language can be applied.")

    # Optional arguments
    parser.add_argument("-ca", "--category", type=str,
                        help="Filter publishers/articles by a specific news category (e.g., 'business', 'sports'). Applies to both publishers and articles.")
    parser.add_argument("-co", "--country", type=str,
                        help="Filter publishers/articles by country using ISO country codes (e.g., 'us' for the United States, 'gb' for Great Britain). Applies to both publishers and articles.")
    parser.add_argument("-la", "--language", type=str,
                        help="Filter publishers/articles by language using ISO language codes (e.g., 'en' for English, 'es' for Spanish). Applies to both publishers and articles.")
    parser.add_argument("-k", "--keyword", type=str, help="Search articles with a specific keyword in the title.")
    parser.add_argument("-do", "--domain", type=str, help="Search articles in a specific domain.")
    parser.add_argument("-so", "--sortby", type=str, choices=['publishedAt', 'relevancy', 'popularity'],
                        help="Sort retrieved articles by 'publishedAt', 'relevancy', or 'popularity'. Applicable only for articles.")

    args = parser.parse_args()

    if args.publishers:
        print("---10  Publishers---")
        articles_generator.get_publishers(args)

    if args.articles:
        print("---10 Latest Articles---")
        articles_generator.get_latest_articles(args)

    if args.weekly:
        print("---10 Articles of this week---")
        articles_generator.get_this_week_articles(args)


if __name__ == "__main__":
    main()
