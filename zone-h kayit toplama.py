#coding:utf-8
import re
import requests
print ("""
####################################################################
#   Coder : Cüneyt Tanrısever                                      #
#   Notifier adinizi giriniz                                       #
#   Ornek Hacker_adi                                               #
#   Kac sayfa cekmek istiyorsaniz o kadar sayi giriniz             #
#   zone-h sayfasina girip firefoxtan cookieleri alip              #
#   sadece cookielerden ZH ve PHPSESSID degerleri alip             #
#   dosya icindeki yerleri bulup ZH= ile PHPSESSID editleyiniz.    #
#################################################################### """)
Hackeradi=input("Hacker adı =  ")
d = input("Kac sayfa zone cekmek istiyorsunuz =  ")
yaz = open("zoneler.txt", "w+")
yaz.close()
ara="/mirror/id/(.*?)\"\>mirror"
zoneler=[]
for i in range(int(d)):
    say1=  i+1
    urlc= "http://zone-h.org/archive/notifier=%s/page=%s" %(Hackeradi,say1)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
    rq=requests.session()
    rq.headers.update(headers)
    cookies= {'ZHE':'7eda371aaa927ceb7b686a1813d0ae7f', 'PHPSESSID':'mbtdq37armftau3cdspte4ngf7'}
    rq = requests.get(urlc, cookies=cookies)
    dex=rq.content.decode('utf-8')
    pattern  = re.compile(ara)
    dex1=re.findall(ara,dex)
    c = "http://www.zone-h.org/mirror/id/"
    for ii in dex1:
        dd= str("http://www.zone-h.org/mirror/id/") + str(ii) 
        c=zoneler.count(dd)

        if c==0:
            zoneler.append(dd)
for  i in zoneler:
    print(i)
    yaz = open("zoneler.txt", "a")
    yaz.write(i+"\n")
    yaz.close()
