from utils import getAbsoluteLinks, logUrls

DEFAULT_DEPTH = 3

def crawler(url, depth=DEFAULT_DEPTH):
  if depth != 0:
    absLinks = getAbsoluteLinks(url)
    logUrls(url, absLinks)
    for link in absLinks:
      crawler(link, depth-1)
