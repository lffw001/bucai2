import json,sendNotify
import requests,time
from urllib.parse import unquote,quote
import base64
import hashlib,sys,os
from sendNotify import gg
from notify import send

#by:不才
#APP上观新闻，积分卡券或者实物，下载链接https://a.app.qq.com/o/simple.jsp?pkgname=com.shwatch.news
#变量名：sgxwck,多号用&连接，由于只需要id所以做不了登录任务，评论也做不了，其它正常，一天200多积分
#ck获取，登录app，把用户名的数字复制填写即可，例：export sgxwck="8018XX",只需要前六位

uid0 = os.getenv("sgxwck")

deviceid = "dd8d90b-a519-4c45-8c72-28753734c1c5"#建议抓包改成自己的


uid1 =uid0 .split ("&")#line:1
b =0 #line:2
log_content =''#line:3
class LoggerWriter :#line:4
    def __init__ (OOOOOO0OOO0O0OOO0 ,OO00O0O00OO0000O0 ):#line:5
        OOOOOO0OOO0O0OOO0 .level =OO00O0O00OO0000O0 #line:6
    def write (O0O0O000OOO0O0OO0 ,OO0O0000O0OO00O0O ):#line:8
        global log_content #line:9
        O0O0O000OOO0O0OO0 .level .write (OO0O0000O0OO00O0O )#line:10
        log_content +=OO0O0000O0OO00O0O #line:11
    def flush (OOOO0O0OOOOO0O000 ):#line:13
        return None #line:14
sys .stdout =LoggerWriter (sys .stdout )#line:15
print (gg (),"\n不才提醒您：当前执行'上观新闻'"+"   v:1.1")#line:16
for b in range (len (uid1 )):#line:18
   c =0 #line:19
   uid =uid1 [b ]#line:20
   nowtime =str (round (time .time ()*1000 ))#line:21
   def md5_encrypt (OOO00O0O0O0OOOO0O ):#line:22
      OOO00O0O0O0OOOO0O =OOO00O0O0O0OOOO0O .encode ('utf-8')#line:24
      OOO0OO0O0O000000O =hashlib .md5 ()#line:26
      OOO0OO0O0O000000O .update (OOO00O0O0O0OOOO0O )#line:27
      return OOO0OO0O0O000000O .hexdigest ()#line:28
   data =f"615607${deviceid}${nowtime}$rVX9ITrrTPrCurUe"#line:30
   dz =md5_encrypt (data )#line:31
   data =f"{uid}${nowtime}$rVX9ITrrTPrCurUe"#line:33
   yh =md5_encrypt (data )#line:34
   data =f"{uid}${nowtime}$rVX9ITrrTPrCurUe"#line:39
   sp =md5_encrypt (data )#line:40
   data =f"62981${nowtime}$rVX9ITrrTPrCurUe"#line:45
   yd =md5_encrypt (data )#line:46
   data =f"615201${deviceid}${nowtime}$rVX9ITrrTPrCurUe"#line:51
   fx =md5_encrypt (data )#line:52
   data =f"615602${uid}${nowtime}$rVX9ITrrTPrCurUe"#line:54
   pl =md5_encrypt (data )#line:55
   print ("账号"+str (b +1 )+"开始运行")#line:57
   url1 ="https://services.shobserver.com:443/score/userScore"#line:59
   url2 ="https://services.shobserver.com:443/user/addScore"#line:61
   url3 ="https://services.shobserver.com:443/news/getdetail_v3.5/id"#line:63
   url4 ="https://services.shobserver.com:443/news/save/praise"#line:65
   url5 ="https://services.shobserver.com:443/news/replay/save"#line:67
   url6 ="https://services.shobserver.com:443/news/share/Statistics"#line:69
   url7 ="https://services.shobserver.com:443/user/addScore"#line:71
   url8 ="https://services.shobserver.com:443/user/addScore"#line:73
   payload1 ="uid="+uid +f"&times={nowtime}&sign={yh}&versionCode=9.9.6&platform=2"#line:75
   payload2 ="actiontype=1&uid="+uid +f"&times={nowtime}&devicecode={deviceid}&sign={sp}&platform=2&versionCode=9.9.6"#line:76
   payload3 ="uid="+uid +f"&times={nowtime}&sign={yd}&id=62981&deviceid={deviceid}&versionCode=9.9.6&platform=2&sid=11"#line:77
   payload4 ="uid="+uid +f"&ipaddress={deviceid}&times={nowtime}&nid=615607&sign={dz}&platform=2"#line:78
   payload5 ="uid="+uid +f"&times={nowtime}&devicecode={deviceid}&nid=622004&sign={pl}&ruid=0&value=%E6%94%AF%E6%8C%81%E6%94%AF%E6%8C%81%E6%94%AF%E6%8C%81%E6%94%AF%E6%8C%81%E6%94%AF%E6%8C%81%E6%94%AF%E6%8C%81&platform=2"#line:79
   payload6 ="uid="+uid +f"&ipaddress=&times={nowtime}&sharestyle=3&nid=615201&sign={fx}&sessionid={deviceid}&secondshare=0&platform=2&versionCode=9.9.6&newstype=0"#line:80
   payload7 ="actiontype=3&uid="+uid +f"&times={nowtime}&devicecode={deviceid}&sign={sp}&platform=2&versionCode=9.9.6"#line:81
   payload8 ="actiontype=2&uid="+uid +f"&times={nowtime}&devicecode={deviceid}&sign={sp}&platform=2&versionCode=9.9.6"#line:82
   headers1 ={'Content-Type':'application/x-www-form-urlencoded','Content-Length':'97','Host':'services.shobserver.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','User-Agent':'okhttp/3.8.0',}#line:91
   headers2 ={'Host':'services.shobserver.com','Connection':'Keep-Alive','User-Agent':'okhttp/3.8.0','Content-Type':'application/x-www-form-urlencoded','Accept':'*/*',}#line:99
   headers3 ={'Host':'services.shobserver.com','Connection':'Keep-Alive','User-Agent':'okhttp/3.8.0','Content-Type':'application/x-www-form-urlencoded','Accept':'*/*',}#line:106
   headers4 ={'Content-Type':'application/x-www-form-urlencoded','Content-Length':'137','Host':'services.shobserver.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','User-Agent':'okhttp/3.8.0',}#line:115
   headers5 ={'Content-Type':'application/x-www-form-urlencoded','Content-Length':'162','Host':'services.shobserver.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','User-Agent':'okhttp/3.8.0',}#line:123
   headers6 ={'Content-Type':'application/x-www-form-urlencoded','Content-Length':'382','Host':'services.shobserver.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','User-Agent':'okhttp/3.8.0',}#line:131
   headers7 ={'Content-Type':'application/x-www-form-urlencoded','Content-Length':'158','Host':'services.shobserver.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','User-Agent':'okhttp/3.8.0',}#line:139
   headers8 ={'Content-Type':'application/x-www-form-urlencoded','Content-Length':'158','Host':'services.shobserver.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','User-Agent':'okhttp/3.8.0',}#line:147
   response1 =requests .request ("POST",url1 ,headers =headers1 ,data =payload1 )#line:148
   if response1 .status_code ==200 :#line:150
      xxdata =json .loads (response1 .text )#line:151
      if xxdata .get ("success")==True :#line:152
         xxdata1 =xxdata .get ("object")#line:153
         xxdata2 =xxdata1 .get ("score")#line:154
         print ("账号"+str (b +1 )+"当前总积分为："+str (xxdata2 ))#line:155
         xx0 =f"账号{str(b + 1)}当前总积分为：{str(xxdata2)}"#line:156
      else :#line:157
         print ("账号"+str (b +1 )+"未知错误")#line:158
         xx0 =f"账号{str(b + 1)}未知错误"#line:159
   else :#line:160
      print ("账号"+str (b +1 )+"未知错误")#line:161
      xx0 =f"账号{str(b+1)}未知错误"#line:162
   time .sleep (2 )#line:163
   for c in range (5 ):#line:164
      time .sleep (1 )#line:165
      response2 =requests .request ("POST",url2 ,headers =headers2 ,data =payload2 )#line:166
      if response2 .status_code ==200 :#line:167
         spdata =json .loads (response2 .text )#line:168
         if spdata .get ("success")==True :#line:169
            spdata1 =spdata .get ("object")#line:170
            spdata2 =spdata1 .get ("score")#line:171
            if spdata2 !=0 :#line:172
               print ("账号"+str (b +1 )+"看视频获得积分："+str (spdata2 ))#line:173
               d =5 *(c +1 )#line:174
               xx2 =f"账号{str(b + 1)}看视频获得积分：{d}"#line:175
            else :#line:176
               print ("账号"+str (b +1 )+"看视频获得积分已完成")#line:177
               xx2 ="账号"+str (b +1 )+"看视频获得积分已完成"#line:178
               break #line:179
      else :#line:180
         print ("账号"+str (b +1 )+"看视频未知错误")#line:181
         xx2 ="账号"+str (b +1 )+"看视频未知错误"#line:182
         break #line:183
   time .sleep (2 )#line:184
   for c in range (10 ):#line:185
      time .sleep (2 )#line:186
      response3 =requests .request ("POST",url3 ,headers =headers3 ,data =payload3 )#line:187
      if response3 .status_code ==200 :#line:188
         yddata =json .loads (response3 .text )#line:189
         if yddata .get ("breturn")==True :#line:190
            yddata1 =yddata .get ("object")#line:191
            yddata2 =yddata1 .get ("score")#line:192
            if yddata2 !=0 :#line:193
               print ("账号"+str (b +1 )+"阅读文章获得积分："+str (yddata2 ))#line:194
               d =2 *(c +1 )#line:195
               xx4 ="账号"+str (b +1 )+"阅读文章获得积分："+str (d )#line:196
            else :#line:197
               print ("账号"+str (b +1 )+"阅读文章获得积分已完成")#line:198
               xx4 ="账号"+str (b +1 )+"阅读文章获得积分已完成"#line:199
               break #line:200
      else :#line:201
         print ("账号"+str (b +1 )+"阅读未知错误")#line:202
         xx4 ="账号"+str (b +1 )+"阅读未知错误"#line:203
         break #line:204
   time .sleep (2 )#line:205
   for c in range (10 ):#line:206
      time .sleep (2 )#line:207
      response4 =requests .request ("POST",url4 ,headers =headers4 ,data =payload4 )#line:208
      if response4 .status_code ==200 :#line:209
         dzdata =json .loads (response4 .text )#line:210
         if dzdata .get ("breturn")==True :#line:211
            dzdata1 =dzdata .get ("object")#line:212
            dzdata2 =dzdata1 .get ("score")#line:213
            if dzdata2 !=0 :#line:214
               print ("账号"+str (b +1 )+"文章点赞获得积分："+str (dzdata2 ))#line:215
               xx6 ="账号"+str (b +1 )+"文章点赞获得积分："+str (2 *(c +1 ))#line:216
            else :#line:217
               print ("账号"+str (b +1 )+"文章点赞获得积分已完成")#line:218
               xx6 ="账号"+str (b +1 )+"文章点赞获得积分已完成"#line:219
               break #line:220
      else :#line:221
         print ("账号"+str (b +1 )+"点赞未知错误")#line:222
         xx6 ="账号"+str (b +1 )+"点赞未知错误"#line:223
         break #line:224
   time .sleep (2 )#line:225
   for c in range (10 ):#line:226
      response5 =requests .request ("POST",url5 ,headers =headers5 ,data =payload5 )#line:227
      if response5 .status_code ==200 :#line:228
         pldata =json .loads (response5 .text )#line:229
         if pldata .get ("breturn")==True :#line:230
            pldata1 =pldata .get ("object")#line:231
            pldata2 =pldata1 .get ("score")#line:232
            if pldata2 !=0 :#line:233
               print ("账号"+str (b +1 )+"文章评论获得积分："+str (pldata2 ))#line:234
            else :#line:236
               print ("账号"+str (b +1 )+"文章评论获得积分已完成")#line:237
               break #line:238
         else :#line:239
            print ("账号"+str (b +1 )+"评论失败")#line:240
            break #line:241
      else :#line:242
         print ("账号"+str (b +1 )+"评论未知错误")#line:243
         break #line:244
   time .sleep (2 )#line:245
   for c in range (15 ):#line:246
      time .sleep (2 )#line:247
      response6 =requests .request ("POST",url6 ,headers =headers6 ,data =payload6 )#line:248
      if response6 .status_code ==200 :#line:249
         fxdata =json .loads (response6 .text )#line:250
         if fxdata .get ("breturn")==True :#line:251
            fxdata1 =fxdata .get ("object")#line:252
            fxdata2 =fxdata1 .get ("score")#line:253
            if fxdata2 !=0 :#line:254
               print ("账号"+str (b +1 )+"文章分享获得积分："+str (fxdata2 ))#line:255
               xx9 ="账号"+str (b +1 )+"文章分享获得积分："+str (5 *(c +1 ))#line:256
            else :#line:257
               print ("账号"+str (b +1 )+"文章分享获得积分已完成")#line:258
               xx9 ="账号"+str (b +1 )+"文章分享获得积分已完成"#line:259
               break #line:260
         else :#line:261
            print ("账号"+str (b +1 )+"分享失败")#line:262
            xx9 ="账号"+str (b +1 )+"分享失败"#line:263
            break #line:264
      else :#line:265
         print ("账号"+str (b +1 )+"分享未知错误")#line:266
         xx9 ="账号"+str (b +1 )+"分享未知错误"#line:267
         break #line:268
   time .sleep (2 )#line:269
   for c in range (1 ):#line:270
      response7 =requests .request ("POST",url7 ,headers =headers7 ,data =payload7 )#line:271
      if response7 .status_code ==200 :#line:272
         ewmdata =json .loads (response7 .text )#line:273
         if ewmdata .get ("breturn")==True :#line:274
            ewmdata1 =ewmdata .get ("object")#line:275
            ewmdata2 =ewmdata1 .get ("score")#line:276
            if ewmdata2 !=0 :#line:277
               print ("账号"+str (b +1 )+"分享二维码获得积分："+str (ewmdata2 ))#line:278
               xx11 ="账号"+str (b +1 )+"分享二维码获得积分："+str (20 *(c +1 ))#line:279
            else :#line:280
               print ("账号"+str (b +1 )+"分享二维码获得积分已完成")#line:281
               xx11 ="账号"+str (b +1 )+"分享二维码获得积分已完成"#line:282
               break #line:283
         else :#line:284
            print ("账号"+str (b +1 )+"二维码分享失败")#line:285
            xx11 ="账号"+str (b +1 )+"二维码分享失败"#line:286
            break #line:287
      else :#line:288
         print ("账号"+str (b +1 )+"分享二维码未知错误")#line:289
         xx11 ="账号"+str (b +1 )+"分享二维码未知错误"#line:290
         break #line:291
   time .sleep (2 )#line:292
   for c in range (3 ):#line:293
      response8 =requests .request ("POST",url8 ,headers =headers8 ,data =payload8 )#line:294
      if response8 .status_code ==200 :#line:295
         zbdata =json .loads (response8 .text )#line:296
         if zbdata .get ("breturn")==True :#line:297
            zbdata1 =zbdata .get ("object")#line:298
            zbdata2 =zbdata1 .get ("score")#line:299
            if zbdata2 !=0 :#line:300
               print ("账号"+str (b +1 )+"观看直播获得积分："+str (zbdata2 ))#line:301
               xx13 ="账号"+str (b +1 )+"观看直播获得积分："+str (10 *(c +1 ))#line:302
            else :#line:303
               print ("账号"+str (b +1 )+"观看直播获得积分已完成")#line:304
               xx13 ="账号"+str (b +1 )+"观看直播获得积分已完成"#line:305
               break #line:306
         else :#line:307
            print ("账号"+str (b +1 )+"观看直播失败")#line:308
            xx13 ="账号"+str (b +1 )+"观看直播失败"#line:309
            break #line:310
      else :#line:311
         print ("账号"+str (b +1 )+"观看直播未知错误")#line:312
         xx13 ="账号"+str (b +1 )+"观看直播未知错误"#line:313
         break #line:314
   print ("---------3秒后进行下一个账号---------")#line:316
   time .sleep (3 )#line:317
send ("上观新闻",log_content )
