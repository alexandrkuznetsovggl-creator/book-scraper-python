import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "http://books.toscrape.com/catalogue/"
current_url = "http://books.toscrape.com/catalogue/page-1.html"

books_data = [ ]

    

while current_url:
    print(f"Scraping page: {current_url}")

    response = requests.get(current_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    books = soup.find_all('article', class_='product_pod')

    for book in books:
        title = book.find('h3').find('a')['title']
        price = book.find('p', class_='price_color').text.strip()
        stock = book.find('p', class_='instock availability').text.strip()
        
        books_data.append({'Title': title, 'Price': price, 'Availability': stock})

    next_button = soup.find('li', class_='next')

    if next_button:
        next_page_link = next_button.find('a')['href']
        current_url = base_url + next_page_link
    else:
        current_url = None

df = pd.DataFrame(books_data)

df.to_csv("toscrape_books_pandas.csv", index=False, encoding='utf-8-sig')


print("Task completed. File is ready.")        