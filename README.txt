Hello!

Thanks for the opportunity to be part of Tractian! This the README file for my case project.

It was really challenging but a rewarding journey nonetheless! 

I couldn't manage to complete all the tasks (e.g. downloading CAD files) nor make the output as clean or as organized as I'd like due to time/deadline issue and some personal problems :(

But getting to the meat of it, my project is structured in five Python files:
    1. http_requests.py: this script makes HTTP requests, using the requests Python library, and catches the HTML response
    2. html_parser: this script parses the HTML with the use of the scrapy Python library
    3. product_data: this script extracts the relevant product information from the webpage, using the scrapy's Selector and CSS Selector notation
    4. assests: this scripts retrieves the relevant assests such as the manuals as PDFs and the product's image as JPG
    5. main.py: this script manages all the others so that we can scrape more than one site

A quick note: There're some optimizations I could've made (like using scrapy's Spiders instead of a for loop), but that I didn't manage to do it on time. However, I'm happy to discuss the alternatives that I've thought, if you think it makes sense.

Also, there's the requirements.txt for managing dependencies.