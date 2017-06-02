#coding=utf-8
import urllib2
import urllib
import re

url='http://daily.zhihu.com/'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
header = {'User-Agent':user_agent}

def getHtml():
    value = urllib2.Request(url,header)
    response = urllib2.urlopen(value)
    html = response.read()
    return html

def getImg(html):
    reg = re.compile('<img src="(.*?\.jpg)"')
    urllist = re.findall(reg,html)
    x = 0
    for imgurl in urllist:
        urllib.urlretrieve(imgurl,'/Users/liubo/workspace/image/%s.jpg' %x)
        x += 1

html = getHtml()
getImg(html)