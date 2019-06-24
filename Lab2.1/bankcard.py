import json
import requests
import pprint
from time import sleep

data = open('C:\\Users\\pucher\\Documents\\Seafile\p4ne_training\\card2.json')
url_start = 'https://lookup.binlist.net/'
output = []
data_json = json.load(data)
for i in data_json:
    card_id = str(i['CreditCard']['CardNumber'])[0:8]
    r = requests.get(url_start + card_id, headers={'Accept-Version': "3"})
    if r.status_code == 200:
        r_json = r.json()
        if 'name' in r_json['bank']:
            output.append(r_json['bank']['name'])
    sleep(2)
out_dict = dict.fromkeys(sorted(output))

for i in out_dict.keys():
    print(i)
