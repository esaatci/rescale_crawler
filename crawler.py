from threading import Thread, BoundedSemaphore, Lock
from utils import get_absolute_links, log_urls


DEFAULT_DEPTH = 3


def crawler_single(url, depth=DEFAULT_DEPTH):
    """
    Single threaded
    """
    if depth != 0:
        abs_urls = get_absolute_links(url)
        log_urls(url, abs_urls)
        for link in abs_urls:
            crawler_single(link, depth - 1)


urls_to_visit = []

urls_lock = Lock()

MAX_THREAD_COUNT = 300

sem = BoundedSemaphore(MAX_THREAD_COUNT)


def crawler_parallel(url):
    """crawler that runs in parallel"""
    # put the initial url to the visit
    urls_to_visit.append(url)
    while True:
        # get the lock to the urls
        with urls_lock:
            if urls_to_visit:
                url_to_visit = urls_to_visit.pop()
                with sem:
                    # start a thread
                    t = Thread(target=crawl_task, args=(url_to_visit,))
                    t.start()


def crawl_task(url):
    """thread task that runs in a spawned Thread"""
    abs_urls = get_absolute_links(url)
    log_urls(url, abs_urls)
    with urls_lock:
        for link in abs_urls:
            urls_to_visit.append(link)
        sem.release()
