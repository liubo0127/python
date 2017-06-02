#import platform
#print platform.python_version()
#
#import sys
#print sy#s.version

#import random
#a = random.randint(0,9)
#value = input("please input a number:")
#if value == a:
#    print "you are right"
#else:
#    print "you are wrong,a = %s" %(a)#

#coding=utf-8
import requests
import re
import urllib2
import HTMLParser

url = 'http://daily.zhihu.com/'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
header = {'User-Agent':user_agent}

def getHtml(url,header):
    value = urllib2.Request(url,headers=header)
    response = urllib2.urlopen(value)
    text = response.read()
    return text

def getUrls(url,html):
    pattern = re.compile('<a href="/story/(.*?)"')
    items = re.findall(pattern,html)
    urls = []
    for item in items:
        urls.append(url+'story/'+item)
    return urls

def getContent(url):
    html = getHtml(url,header)
    pattern = re.compile('<h1 class="headline-title">(.*?)</h1>')
    items = re.findall(pattern,html)
    print '*********************'+items[0]+'*******************'

    pattern = re.compile('<div class="content">\\n<p>(.*?)</div>',re.S)
    items1 = re.findall(pattern,html)
    for item in items1:
        print item


html = getHtml(url,header)
urls = getUrls(url,html)
for url in urls:
    try:
        getContent(url)
    except Exception,e:
        pass
