# Main script

# Importing necessary functions
from http_requests import make_http_requests
from html_parser import parse_html
from product_data import product_data_to_json, get_product_id
from assets import retrieve_product_assets

# Importing necessary libraries
import scrapy
import requests
import os
import json

# Defining list of urls to be scraped
list_url = ['https://www.baldor.com/catalog/CEBM3546T',
            'https://www.baldor.com/catalog/CEL11303',
            'https://www.baldor.com/catalog/CEBM3554T',
            'https://www.baldor.com/catalog/CEBM3558T',
            'https://www.baldor.com/catalog/CEBM3611T',
            'https://www.baldor.com/catalog/CEBM3615T',
            'https://www.baldor.com/catalog/CEBM3710T',
            'https://www.baldor.com/catalog/CEBM3714T',
            'https://www.baldor.com/catalog/CECP4402T-4',
            'https://www.baldor.com/catalog/CEL11301']

# Defining headers to get passed the block
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Extracting data from all selected products
for url in list_url:
    html = make_http_requests(url, headers=headers)
    sel = parse_html(html)
    json = product_data_to_json(sel)
    retrieve_product_assets(sel, headers, url, get_product_id(sel))