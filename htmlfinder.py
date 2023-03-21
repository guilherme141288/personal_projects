
import sqlite3
import urllib.error
import ssl
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.request import urlopen
from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE





starturl = input(urlopen('Enter web url or enter: ' , context=ctx) )
html = starturl.read()

#if starturl.getcode() == 200 :
if ( html.endswith('.htm') or starturl.endswith('.html') ) :
    pos = html.rfind('/')
    web = html[:pos]
    print(html)

webs = list()
for row in web:
    row.append(str(row[0]))

url = web

print (webs)

document = urlopen(url, context=ctx)

html = starturl.read()

if starturl.getcode() == 200 :
    print('('+str(len(html))+')', end=' ')

soup = BeautifulSoup(html, "html.parser")