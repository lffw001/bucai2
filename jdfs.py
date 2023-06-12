import requests,json,time,os
from sendNotify import gg
'''''
京东公众号--》签到兑红包，抓全部cookie
变量名：jdck,多号用&或者新建变量
完成签到,兑换50金豆，任务概率完成一般都是火爆
定时 cron 0 0 0,10 * * *
'''''
cookie0 = os.getenv("jdck")
ck = cookie0.split("&")


'''''
    url7 = "https://api.m.jd.com/officialAccountSign_exchange"
    data7 = 'appid=large_account&functionId=officialAccountSign_exchange&client=android&clientVersion=1.0.0&loginType=1&loginWQBiz=dzhsign&body={"encryptAssignmentId":"4Qjm7TrkpbL8wVVug7tfhaJMpB93"}'
    data1 = 'appid=large_account&functionId=officialAccountSign_scan&client=android&clientVersion=1.0.0&loginType=1&loginWQBiz=dzhsign&body={"actionType":0,"scanAssignmentId":"24khHYti3ArfpbvAJxo4NfLjjVRx","itemId":"1401741011"}'
    data2 = 'appid=large_account&functionId=officialAccountSign_scan&client=android&clientVersion=1.0.0&loginType=1&loginWQBiz=dzhsign&body={"actionType":0,"scanAssignmentId":"TJdrk6wh74XEaur1qh1v4bwTXfe","itemId":"1701777013"}'
    data3 = 'appid=large_account&functionId=officialAccountSign_scan&client=android&clientVersion=1.0.0&loginType=1&loginWQBiz=dzhsign&body={"actionType":0,"scanAssignmentId":"2RN7wq4FH71BMwxS6uZeuejL6WFw","itemId":"0701770809"}'
    data4 = 'appid=large_account&functionId=officialAccountSign_scan&client=android&clientVersion=1.0.0&loginType=1&loginWQBiz=dzhsign&body={"actionType":0,"scanAssignmentId":"3VLETkyfAKpUFBtFE59LAq9xXqL6","itemId":"9001745652"}'
    data5 = 'appid=large_account&functionId=officialAccountSign_scan&client=android&clientVersion=1.0.0&loginType=1&loginWQBiz=dzhsign&body={"actionType":0,"scanAssignmentId":"DWNQCgutr78zZQ64PVMsMpig8Xb","itemId":"9601762841"}'
    data6 = 'appid=large_account&functionId=officialAccountSign_scan&client=android&clientVersion=1.0.0&loginType=1&loginWQBiz=dzhsign&body={"actionType":0,"scanAssignmentId":"yZiCmoQX7W3ixqh1xrursgPyqVd","itemId":"7401766134"}'
    data0 = 'appid=large_account&functionId=officialAccountSign_sign&client=android&clientVersion=1.0.0&loginType=1&loginWQBiz=dzhsign&body={"itemId":"1"}'
    
''' ''#line:12
print(gg())#line:13
for i in range (len (ck )):#line:14
    cookie =ck [i ]#line:15
    print (f"----------开始第{i+1}个号----------")#line:16
    url1 ="https://api.m.jd.com/officialAccountSign_scan"#line:17
    url11 ="https://pro.m.jd.com/wq/active/rCTeA6sMFe1Nt3kSq7YcohwrQEA/index.html?babelChannel=ttt6"#line:18
    url0 ="https://api.m.jd.com/officialAccountSign_sign"#line:19
    url7 ="https://api.m.jd.com/officialAccountSign_exchange"#line:20
    data7 ='appid=large_account&functionId=officialAccountSign_exchange&client=android&clientVersion=1.0.0&loginType=1&loginWQBiz=dzhsign&body={"encryptAssignmentId":"4Qjm7TrkpbL8wVVug7tfhaJMpB93"}'#line:21
    data1 ='appid=large_account&functionId=officialAccountSign_scan&client=android&clientVersion=1.0.0&loginType=1&loginWQBiz=dzhsign&body={"actionType":0,"scanAssignmentId":"24khHYti3ArfpbvAJxo4NfLjjVRx","itemId":"1401741011"}'#line:22
    data2 ='appid=large_account&functionId=officialAccountSign_scan&client=android&clientVersion=1.0.0&loginType=1&loginWQBiz=dzhsign&body={"actionType":0,"scanAssignmentId":"TJdrk6wh74XEaur1qh1v4bwTXfe","itemId":"1701777013"}'#line:23
    data3 ='appid=large_account&functionId=officialAccountSign_scan&client=android&clientVersion=1.0.0&loginType=1&loginWQBiz=dzhsign&body={"actionType":0,"scanAssignmentId":"2RN7wq4FH71BMwxS6uZeuejL6WFw","itemId":"0701770809"}'#line:24
    data4 ='appid=large_account&functionId=officialAccountSign_scan&client=android&clientVersion=1.0.0&loginType=1&loginWQBiz=dzhsign&body={"actionType":0,"scanAssignmentId":"3VLETkyfAKpUFBtFE59LAq9xXqL6","itemId":"9001745652"}'#line:25
    data5 ='appid=large_account&functionId=officialAccountSign_scan&client=android&clientVersion=1.0.0&loginType=1&loginWQBiz=dzhsign&body={"actionType":0,"scanAssignmentId":"DWNQCgutr78zZQ64PVMsMpig8Xb","itemId":"9601762841"}'#line:26
    data6 ='appid=large_account&functionId=officialAccountSign_scan&client=android&clientVersion=1.0.0&loginType=1&loginWQBiz=dzhsign&body={"actionType":0,"scanAssignmentId":"yZiCmoQX7W3ixqh1xrursgPyqVd","itemId":"7401766134"}'#line:27
    data0 ='appid=large_account&functionId=officialAccountSign_sign&client=android&clientVersion=1.0.0&loginType=1&loginWQBiz=dzhsign&body={"itemId":"1"}'#line:28
    headers1 ={'Host':'api.m.jd.com','Connection':'keep-alive','Content-Length':'215','Accept':'application/json, text/plain, */*','Origin':'https://bigaccount-fanssiginin-pro.pf.jd.com','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63040026)','Content-Type':'application/x-www-form-urlencoded','Cookie':cookie ,'Sec-Fetch-Site':'same-site','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':'https://bigaccount-fanssiginin-pro.pf.jd.com/?ptag=17005.2.140&utm_term=dzh_h5_Menu_Fanswelfare_101&utm_source=weixin&utm_campaign=t_1000072662_17005_001&utm_medium=weixin','Accept-Encoding':'gzip, deflate, br','Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',}#line:46
    headers0 ={'Host':'api.m.jd.com','Connection':'keep-alive','Content-Length':'141','Accept':'application/json, text/plain, */*','Origin':'https://bigaccount-fanssiginin-pro.pf.jd.com','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63040026)','Content-Type':'application/x-www-form-urlencoded','Cookie':cookie ,'Sec-Fetch-Site':'same-site','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':"https://bigaccount-fanssiginin-pro.pf.jd.com/?ptag=17005.2.140&utm_term=dzh_h5_Menu_Fanswelfare_101&utm_source=weixin&utm_campaign=t_1000072662_17005_001&utm_medium=weixin",'Accept-Encoding':'gzip, deflate, br','Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',}#line:62
    headers7 ={'Host':'api.m.jd.com','Connection':'keep-alive','Content-Length':'185','Accept':'application/json, text/plain, */*','Origin':'https://bigaccount-fanssiginin-pro.pf.jd.com','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63040026)','Content-Type':'application/x-www-form-urlencoded','Cookie':cookie ,'Sec-Fetch-Site':'same-site','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':"https://bigaccount-fanssiginin-pro.pf.jd.com/?ptag=17005.2.140&utm_term=dzh_h5_Menu_Fanswelfare_101&utm_source=weixin&utm_campaign=t_1000072662_17005_001&utm_medium=weixin",'Accept-Encoding':'gzip, deflate, br','Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',}#line:78
    headers99 ={'Host':'pro.m.jd.com','Connection':'keep-alive','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63040026)','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','Cookie':cookie ,'Sec-Fetch-Site':'same-site','Sec-Fetch-Mode':'navigate','Sec-Fetch-User':'?1','Sec-Fetch-Dest':'document','Referer':'https://bigaccount-fanssiginin-pro.pf.jd.com/?ptag=17005.2.140&utm_term=dzh_h5_Menu_Fanswelfare_101&utm_source=weixin&utm_campaign=t_1000072662_17005_001&utm_medium=weixin','Accept-Encoding':'gzip, deflate, br','Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',}#line:95
    def dhdd ():#line:99
        OOO0O00OO0O000OO0 =requests .request ("POST",url7 ,headers =headers7 ,data =data7 )#line:100
        OO000OO00000O0O0O =json .loads (OOO0O00OO0O000OO0 .text )#line:101
        OOO0000O0000000O0 =OO000OO00000O0O0O .get ("code")#line:102
        OO0O0O00OOOOOO000 =OO000OO00000O0O0O .get ("message")#line:103
        O000OOOO00O00OOO0 =OO000OO00000O0O0O .get ("subCode")#line:104
        if O000OOOO00O00OOO0 ==5006 :#line:105
            print (OO0O0O00OOOOOO000 )#line:106
        elif O000OOOO00O00OOO0 ==0 and OO000OO00000O0O0O .get ("data")!=None :#line:107
            O0OO0O00000OOOOOO =OO000OO00000O0O0O .get ("data").get ("rewardName")#line:108
            print (f"恭喜获得:{O0OO0O00000OOOOOO}")#line:109
        else :#line:111
            print (OOO0O00OO0O000OO0 .text )#line:112
    print ("\n----------京东粉丝50豆兑换1----------\n")#line:114
    dhdd ()#line:115
    print ("\n----------京东粉丝任务执行中----------\n")#line:116
    res0 =requests .request ("POST",url0 ,headers =headers0 ,data =data0 )#line:117
    if res0 .status_code ==200 :#line:118
        qd0 =json .loads (res0 .text )#line:119
        qd1 =qd0 .get ("data")#line:120
        qd4 =qd0 .get ("message")#line:122
        qd5 =qd0 .get ("subCode")#line:123
        if qd5 ==0 :#line:124
            qd2 =qd1 .get ("signDays")#line:125
            qd3 =qd1 .get ("point")#line:126
            print ("签到成功，获得："+str (qd3 ),"连续签到"+str (qd2 ))#line:127
        elif qd5 ==3010 :#line:128
            print (qd4 )#line:129
        else :#line:130
            print ("ck错误或者过期")#line:131
    def rw1 ():#line:134
        OOO00O0000O00O00O =requests .request ("POST",url1 ,headers =headers1 ,data =data1 )#line:135
        if OOO00O0000O00O00O .status_code ==200 :#line:136
            OO000OOO0OOO0O00O =json .loads (OOO00O0000O00O00O .text ).get ("message")#line:137
            print (OO000OOO0OOO0O00O )#line:138
    res1 =requests .request ("POST",url1 ,headers =headers1 ,data =data1 )#line:141
    if res1 .status_code ==200 :#line:142
        task1 =json .loads (res1 .text ).get ("message")#line:143
        print (task1 )#line:144
        res11 =requests .request ("GET",url11 ,headers =headers99 ,data ='')#line:145
        time .sleep (5 )#line:146
        rw1 ()#line:147
    res2 =requests .request ("POST",url1 ,headers =headers1 ,data =data2 )#line:148
    def rw2 ():#line:149
        if res2 .status_code ==200 :#line:150
            OO0OOO0OOOO0OO0O0 =json .loads (res2 .text ).get ("message")#line:151
            print (OO0OOO0OOOO0OO0O0 )#line:152
    if res2 .status_code ==200 :#line:154
        task2 =json .loads (res2 .text ).get ("message")#line:155
        print (task2 )#line:156
        res22 =requests .request ("GET",'https://pro.m.jd.com/wq/active/2CEfVapP9jVUNoGVJ2uL2Y57bAs2/index.html',headers =headers99 ,data ='')#line:157
        time .sleep (5 )#line:158
        rw2 ()#line:159
    res3 =requests .request ("POST",url1 ,headers =headers1 ,data =data3 )#line:160
    if res3 .status_code ==200 :#line:161
        task3 =json .loads (res3 .text ).get ("message")#line:162
        print (task3 )#line:163
        time .sleep (5 )#line:164
    res4 =requests .request ("POST",url1 ,headers =headers1 ,data =data4 )#line:165
    if res4 .status_code ==200 :#line:166
        task4 =json .loads (res4 .text ).get ("message")#line:167
        print (task4 )#line:168
        time .sleep (5 )#line:169
    def rw5 ():#line:170
        O00OO0O0OO0O0O00O =requests .request ("POST",url1 ,headers =headers1 ,data =data5 )#line:171
        if O00OO0O0OO0O0O00O .status_code ==200 :#line:172
            O0OOOO000000000O0 =json .loads (O00OO0O0OO0O0O00O .text ).get ("message")#line:173
            print (O0OOOO000000000O0 )#line:174
    res5 =requests .request ("POST",url1 ,headers =headers1 ,data =data5 )#line:175
    if res5 .status_code ==200 :#line:176
        task5 =json .loads (res5 .text ).get ("message")#line:177
        print (task5 )#line:178
        res55 =requests .request ("GET",'https://pro.m.jd.com/mini/active/3AWQD5ttD6aUg8nue6D7CryKptzW/index.html?wxAppName=jd&babelChannel=ttt1',headers =headers99 ,data ='')#line:180
        time .sleep (5 )#line:181
        rw5 ()#line:182
    def rw6 ():#line:183
        O0O00OO0OOO0OOO0O =requests .request ("POST",url1 ,headers =headers1 ,data =data6 )#line:184
        if O0O00OO0OOO0OOO0O .status_code ==200 :#line:185
            O0OO000OO00OO0O0O =json .loads (O0O00OO0OOO0OOO0O .text ).get ("message")#line:186
            print (O0OO000OO00OO0O0O )#line:187
    res6 =requests .request ("POST",url1 ,headers =headers1 ,data =data6 )#line:188
    if res6 .status_code ==200 :#line:189
        task6 =json .loads (res6 .text ).get ("message")#line:190
        print (task6 )#line:191
        res55 =requests .request ("GET",'https://wqitem.jd.com/item/view?sku=44497441036',headers =headers99 ,data ='')#line:192
        time .sleep (5 )#line:193
        rw6 ()#line:194
    print ("\n----------京东粉丝50豆兑换2----------\n")#line:195
    dhdd ()
