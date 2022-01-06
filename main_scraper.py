from csv import writer
import pandas as pd
import requests
import json
from requests.api import head
from requests.exceptions import ConnectionError

cat = []
sub_cat = []
product_id = []
link = []
price = []
brand = []
qty = []
name = []

header = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'}
base_url = requests.get("https://www.bigbasket.com/product/get-products/?page=1&tab_type=[%22all%22]&sorted_on=alpha&listtype=pc", headers=header)
base_info = base_url.json()
base_products = ((((base_info['tab_info'])[0])['product_info'])['products'])
#print(base_products)

for i in base_products:
    product_id.append(i['sku'])
    name.append(i['p_desc'] + " " + i['pack_desc'])
    brand.append(i['p_brand'])
    cat.append(i['tlc_n'])
    sub_cat.append(i['pc_n'])
    qty.append(i['w'])
    price.append(i['mrp'])
    link.append(i['absolute_url'])

try:
    for i in range(2,1000):
        node_url = requests.get("https://www.bigbasket.com/product/get-products/?page="+str(i)+"&tab_type=[%22all%22]&sorted_on=alpha&listtype=pc", headers=header)
        node_info = json.loads(node_url.text)
        tab = node_info['tab_info']
        #print(node_info)
        node_products = tab["product_map"]["all"]["prods"]
        for i in node_products:
            product_id.append(i['sku'])
            name.append(i['p_desc'] + " " + i['pack_desc'])
            brand.append(i['p_brand'])
            cat.append(i['tlc_n'])
            sub_cat.append(i['pc_n'])
            qty.append(i['w'])
            price.append(i['mrp'])
            link.append(i['absolute_url'])

except ConnectionError as e:
    bigb = {'Product ID': product_id, 'Product Name': name, 'Brand': brand, 'Product Category': cat, 'Product Sub-category': sub_cat, 'Weight': qty, 'MRP': price, 'Product URL': link}
    bigb_df = pd.DataFrame(bigb)

    bigb_df.to_csv('Big_Basket_Products.csv', index=False, mode='a', header=True)
    bigb_df.to_json('Big_Basket_Products.json',orient='records')
    print(e)
    r = "No response"


bigb = {'Product ID': product_id, 'Product Name': name, 'Brand': brand, 'Product Category': cat, 'Product Sub-category': sub_cat, 'Weight': qty, 'MRP': price, 'Product URL': link}
bigb_df = pd.DataFrame(bigb)
#print(bigb_df)

bigb_df.to_csv('Big_Basket_Products.csv',index=False, mode='a', header=True)
bigb_df.to_json('Big_Basket_Products.json',orient='records')
