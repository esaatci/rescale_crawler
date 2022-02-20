import sys
from crawler import crawler_single, crawler_parallel
from utils import is_valid_input


def main():
    """
    Main function of the crawler program
    runs in either serial or parallel
    """
    url = ""
    crawler = crawler_single
    if len(sys.argv) == 2:  # single threaded
        url = url = sys.argv[1]

    elif len(sys.argv) == 3 and sys.argv[1] == "-p":  # parallel flag is set
        url = sys.argv[2]
        crawler = crawler_parallel

    else:
        print("invalid number of arguments")
        sys.exit(1)

    if not is_valid_input(url):
        print("invalid url supplied")
        sys.exit(1)

    crawler(url)


if __name__ == "__main__":
    main()
