# -*- coding: utf-8 -*-
"""
Created on Mon Mar 07 13:58:10 2016
@author: tkabelan
"""


from bs4 import BeautifulSoup
import urllib2
import re

url = urllib2.urlopen("http://www.publications.parliament.uk/pa/bills/lbill/2015-2016/0056/en/16056en01.htm")
content = url.read()
soup = BeautifulSoup(content, 'html.parser')

#print(soup.prettify())

#print soup.title
for link in soup.find_all('a'):
    print(link.get('href'))
    
print(soup.get_text())
#for a in soup.findAll('a',href=True):
#    if re.findall('python', a['href']):
#        print "Found the URL:", a['href']