import urllib
import urllib.request
import re
print ("hello")
response = urllib.request.urlopen('https://so.gushiwen.org/shiwenv_658935680f61.aspx')
txt = response.read()
findword = u"(子+)"
