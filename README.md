# Python-WebCrawler
A Python-based web crawler capable of extracting URLs from websites and subdomains with an optional depth limit. Provides a solid foundation for web scraping projects.

## Features

- **Supports Multiple File Types**: Handles common web page extensions
- **Domain Filtering**: Allows crawling within a specific domain, with an option to include subdomains.
- **Depth Control**: Limits the crawl to a specified depth, preventing excessive recursion.

## Usage

To use this web crawler, start by specifying the URL (`WEBSITE_URL`) where the crawl should begin. 
By default, `max_depth` is 2. The larger the value, the more recurssion. Set to `-1` for unlimited depth, allowing the crawler to follow links indefinitely until it exhausts all reachable URLs within the allowed domain(s).

## Dependencies

- `requests`
- `beautifulsoup4`
- `lxml`


## Installation

Ensure you have Python installed on your system. Then, install the required dependencies using pip:
```bash
  pip install requests beautifulsoup4 lxml
```

## TODO
- **Pagination Support**: Currently, the crawler does not handle pagination
- **Concurrent Operations**: Future versions should allow for concurrent crawling
- **Smart Rate Limiting**: Limit the number requests to prevent server throttling
