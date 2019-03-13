from xml.dom import minidom
import xml.etree.ElementTree as ET
import os
import pandas as pd



df =  pd.DataFrame(columns=['Image_names','cell_type','xmin','xmax','ymin','ymax'])
path_xml = "BCCD/Annotations/"
for fn in os.listdir(path_xml):
    print(fn)
    tree = ET.parse(path_xml+fn)
    root = tree.getroot()
    for obj in tree.findall('object'):
        name_cell = obj.find('name').text
        name_f = str(fn).replace(".xml",".jpg")
        bndbox = obj.find('bndbox')
        xmin = bndbox.find('xmin').text
        xmax = bndbox.find('xmax').text
        ymin = bndbox.find('ymin').text
        ymax = bndbox.find('ymax').text
        print(name_f,name_cell,xmin,ymin,xmax,ymax)
        df = df.append({'Image_names'    : name_f ,
                   'cell_type'      : name_cell,
                   'xmin'           : xmin,
                   'xmax'           : xmax,
                   'ymin'           : ymin,
                   'ymax'           : ymax
                   },ignore_index=True)

df.to_csv('blood_cell.csv')
print('done!')



