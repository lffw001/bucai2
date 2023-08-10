import datetime
import json, os
import requests, time
from notify import send
from sendNotify import gg
# by：不才，2023/8/10
# 兑换id，根据需求填入wxchangeid中，默认兑换1.88，一周兑换一次,实现签到兑换，领取还没完成
# 环境变量cshck,0 10,18 * * *
#  '647894196522340352'  // 188积分 1.08元
#  '622187839353806848'  // 288积分 1.88元
#  '622187928306601984'  // 588积分 3.88元
#  '622188100122075136'  // 888积分 5.88元
#入口：#小程序://好奇车生活/Y0ftkJgc3rvc2UB
# 好奇车生活小程序抓包https://channel.cheryfs.cn/域名中的accountId#wxappid，多号用&连接
#v1.0
name = "好奇车生活签到兑换"
exchangeid = '647894196522340352'  # 默认兑换1.08

#通知pushplush
token = ""
user = ""


gg = requests.request("GET", "https://ghproxy.com/https://raw.githubusercontent.com/241793/bucai2/main/gg")
if gg.status_code ==200:
    print(gg.text)
    xx0 =(gg.text)#line:2
else:
    print("不才提醒您网路连接超时")
    xx0 =("不才提醒您网路连接超时")#line:2

cshck =os .getenv ("cshck")#line:3
ck =cshck .split ("&")#line:4
b =0 #line:5
if exchangeid =='622187839353806848':#line:6
    jf ='288'#line:7
    money ="1.88"#line:8
elif exchangeid =='647894196522340352':#line:9
    jf ='188'#line:10
    money ="1.08"#line:11
elif exchangeid =='622187928306601984':#line:12
    jf ='588'#line:13
    money ="3.88"#line:14
elif exchangeid =='622188100122075136':#line:15
    jf ='588'#line:16
    money ="5.88"#line:17
def pushplus (OOOO0O0O0O000O0OO ,O0OO000000O000O00 ):#line:18
    OOO0O0OO00OOOO0OO ='好奇车生活: '#line:19
    OOO000O0OO000OO0O ='http://www.pushplus.plus/send'#line:20
    OOOOO000OO0OOO0O0 ={'token':O0OO000000O000O00 ,'title':OOO0O0OO00OOOO0OO ,'user':user ,'content':OOOO0O0O0O000O0OO }#line:26
    O00O0OOOOOO000O00 =requests .post (OOO000O0OO000OO0O ,data =OOOOO000OO0OOO0O0 ).json ()#line:27
    try :#line:29
        O0O0000OO0OO0O000 ='推送成功！'if O00O0OOOOOO000O00 ['code']==200 else O00O0OOOOOO000O00 ['msg']#line:30
        print (O0O0000OO0OO0O000 )#line:31
    except :#line:32
        print ('推送异常！')#line:33
for b in range (len (ck )):#line:34
    id =ck [b ]#line:35
    ck1 =id .split ("#")#line:36
    acid =ck1 [0 ]#line:37
    apid =ck1 [1 ]#line:38
    url ="https://channel.cheryfs.cn/archer/activity-api/pointsmall/exchangeCard?pointsMallCardId="+exchangeid +"&exchangeCount=1&mallOrderInputVoStr=%7B%22person%22:%22%22,%22phone%22:%22%22,%22province%22:%22%22,%22city%22:%22%22,%22area%22:%22%22,%22address%22:%22%22,%22remark%22:%22%22%7D&channel=1&exchangeType=0&exchangeNeedPoints="+jf +"&exchangeNeedMoney=0&cardGoodsItemIds="#line:39
    url1 ="https://channel.cheryfs.cn/archer/activity-api/signinact/signin"#line:40
    url2 ="https://channel.cheryfs.cn/archer/activity-api/common/accountPointLeft?pointId=620415610219683840&showExpire=true&timeType=day&indexDay="#line:41
    payload =''#line:43
    headers ={'Host':'channel.cheryfs.cn','Connection':'keep-alive','wxappid':apid ,'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat','tenantId':'619669306447261696','activityId':'621950054462152705','requestUrl':'https://channel.cheryfs.cn/archer/act/619669306447261696/619669369294712832/activity/pointsmall-detail/621950054462152705/167LW42SYdAzn0n2?pageId=page1607309582231&num=1&cardId=622187839353806848&anchorId=&anchorAnimateType=','Accept':'application/json, text/plain, */*','timestamp':str (round (time .time ()*1000 )),'assemblyName':'%E7%A7%AF%E5%88%86%E5%95%86%E5%9F%8E%E5%85%91%E6%8D%A22','sign':'88975a8b7ff1023448012adb664f15bc','accountId':acid ,'Sec-Fetch-Site':'same-origin','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':'https://channel.cheryfs.cn/archer/act/619669306447261696/619669369294712832/activity/pointsmall-detail/621950054462152705/167LW42SYdAzn0n2?pageId=page1607309582231&num=1&cardId=622187839353806848&anchorId=&anchorAnimateType=','Accept-Encoding':'gzip, deflate, br','Accept-Language':'en-us,en',}#line:64
    headers1 ={'Host':'channel.cheryfs.cn','wxappid':apid ,'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat','tenantId':'619669306447261696','activityId':'620810406813786113','Accept':'application/json,text/plain, */*','accountId':acid }#line:75
    headers2 ={'Host':'channel.cheryfs.cn','wxappid':apid ,'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat','tenantId':'619669306447261696','activityId':'621883730893492225','Accept':'application/json,text/plain, */*','accountId':acid }#line:84
    response2 =requests .request ("GET",url2 ,headers =headers2 ,data =payload )#line:86
    if response2 .status_code ==200 :#line:87
        zjf =json .loads (response2 .text )#line:88
        zjf1 =zjf .get ("result")#line:89
        print ("不才提醒您,当前运行'好奇车生活'\n账号"+str (b +1 )+"当前积分为：",zjf1 )#line:90
        xx1 =f"不才提醒您,当前运行'好奇车生活'\n账号{str(b + 1)} 当前积分为：{zjf1}"#line:91
    if 10 <=datetime .datetime .now ().hour <=22 :#line:93
        response1 =requests .request ("GET",url1 ,headers =headers1 ,data =payload )#line:94
        if response1 .status_code ==200 :#line:95
            qd =json .loads (response1 .text )#line:96
            qd1 =qd .get ("result")#line:97
            if qd1 ==None :#line:98
                print ("账号"+str (b +1 )+"数据错误或者失效")#line:99
                xx2 =f"账号{str(b + 1)} 数据错误或者失效"#line:100
            else :#line:101
                qd2 =qd1 .get ("message")#line:102
                qd3 =qd .get ("amount")#line:103
                if qd2 =="今日已签到":#line:104
                    print ("账号"+str (b +1 )+"❌签到失败，原因："+qd2 )#line:105
                    xx2 =f"账号{str(b + 1)}❌签到失败，原因：{qd2}"#line:106
                else :#line:107
                    print ("账号"+str (b +1 )+"✅签到成功")#line:108
                    xx2 =f"账号{str(b + 1)} ✅签到成功"#line:109
        else :#line:110
            print ("账号"+str (b +1 )+"❌签到异常")#line:111
            xx2 =f"账号{str(b + 1)}❌签到异常"#line:112
    else :#line:113
        print ("请于10-22点间签到,当前时间:",str (datetime .datetime .now ().hour )+':'+str (datetime .datetime .now ().minute ))#line:114
    if 18 <=datetime .datetime .now ().hour <22 :#line:115
        for c in range (10 ):#line:116
            response =requests .request ("GET",url ,headers =headers ,data =payload )#line:117
            if response .status_code ==200 :#line:118
                dh =json .loads (response .text )#line:119
                dh1 =dh .get ("result")#line:120
                if qd1 ==None :#line:121
                    print ("账号"+str (b +1 )+"数据错误或者失效")#line:122
                    xx3 =f"账号{str(b + 1)}数据错误或者失效"#line:123
                    break #line:124
                elif dh1 !=None :#line:125
                    dh2 =dh1 .get ("errMsg")#line:126
                    print ("账号"+str (b +1 )+"开始兑换"+money +':'+dh2 ,"可能已经兑换成功或者兑换过了，去礼包康康吧")#line:128
                    xx3 =f"账号{str(b + 1)}开始兑换{money}:{dh2}, 可能已经兑换成功了，去礼包康康吧"#line:129
                    break #line:130
                else :#line:131
                    print ("积分不足或者超过兑换次数")#line:132
                    xx3 ="积分不足或者超过兑换次数"#line:133
    else :#line:135
        print ("账号"+str (b +1 )+"未到兑换时间,当前时间:",str (datetime .datetime .now ().hour )+':'+str (datetime .datetime .now ().minute ))#line:136
        xx3 =f"账号{str(b + 1)}未到兑换时间,当前时间:, {str(datetime.datetime.now().hour)}:{str(datetime.datetime.now().minute)}"#line:137
    url3 ="https://channel.cheryfs.cn/archer/activity-api/cardpacket/useCard?cardItemId=676863241435131905&payRemind=&channel=1"#line:139
pushplus (f"{xx0}\n{xx1}\n{xx2}\n{xx3}",token )
