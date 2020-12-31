#!/usr/bin/env python3

import csv

from uk_covid19 import Cov19API

# For valid filter and structure values, see
# https://coronavirus.data.gov.uk/details/developers-guide

filters = [
    'areaType=overview'
]

structure = {
    'date': 'date',
    'newPeopleReceivingFirstDose': 'newPeopleReceivingFirstDose',
    'cumPeopleReceivingFirstDose': 'cumPeopleReceivingFirstDose',
    'newPeopleReceivingSecondDose': 'newPeopleReceivingSecondDose',
    'cumPeopleReceivingSecondDose': 'cumPeopleReceivingSecondDose',
}

outfile = 'data.csv'

api = Cov19API(filters, structure)
data = api.get_json()

with open(outfile, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=structure.keys())
    writer.writeheader()
    for row in reversed(data['data']):
        writer.writerow(row)
