# -*- coding: utf-8 -*-
import re
import requests
import json

URL = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'

def load_exchange():
    """
    Loads the exchange rates from the specified URL and returns them as a list of dictionaries.
    """
    response = requests.get(URL)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        print("Failed to load exchange rates:", response.status_code)
        return []

def get_exchange(ccy_key):
    """
    Returns the exchange rates for the requested currency.
    """
    for exc in load_exchange():
        if ccy_key == exc['ccy']:
            return exc
    return False

def get_exchanges(ccy_pattern):
    """
    Returns a list of currencies according to a pattern.
    """
    result = []
    ccy_pattern = re.escape(ccy_pattern) + '.*'
    for exc in load_exchange():
        if re.match(ccy_pattern, exc['ccy'], re.IGNORECASE) is not None:
            result.append(exc)
    return result
