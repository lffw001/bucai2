import json
import os
import time
from urllib.parse import quote,unquote
#1.1
# 乐乐看提现，变量名:lelekck，配合蛋姨的脚本，定时在其前面即可
# 需要抓包apillk.cengaw.cn/请求头里面的device#Authorization，（Authorization只需要Bearer后面的部分）
import requests
ua = ''#改成自己的


money = "5"#提现金额，默认5
num = 3#循环次数，有时会提示太快


Auth0 =os .getenv ("lelekck")#line:2
ck =Auth0 .split ("#")#line:3
device =ck [0 ]#line:4
Auth =ck [1 ]#line:5
time1 =str (round (time .time ())*1000 )#line:6
url ="https://apillk.cengaw.cn/api/v2/cash/exchange"#line:8
gg =requests .request ("GET",unquote ("http%3A%2F%2Fgh.qninq.cn%2Fhttps%3A%2F%2Fraw.githubusercontent.com%2F241793%2Fbucai2%2Fmain%2Fgg",'utf-8'))#line:9
print (gg .text )#line:10
print ('\n开始提现'+str (money ))#line:11
payload ='gate=wechat&amount='+money +'&lat=&lng=&root=0&sim=1&debug=1&model=V2055A&power=0&vpn=0'#line:12
headers ={'accept':'application/json','device':device ,'oaid':device ,'store':'baidu','version':'105','platform':'1','Authorization':"Bearer "+Auth ,'Content-Type':'application/x-www-form-urlencoded','User-Agent':ua,'Host':'apillk.cengaw.cn','Connection':'Keep-Alive','Accept-Encoding':'gzip','Content-Length':'79',}#line:28
for i in range (num ):#line:30
   response =requests .request ("POST",url ,headers =headers ,data =payload )#line:31
   if response .status_code ==200 :#line:32
      qg =json .loads (response .text )#line:33
      qg1 =qg .get ("message")#line:34
      qg2 =qg .get ("result")#line:35
      if qg .get ("success")==True and qg !=None :#line:36
        qg3 =qg2 .get ("title")#line:37
        qg4 =qg2 .get ("message")#line:38
        print (f"{qg2}\n{qg4}")#line:39
        time .sleep (2 )#line:40
      else :#line:41
        print (qg1 )#line:42
   else :#line:43
      print (response .json ())#line:44
      break #line:45










