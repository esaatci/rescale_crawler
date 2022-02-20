from crawler import crawler
from utils import isValidInput
import sys

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("invalid arguments")
    sys.exit(1)

  url = sys.argv[1]
  if not isValidInput(url):
    print("invalid url supplied")
    sys.exit(1)

  crawler(url)
