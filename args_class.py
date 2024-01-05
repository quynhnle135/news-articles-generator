from typing import Optional


class Args:
    # Existing attributes
    category: Optional[str]
    language: Optional[str]
    country: Optional[str]

    # Additional attributes for get_latest_articles
    query: Optional[str]
    keyword: Optional[str]
    sortby: Optional[str]
    domain: Optional[str]
    fromdate: Optional[str]
    todate: Optional[str]

    def __init__(self, category: Optional[str] = None, language: Optional[str] = None, country: Optional[str] = None,
                 query: Optional[str] = None, keyword: Optional[str] = None, sortby: Optional[str] = None,
                 domain: Optional[str] = None, fromdate: Optional[str] = None, todate: Optional[str] = None):
        self.category = category
        self.language = language
        self.country = country
        self.query = query
        self.keyword = keyword
        self.sortby = sortby
        self.domain = domain
        self.fromdate = fromdate
        self.todate = todate