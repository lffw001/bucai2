import json
import os
import time
from urllib.parse import quote,unquote
#乐乐看pro提现，变量名:lelekck，需要抓包apillk.cengaw.cn/请求头里面的device#Authorization，（Authorization只需要Bearer后面的部分）
import requests
money = "5"#提现金额，默认5
num = 3#循环次数，有时会提示太快



Auth0 =os .getenv ("llkck")#line:1
ck =Auth0 .split ("#")#line:2
device =ck [0 ]#line:3
Auth =ck [1 ]#line:4
time1 =str (round (time .time ())*1000 )#line:5
url ="https://apillkpro.cengaw.cn/api/v2/cash/exchange"#line:6
gg =requests .request ("GET",unquote ("http%3A%2F%2Fgh.qninq.cn%2Fhttps%3A%2F%2Fraw.githubusercontent.com%2F241793%2Fbucai2%2Fmain%2Fgg",'utf-8'))#line:7
print (gg .text )#line:8
print ('\n开始提现'+str (money ))#line:9
payload ='gate=wechat&amount='+money +'&lat=&lng=&root=0&sim=1&debug=1&model=V2055A&power=0&vpn=0'#line:10
headers ={'accept':'application/json','device':device ,'oaid':device ,'store':'website','version':'108','platform':'1','Authorization':"Bearer "+Auth ,'Content-Type':'application/x-www-form-urlencoded','User-Agent':'Dalvik/2.1.0 (Linux; U; Android 12; V2055A Build/TP1A.220624.014)','Host':'apillkpro.cengaw.cn','Connection':'Keep-Alive','Accept-Encoding':'gzip','Content-Length':'79',}#line:26
for i in range (num ):#line:28
   response =requests .request ("POST",url ,headers =headers ,data =payload )#line:29
   if response .status_code ==200 :#line:30
      qg =json .loads (response .text )#line:31
      qg1 =qg .get ("message")#line:32
      qg2 =qg .get ("result")#line:33
      if qg .get ("success")==True and qg !=None :#line:34
        qg3 =qg2 .get ("title")#line:35
        qg4 =qg2 .get ("message")#line:36
        print (f"{qg2}\n{qg4}")#line:37
        time .sleep (2 )#line:38
      else :#line:39
        print (qg1 )#line:40
   else :#line:41
      print (response .json ())#line:42
      break 










