#coding=utf-8
import requests
import urllib2
import re
import imghdr

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
header = {'User-Agent':user_agent}

def getImage():
    value = raw_input("请输入关键字：")
    url = 'https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%B1%A9%C2%FE%B1%ED%C7%E9&fr=ala&ori_query=' + value + '&pos=0&hs=2&xthttps=111111'
    html = requests.get(url,headers=header,timeout=2).text
    urllist = re.findall('"objURL":"(.*?)"',html,re.S)
    x = 0
    print "搜索关键字:" + value + ",开始下载图片......"
    for imgurl in urllist:
        print imgurl
        try:
            pic = requests.get(imgurl,timeout=2)
        except requests.ConnectionError:
            print '【错误】当前图片无法下载'
            continue
        request = urllib2.Request(imgurl,headers=header)
        response = urllib2.urlopen(request)
        imginfo = response.read()
        type = imghdr.what('',imginfo)
        string = "/Users/liubo/workspace/image/picture"+str(x)+"."+type
        with open(string,'wb') as image:
            image.write(pic.content)
        x += 1
if __name__ == "__main__":
    getImage()