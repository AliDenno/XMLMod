import xml.etree.ElementTree as ET
import os
import zipfile
import time
import ChknOperations as Op


tree = ET.parse('index.xml')
root = tree.getroot()
for i in root:
    for j in i:
        for q in j:
            for t in q:
                print(t.tag)