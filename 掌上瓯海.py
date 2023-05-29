import requests
import json,os
#by：不才64643f632cd91836ea7e0a79，'6465cc2d8bee4a43a2e1d8aa'
#只有签到和进入本地生活,分享，低保版本

# zsohck = os.getenv('zsohck')
sessionid = "646729837dee053719427b45"



# zsohck1 = zsohck.split("&")
# accountid = zsohck1[0]
# sessionid = zsohck1[1]
v = "1.1"
name = "掌上瓯海"
url1 = "https://vapp.tmuyun.com/api/user_mumber/sign"
url2 = "https://vapp.tmuyun.com/api/user_mumber/doTask"
url3 = "https://vapp.tmuyun.com/api/user_mumber/numberCenter?is_new=1"
url4 = "https://vapp.tmuyun.com/api/favorite/like"
url5 = "https://vapp.tmuyun.com/api/user_mumber/doTask"
payload = "memberType=6&member_type=6"
payload1={}
payload4 = "action=true&id=4313214"
payload5 = "memberType=3&member_type=3&target_id=4313233"
headers1 = {
   'X-SESSION-ID': sessionid,

   #只是签到的head，域名https://vapp.tmuyun.com/api/user_mumber/sign，根据内容改下面的
   'X-REQUEST-ID': 'daa9d189-eabe-4fa1-8941-47506c191193',
   'X-TIMESTAMP': '1684415148797',
   'X-SIGNATURE': '907e7aca4a4024bdb13c466a8d817e8be2a6cfef2d79b56a9851c60260325941',
   'X-TENANT-ID': '78',
   'User-Agent': '5.0.0;00000000-6470-e940-ffff-ffffc64eaab3;Vivo V2055A;Android;13;Release',
   'Cache-Control': 'no-cache',
   'Host': 'vapp.tmuyun.com',
   'Connection': 'Keep-Alive',
   'Accept': '*/*',

}

headers2 = {
   'X-SESSION-ID': sessionid,

   #https://vapp.tmuyun.com/api/user_mumber/doTask里面内容改下面
   'X-REQUEST-ID': '84be0961-cd38-4e5b-8edf-c3d5acf40e7b',
   'X-TIMESTAMP': '1684415339381',
   'X-SIGNATURE': '11a0309de326e2ab10430c929f1a510b56b024f4437c95098ecbf049c8d2f20d',
   'X-TENANT-ID': '78',
   'User-Agent': '5.0.0;00000000-6470-e940-ffff-ffffc64eaab3;Vivo V2055A;Android;13;Release',
   'Cache-Control': 'no-cache',
   'Host': 'vapp.tmuyun.com',
   'Connection': 'Keep-Alive',
   'Content-Type': 'application/x-www-form-urlencoded',
   'Accept': '*/*',

}
headers3 = {
   'X-SESSION-ID': sessionid,

   #https://vapp.tmuyun.com/api/user_mumber/numberCenter?is_new=1，完成本地服务后可或者这个，改下面的
   'X-REQUEST-ID': '70f0d89f-534b-4db0-88ae-3b51d7ca1cdb',
   'X-TIMESTAMP': '1684415146247',
   'X-SIGNATURE': '8bf82cb8c01efcdde0157bc442232215853c769b91187c0545f2532c3f38d4f2',
   'X-TENANT-ID': '78',
   'User-Agent': '5.0.0;00000000-6470-e940-ffff-ffffc64eaab3;Vivo V2055A;Android;13;Release',
   'Cache-Control': 'no-cache',
   'Host': 'vapp.tmuyun.com',
   'Connection': 'Keep-Alive',
   'Accept': '*/*'
}
headers4 = {
   'X-SESSION-ID': sessionid,

   #https://vapp.tmuyun.com/api/favorite/like，完成点赞任务，改
   'X-REQUEST-ID': '362b532d-362f-45c3-8156-ba5a61aa0799',
   'X-TIMESTAMP': '1684479353248',
   'X-SIGNATURE': 'a96dbe2fa9ba8f3580eeb4d3e0ace38fda5de3bc0dc4b47ebdb6bb06ff9e8888',
   'X-TENANT-ID': '78',
   'User-Agent': '5.0.0;00000000-6470-e940-ffff-ffffc64eaab3;Vivo V2055A;Android;13;Release',
   'Cache-Control': 'no-cache',
   'Host': 'vapp.tmuyun.com',
   'Connection': 'Keep-Alive',
   'Content-Type': 'application/x-www-form-urlencoded',
   'Accept': '*/*',
}
headers5 = {
   'X-SESSION-ID': sessionid,

   #https://vapp.tmuyun.com/api/user_mumber/doTask，完成分享任务改，注意还要看一下响应里面提示是不是分享任务
   'X-REQUEST-ID': '419ecf28-f741-41e5-a481-1a057d0f0cd2',
   'X-TIMESTAMP': '1684481293520',
   'X-SIGNATURE': '42a9ca6a1614738ea29339ea0ed1a6a6962ab226ef4f06c7491746f8d6f9f794',
   'X-TENANT-ID': '78',
   'User-Agent': '5.0.0;00000000-6470-e940-ffff-ffffc64eaab3;Vivo V2055A;Android;13;Release',
   'Cache-Control': 'no-cache',
   'Host': 'vapp.tmuyun.com',
   'Connection': 'Keep-Alive',
   'Content-Type': 'application/x-www-form-urlencoded',
   'Accept': '*/*',

}

print("不才提醒您：")
response1 = requests.request("GET", url1, headers=headers1, data=payload1)
response2 = requests.request("POST", url2, headers=headers2, data=payload)
response3 = requests.request("GET", url3, headers=headers3, data=payload)
response4 = requests.request("POST", url4, headers=headers4, data=payload4)

#用户名和总金币
# if response3.status_code != 404:
#    jfdata = json.loads(response3.text)
#    jfdata1 = jfdata.get("data")
#    jfdata2 = jfdata1.get("rst")
#    username = jfdata2.get("nick_name")
#    total_integral = jfdata2.get("total_integral")
#    print("用户："+username,"总金币:",total_integral)
print(response3.text)


#签到
data = json.loads(response2.text)
mess = data.get("message")
xydata = data.get("data")
qddata = json.loads(response1.text)
qdxydata = qddata.get("data")
mess1 = qddata.get("message")
if mess == "success":
   sign = qdxydata.get("signIntegral")
   print("掌上瓯海签到获得：",sign,"金币")
else:
   print("数据错误，请检查")

#本地生活
if xydata ==None and mess == "success":
    print("已经进入过本地生活")
elif xydata != None and mess == "success":
   xydata2 = xydata.get("score_notify")
   gold = xydata2.get("integral")
   print("进入本地生活获得",gold,"金币")

#点赞
# xwdata = json.loads(response4.text)
# xwdata1 = xwdata.get("message")
# xwdata2 = xwdata.get("data")
# print(response4.text)
# if response4.status_code != 404:
#    if xwdata1 == "success" and xwdata2 !=None:
#       xwdata3 = xwdata.get("integral")
#       xwdata4 = xwdata2.get("name")
#       print(xwdata4+"获得",xwdata3,"金币")
#    elif xwdata1 == "success" and xwdata2 ==None:
#       print("点赞今日已经完成过了")
# else:
#    print("错误")
#分享咨询
for i in range(0,3):
   response5 = requests.request("POST", url5, headers=headers5, data=payload5)


fxdata = json.loads(response5.text)
fxdata1 = fxdata.get("message")
fxdata2 = fxdata.get("data")
if response5.status_code != 404:
   if fxdata1 == "success" and fxdata2 !=None:
      fxdata3 = fxdata.get("integral")
      fxdata4 = fxdata2.get("name")
      print(fxdata4+"获得",fxdata3,"金币")
   elif fxdata1 == "success" and fxdata2 ==None:
      print("分享咨询今日已经完成过了")
else:
   print("错误")
