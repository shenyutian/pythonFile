import urllib.request
import re
# file = urllib.request.urlopen("http://www.baidu.com")
# data = file.read()
# print(data)
# dataline = file.readline()
# print(dataline)

# fhandle = open("F:/student/Python_file/1.html","wb")
# fhandle.write(data)
# fhandle.close()

# filename = urllib.request.urlretrieve("http://127.0.0.1:81/mysql_tools/getcord.php",filename="F:/student/Python_file/2.html")
# print(file.info())
# 
# 状态码
# print(file.getcode())
# print(file.geturl())
# urllib.request.urlcleanup()
# print(urllib.request.quote("http://www.baidu.com"))
# 
# url = "https://blog.csdn.net/weiwei_pig/article/details/51178226"
# headers = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
# opener = urllib.request.build_opener()
# opener.addheaders = [headers]
# data = opener.open(url).read()
# print(data)

# for i in range(1,2):
# 	try:
# 		file=urllib.request.urlopen("https://xiaomi.tmall.com/search.htm?keyword=%D0%A1%C3%D78&orderType=hotkeep_desc")
# 		data=file.read()
# 		print(len(data))
# 	except Exception as e:
# 		print("出现异常"+str(e))
# 		raise
# 	else:
# 		pass
# 	finally:
# 		pass
# 	
# 		
# 			GET方法
# url = "https://s.taobao.com/search?q="
# url_two = "&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306"
# key = "小米"
# key_code = urllib.request.quote(key)
# url_all = url + key_code + url_two
# req = urllib.request.Request(url_all)
# print(url_all)
# data = urllib.request.urlopen(req).read()
# print(data)
# fh = open("F:/student/Python_file/3.html" , "wb")
# fh.write(data)
# fh.close
#       POST方法
# import urllib.parse
# url = "http://www.iqianyue.com/mypost"
# postdata = urllib.parse.urlencode({
# 	"name":"shenyutian",
# 	"pass":"123456"
# 	}).encode('utf-8')
# req = urllib.request.Request(url,postdata)
# data = urllib.request.urlopen(req).read()
# print(data)

# file = urllib.request.urlopen("http://www.baidu.com").read()
# pattern = "img.alicdn.com/\S{1,100}240x240.jpg"
# result1 = re.search(pattern,file)
# print(result1)

num = "123456"
print(tuple(num.split()))
