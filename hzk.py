import json
import os
from urllib.parse import unquote
import requests,time
#@不才
#互助康，感觉像杀猪盘，签到换实物，听群友说会发货
#https://www.huzhukang.pro/h5/register/712115入口复制到微信打开，需要实名认证和银行卡，可以用社工实名
#变量：hzkck,   数据cookie#token，多号用&连接     ,数据在https://www.huzhukang.pro获取


ck =os .getenv ("hzkck")#line:2
ck0 =ck .split ("&")#line:4
nowtime =str (round (time .time ()*1000 ))#line:5
gg =requests .request ("GET",unquote ("http%3A%2F%2Fgh.qninq.cn%2Fhttps%3A%2F%2Fraw.githubusercontent.com%2F241793%2Fbucai2%2Fmain%2Fgg",'utf-8'))#line:6
print (gg .text )#line:7
for i in range (len (ck0 )):#line:8
   ck1 =ck0 [i ]#line:9
   ck2 =ck1 .split ("#")#line:10
   token =ck2 [1 ]#line:11
   cookie =ck2 [0 ]#line:12
   url ="https://www.huzhukang.pro/api/?c=Gift&a=signAct"#line:13
   url1 ="https://www.huzhukang.pro/api/?c=User&a=index"#line:14
   payload =""#line:15
   headers ={'Connection':'keep-alive','Content-Length':'0','Accept':'application/json, text/plain, */*','Origin':'https://www.huzhukang.pro','X-Requested-With':'XMLHttpRequest','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63040026)','Token':token ,'Content-Type':'application/x-www-form-urlencoded;charset=utf-8','Cookie':cookie ,'Sec-Fetch-Site':'same-origin','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':'https://www.huzhukang.pro/h5/gift/sign','Accept-Encoding':'gzip, deflate, br','Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',}#line:33
   print (f"----------互助康账号{i+1}运行中----------\n")#line:34
   response1 =requests .request ("POST",url1 ,headers =headers ,data =payload )#line:35
   if response1 .status_code ==200 :#line:36
      yh =json .loads (response1 .text )#line:37
      yh1 =yh .get ("code")#line:38
      yh2 =yh .get ("msg")#line:39
      yh3 =yh .get ("data")#line:40
      if yh1 ==1 and yh2 =="ok"and yh3 !=None :#line:41
         yh4 =yh3 .get ('user').get ("account_flag")#line:42
         yh5 =yh3 .get ("wallet5").get ("balance")#line:43
         print (f"用户:{yh4}  总积分:{yh5}")#line:44
      else :#line:45
         print ("未知错误")#line:46
   else :#line:47
      print ("数据出错")#line:48
   response =requests .request ("POST",url ,headers =headers ,data =payload )#line:51
   if response .status_code ==200 :#line:52
      qd =json .loads (response .text )#line:53
      qd1 =qd .get ("code")#line:54
      qd2 =qd .get ("msg")#line:55
      qd3 =qd .get ("data")#line:56
      if qd1 ==1 and qd2 =="签到成功":#line:57
         print (f"{qd2}获得{qd3.get('money')}")#line:58
      elif qd1 ==-1 :#line:59
         print (qd2 )#line:60
      else :#line:61
         print ("数据出错")#line:62
   else :#line:63
      print ("数据出错")#line:64
