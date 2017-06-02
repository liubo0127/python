#coding=utf-8
#i=1
#if i:
#    print "True"
#else:
#    print "False"

#a = 1
#b = 2
#c = 3
#value = a + \
#        b + \
#        c
#print value

#value=input("please enter a number:\n")
##print "value=" + value
#if value >= 80:
#    print "grade is A"
#elif value >= 60:
#    print "grade is B"
#else:
#    print "not pass"


#a, b, c = 1, "abc", 5.20
#print a,b,c

#count = 1
#number = 0
#while count < 10:
#    number = number + count
#    count += 1
#print number


#str = input("please input:");
#print "你输入的内容是：",str;

#F = open('/Users/liubo/Documents/tidb/text','r');
#value = F.read();
#print type(value);
#print value

#try:
#    input = raw_input
#except:
#    pass#


#import json
#F = open('/Users/liubo/Documents/tidb/text','r')
#value = F.read()
#F.close()
#d = json.loads(value)
#print d['rows'][1]['panels'][1]
#for x in d:
#    print "%s:%s" %(x,d[x])

#import json
#with open('/Users/liubo/Documents/tidb/text','r') as f:
#    data = json.load(f)
#
##for key in data.keys():
##        print "%s:%s" %(key,data[key])
#aaa = data['rows']
#print aaa[0]['panels'][0]['targets'][0]['expr']#
#print aaa[0]['panels'][0]['targets'][1]['expr']
#for bbb in aaa[0]['panels']
#    print bbb['title']
#    print bbb['targets']

#import urllib2#
#request = urllib2.Request('http://www.baidu.com')
#data = urllib2.urlopen(request)
#print data.read()
#

#import urllib2
#import urllib
#login #= {'username':'2508775134@qq.com','password':'liubo0127*/'}
#data = urllib.urlencode(login)
#user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
#headers = {'User-Agent':user_agent}
##url = 'https://passport.csdn.net/account/login?from=http%3A%2F%2Fmy.csdn.net%2Fmy%2Fmycsdn'
#url = 'http://blog.csdn.net/cqcre'
#request = urllib2.Request(url,data,headers)
#response = urllib2.urlopen(request)
#print response.read()

#import urllib
#import urllib2
#
#login = {'username':'2508775134@qq.com','password':'liubo0127*/'}
#data = urllib.urlencode(login)
#url = 'http://passport.csdn.net/account/login'
#geturl = url + '?' + data
#print geturl
#request = urllib2.Request(geturl)
#response = urllib2.urlopen(request)
#print respo#nse.read()

#import urllib2
#user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
#headers = {'User-Agent':user_agent}
#
#req = urllib2.Request('http://blog.csdn.net/cqcre','',headers)
#response = urllib2.urlopen(req)
#print response.read()


#try:
#    urllib2.urlopen(req)
#except urllib2.HTTPError, e:
#    print e.code
#    print e.reason##


#import urllib2
#import cookielib
#cookie = cookielib.CookieJar()
#handler = urllib2.HTTPCookieProcessor(cookie)
#opener = urllib2.build_opener(handler)
#response = opener.open('http://www.baidu.com')
#for item in cookie:
#    print item
#for item in cookie:
#    print 'Name = ' + item.name
#    print 'Value = ' + item.value

#import urllib2
#import cookielib
##声明一个CookieJar对象实例来保存cookie
#cookie = cookielib.CookieJar()
##利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
#handler = urllib2.HTTPCookieProcessor(cookie)
##通过handler来构建opener
#opener = urllib2.build_opener(handler)
##此处的open方法同urllib2的urlopen方法，也可以传入request
#response = opener.open('http://www.baidu.com')#
#for item in cookie:
##    print 'Name = '+item.name
##    print 'Value = '+item.value
#    print item


#src = dict(
#    dashboards={"node": 'node.json',
#                "pd"  : 'pd.json',
#                "tidb": 'tidb.json',
#                "tikv": 'tikv.json'})
#print src['dashboards']['node']

import re
#a = '<p><strong>为什么偏偏是拉面</strong></p>'
a = '<p><strong><strong>为什么偏偏是拉面</strong></strong></p>'
#b = re.sub('<[^>]+>','',a)
b = re.sub('(<strong>)+(.*?)(</strong>)+',r'\2',a)
print b