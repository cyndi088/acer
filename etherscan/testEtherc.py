import requests
from db import db
import json


def test():
    parse_urls = 'http://api.etherscan.io/api?module=account&action=tokentx&contractaddress=%s&startblock=5690000&endblock=5700000&sort=desc&apikey=18RC3HD9A4Z7E21DA4DWTFX8TZ6VNWYI7M'
    details = db['etherscan_contract_address'].find()

    for address in details:
        # request = Request(parse_urls % address['contract_address'], callback=self.parse)
        # yield request
        parse_urls = 'http://api.etherscan.io/api?module=account&action=tokentx&contractaddress=%s&startblock=5690000&endblock=5700000                      &sort=desc&apikey=18RC3HD9A4Z7E21DA4DWTFX8TZ6VNWYI7M'
        msg = requests.get(parse_urls % address['contract_address']).text
        print(msg)



test()

