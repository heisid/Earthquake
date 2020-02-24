#!/usr/bin/env python3

import geojson 
from CSV_Parser import CSV_Parser

def create_geojson(parsed_data):
    geo_map = {'type': 'FeatureCollection'}
    map_data = list()
    
    for index, line in enumerate(parsed_data):

        point_data = dict()

        point_data['type'] = 'Feature'
        point_data['id'] = index
        point_data['properties'] = {'Mag (SR)': line['Magnitudo (SR)'],
                                    'Date (GMT)': line['Tanggal (GMT)'],
                                    'Depth (km)': line['Kedalaman (km)']}
        point_data['geometry'] = {'type': 'Point',
                                  'coordinates': (line['Lintang (°)'], line['Bujur (°)'])}

        map_data.append(point_data)
        geo_map.setdefault('features', []).append(point_data)

    with open('earthquake_map.geojson', 'w') as f:
        f.write(geojson.dumps(geo_map))

if __name__ == '__main__':
    parser = CSV_Parser('data/20200214_20200224/laporan_data_gempa.csv')
    parsed_data = parser.parsed_data
    create_geojson(parsed_data)
