from threading import Lock
from concurrent.futures import ThreadPoolExecutor
from utils import get_absolute_links, log_urls

DEFAULT_DEPTH = 3


def crawler_serial(url, depth=DEFAULT_DEPTH):
    """
    Single threaded
    """
    if depth != 0:
        abs_urls = get_absolute_links(url)
        log_urls(url, abs_urls)
        for link in abs_urls:
            crawler_serial(link, depth - 1)


urls_to_visit = []

urls_lock = Lock()

MAX_THREAD_COUNT = 300


def crawler_parallel(url):
    """crawler that runs in parallel"""
    # put the initial url to the visit
    # since we haven't started threading it's safe put things
    # into the list without acquiring the lock
    urls_to_visit.append(url)
    with ThreadPoolExecutor(max_workers=MAX_THREAD_COUNT) as executor:
        while True:
            with urls_lock:
                if urls_to_visit:
                    url_to_visit = urls_to_visit.pop()
                    executor.submit(crawl_task, url_to_visit)


def crawl_task(url):
    """task that runs in the thread pool"""
    abs_urls = get_absolute_links(url)
    log_urls(url, abs_urls)

    with urls_lock:
        for link in abs_urls:
            urls_to_visit.append(link)
