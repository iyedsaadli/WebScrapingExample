from app import books
from colorama import Fore

USER_CHOICE = ''' Enter one of the following

- 'b' to look at 5-star books 
- 'c' to look at the cheapest books
- 'bc' to look at the best and the cheapest books
- 'n' to just get the next available book on the catalogue
- 'q' to exit

'''


def best_books():
    best_books = sorted(books, key=lambda x: x.rating * -1)[:3]
    for book in best_books:
        print(book)


def cheapest_books():
    cheapest_book = sorted(books, key=lambda x: x.price)[:3]
    for book in cheapest_book:
        print(book)


def best_cheapest_books():
    cheapest_best = sorted(books, key=lambda x: (x.rating * -1, x.price))[:3]
    print('the length is ' + str(len(cheapest_best)))
    for book in cheapest_best:
        print(book)


book_generator = (x for x in books)


def next_book():
    print(next(book_generator))

"""
def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'b':
            print(Fore.BLUE + '------ ** best books ** ------')
            best_books()
        elif user_input == 'c':
            print(Fore.YELLOW + '------ ** cheapest books ** ------')
            cheapest_books()
        elif user_input =='bc':
            print(Fore.GREEN + '------ ** best _ cheapest books ** ------')
            best_cheapest_books()
        elif user_input == 'n':
            next_book()
        else:
            print('Please enter a valid choice.')
        print('\n')
        user_input = input(USER_CHOICE)

"""


# this is more efficient way of creating menu

user_choice = {
    'b': best_books,
    'c': cheapest_books,
    'bc': best_cheapest_books,
    'n': next_book
}


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in ('b', 'c', 'bc', 'n'):
            user_choice[user_input]()
        else:
            print('Please enter a valid choice')

        user_input = input(USER_CHOICE)


menu()