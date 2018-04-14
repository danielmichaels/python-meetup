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
    html = test(json_)
    save_output(html)


def setup():
    """Query the endpoint and return JSON."""
    api.query()
    json_ = api.get_json
    return json_


def test(resp):
    """Pass in JSON and return html table."""
    return json2html.convert(json=resp)


def save_output(html):
    with open('test.html', 'w') as f:
        for line in html:
            f.write(line)


if __name__ == '__main__':
    main()
