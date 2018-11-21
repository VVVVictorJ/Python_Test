import re
import urllib.request
import urllib.error
def craw(url,page):
    html1=urllib.request.urlopen(url).read()
    html1=str(html1)
    pat1='<section class="container".+?<aside class="sidebar">'
    result1=re.compile(pat1).findall(html1)
    result1=result1[0]
    pat2='<img src="http://(.:+?\.jpg)">'
    imagelist=re.compile(pat2).findall(result1)
    x=1
    for imageurl in imagelist:
        imagename="D:/Python程序/zhaifuli/"+str(page)+str(x)+".jpg"
        imageurl="http://"+imageurl
        try:
            urllib.request.urlretrieve(imageurl,filename=imagename)
        except urllib.error.URLError as e:
            if hasattr(e,"code"):
                x+=1
            if hasattr(e,"reason"):
                x+=1
        x+=1
for i in range(2,8):
    url="http://yxpjw.club/luyilu/2017/1113/4189_"+str(i)+".html"
    craw(url,i)
