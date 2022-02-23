from threading import Thread
from concurrent.futures import ThreadPoolExecutor
from utils import get_absolute_links, log_urls
from LRUCache import LRUCache
from queue import Queue, Empty


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


VISIT_QUEUE_SIZE = 100000

urls_to_visit = Queue(VISIT_QUEUE_SIZE)

LOG_QUEUE_SIZE = 100000

urls_to_log = Queue(LOG_QUEUE_SIZE)

# a long url (ex. a google search url) is around 350 bytes
# This cache size should use something around 35 MB.
CACHE_SIZE = 100000


def crawler_parallel(url):
    """crawler that runs in parallel"""
    # put the initial url to the visit
    urls_to_visit.put(url)

    visited = LRUCache(CACHE_SIZE)
    start_logger()
    with ThreadPoolExecutor() as executor:
        while True:
            url_to_visit = urls_to_visit.get()
            if not visited.has(url_to_visit):
                executor.submit(crawl_task, url_to_visit)
                visited.insert(url_to_visit)
            urls_to_visit.task_done()


def crawl_task(url):
    """task that runs in the thread pool"""
    abs_urls = get_absolute_links(url)
    urls_to_log.put((url, abs_urls))

    for link in abs_urls:
        urls_to_visit.put(link)


def logger_task():
    """
    Logger task that recieves the data from Thread Pool via the
    urls_to_log queue
    uses log_urls function to log them
    """
    while True:
        try:
            log_data = urls_to_log.get_nowait()
            url = log_data[0]
            abs_urls = log_data[1]
            log_urls(url, abs_urls)
            urls_to_log.task_done()
        except Empty:
            continue


def start_logger():
    t = Thread(target=logger_task, daemon=True)
    t.start()
