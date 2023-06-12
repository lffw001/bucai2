import sendNotify
import requests, time, datetime
import json
from urllib.parse import quote, unquote
from sendNotify import gg
# @不才
# 饿了么社区签到换会员，单号版
# 变量：elmck，多号&或者单独设置elmck（跟京东一样）隔开，定时cron 0 0 10 * * *
#v1.1,需要我发的的依赖
ck = os.getenv("elmck")
token = ""#pushplus的token，不需要通知的可以不填
user = ""#pushplus的用户群组



nowtime = str(round(time.time() * 1000))

def pushplus (OO0OO0OO0OO0O00O0 ,O0OO0O0OO0O0O00OO ):#line:2
    O00000OOOO000O00O ='饿了么社群打卡: '#line:3
    O0O000000OO00O0OO ='http://www.pushplus.plus/send'#line:4
    OOOO00O0OOO00OOOO ={'token':O0OO0O0OO0O0O00OO ,'title':O00000OOOO000O00O ,'user':user ,'content':OO0OO0OO0OO0O00O0 }#line:10
    O00O0OOO0OOO00O00 =requests .post (O0O000000OO00O0OO ,data =OOOO00O0OOO00OOOO ).json ()#line:11
    try :#line:13
        OO000000OO0OOOOO0 ='推送成功！'if O00O0OOO0OOO00O00 ['code']==200 else O00O0OOO0OOO00O00 ['msg']#line:14
        print (OO000000OO0OOOOO0 )#line:15
    except :#line:16
        print ('推送异常！')#line:17
gg =requests .request ("GET",unquote ("http%3A%2F%2Fgh.qninq.cn%2Fhttps%3A%2F%2Fraw.githubusercontent.com%2F241793%2Fbucai2%2Fmain%2Fgg",'utf-8'))#line:19
print (gg())#line:20
print ("单号版")#line:21
url0 ="https://waimai-guide.ele.me/h5/mtop.alsc.wechat.biz.api.community.homepage/1.0/4.0/?jsv=2.4.12&appKey=32529321&t="+nowtime +"&sign=cc554ef10e6f16f1ba68e5e616dc6f68&c=65132fab890611a36ea4c56426be6bc5_1685709597766%3Bde94d00b67ff8d2082f9efeeaf38cfd4&api=mtop.alsc.wechat.biz.api.community.homepage&dataType=json&method=GET&timeout=10000&v=1.0&type=originaljson&ttid=wxece3a9a4c82f58c9%40wechat_ios_10.20.1&accountSite=eleme&data=%7B%22sceneCode%22%3A%22%22%2C%22inviter%22%3A%2299388458%22%2C%22unionId%22%3A%22o_PVDuFVUiMuXa6jZ4cdWpremOXc%22%2C%22communityType%22%3A1%2C%22groupEnvironment%22%3Atrue%2C%22encryptedData%22%3A%22%22%2C%22iv%22%3A%22%22%2C%22code%22%3A%22%22%7D&_bx-m=1"#line:23
payload0 ={}#line:25
headers0 ={'Host':'waimai-guide.ele.me','Connection':'keep-alive','Accept':'application/json','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat','X-UA':'MiniAppVersion/10.20.1 DeviceId/o_PVDuFVUiMuXa6jZ4cdWpremOXc','bx-ua':'303$bZdE95b8sTs8MDsiexRRS/Ez1qtZFtT1I1zFzFMzYs7DGC/EWG8S/lmy7xVK7xEvatk2itmmLFo0t3usT+xYvKNXtfyVb4eaiLMeTMgSIAR7TYqV3dD2lrmYvU8sgmCq+6PoF9YXQd7Ab10uy1+TAXWbI2cg+2h5/YqJFcX7ZQXxu3PmLgRwpciFcnoWbPEheM+zjGmXeDBTiDdMOW7DWR5ptZfDKXkp0lOW+6GoA9mFBSl6Dg5vMbm2elHVa2NXL3u2633yb7SWRyLkexgK2E6//CyJGZt4qh8Jta/Xfcg8A5YYfnzWlVSi2p8bc/T4QVv5QNRWWyIIx+wcAUHm6Xse9S3e2V5G6xLGOWPKtnUEXk0y5yzsXUNgoi/VL1FSIr96iv34L3mqihV0CrpH7e4NEpb7aND2Tce3HmbnxY0aod16crOeI5dndB84v/hN32VPSVX+CbtsDXR6ED7hmItMGKpnJ7h/gXmIK6AzELHEr3od','bx-umidtoken':'S2gAWFvrznqymrKnNNrp-ilU26sxMCmsn-uDNWWg_gvVk08ZG5CG2lyLJzk22ooWb0nofjr-6WkDRnOoHnS54MihKN7ZY2pAaXtHOOQ9nibfgw==','mini-janus':'3%40sK%2FYD1mBDW%2FgQsUtZIbTW1nYjEZL2l0jsXinukFRoD6eT6S26SHLEpBLpcR%3D','x-decode-ua':'false','x-ele-check':'qbks7jvclY8g1AKx9OY4pAuNxblgBCeX59pnG1mvihT2BUW8rNe2DV1GzUFyWVcr4ldbFkFDT51R4iOUsZ+kvwnEE26LqVymaYFklmwAr9L6ftJlG1OpEBzVSj3nKYryp+kcPlTV6GBGHCEmX8z+ImS9+SgmlSlI+M6665Nn+0fUP4AWkAGkwQIVc25+cqdQcxruCn5PhR1hidMODRSe4RN8cgQrgvJZge3qWEdhbQ/YXb0Ovp8TCgqPSmUzYaLeAVIlKNFRdlrICpRmvQBFFAr2mS7hzx/FEeSlBb+HLpRzdBKfTk3uCzjUN3rSXC+LrKROAcm/8twHmwOu7bYqK+CelnPHXrDmqRDHVWIg2D5/k+FHsrvV6XQWYPtNfxmBlKxxo+3VMCBotDCoB47E+GcKohQZOtMQicaFbvnNOYBh8d4S4SfGYBFMLnbL0Gr/WgQR9i4ke2S9TlRJ5mYDpFs156KNwT/gvs2X7d8dFatGDd8LsQJc+56U8TROio8X','x-ele-ua':'RenderWay/miniProgram MiniAppId/wxece3a9a4c82f58c9 MiniAppVersion/10.20.1 DeviceId/o_PVDuFVUiMuXa6jZ4cdWpremOXc AppName/Wechat microsoft/microsoft windows/10 Wechat/3.4.0 channel/wechat_app subChannel/wechat_app.default MicroMessenger/8.0.6','x-secext-city':'21','x-smallstc':'{"loginSucResultAction":"loginResult","st":"tb_s_ele_1ADg6Le-9nIGfIQpspL2mGA","loginType":"snsLogin","open_id":"oQZUI0dAar6UJEJjyqlF_EpvOxao","loginScene":"miniProgramLogin","unb":2209633667417,"resultCode":100,"appEntrance":"weixin","elemeExt":"{}","smartlock":false,"snsType":"weixin_mini_program","sid":"12be3156d10c030cec5acf731cc19408","cookie2":"12be3156d10c030cec5acf731cc19408","munb":2209633667417,"SID":"MTJiZTMxNTZkMTBjMDMwY2VjNWFjZjczMWNjMTk0MDjMFG-U2x_nu2TxBkH-SqbB","bindTag":"existed","loginResult":"success","sgcookie":"M100gXLFvYP5Fr2PcLvry0ZbmxyWQoKIKBAyF7mJsrmbyn8NDS84jY/MTCUTf+a5Iz6vMBvY7EovOaKViS1KUxTf9/CB2ktVude/f4YNmQvy01o=","user_id":"1000127450482","csg":"1564a413","union_id":"o_PVDuFVUiMuXa6jZ4cdWpremOXc","USERID":"1000127450482","UTUSER":"1000127450482"}','x-tap':'wx','x-ticid':'AajHukEBWqrofxIrcnI9ipFGHO5ZzwzX_pkYydYIMcFyxAps43eqgj5F6Nyy6sSzPuAct11CyPuOVYJ-nfsgQ7bd5keq','Referer':'https://servicewechat.com/wxece3a9a4c82f58c9/496/page-frame.html','Cookie':ck ,'content-type':'application/x-www-form-urlencoded'}#line:45
print ("----------账号1开始社群打卡----------\n")#line:46
xx2 ="----------账号1开始社群打卡----------\n"#line:47
response0 =requests .request ("GET",url0 ,headers =headers0 ,data =payload0 )#line:48
if response0 .status_code ==200 :#line:49
    id =json .loads (response0 .text )#line:50
    id1 =id .get ("data")#line:51
    if id1 =={}:#line:53
        id2 =id .get ("ret")#line:54
        print ("账号1",id2 )#line:55
        xx0 ="账号1",id2 #line:56
    elif id1 !=None :#line:57
        id3 =id1 .get ("subType")#line:58
        if id3 =="":#line:59
            print (id .get ("ret"))#line:60
            xx0 =id .get ("ret")#line:61
        else :#line:62
            id1 =id .get ("data").get ("communityInfo").get ("communityName")#line:63
            sqdata =id .get ("data").get ("communityInfo").get ("sceneCode")#line:64
            sqdata1 =id .get ("data").get ("userInfo").get ("userAccount")#line:65
            print ("获取饿了么社群："+id1 ,"用户金币："+str (sqdata1 ))#line:66
            xx0 ="获取饿了么社群："+id1 +"  用户金币："+str (sqdata1 )#line:67
            time .sleep (2 )#line:68
            url ='https://waimai-guide.ele.me/h5/mtop.alsc.wechat.biz.api.checkin/1.0/4.0/?jsv=2.4.12&appKey=32529321&t="+nowtime+"&sign=19bcc772739e471dd8bae51cf7abb34c&c=65132fab890611a36ea4c56426be6bc5_1685709597766%3Bde94d00b67ff8d2082f9efeeaf38cfd4&api=mtop.alsc.wechat.biz.api.checkin&dataType=json&method=GET&timeout=10000&v=1.0&type=originaljson&ttid=wxece3a9a4c82f58c9%40wechat_ios_10.20.1&accountSite=eleme&data={"sceneCode":"'+sqdata +'","firstCheckIn":false}&_bx-m=1'#line:70
            payload ={}#line:72
            headers ={'Host':'waimai-guide.ele.me','Connection':'keep-alive','Accept':'application/json','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat','X-UA':'RenderWay/miniProgram MiniAppId/wxece3a9a4c82f58c9 MiniAppVersion/10.20.1 DeviceId/o_PVDuFVUiMuXa6jZ4cdWpremOXc AppName/Wechat','bx-ua':'303$bqxE95b898QfMaIsexRSS/Ez1qtZFtT1I1zFzFMzYs7DGC/4WG8S/lmy7xVK7xEvatk2itmmLFo0t3usT+xYvKNXtfyVb4eaiLMeTMgSIAR7TYqV3dD2lrmYvU8sgmCq+6PoF9YXQd7JbKFPs1+TAXWbI2cg+2h5/YqJFcX7ZQXxueBXnTXNhWqo30Vr2imcaQIYkL+SwcbP3X2CJyVeO/2N0FmVxaGj4Y5uk3uXScNvzhL7SdpRoqM5ccnIF23W8hD2ZdG5IOkulEPYMIO9i/mttQPfUNyWM7H1kk0NJqTaVsACWDj4z2Xhr4TOTbr8UJiZczA8ap593XmFlbN3HEeqsKs5k3ZDrn1E63lEGNJWZsZDc8mkYWdYKkEQK+JuhVamCCSDPByRqJHfzlrwMLq6doyuCLqamJUcpxogZ06uAX6/d8VLOHnC2Ybv+2wPiTtXiqGL886tv2LmL+9JibEhBeEu2hSodppC8VJ/CYVshwFWxj2TNi16iKW7MFyi7x+GmZZ03KgpqZ0aL14xeMq/DxykbTghL5dVPBFZcfL=','bx-umidtoken':'S2gAWFvrznqymrKnNNrp-ilU26sxMCmsn-uDNWWg_gvVk08ZG5CG2lyLJzk22ooWb0nofjr-6WkDRnOoHnS54MihKN7ZY2pAaXtHOOQ9nibfgw==','mini-janus':'3%40sBaI71cZCCLEtQgQ3%2FRSsC3tchizJmMPsmFJKAK6hSKuRu8d6oaXhxM4YfG%3D','x-decode-ua':'false','x-ele-check':'RuTUhNLhmjbNmMWBEhgWpHFZfeTYjcv+VspUSIWqdxn+jezT/w/o/iDSVD5ED4WiAR9ZDDd5TjumYKBoKSSHkCLi+Khc91YO3Nbp43H7ws/FAlPTBOHz1ONmRjrmHFSljsFQz7eKw3XmO4CC8YTqAoSsPxllV7v224aDliyze80AfTGbnlNk3NH6yjvWyVw2EzW8DjTJut2YzFXhYDAzXmw0Eot+7ww0oXIJMm2S10XuALrBmsqWTs2m6Rw2RxB2mcSd3qxPbOn8fBKxooPRbHxHRNhxRpK0zu2XPLp7dcGuhkbIx5WFKM8KwiueMmed5iaHJcqnmTlGCrRG7EwaMI4noZYoXfUNlQeJslWKOXfqJ6VpXPN7ORJsXmSu/sn/QKxDZgMd2i0V73A0+LkL+UOipaCvJorGo14+bfOyYSCqAGPiSb83tmLxax4eVXc8NDNWLqfeE9mT8zdOfjqjBRf52vLwX7HIjAp3SM6GdV++sUPJRVaU1OGZOaQHtrmQ','x-ele-ua':'RenderWay/miniProgram MiniAppId/wxece3a9a4c82f58c9 MiniAppVersion/10.20.1 DeviceId/o_PVDuFVUiMuXa6jZ4cdWpremOXc AppName/Wechat microsoft/microsoft windows/10 Wechat/3.4.0 channel/wechat_app subChannel/wechat_app.default MicroMessenger/8.0.6','x-secext-city':'21','x-smallstc':'{"loginSucResultAction":"loginResult","st":"tb_s_ele_1ADg6Le-9nIGfIQpspL2mGA","loginType":"snsLogin","open_id":"oQZUI0dAar6UJEJjyqlF_EpvOxao","loginScene":"miniProgramLogin","unb":2209633667417,"resultCode":100,"appEntrance":"weixin","elemeExt":"{}","smartlock":false,"snsType":"weixin_mini_program","sid":"12be3156d10c030cec5acf731cc19408","cookie2":"12be3156d10c030cec5acf731cc19408","munb":2209633667417,"SID":"MTJiZTMxNTZkMTBjMDMwY2VjNWFjZjczMWNjMTk0MDjMFG-U2x_nu2TxBkH-SqbB","bindTag":"existed","loginResult":"success","sgcookie":"M100gXLFvYP5Fr2PcLvry0ZbmxyWQoKIKBAyF7mJsrmbyn8NDS84jY/MTCUTf+a5Iz6vMBvY7EovOaKViS1KUxTf9/CB2ktVude/f4YNmQvy01o=","user_id":"1000127450482","csg":"1564a413","union_id":"o_PVDuFVUiMuXa6jZ4cdWpremOXc","USERID":"1000127450482","UTUSER":"1000127450482"}','x-tap':'wx','x-ticid':'ARF-8TDuE8Hp-BvQA-2Kt6CXRWVIVYXQP17Rkkd3yLqT43On0ljjKb9CYZSD9R0o39xFvMytwZBFkkuljESZ-Bc6X4xb','Referer':'https://servicewechat.com/wxece3a9a4c82f58c9/496/page-frame.html','Cookie':ck ,'content-type':'application/x-www-form-urlencoded'}#line:92
            response =requests .request ("GET",url ,headers =headers ,data =payload )#line:95
            dk =json .loads (response .text )#line:96
            dk1 =dk .get ("data")#line:97
            dk2 =dk .get ("ret")#line:98
            if response .status_code ==200 :#line:99
                if dk1 !={}:#line:100
                    dk3 =dk1 .get ("desc")#line:101
                    print ("饿了么社群打卡："+dk3 )#line:102
                    xx1 ="饿了么社群打卡："+dk3 #line:103
                else :#line:104
                    dk4 =dk2 [0 ]#line:105
                    print ("饿了么社群打卡："+dk4 )#line:106
                    xx1 ="饿了么社群打卡："+dk4 #line:107
            else :#line:108
                print ("出现未知错误")#line:109
                xx1 ="出现未知错误"#line:110
    else :#line:111
        print ("ck过期或者未加入社群\n")#line:112
        xx1 ="ck过期或者未加入社群\n"#line:113
else :#line:114
    print ("ck过期或者未加入社群\n")
pushplus(f"{xx2}\n{xx0}\n{xx1}",token)
