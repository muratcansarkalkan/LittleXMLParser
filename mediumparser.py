# Originally made for Python course of Charles Severance, XML homework. This calculates sum of counts in a XML file. made by me

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Asks service url
serviceurl = input("Enter comments xml")
if len(serviceurl) <= 1:
    serviceurl = 'http://py4e-data.dr-chuck.net/comments_42.xml'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

totsum = 0

# Url is serviceurl
url = serviceurl
print('Retrieving', url)

# Opens url
uh = urllib.request.urlopen(url, context=ctx)

# Reads the url data
data = uh.read()

# Gives total character number
print('Retrieved', len(data), 'characters')
# print(data.decode())
tree = ET.fromstring(data)

# results = tree.findall('comments')
# To print total count of counts
counts = tree.findall('.//count')
print("Count: " + str(len(counts)))

# Finds all values in counts
for child in tree:
    for grandchild in child.iter('count'):
        totsum += int(grandchild.text)

# for i in range(0,len(results)):
#     lat = results[i].find('comment').find('count').text
#     lat = int(lat)
#     sum.append(lat)

# Prints sum
print("Sum: " + str(totsum))