import json
import os
import time
from urllib.parse import quote,unquote
#自己定时在任务脚本前面
#乐乐看pro提现，变量名:lelekck，需要抓包apillk.cengaw.cn/请求头里面的device#Authorization，（Authorization只需要Bearer后面的部分）
import requests
money = "5"#提现金额，默认5
num = 3#循环次数，有时会提示太快







Auth0 =os .getenv ("llkck")#line:1
ck =Auth0 .split ("#")#line:2
device =ck [0 ]#line:3
Auth =ck [1 ]#line:4
time1 =str (round (time .time ())*1000 )#line:5
print (device )#line:6
print (Auth )#line:7
url ="https://apillkpro.cengaw.cn/api/v2/cash/exchange"#line:8
gg =requests .request ("GET",unquote ("http%3A%2F%2Fgh.qninq.cn%2Fhttps%3A%2F%2Fraw.githubusercontent.com%2F241793%2Fbucai2%2Fmain%2Fgg",'utf-8'))#line:9
print (gg .text )#line:10
print ('\n开始提现'+str (money ))#line:11
payload ='gate=wechat&amount='+money +'&lat=&lng=&root=0&sim=1&debug=1&model=V2055A&power=0&vpn=0'#line:12
headers ={'accept':'application/json','device':device ,'oaid':device ,'store':'website','version':'108','platform':'1','Authorization':"Bearer "+Auth ,'Content-Type':'application/x-www-form-urlencoded','User-Agent':'Dalvik/2.1.0 (Linux; U; Android 13; V2055A Build/TP1A.220624.014)','Host':'apillkpro.cengaw.cn','Connection':'Keep-Alive','Accept-Encoding':'gzip','Content-Length':'79',}#line:28
for i in range (num ):#line:30
   response =requests .request ("POST",url ,headers =headers ,data =payload )#line:31
   if response .status_code ==200 :#line:32
      qg =json .loads (response .text )#line:33
      qg1 =qg .get ("message")#line:34
      print (qg1 )#line:35
      time .sleep (2 )#line:36
   else :#line:37
      print (response .json ())#line:38
      break 
