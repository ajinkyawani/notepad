import xml.etree.ElementTree as ET

tree = ET.parse("cd_catalog.xml")

# this element holds the phonebook entries
"""container = tree.getroot()

data = []
for elem in container:
    key = elem.findtext("PRICE")
    print(key)
    print(elem)
    data.append(key)

print(data)"""


root = tree.getroot()

data = []
for child in root:
    for item in child:
        if item.tag == "COUNTRY":
            print(item.text)
            data.append((item.tag, item.text))

data.sort()

print("Sorted  ", data)
# insert the last item from each tuple
