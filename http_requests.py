# Script for making HTTP requests

# Importing necessary libraries
import requests

# Defining function to make HTTP requests and catch the HTML
def make_http_requests(url, headers, timeout=20):
    session = requests.Session()
    response = session.get(url, timeout=timeout, headers=headers)
    return response.content
    