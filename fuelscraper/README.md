# Python Meetup Group Fuelwatch Scraper

## Usage

**taken from `fuelwatcher` package README.**

see [here](https://github.com/danielmichaels/fuelwatcher/blob/master/README.md)
for more information.

### Basic Usage

```python
from fuelwatch import FuelWatch

api = FuelWatch()

api.query(product=2, region=25, day='yesterday')
# returns byte string of xml.
xml_query = api.get_xml
# iterates over each fuel station entry in the byte string
# and returns list of dictionaries in human readable text.

print(parsed_query)

>>>> [{'title': '138.5: Puma Bayswater', 'description': 'Address: 502 Guildford Rd, BAYSWATER, Phone: (08) 9379 1322, Open 24 hours', 'brand': 'Puma', 'date': '2018-04-05', 'price': '138.5', 'trading-name': 'Puma Bayswater', 'location': 'BAYSWATER', 'address': '502 Guildford Rd', 'phone': '(08) 9379 1322', 'latitude': '-31.919556', 'longitude': '115.929069', 'site-features': ', Open 24 hours'} ..snip.. ]
```

Fuelwatcher can also transform the XML into JSON format. It is as simple as calling the `get_json` method.

```python

api = FuelWatch()

api.query(region=1)

json_response = api.get_json

>>>> [
>>>>   {
>>>>       "title": "143.9: United Boulder Kalgoorlie",
>>>>       "description": "Address: Cnr Lane St & Davis St, BOULDER, Phone: (08) 9093 1543",
>>>>       "brand": "United",
>>>>       "date": "2018-04-13",
>>>>       "price": "143.9",
>>>>       ... snip ...
>>>>       "longitude": "121.433746",
>>>>       "site-features": "Unmanned Station, "
>>>>   }
>>>> ]
```

For most operations the `get_xml` or `get_json` method will be sufficient. If the developer wants to parse the raw RSS XML then the `get_raw()` method is available.

```python
get_raw = api.get_raw

print(get_raw)

>>>> (b'<?xml version="1.0" encoding="UTF-8"?>\r\n<rss version="2.0"><channel><title>FuelWatch Prices For North of River</title><ttl>720</ttl><link>http://www.fuelwatch.wa.gov.au</link><description>05/04/2018 - North of River</description><language>en-us</language><copyright>Copyright 2005 FuelWatch... snip...</item></channel></rss>\r\n')
```

The query method takes several keyword arguments. By defaults it will return every fuel station across Western Australia.

As guide query takes the following kwargs

```python
def query(self, product: int = None, suburb: str = None, region: int = None,
            brand: int = None, surrounding: str = None, day: str = None):
```
## Installation

Requires `fuelwatcher` package for scraping the FuelWatch RSS feed and `json2html` for creating HTML tables.

```sh
pip install fuelwatcher json2html
```

