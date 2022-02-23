# rescale_crawler


This project implements a web crawler that logs and follows links.

# Philosopy

I tried to keep the implementation as simple as possible. Most of the code is written in a somewhat functional style with lots of composition along the way. File structure is also intentionally flat.

# Content

There are 6 python files in this project which are:

1. crawler.py
2. main.py
3. utils.py
4. test_get_absolute_links.py
5. LRUCache.py
6. test_LRUCache.py

### crawler.py
Contains two crawlers, one serial and one parallel. I decided to keep the serial crawler to see the evolution between two different versions.

Serial crawler implements a recursive Depth First Search approach with an optional depth argument. It is defaulted to 3 and can be changed in the code. Once crawler reaches the provided depth, it'll stop.

Parallel crawler is very similar, but uses threads to increase the throughput. It doesn't have a stop conditon.

### main.py
The main entry point of the project. Parses the command line args and starts the crawler. Refer to the Usage section for more info.

### utils.py
Utility functions that are used by the crawlers and the main function. Url fetching, parsing etc. is done inside this file.

### test_get_absolute_links.py
Contains a unit test to validate getting links from a url

### LRUCache.py
Contains a cache to keep track of visited urls

### test_LRUCache.py
Contains unit tests for the LRUCache

# Parallelization
The parallelization is achieved by using Python's built-in `ThreadPoolExecutor` to implement a thread pool. Maximum number of threads is set to 300. This number is selected arbitrarily. Threads access a url, retrieve the links and adds the next batch of urls to a shared list. The main thread (crawler_parallel) and tasks communicate using this lifo queue. Access to this is controlled by `Lock` object in python.

I chose using the threadpool over the `multiprocessing` library because this program is mostly I/O bound.

# Extra libraries
There are 3 extra libraries used.

1. `BeautifulSoup` is used for parsing html
2. `black` is used for formatting
3. `requests` is used for network requests

# Installation
I'm making the assumption that this will be run on a Linux/MacOs environment and the machine has git and python version 3 installed.

Step 1: Clone the Repository

`git clone https://github.com/esaatci/rescale_crawler.git`

Step 2: go into the cloned directory

`cd path/to/the/cloned/repo`

Step 3: Create a virtual environment

`python3 -m venv .`

Step 4: Activate the virtual environment

`source bin/activate`

Step 5: Install the dependencies

`pip install -r requirements.txt`


# Usage
After the installation is complete if you are not inside the project directory with the virtual environment activated, perform Step 2 and Step 4 from the installation section.

To run the crawler use the following command:

`python3 main.py -p https://theUrlYouWantToStartFrom.com`

It is important to format the url in absolute format with either http or https. Otherwise the program will exit.

the `-p` signifies that the program will run in parallel mode. To run in serial replace `-p` with `-s`:

`python3 main.py -s https://theUrlYouWantToStartFrom.com`

to stop the program:

`ctrl + c`

to run the unit test:

`python3 -m unittest`

# Further Improvements

There are couple of things that can be done to improve this project in the future.

1. Adding more unit tests
2. Adding the support for writing to a file
3. Adding stop conditions to the parallel crawler. Ex. time based, depth-based, link-based
4. Better command line arg support. Passing stop conditions, thread count etc.
5. Dockerizing the project.
6. Different ways of parallelizing
