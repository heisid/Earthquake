#!/usr/env/bin python3

import csv

class CSV_Parser:
    def __init__(self, datafile, delimiter=','):
        self.datafile = datafile
        self.delimiter = delimiter
        self.__parsing_data()
    
    def __parsing_data(self):
        raw_data = open(self.datafile)
        csv_data = csv.reader(raw_data, delimiter=self.delimiter)
        self.parsed_data = list()
        fields = next(csv_data)
        for row in csv_data:
            (self.parsed_data.append(dict(zip(fields, row)))
        raw_data.close()

if __name__ == '__main__':
    from sys import argv
    if len(argv) <= 2:
        delimiter = ','
    else:
        delimiter = argv[2]

    earthquake_data = CSV_Parser(argv[1], delimiter)
    print(earthquake_data.parsed_data)
