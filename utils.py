import pandas as pd
from urllib.parse import urljoin
import mysql.connector


def save_to_csv(data, filename):
    
    df = pd.DataFrame(data)
    df.to_csv(filename, header=True)
    print(f"Data saved to {filename}")

def build_full_url(current_url, next_page_href):
    return urljoin(current_url, next_page_href)


def save_to_db(data):
    # Connect to server
    mydb = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="Angel@1370",  # I removed my pass to db
    database="books_db"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO books (title, price, availability, created_at) VALUES (%s, %s, %s, NOW())"

    # Insert each book
    for book in data:
        val = (book['title'], book['price'], book['availability'])
        mycursor.execute(sql, val)

    # Commit the transaction
    mydb.commit()

    print(mycursor.rowcount, "records inserted in database!")
    mycursor.close()
    mydb.close()
    print("Database connection closed.")