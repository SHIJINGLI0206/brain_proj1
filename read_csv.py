from xml.dom import minidom
import xml.etree.ElementTree as ET

tree = ET.parse("../BCCD/Annotations/BloodImage_00000.xml")
root = tree.getroot()

for obj in tree.findall('object'):
    name = obj.find('name').text
    bndbox = obj.find('bndbox')
    xmin = bndbox.find('xmin').text
    xmax = bndbox.find('xmax').text
    ymin = bndbox.find('ymin').text
    ymax = bndbox.find('ymax').text
    print(name,xmin,ymin,xmax,ymax)



