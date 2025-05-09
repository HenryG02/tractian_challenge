# Script for extracting product data from the website

# Importing necessary libraries
import scrapy
import json

# Defining function to extract relevant information from the product
def product_data_to_json(sel):

    # Extracting general information about the product
    product_id = sel.css('div.page-title > h1::text').extract_first()
    description = sel.css('div#catalog-detail > div.product-description::text').extract_first()
    hp = sel.css('table.nameplate > tbody > tr:nth-of-type(3) > td::text').extract_first()
    voltage = sel.css('table.nameplate > tbody > tr:nth-of-type(4) > td::text').extract_first()
    rpm = sel.css('table.nameplate > tbody > tr:nth-of-type(6) > td::text').extract_first()
    frame = sel.css('table.nameplate > tbody > tr:nth-of-type(7) > td:nth-of-type(1)::text').extract()

    # Extracting BOM info
    bom_info = sel.css('div[class="pane"][data-tab="parts"] > table.data-table td::text').extract()
    bom_list = [{'part_number': bom_info[i], 'description': bom_info[i+1], 'quantity': bom_info[i+2]} for i in range(0, len(bom_info), 3)]

    data = {'product_id': product_id, 'description': description, 'specs': {'hp': hp, 
                                                                            'voltage': voltage,
                                                                            'rpm': rpm, 'frame': frame},
            'bom': bom_list}
    
    # Creating JSON file for the product
    with open(product_id + '.json', 'w') as file:
        json.dump(data, file, indent=4)

# Defining function for getting the product ID only
def get_product_id(sel):
    return sel.css('div.page-title > h1::text').extract_first()