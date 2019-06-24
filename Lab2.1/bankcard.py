import json
import requests
import pprint
from time import sleep

data = open('C:\\Users\\pucher\\Documents\\Seafile\p4ne_training\\card1.json')
url_start = 'https://lookup.binlist.net/'

output = []

data_json = json.load(data)
for i in data_json:
    cd = str(i['CreditCard']['CardNumber'])[0:8]
    print(cd)
    r = requests.get('https://lookup.binlist.net/' + cd, headers={'Accept-Version': "3"})
    if r.status_code == 200:
        rj = r.json()
        if 'name' in rj['bank']:
            output.append(rj['bank']['name'])
    sleep(2)
out_dict = dict.fromkeys(sorted(output))

for i in out_dict.keys():
    print(i)
