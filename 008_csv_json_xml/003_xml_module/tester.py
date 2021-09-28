from xml.etree import ElementTree

tree = ElementTree.parse('xml_files/cd_catalog.xml')
root = tree.getroot()

cd = root[0]
data = next(cd.iter('Y1985'))
data.text = str(int(data.text) + 500000)
total_count = cd[6]
total_count.set("type", "All sold")
print(total_count)

total_sold = ElementTree.Element('TOTAL')
total_sold.text = "2000000"
cd.append(total_sold)
print(total_sold.text)