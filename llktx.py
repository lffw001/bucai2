import json
import os
import time
from urllib.parse import quote,unquote
#自己定时在任务脚本前面
#乐乐看提现，变量名:lelekck，需要抓包apillk.cengaw.cn/请求头里面的device#Authorization，（Authorization只需要Bearer后面的部分）
import requests
money = "5"#提现金额，默认5
num = 3#循环次数，有时会提示太快



Auth0 = os.getenv("lelekck")
ck = Auth0.split("#")
device =ck[0]
Auth = ck[1]
time1 = str(round(time.time())*1000)

url = "https://apillk.cengaw.cn/api/v2/cash/exchange"
gg = requests.request("GET",unquote("http%3A%2F%2Fgh.qninq.cn%2Fhttps%3A%2F%2Fraw.githubusercontent.com%2F241793%2Fbucai2%2Fmain%2Fgg",'utf-8'))
print(gg.text)
print('\n开始提现'+str(money))
payload = 'gate=wechat&amount='+money+'&lat=&lng=&root=0&sim=1&debug=1&model=V2055A&power=0&vpn=0'
headers = {
   'accept': 'application/json',
   'device': device,
   'oaid': device,
   'store': 'baidu',
   'version': '105',
   'platform': '1',
   'Authorization': "Bearer "+Auth,
   'Content-Type': 'application/x-www-form-urlencoded',
   'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 13; V2055A Build/TP1A.220624.014)',
   'Host': 'apillk.cengaw.cn',
   'Connection': 'Keep-Alive',
   'Accept-Encoding': 'gzip',
   'Content-Length': '79',

}

for i in range(num):
   response = requests.request("POST", url, headers=headers, data=payload)
   if response.status_code == 200:
      qg = json.loads(response.text)
      qg1 = qg.get("message")
      print(qg1)
      time.sleep(2)
   else:
      print(response.json())
      break











