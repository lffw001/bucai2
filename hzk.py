import json
import os
from urllib.parse import unquote
import requests,time
''''
@不才
互助康，感觉像杀猪盘，签到换实物，群友保温杯到货，签到3天
https://www.huzhukang.pro/h5/register/712115入口复制到微信或者浏览器打开，需要实名认证和银行卡，可以用社工实名
变量：hzkck,   数据cookie#token，多号用&连接     ,数据在https://www.huzhukang.pro获取
'''''

ck =os .getenv ("hzkck")#line:1
ck0 =ck .split ("&")#line:3
nowtime =str (round (time .time ()*1000 ))#line:4
gg =requests .request ("GET",unquote ("http%3A%2F%2Fgh.qninq.cn%2Fhttps%3A%2F%2Fraw.githubusercontent.com%2F241793%2Fbucai2%2Fmain%2Fgg",'utf-8'))#line:5
print (gg .text )#line:6
for i in range (len (ck0 )):#line:7
   ck1 =ck0 [i ]#line:8
   ck2 =ck1 .split ("#")#line:9
   token =ck2 [1 ]#line:10
   cookie =ck2 [0 ]#line:11
   url ="https://www.huzhukang.pro/api/?c=Gift&a=signAct"#line:12
   url1 ="https://www.huzhukang.pro/api/?c=User&a=index"#line:13
   payload =""#line:14
   headers ={'Connection':'keep-alive','Content-Length':'0','Accept':'application/json, text/plain, */*','Origin':'https://www.huzhukang.pro','X-Requested-With':'XMLHttpRequest','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63040026)','Token':token ,'Content-Type':'application/x-www-form-urlencoded;charset=utf-8','Cookie':cookie ,'Sec-Fetch-Site':'same-origin','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':'https://www.huzhukang.pro/h5/gift/sign','Accept-Encoding':'gzip, deflate, br','Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',}#line:32
   print (f"----------互助康账号{i+1}运行中----------\n")#line:33
   response1 =requests .request ("POST",url1 ,headers =headers ,data =payload )#line:34
   if response1 .status_code ==200 :#line:35
      yh =json .loads (response1 .text )#line:36
      yh1 =yh .get ("code")#line:37
      yh2 =yh .get ("msg")#line:38
      yh3 =yh .get ("data")#line:39
      if yh1 ==1 and yh2 =="ok"and yh3 !=None :#line:40
         yh4 =yh3 .get ('user').get ("account_flag")#line:41
         yh5 =yh3 .get ("wallet5").get ("balance")#line:42
         print (f"用户:{yh4}  总积分:{yh5}")#line:43
      else :#line:44
         print ("未知错误")#line:45
   else :#line:46
      print ("数据出错")#line:47
   response =requests .request ("POST",url ,headers =headers ,data =payload )#line:50
   if response .status_code ==200 :#line:51
      qd =json .loads (response .text )#line:52
      qd1 =qd .get ("code")#line:53
      qd2 =qd .get ("msg")#line:54
      qd3 =qd .get ("data")#line:55
      if qd1 ==1 and qd2 =="签到成功":#line:56
         print (f"{qd2}获得{qd3.get('money')}")#line:57
      elif qd1 ==-1 :#line:58
         print (qd2 )#line:59
      else :#line:60
         print ("数据出错")#line:61
   else :#line:62
      print ("数据出错")
