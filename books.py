#########################################################
# Import of modules
#########################################################

import requests
from bs4 import BeautifulSoup
import re
import os
import csv

#########################################################
# Script that extracts data from a book
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
#########################################################
# Script that allows the extraction of data from a book category taking into account the pagination
#########################################################

# The get_categories_info function receives the url of each category and returns the link of each book article it has

def get_category_info(link_cat,category_name):

    current_category = link_cat # Creation of an intermediate variable to facilitate iteration

    while  current_category!= None:

        r = requests.get(current_category)
        soup = BeautifulSoup(r.text, "html.parser")
        book_links = soup.findAll("h3")
        for h3 in book_links:
            a = h3.find("a")
            link = a["href"][9:]
            url_book = "http://books.toscrape.com/catalogue/" + link

            
            book_infos = get_product_info(url_book) # Send urls of each book to get_product-info
            save_product_info(category_name,book_infos) # Data recording of each book
   
        # Taking into account the pagination
        test_tag_next=soup.find("li",class_="next")

        if test_tag_next!=None:
            next_page=test_tag_next.find("a")["href"]
            current_category = link_cat + next_page

        else:
            current_category=None

#########################################################
# Script data backup
#########################################################

def save_product_info(category_name,data):

    # Create directory where we will save all the category directory, csv files and images
    try:
        os.mkdir('categories/'+ category_name)
    except:
        pass

    # Check if category file exists
    if os.path.isfile("categories/"+ category_name +"/" + category_name +'.csv'):
        with open('categories/'+ category_name +"/" + category_name +".csv","a",newline="", encoding="utf-8") as category_file:
            csv_writer = csv.writer(category_file)
            csv_writer.writerow([data['product_page_url'], data['universal_product_code'], data['title'], data['price_including_tax'], data['price_excluding_tax'], data['number_available'], data['product_description'], data['category'], data['review_rating'], data['image_url']])
    else:
        with open('categories/'+ category_name +"/" + category_name +".csv","a",newline="", encoding="utf-8") as category_file:
            csv_writer = csv.writer(category_file)
            csv_writer.writerow(['product_page_url', 'universal_product_code', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url'])
            csv_writer.writerow([data['product_page_url'], data['universal_product_code'], data['title'], data['price_including_tax'], data['price_excluding_tax'], data['number_available'], data['product_description'], data['category'], data['review_rating'], data['image_url']])

    # Downlord and save all images of each directory
    image_title = re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,*]", "", data['title']) # the re module allows special characters to be taken into account
    image_url = data['image_url']
       
    with open("categories/"+ category_name +"/" + image_title +".jpg","wb") as image_file:
        im = requests.get(image_url)
        image_file.write(im.content)         

#########################################################
# Script that extracts all category url
#########################################################

# get_all_category function retrieves and returns the link of each category to get_category_info
def get_all_category(url):

    # Create directory where we will save all the files
    try:
        os.mkdir('./categories')
    except:
        pass
    
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    cat_links = soup.findAll("ul", attrs={"class": "nav nav-list"})
    for ul in cat_links:
        cat_link = ul.findAll("a")[1:]
        for link in cat_link:
            if "href" in link.attrs:
                link_cat = "http://books.toscrape.com/" + link.attrs["href"].replace('index.html','')

                #Get category name. Strip method is useful to remove white spaces around the category name
                category_name = link.string.strip()

                get_category_info(link_cat,category_name)

get_all_category("http://books.toscrape.com/")


