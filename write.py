import json
import xml.etree.ElementTree as ET
from xml.dom import minidom


def xspf(data):
    playlist = ET.Element('playlist', xmlns='http://xspf.org/ns/0/', version='1')
    ET.SubElement(playlist, 'title').text = 'Radios'
    tracklist = ET.SubElement(playlist, 'trackList')

    for broadcaster, stations in data.items():
        for station in stations:
            track = ET.SubElement(tracklist, 'track')
            ET.SubElement(track, 'creator').text = broadcaster
            ET.SubElement(track, 'location').text = station['url']
            ET.SubElement(track, 'title').text = station['radio']
            ET.SubElement(track, 'album').text = station['radio']

    xmlstr = minidom.parseString(ET.tostring(playlist)).toprettyxml(indent='    ')
    return xmlstr


def main():
    with open('radios.json', 'r') as f:
        data = json.load(f)
    xmlstr = xspf(data)
    with open('new.xspf', 'w') as f:
        print(xmlstr, file=f)


main()
