import requests
import bs4

r = requests.get("https://www.webketab.ir/")
data = r.text
structure = bs4.BeautifulSoup(data)

# title
title = structure.select("title")
print(title)

# class
books_titles = structure.select(".product-preview-info .product-preview-title a span")
for book_title in books_titles:
    print(book_title.text)
print(len(books_titles))

# pictures
books_images = structure.select(".product-preview-image img")
for book_image in books_images:
    src = book_image.get("src")
    src = (f"https://www.webketab.ir/{src}")
    print(src)
