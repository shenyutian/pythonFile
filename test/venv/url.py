import urllib.request
import re
def getlistsyt(url):

    urls = urllib.request.urlopen(url).read()
    urls = str(urls)
    pate = '(http?://[^\s)";]+\.(\w|/)*)'
    link = re.compile(pate).findall(urls)
    print (urls)
    return link

url = 'http://www.janpn.com/book/shenjilongwei.html'
lists = getlistsyt(url)
for link in lists:
    print(link)