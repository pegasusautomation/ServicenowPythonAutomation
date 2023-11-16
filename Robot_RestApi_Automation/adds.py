import requests
import json

#Get ID of each variable by passing the RITM number in the first request
ritm = 'RITM0000005'
user = 'admin'
pwd = 'Rathna@123!@#'
headers = {"Accept": "application/json"}

mtom_link = "https://dev176532.service-now.com/api/now/table/sc_item_option_mtom?sysparm_display_value=true&sysparm_exclude_reference_link=True&sysparm_query=request_item%3D" + str(
    ritm) + "&sysparm_fields=sc_item_option"
mtomresponse = requests.get(mtom_link, auth=(user, pwd), headers=headers)
mjsondata = mtomresponse.text
loadmjsondata = json.loads(mjsondata)
mdata = loadmjsondata['result']
mtomkeys = []

# Poll and collect each key
for m in mdata:
    mtom_value = m['sc_item_option']
    mtomkeys.append(mtom_value)

# For each key call API to retreive fieldnames and values
for key in mtomkeys:
    key_link = "https://dev176532.service-now.com/api/now/table/sc_item_option?sysparm_limit=10&sysparm_display_value=True&sysparm_exclude_reference_link=True&sysparm_query=sys_id%3D" + str(
        key) + "&sysparm_fields=item_option_new,value,description"
    mtomkeyresponse = requests.get(key_link, auth=(user, pwd), headers=headers)
    if mtomkeyresponse.status_code != 200:
        print('Status:', mtomkeyresponse.status_code, 'Headers:', mtomkeyresponse.headers, 'Error Response:', mtomkeyresponse.content)
        exit()
    kjsonload = mtomkeyresponse.json()
    result = kjsonload['result']

    for vn in result:
        varname = vn['item_option_new']
        value = vn['value']
        if varname and varname not in ["Patching information"]:
            print("{} => {} : {}".format(key, varname, value)) #Print to view the result