import logging
from locators.book_locators import BookLocators

logger = logging.getLogger('scraping.book_parser')


class BookParser:
    def __init__(self, parent):
        logger.info(f'New book parser ceated from  `{parent}` ')
        self.parent = parent

    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __repr__(self):
        return f"<Book : {self.name}, priced : £{self.price}, reted : ({self.rating} stars).>"

    @property
    def name(self):
        logger.info('Finding book name...')
        locator = BookLocators.NAME_LOCATOR
        item_link = self.parent.select_one(locator)
        item_name = item_link.attrs['title']
        logger.info(f'Found book name , `{item_name}`')
        return item_name

    @property
    def link(self):
        logger.info('Finding book link...')
        locator = BookLocators.LINK_LOCATOR
        item_set = self.parent.select_one(locator)
        item_link = item_set.attrs['href']
        logger.info(f'Found book link , `{item_link}`')
        return item_link

    @property
    def price(self):
        logger.info('Finding book price...')
        locator = BookLocators.PRICE_LOCATOR
        the_price = self.parent.select_one(locator).string
        logger.info(f'Found book price , `{the_price}`')
        return float(the_price.replace('£', ''))

    @property
    def rating(self):
        logger.info('Found book rating...')
        locator = BookLocators.RATING_LOCATOR
        star_rating = self.parent.select_one(locator)
        classes = star_rating.attrs['class']
        rating_class = [rating for rating in classes if rating != 'star-rating']
        rating_number = BookParser.RATINGS.get(rating_class[0])
        logger.info(f'Found book rating , `{rating_number}`')
        return rating_number
