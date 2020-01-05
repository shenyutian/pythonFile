import requests
from bs4 import BeautifulSoup
import csv


# num 记录序号
url_head = "https://search.51job.com/list/050000,000000,0000,00,9,99,"
url_content = ",2,"
url_tail = ".html"
Num = 0
Filename = "boss.csv"
category = ['java', '大数据', 'web']


def write_csv(msg_list):
    """写入数据"""
    out = open(Filename, 'a', newline='')
    csv_write = csv.writer(out, dialect='excel')
    # 数据写入
    for msg in msg_list:
        csv_write.writerow(msg)
    out.close()


def get_pages_urls():
    """爬取所有的网页"""
    urls = []
    for i, cate in range(1, 14), category:
        urls.append(url_head + cate + url_content + str(i) + url_tail)
    return urls


def acc_page_msg(page_url):
    web_data = requests.get(page_url).content.decode('gbk')
    soup = BeautifulSoup(web_data, 'html.parser')
    print(soup)


def run():
    """这是开始程序"""
    print("开始爬虫")
    # 创建csv表
    # out = open(Filename, 'a', newline='')
    # csv_write = csv.writer(out, dialect='excel')
    # # 分为3个属性  第一是工作的类别 例如java
    # #  第二 工作名称  第三工资
    # title = ("category", "work", "price")
    # csv_write.writerow(title)
    # out.close()
    urls = get_pages_urls()
    for url in urls:
        try:
            acc_page_msg(url)
        except:
            print("格式出错")


acc_page_msg("https://search.51job.com/list/050000,000000,0000,00,9,99,java,2,2.html")
