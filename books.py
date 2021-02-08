#########################################################
# Import of modules
#########################################################

import requests
from bs4 import BeautifulSoup
import re
import os
import csv

#########################################################
# script that extracts data from a book
#########################################################

# The get_product_info function which receives the url of each book and returns the data concerning it
def get_product_info(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    product_page_url = url
    universal_product_code = soup.find("td").text
    title = soup.find("h1").text
    price_including_tax = soup.findAll("td")[3].text[1:]
    price_excluding_tax = soup.findAll("td")[2].text[1:]
    number_available = soup.findAll("td")[5].text
    product_description = soup.findAll("p")[3].text
    category = soup.findAll("li")[2].text
    review_rating = soup.find("p", "star-rating")["class"][-1]
    image_url = "http://books.toscrape.com/" + soup.find("img")["src"][6:]
    book_ref = {
            "product_page_url": product_page_url,
            "universal_product_code": universal_product_code,
            "title": title,
            "price_including_tax": price_including_tax,
            "price_excluding_tax": price_excluding_tax,
            "number_available": number_available,
            "product_description": product_description,
            "category": category,
            "review_rating": review_rating,
            "image_url": image_url,
        }
    return book_ref
