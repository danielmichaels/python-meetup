#!/usr/bin/env python3
from json2html import *

from fuelwatcher import FuelWatch

api = FuelWatch()

"""
Fuelwatch RSS XML Scraper that outputs a html file containing a
html table with the results of query.

Requires the fuelwatcher module which parses the raw XML into JSON format.
"""


def main():
    json_ = setup()
    resp = json_to_html(json_)
    save_output(resp)


def setup():
    """Query the endpoint and return JSON.

    Variables accepted by `query()`:

    def query(self, product: int = None, suburb: str = None, region: int = None, 
            brand: int = None, surrounding: str = None, day: str = None):

    Example:

    api.query(product=4, region=25, day='yesterday')

    :return json formatted query response.
    """
    api.query()
    json_ = api.get_json
    return json_


def json_to_html(resp):
    """Pass in JSON and return html table."""
    return json2html.convert(json=resp)


def save_output(html):
    """Creates html file for storing html table object.

    Minimal product for testing purposes.
    Could generate name based on day, product, region etc; append; prettify
    table with css etc.

    :return html file containing table data.
    """
    with open('table.html', 'w') as f:
        for line in html:
            f.write(line)


if __name__ == '__main__':
    main()
