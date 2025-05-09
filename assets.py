# Script for obtaing the product's asset from the website

# Importing necessary libraries
import requests
import os
import scrapy

# Defining a function to obtain a product's asset from the website
def retrieve_product_assets(sel, headers, url, product_id, timeout=20):

# Retrieving the PDF file for the manual
    manual_link = sel.css('a#infoPacket::attr(href)').extract_first()
    complete_manual_link = 'https://www.baldor.com' + manual_link
    session = requests.session()
    pdf_response = session.get(complete_manual_link, timeout=timeout, headers=headers)
    assets_product_directory = 'assets/' + product_id
    if not os.path.exists(assets_product_directory):
        os.makedirs(assets_product_directory)
    with open(('assets/' + product_id + '/' + 'manual.pdf'), 'wb') as f:
        f.write(pdf_response.content)

# Retrieving the product image
    image_link = sel.css('div#catalog-detail > img::attr(data-src)').extract_first()
    complete_image_link = 'https://www.baldor.com' + image_link
    image_response = session.get(complete_image_link, timeout=20, headers=headers)
    with open(('assets/' + product_id + '/' + 'img.jpg'), 'wb') as g:
        g.write(image_response.content)