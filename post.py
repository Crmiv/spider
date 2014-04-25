#!/usr/bin/python
#coding:utf-8
import urllib
import urllib2
import socket

url = 'http://202.144.18.218/main.aspx'
values = {
		'__EVENTTARGET' : "",
		'__EVENTARGUMENT' : "",
		'__LASTFOCUS' : "",
		'__VIEWSTATE' : "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",
		'__EVENTVALIDATION':"/wEWGwKvzJiODwLorceeCQLc1sToBgK50MfoBgKhi6GaBQLdnbOlBgLtuMzrDQLrwqHzBQKX+9a3BAK/yONFArDhhMwNArvghMwNAr/I87wGAqTghMwNApSUsNoIAoOU+OMOAoKU+OMOAoGU+OMOAoCU+OMOAoeU+OMOAoaU+OMOAo+UvJ4CAvrV2qsGAtLCmdMIAtLC1eQCAuzR9tkMAuzRirUFusc96tzLOW0MUd1iz1Asc2zQ7YA==",
		'programId' : "东区",
		'txtyq' : "沁苑东十一舍",
		'txtId' : "6层",
		'Txtroom' : "627",
		'ImageButton1.x' : "58",
		'ImageButton1.y' : "11",
		'TextBox2' : "",
		'TextBox3' : ""
		}
#httpHandler = urllib2.HTTPHandler(debuglevel=1)  
#httpsHandler = urllib2.HTTPSHandler(debuglevel=1)  
#opener = urllib2.build_opener(httpHandler, httpsHandler)  
#urllib2.install_opener(opener)  
data = urllib.urlencode(values)
headers = { 'Host':'202.114.18.218',
			'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:28.0) Gecko/20100101 Firefox/28.0',
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			'Accept-Language':'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
			'Accept-Encoding':'gzip, deflate',
			'Referer':'http://202.114.18.218/main.aspx',
			'Connection':'keep-alive'
		}
req = urllib2.Request(url,data)
print "aaa"
result = urllib2.urlopen(req)
page = result.read()
print page

