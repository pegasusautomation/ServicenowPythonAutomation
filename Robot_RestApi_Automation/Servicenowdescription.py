#Need to install requests package for python
#easy_install requests
import json
from math import dist
import re
from unittest import result
import requests
from bs4 import BeautifulSoup


req_item_number_list = []
req_item_link_list = []
product_list = ["Galaxy","Retina","S7","Lenovo"]
req_item_desc_list  = []
requested_list = []
req_item_sysid_list = []

# Set the request parameters
req_item_url = 'https://dev176532.service-now.com/api/now/table/sc_req_item?sysparm_limit=10'

    # Eg. User name="admin", Password="admin" for this code sample.
user = 'admin'
pwd = 'Rathna@123!@#'

    # Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}

    # Do the HTTP request
response = requests.get(req_item_url, auth=(user, pwd), headers=headers )

    # Check for HTTP codes other than 200
if response.status_code != 200: 
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()

    # Decode the JSON response into a dictionary and use the data
data = response.json()
d2 = data['result']
    # print(data['result'][0]['number'])
for element in d2:
    req_item_number_list.append(element['number'])
    req_item_sysid_list.append(element['sys_id'])
    req_item_link_list.append(element['cat_item']['link'])
    
    


for item in req_item_link_list:
# Set the request parameters
    req_item_url = item
    # Do the HTTP request
    response = requests.get(req_item_url, auth=(user, pwd), headers=headers )

    # Check for HTTP codes other than 200
    if response.status_code != 200: 
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
        exit()

    # Decode the JSON response into a dictionary and use the data
    data = response.json()
    d2 = data['result']['description']
    soup = BeautifulSoup(d2,features="lxml")
    req_item_desc_list.append(soup.get_text())

for desc in req_item_desc_list:
    for product in product_list:    
        if desc.__contains__(product) == True:
            requested_list.append(product)

my_dist_req_number = dict(zip(req_item_number_list,requested_list))
my_dist_req_sysid = dict(zip(req_item_number_list,req_item_sysid_list))
print(my_dist_req_number)
print(my_dist_req_sysid)