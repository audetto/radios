import json
import xml.etree.ElementTree as ET

import pandas as pd


def main():
    et = ET.parse('radio.xspf')
    root = et.getroot()

    namespace = {'ns': 'http://xspf.org/ns/0/'}

    fields = ['location', 'title', 'creator', 'album']

    tracks = root.find('ns:trackList', namespace)
    records = []
    radios = {}
    for track in tracks.findall('ns:track', namespace):
        item = {}
        for field in fields:
            node = track.find(f'ns:{field}', namespace)
            if node is not None:
                item[field] = node.text
        if item:
            records.append(item)
            creator = item['creator']
            if creator not in radios:
                radios[creator] = []
            
            item = item.copy()
            del item['creator']
            radios[creator].append(item)

    df = pd.DataFrame(data=records)
    with open('radios.json', 'w') as f:
        json.dump(radios, f, indent=4)


main()
