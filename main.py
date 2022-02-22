import sys
from crawler import crawler_serial, crawler_parallel
from utils import is_valid_input
import signal


def main():
    """
    Main function of the crawler program
    runs in either serial or parallel
    """
    if len(sys.argv) != 3:
        print("invalid number of arguments")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "-p":
        crawler = crawler_parallel
    elif cmd == "-s":
        crawler = crawler_serial
    else:
        print("unknown command")
        sys.exit(1)

    url = sys.argv[2]
    if not is_valid_input(url):
        print("invalid url supplied")
        sys.exit(1)

    crawler(url)


def handler(signum, frame):
    sys.exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, handler)
    main()
