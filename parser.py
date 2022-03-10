import xml.etree.ElementTree as ET
import glob
# List of arguments, Finds every file with .xml
path = "./xmls/"
countries = glob.glob(path + '*.xml',)
# Sets .txt file
contents = open(f'FIFA10 South America.txt', 'w', encoding="utf-8")
# I made a header
contents.write("Here is the list of stadiums in FIFA 10 collection:\n")

# Gets stadium names :D
for i in countries:
  # Parse XML files
  tree = ET.parse('{}'.format(i))
  # Gets root
  root = tree.getroot() 
  # Gets the child root
  for child in root:
    # Gets the grandchild root
    for grandchild in child.iter('name'):
      x = grandchild.text + "\n"
      contents.write(x)
