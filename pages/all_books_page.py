import logging
from bs4 import BeautifulSoup

from locators.all_books_page import AllbooksPageLocators
from parsers.book_parser import BookParser

logger = logging.getLogger('scraping.all_books_page')


class AllBooksPage:
    def __init__(self, page_content):
        logger.info('Parsing page content with beautiftulsoup')
        self.soup = BeautifulSoup(page_content, 'html.parser')

    @property
    def books(self):
        logger.info(f'Finding all books in page using {AllbooksPageLocators.BOOKS}.')
        result_set = self.soup.select(AllbooksPageLocators.BOOKS)
        return [BookParser(e) for e in result_set]