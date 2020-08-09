from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_India'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('td')
for tag in tags:
    scope_attribute=tag.get('scope')
    if scope_attribute=='row':
        anchor_tag=tag.contents[0]
        print(anchor_tag.contents[0])
