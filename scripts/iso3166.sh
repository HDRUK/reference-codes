#!/usr/bin/env bash

wget https://salsa.debian.org/iso-codes-team/iso-codes/-/raw/main/data/iso_3166-1.json -O data/iso_3166-1.json
wget https://salsa.debian.org/iso-codes-team/iso-codes/-/raw/main/data/iso_3166-2.json -O data/iso_3166-2.json

python scripts/iso3166.py