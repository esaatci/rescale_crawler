from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests


def get_absolute_links(url):
    """
    returns all the absolute paths in a given URL
    String -> [String]
    """
    html = get_html(url)
    anchors = get_anchors(html)
    urls = map(get_url, anchors)
    return list(filter(is_absolute, urls))


def get_html(url):
    """
    String -> String
    gets the html from a given url
    to simplify things, if a request fails then it'll return an empty string
    """
    response = requests.get(url)
    if response.ok:
        return response.text
    return ""


def get_anchors(html):
    """
    String -> ResultSet
    gets the anchor tags from an html file
    """
    soup = BeautifulSoup(html, "html.parser")
    return soup.find_all("a")


def get_url(anchor):
    """
    Gets the href field from an anchor tag
    """
    return anchor.get("href")


def is_absolute(url):
    """
    checks if the given url is absolute
    """
    return bool(urlparse(url).netloc)


def log_urls(location, urls):
    """
    prints the given urls to the stdout
    based on the format given in the pdf
    """
    print(location)
    for url in urls:
        print(f"\t{url}".format(url))


def is_valid_input(url):
    """
    Validates the command line input
    """
    return is_absolute(url)
