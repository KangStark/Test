import urllib.parse

testurl='http://www.b aidu.com:8443/index.html?userid=kkk&acs=sssS-_~+*%7E'

print(urllib.parse.quote(testurl,safe = ''))

str2 = urllib.parse.quote_plus(testurl,safe = '')
print (str2)
