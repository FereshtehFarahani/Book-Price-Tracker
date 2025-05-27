from bs4 import BeautifulSoup

def parse_books(html):

    # parse html content
    soup = BeautifulSoup(html , 'html.parser')

    # find all book containers
    books = soup.find_all('article', class_='product_pod')

    all_books = []

    for book in books:
        # for every book initialize an empty dictionary        
        book_dict = {}

        # Extract data from the HTML
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        availability = book.find('p', class_='instock availability').text.strip()    

        # fill the dictionary 
        book_dict['title'] = title
        book_dict['price'] = price
        book_dict['availability'] = availability

        # Add to the main list
        all_books.append(book_dict)

    return all_books
