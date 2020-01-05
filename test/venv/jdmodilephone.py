import re
import urllib.request

# craw 真正实现的函数
def craw(url,page):
    html1 = urllib.request.urlopen(url).read()
    html1 = str(html1)
    pat1 = '<div id="plist".+? <div class="page clearfix">'
    result1 = re.compile(pat1).findall(html1)
    result1 = result1[0]
    pat2 = '<img width="220" height="220" data-img="1" \S+="//(.+?\.jpg)">'
    imagelist = re.compile(pat2).findall(result1)
    pat3 = '<em>\s+[\u4e00-\u9fa5]{2,5}\S{2,10}'
    imagelist2 = re.compile(pat3).findall(result1)
    x = 1
    for imageurl in imagelist:
        imagename = "F:/student/Python_file/jd_phone/"+str(page)+"页"+str(x)+".jpg"
        imageurl = "http://"+imageurl
        try:
            urllib.request.urlretrieve(imageurl, filename=imagename)
        except urllib.error.URLError as e:
            if hasattr(e,"code"):
                # print("错误："+str(x))
                x+=1
            if hasattr(e,"reason"):
                # print("错误：" + str(x))
                x+=1
        x+=1
for i in range(1,2):
    url = "https://list.jd.com/list.html?cat=9987,653,655&page="+str(i);
    craw(url,i)