import json
import os
from sendNotify import gg
import requests,datetime

#by：不才，25-15整合
#1.2优化通知，修复因为404报错停止运行,整合两场时间，定时:57 29,59 10,14 * * *
#25-15,10:30  419967B3A4064140BA78E6A046DF0FC1
#25-15 15:30  687D57731F804A2CAE1F455331F83524
#美团的token=xxx
#提示时间验证失败是正常的，
ck= os.getenv("mtck")

num = 20
#抢购次数,抢之前测试一下，提示时间验证失败才设置50，提示抢完的进去一下活动页面即可
#定时建议提前几秒

#下面的自己抓
mtgsig = ''
mtFingerprint = ""

#不要通知的不用管这个
notice = 0#开启通知
token = ''#pushplus的token




time =datetime .datetime .now ()#line:2
if time .hour <11 and time .minute <55 :#line:3
    couponReferId ='419967B3A4064140BA78E6A046DF0FC1'#line:4
    print ("10:30场开始")#line:5
elif 12 <=time .hour <16 and time .minute <30 :#line:6
    couponReferId ='687D57731F804A2CAE1F455331F83524'#line:7
    print ("15:00场开始")#line:8
else :#line:9
    print ("时间未到，报错正常：可于10:55前或14:30后运行,NOW",datetime .datetime .now ())#line:10
name ='美团18-18抢购'#line:11
v ="1.2"#line:12
url0 ="https://promotion.waimai.meituan.com/lottery/limitcouponcomponent/info?couponReferIds="+couponReferId +"&actualLng=0&actualLat=0&geoType=2"#line:14
payload0 ={}#line:15
headers0 ={'Host':'promotion.waimai.meituan.com','Connection':'keep-alive','Accept':'application/json, text/plain, */*','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat','Sec-Fetch-Site':'same-site','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':'https://market.waimai.meituan.com/','Accept-Language':'en-us,en',"Cookie":ck ,}#line:27
headers ={'Accept':'application/json, text/plain, */*','Accept-Language':'zh-CN,zh;q=0.9,ru;q=0.8','Connection':'keep-alive','Content-Type':'application/json','Cookie':ck ,'Origin':'https://market.waimai.meituan.com','Referer':'https://market.waimai.meituan.com/','Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors','Sec-Fetch-Site':'same-site','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat','mtgsig':mtgsig ,'sec-ch-ua':'"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"',}#line:44
params ={'couponReferId':couponReferId ,'actualLng':'113.551454','actualLat':'23.32507','geoType':'2','gdPageId':'379391','pageId':'378925','version':'1','utmSource':'70200','utmCampaign':'wmsq-678762','instanceId':'16619982800580.30892480633143027','componentId':'16619982800580.30892480633143027',}#line:58
json_data ={'cType':'wm_wxapp','fpPlatform':1 ,'wxOpenId':'','appVersion':'','mtFingerprint':mtFingerprint }#line:66
def pushplus (O0OOOOO0O000OOOO0 ,O000O000O0OOO0000 ):#line:69
   O0OOOO000O00OO0O0 ='美团抢购通知: '#line:70
   OOOO00OOO00000000 ='http://www.pushplus.plus/send'#line:71
   OO000OO00OOO0OOOO ={'token':O000O000O0OOO0000 ,'title':O0OOOO000O00OO0O0 ,'content':O0OOOOO0O000OOOO0 }#line:76
   OOOO00O0OOO00O000 =requests .post (OOOO00OOO00000000 ,data =OO000OO00OOO0OOOO ).json ()#line:77
   try :#line:79
      OOOOO00O0O000OO00 ='推送成功！'if OOOO00O0OOO00O000 ['code']==200 else OOOO00O0OOO00O000 ['msg']#line:80
      print (OOOOO00O0O000OO00 )#line:81
   except :#line:82
      print ('推送异常！')#line:83
tip ="不才提醒您:"#line:87
response0 =requests .request ("GET",url0 ,headers =headers0 ,data =payload0 )#line:88
sx =json .loads (response0 .text )#line:89
sx1 =sx .get ("msg")#line:90
print ("刷新:"+sx1 )#line:92
i =0 #line:93
while i <num :#line:94
    response =requests .post ('https://promotion.waimai.meituan.com/lottery/limitcouponcomponent/fetchcoupon',params =params ,headers =headers ,json =json_data ,)#line:100
    if response .status_code ==200 :#line:103
        data =json .loads (response .text )#line:104
        msg =data .get ("msg")#line:105
        data1 =data .get ("data")#line:106
        if data1 !=None :#line:107
            data2 =data1 .get ("couponName")#line:108
            print (data2 )#line:109
        print (tip +msg ,'NOW',datetime .datetime .now ())#line:110
    else :#line:112
        print ("404")#line:113
    i +=1 #line:114
gg ()#line:115
if notice ==1 :#line:116
    pushplus (gg (),'\n不才提醒您'+msg ,token )#line:117
else :#line:118
    print ("未开启推送")

