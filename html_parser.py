# Script for parsing HTML code to scrapy's Selector object

# Importing necessary libraries
import scrapy

# Defining function for parsing HTML code
def parse_html(html_code):
    return scrapy.Selector(text=html_code)

