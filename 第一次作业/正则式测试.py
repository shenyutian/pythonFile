# import re
# str = '[a-zA-z]+://[^\s]*'
# strs = '<a href="http://www.janpn.com/book/173/173131/35550900.html">第1章冰山美人</a>'
# result1 = re.search(str, strs)
# print (result1)

import urllib.request
import re
def getlistsyt(url):
    urls = urllib.request.urlopen(url).read()
    urls = str(urls)
    pate = 'http://www.janpn.com/book/173/173131(.+?\.+html)'
    link = re.compile(pate).findall(urls)
    link = list(set(link))
    return link

url = 'http://www.janpn.com/book/shenjilongwei.html'
lists = getlistsyt(url)
for link in lists:
    print(link)