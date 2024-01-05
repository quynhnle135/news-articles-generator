from unittest.mock import patch, mock_open
from articles_generator import *


# Set up mock data for get_publishers response
mock_publishers_response = {"sources": [{"name": "Publisher 1", "description": "Description 1", "url": "http://source1.com"}] * 10}
mock_articles_response = {"articles": [{"title": "Title 1", "author": "Author 1", "publishedAt": "2021-01-01", "url": "http://article1.com"}] * 10}
params = {
    "category": "Test Category",
    "language": "en",
    "country": "us"
}


# Test get_publishers function
@patch('requests.request')
def test_get_publishers(mock_request):
    base_url = "https://newsapi.org/v2/top-headlines/sources"
    mock_request().json.return_value = mock_publishers_response
    args = Args(category="Test Category", language="en", country="us")

    response = get_publishers(args)

    assert response == mock_publishers_response
    mock_request.assert_called_with(method="GET", url=base_url, headers=header, params=params)


@patch('requests.request')
def test_get_publishers_error(mock_request, capsys):
    base_url = "https://newsapi.org/v2/top-headlines/sources"
    mock_request.side_effect = requests.RequestException("An error occurred")
    args = Args(category="Test Category", language="en", country="us")

    response = get_publishers(args)
    captured = capsys.readouterr()

    assert "An error occurred" in captured.out
    assert response is None
    mock_request.assert_called_once_with(method="GET", url=base_url, headers=header, params=params)


@patch('requests.request')
def test_get_latest_articles(mock_request):
    base_url = "https://newsapi.org/v2/everything"
    test_params = {
        "qInTitle": "technology",  # Default query
        "language": "en",  # Default language
        "sortBy": "popularity"  # Default sorting
    }
    mock_request().json.return_value = mock_articles_response
    args = Args()

    response = get_latest_articles(args=args)

    assert response == mock_articles_response
    mock_request.assert_called_with(method="GET", url=base_url, headers=header, params=test_params)


@patch("requests.request")
def test_get_latest_articles_with_no_article(mock_request, capsys):
    base_url = "https://newsapi.org/v2/everything"
    test_params = {
        "qInTitle": "technology",
        "language": "en",
        "sortBy": "popularity"
    }
    mock_request().json.return_value = {"articles": []}
    args = Args()

    response = get_latest_articles(args)
    capture = capsys.readouterr()

    assert response is None
    assert "No articles based on provided arguments." in capture.out
    mock_request.assert_called_with(method="GET", url=base_url, headers=header, params=test_params)


@patch('requests.request')
def test_get_latest_articles_with_query(mock_request):
    mock_request().json.return_value = mock_articles_response
    base_url = "https://newsapi.org/v2/everything"
    args = Args(keyword="technology", language="en", sortby="popularity", query="test", domain="test_domain", category="test_category", fromdate="test_from_date", todate="test_to_date")
    test_params = {
        "qInTitle": "technology",
        "language": "en",
        "sortBy": "popularity",
        "q": "test",
        "domains": "test_domain",
        "category": "test_category",
        "from": "test_from_date",
        "to": "test_to_date"
    }

    response = get_latest_articles(args)

    mock_request.assert_called_with(method="GET", url=base_url, headers=header, params=test_params)
    assert response == mock_articles_response


@patch('requests.request')
def test_get_latest_articles_error(mock_request, capsys):
    base_url = "https://newsapi.org/v2/everything"
    test_params = {
        "qInTitle": "technology",
        "language": "en",
        "sortBy": "popularity"
    }
    mock_request.side_effect = requests.RequestException("An error occurred")
    args = Args()
    response = get_latest_articles(args=args)

    capture = capsys.readouterr()

    assert "An error occurred" in capture.out
    assert response is None
    mock_request.assert_called_once_with(method="GET", url=base_url, headers=header, params=test_params)


@patch("articles_generator.get_latest_articles")
def test_append_articles_to_file(mock_get_latest_articles):
    mock_get_latest_articles.return_value = mock_articles_response
    args = Args()
    file_path = "dummy_path.txt"

    with patch("builtins.open", mock_open()) as mock_file:
        append_articles_to_file(file_path=file_path, args=args)

        mock_get_latest_articles.assert_called_once_with(args)
        mock_file.assert_called_once_with(file_path, "a")

        mock_file_handle = mock_file()
        mock_file_handle.write.assert_called_with(f"---\n10. Title 1\nWritten by: Author 1\nPublished at: 2021-01-01\nRead the full article at: http://article1.com\n\n")


@patch("articles_generator.get_latest_articles")
def test_append_articles_to_file_with_no_articles(mock_get_latest_articles, capsys):
    mock_get_latest_articles.return_value = {"articles": []}
    args = Args()
    file_path = "dummy_path.txt"

    with patch("builtins.open", mock_open()) as mock_file:
        append_articles_to_file(file_path=file_path, args=args)
        capture = capsys.readouterr()

        mock_get_latest_articles.assert_called_once_with(args)
        mock_file.assert_not_called()

        assert "No articles to append." in capture.out


@patch("articles_generator.get_latest_articles")
def test_append_articles_to_file_error(mock_get_latest_articles, capsys):
    mock_get_latest_articles.return_value = mock_articles_response
    args = Args()
    file_path = "dummy_path.txt"
    with patch("builtins.open", mock_open()) as mock_file:
        mock_file.side_effect = IOError("An error occurred while opening the file")

        append_articles_to_file(file_path=file_path, args=args)
        capture = capsys.readouterr()

        mock_get_latest_articles.assert_called_once_with(args)
        mock_file.assert_called_once_with(file_path, "a")
        assert "An error occurred while opening the file" in capture.out


@patch("articles_generator.get_latest_articles")
def test_generate_files_with_articles(mock_get_latest_articles):
    mock_get_latest_articles.return_value = mock_articles_response
    today = date.today()
    file_name = f"{today.strftime('%Y%m%d')}.md"
    test_directory = "test_directory"
    file_path = f"{test_directory}/{file_name}"
    args = Args()
    with patch("builtins.open", mock_open()) as mock_file:
        generate_files_with_articles(test_directory, args)

        mock_get_latest_articles.assert_called_once_with(args)
        mock_file.assert_called_with(file_path, "a")

        mock_file_handle = mock_file()
        mock_file_handle.write.assert_called_with(f"- [ ] <b>Title 1</b> </br>"
                    f"Written by: Author 1 </br>"
                    f"Published at: 2021-01-01 </br>"
                    f"Read the full article at: http://article1.com </br> "
                    f"</br>"
                    f"\n\n")


@patch("articles_generator.get_latest_articles")
def test_generate_files_with_article_with_no_article(mock_get_latest_articles, capsys):
    mock_get_latest_articles.return_value = {"articles": []}
    test_directory = "test_directory"
    args = Args()
    with patch("builtins.open", mock_open()) as mock_file:
        generate_files_with_articles(test_directory, args)
        capture = capsys.readouterr()

        mock_get_latest_articles.assert_called_once_with(args)
        mock_file.assert_not_called()
        assert "No articles to generate." in capture.out


@patch("articles_generator.get_latest_articles")
def test_generate_file_with_article_with_error(mock_get_latest_articles, capsys):
    mock_get_latest_articles.return_value = mock_articles_response
    today = date.today()
    file_name = f"{today.strftime('%Y%m%d')}.md"
    test_directory = "test_directory"
    file_path = f"{test_directory}/{file_name}"
    args = Args()
    with patch("builtins.open", mock_open()) as mock_file:
        mock_file.side_effect = IOError("An error occurred when opening a file")
        generate_files_with_articles(test_directory, args)
        capture = capsys.readouterr()

        mock_get_latest_articles.assert_called_with(args)
        mock_file.assert_called_with(file_path, "a")
        assert "An error occurred when opening a file" in capture.out