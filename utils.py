from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests

'''
returns all the absolute paths in a given URL
String -> [String]
'''
def getAbsoluteLinks(url):
  html = getHTML(url)
  anchors = getAnchors(html)
  urls = map(getUrl, anchors)
  return list(filter(isAbsolute, urls))

'''
String -> [String]
gets the html from a given url
to simplify things, if a request fails then it'll return an empty string
'''
def getHTML(url):
  r = requests.get(url)
  if r.ok:
    return r.text
  else:
    return ""

def getAnchors(html):
  soup = BeautifulSoup(html, "html.parser")
  return soup.find_all('a')

def getUrl(anchor):
  return anchor.get("href")

def isAbsolute(url):
  return bool(urlparse(url).netloc)

'''
  prints the given urls to the stdout
  based on the format given in the pdf
'''
def logUrls(location, urls):
  print(location)
  for url in urls:
    print("\t{}".format(url))

