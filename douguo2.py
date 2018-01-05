import urllib
import urllib2
import re
 
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

page = 1
url = 'http://www.douguo.com/article/10' + str(page)  
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    html = response.read().decode('utf-8')
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason

'''
xiaobiaoti_pattern = re.compile('<h3>.*?<a.*?>(.*?)</a>.*?</h3>', re.S)
xiaobiaoti_list = re.findall(xiaobiaoti_pattern, html)
for item in xiaobiaoti_list:
    print item

zuozhe_pattern = re.compile('<span class="pbs pts">.*?<a.*?>(.*?)</a>', re.S)
zuozhe_list = re.findall(zuozhe_pattern, html)
for item in zuozhe_list:
    print item

fabiao_pattern = re.compile('<span class="pbs pts">.*?</a>(.*?)</span>', re.S)
fabiao_list = re.findall(fabiao_pattern, html)
for item in fabiao_list:
    print item

chakan_pattern = re.compile('<div class="jiep">.*?<a.*?>(.*?)</a>', re.S)
chakan_list = re.findall(chakan_pattern, html)
for item in chakan_list:
    print item

xiaobai_pattern = re.compile('<div class="jimp">.*?<span class="prm">.*?<a.*?>(.*?)</a>', re.S)
xiaobai_list = re.findall(xiaobai_pattern, html)
for item in xiaobai_list:
    print item
'''



all_pattern = re.compile('<h3>.*?<a.*?>(.*?)</a>.*?</h3>.*?<span class="pbs pts">.*?<a.*?>(.*?)</a>.*?<span class="pbs pts">.*?</a>(.*?)</span>.*?<div class="jiep">.*?<a.*?>(.*?)</a>.*?<div class="jimp">.*?<span class="prm">.*?<a.*?>(.*?)</a>',re.S)
all_list = re.findall(all_pattern, html)
for item in all_list:
    print "xiaobiaoti:" + item[0]
    print "name:" + item[1]
    print "title:" + item[2]
    print "content:" + item[3].strip()
    print "good:" + item[4]
    print "-----------------"

    input = raw_input()
    if input == "":
        print "nextPage:"
        continue
    elif input =="Q":
        break

