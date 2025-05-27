from scraper import fetch_page
from parser import parse_books
from utils import save_to_csv


BASE_URL = "http://books.toscrape.com/catalogue/page-1.html"

html = fetch_page(BASE_URL)
book_data = parse_books(html)
save_to_csv(book_data, "data/books_data.csv") 
