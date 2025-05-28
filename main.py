from scraper import fetch_page
from parser import parse_books
from utils import save_to_csv
from utils import save_to_db
from utils import build_full_url
from bs4 import BeautifulSoup


current_URL = "http://books.toscrape.com/catalogue/page-1.html"
all_books = []


while current_URL is not None:

    # 1. Fetch and parse the page
    html = fetch_page(current_URL)
    all_books.extend(parse_books(html))

    # 2. Use BeautifulSoup to check for "next" link
    soup = BeautifulSoup(html, 'html.parser')
    next_btn = soup.find('li', class_='next')

    if next_btn: 

        # 3. Get the href of the next page (e.g., 'page-2.html') and build the full URL
        next_page = next_btn.a['href']
        current_URL = build_full_url(current_URL, next_page)
    else:
        current_URL = None

# Step 3: Save the collected data
save_to_csv(all_books, "data/books_data.csv")

# Step 4: Save to database
save_to_db(all_books)

