import articles_generator
import argparse


def main():
    parser = argparse.ArgumentParser(description="News Articles Generator")

    parser.add_argument(
        "-p", "--publishers",
        action="store_true",
        help="Retrieve a list of top news publishers. Can be filtered by category, country, and language."
    )
    parser.add_argument(
        "-a", "--articles",
        action="store_true",
        help="Fetch the latest news articles. Filters like keyword, sortby, domain, category, country, and language "
             "can be applied. "
    )
    parser.add_argument(
        "-ap", "--append",
        action="store_true",
        help="Enable this option to append the latest news articles to a specified file. Requires a valid file path "
             "to be provided with the '--file' option. "
    )
    parser.add_argument(
        "-g", "--generate",
        action="store_true",
        help="Enable this option to generate a 'to-read' list in Markdown format. The list will be created in the "
             "directory specified by the '--directory' option. Ensure the specified directory exists and is writable."
    )

    # Optional arguments
    parser.add_argument(
        "-ca", "--category",
        type=str,
        help="Filter publishers/articles by a specific news category (e.g., 'business', 'sports'). Applies to both "
             "publishers and articles. "
    )
    parser.add_argument(
        "-co", "--country",
        type=str,
        help="Filter publishers/articles by country using ISO country codes (e.g., 'us' for the United States, "
             "'gb' for Great Britain). Applies to both publishers and articles."
    )
    parser.add_argument(
        "-la", "--language",
        type=str,
        help="Filter publishers/articles by language using ISO language codes (e.g., 'en' for English, 'es' for "
             "Spanish). Applies to both publishers and articles."
    )
    parser.add_argument("-q", "--query", type=str, help="Search articles with multiple keywords")
    parser.add_argument("-k", "--keyword", type=str, help="Search articles with a specific keyword in the title.")
    parser.add_argument("-do", "--domain", type=str, help="Search articles in a specific domain.")
    parser.add_argument(
        "-so", "--sortby",
        type=str,
        choices=['publishedAt', 'relevancy', 'popularity'],
        help="Sort retrieved articles by 'publishedAt', 'relevancy', or 'popularity'. Applicable only for articles."
    )
    parser.add_argument(
        "-fd", "--fromdate",
        type=str,
        help="Specify the start date for filtering articles. Format: YYYY-MM-DD. "
             "Articles from this date onwards will be included."
    )
    parser.add_argument(
        "-td", "--todate",
        type=str,
        help="Specify the end date for filtering articles. Format: YYYY-MM-DD. "
             "Only articles up to this date will be included."
    )
    parser.add_argument(
        "-f", "--file",
        type=str,
        help="Provide the file path where the articles will be appended. "
             "Ensure the file path is accessible and writable."
    )
    parser.add_argument(
        "-dir", "--directory",
        type=str,
        help="Specify the directory path where the news articles will be saved. Ensure that the directory exists "
             "and has write permissions."
    )

    args = parser.parse_args()

    if args.publishers:
        print("---10  Publishers---")
        articles_generator.get_publishers(args)

    if args.articles:
        print("---10 Articles---")
        articles_generator.get_latest_articles(args)

    if args.append:
        print("---Appending articles to a file---")
        articles_generator.append_articles_to_file(args.file, args)

    if args.generate:
        print("---Generating articles in Markdown---")
        articles_generator.generate_files_with_articles(args.directory, args)


if __name__ == "__main__":
    main()
