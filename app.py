import requests
import logging
from pages.all_books_page import AllBooksPage

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s [%(filename)s %(lineno)d]',
                    level=logging.DEBUG, datefmt='%d-%m-%Y %H:%M:%S', filename='logs.txt')

logger = logging.getLogger('scraping')
logger.info('Loading books list...')

page_content = requests.get('http://books.toscrape.com/').content
page = AllBooksPage(page_content)

books = page.books

for pages in range(1, 5):
    page_content = requests.get('http://books.toscrape.com/catalogue/page-{}.html'.format(pages+1)).content
    page = AllBooksPage(page_content)
    books.extend(page.books)
