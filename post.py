#!/usr/bin/env python
#coding:utf-8
import urllib
import urllib2
import time
import re
from bs4 import BeautifulSoup

#regex
pattern = '((\d{2}|\d{3})\.\d)(</td><td>)(\d){4}-([4]-\d{2})' 
url = "http://202.114.18.218/main.aspx"

class MyOpener(urllib.FancyURLopener):
	version = 'Mozilla/5.0 (X11; Linux x86_64; rv:28.0) Gecko/20100101 Firefox/28.0'


myopener = MyOpener()
f = myopener.open(url)
soup = BeautifulSoup(f)

#parse and retrieve two vital form values
viewstate = soup.select("#__VIEWSTATE")[0]['value']
eventvalidation = soup.select("#__EVENTVALIDATION")[0]['value']
print viewstate

postdata_1 = {
		'__EVENTTARGET' : 'programId',
		'__EVENTARGUMENT' : '',
		'__LASTFOCUS' : '',
		'__VIEWSTATE' : viewstate,
		'__EVENTVALIDATION' : eventvalidation,
		'programId' : '东区',
		'Txtroom' : '',
		'TextBox2' : '',
		'TextBox3' : ''
		}
encodedFields = urllib.urlencode(postdata_1)
f = myopener.open(url,encodedFields)
soup = BeautifulSoup(f)
viewstate = soup.select("#__VIEWSTATE")[0]['value']
eventvalidation = soup.select("#__EVENTVALIDATION")[0]['value']
print viewstate

postdata_2 = {
		'__EVENTTARGET' : 'txtyq',
		'__EVENTARGUMENT' : '',
		'__LASTFOCUS' : '',
		'__VIEWSTATE' : viewstate,
		'__EVENTVALIDATION' : eventvalidation,
		'programId' : '东区',
		'txtyq' : '沁苑东十一舍',
		'Txtroom' : '',
		'TextBox2' : '',
		'TextBox3' : ''
		}
encodedFields = urllib.urlencode(postdata_2)
f = myopener.open(url,encodedFields)
soup = BeautifulSoup(f)
viewstate = soup.select("#__VIEWSTATE")[0]['value']
eventvalidation = soup.select("#__EVENTVALIDATION")[0]['value']

postdata_3 = {
		'__EVENTTARGET' : '',
		'__EVENTARGUMENT' : '',
		'__LASTFOCUS' : '',
		'__VIEWSTATE' : viewstate,
		'__EVENTVALIDATION' : eventvalidation,
		'programId' : '东区',
		'txtyq' : '沁苑东十一舍',
		'txtId' : '6层',
		'Txtroom' : '627',
		'ImageButton1.x' : '58',
		'ImageButton1.y' : '11',
		'TextBox2' : '',
		'TextBox3' : ''
		}
print postdata_3['__VIEWSTATE']
postdata_ = urllib.urlencode(postdata_3)


headers = { 
			'Host': '202.114.18.218',
			'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:28.0) Gecko/20100101 Firefox/28.0',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			'Accept-Language': 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
			'Accept-Encoding': 'gzip, deflate',
			'Referer': 'http://202.114.18.218/main.aspx',
			'Connection': 'keep-alive',
			'X-Forwarded-For' : '192.168.1.109'
		}

req = urllib2.Request(url,postdata_,headers)
result = urllib2.urlopen(req)
text = result.read()
print text
#text_ = re.findall(pattern,text)
#print text_[0][0]
