import urllib.request
import urllib.parse
import http.cookiejar

url = "http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=Lb7C7"
postdata = urllib.parse.urlencode({
    "username": "vanpersea",
    "password": "123456123"
}).encode('utf-8')
req = urllib.request.Request(url, postdata)
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) '
                             'Gecko/20100101 Firefox/57.0')
cjar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
urllib.request.install_opener(opener)
data = urllib.request.urlopen(req).read()
fhandle = open("D:\Python程序\open\\3.html", "wb")
fhandle.write(data)
fhandle.close()
url2 = "http://bbs.chinaunix.net/"
req2 = urllib.request.Request(url2, postdata)
req2.add_header('User-Agent', 'Mozilla/5.0 '
                              '(Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0')
data2 = urllib.request.urlopen(req2).read()
fhandle = open("D:\Python程序\open\\4.html", "wb")
fhandle.write(data2)
fhandle.close()
