import sys
import json
import csv
import copy
from pprint import pprint

def read_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def write_json(data, filename=None, indent=2):
   with (open(filename, 'w') if filename else sys.stdout) as file:
        json.dump(data, file, indent=indent)

def read_csv(filename):
    ROWS = []
    with open(filename, 'r', encoding='ISO-8859-1') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            ROWS.append(row)
    return ROWS

def write_csv(data, filename, header):
    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        writer.writerows(data)

def process_iso3166_codes(iso3166_1, iso3166_2):
    iso3166 = {}

    # loop though countries
    for c in iso3166_1['3166-1']:
        code = {
            'code': c['alpha_2'],
            'name': c.get('common_name', c.get('name')),
            'type': 'Country or Territory',
            'level': 1,
            'parent_code': '',
            'parent_name': '',
        }
        iso3166[code['code']] = code
    
    # loop though subdivisions
    for c in iso3166_2['3166-2']:
        parent_code = c['code'].split('-')[0] # split on country code
        code = {
            'code': c['code'],
            'name': c['name'],
            'type': c['type'],
            'level': 2,
            'parent_code': parent_code,
            'parent_name': iso3166[parent_code]['name'] # lookup country code
        }
        iso3166[code['code']] = code
    
    return list(iso3166.values())

def main():
    iso3166_1 = read_json('data/iso_3166-1.json')
    iso3166_2 = read_json('data/iso_3166-2.json')
    iso3166 = process_iso3166_codes(iso3166_1, iso3166_2)
    # sort by code
    iso3166 = sorted(iso3166, key=lambda c: c['code'])

    headers = ['code', 'name', 'type', 'level', 'parent_code', 'parent_name']
    write_csv(iso3166, "data/iso_3166.csv", headers)
    write_json(iso3166, 'data/iso_3166.json', 2)

    

if __name__ == '__main__':
    main()