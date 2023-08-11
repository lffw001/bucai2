import datetime

import requests, logging
import json, sys, time, os
from notify import send

# 1.4  修复
#乐乐看pro提现（配合蛋姨的本），变量名:llkck，需要抓包apillkpro.cengaw.cn/请求头里面的device#Authorization，（Authorization只需要Bearer后面的部分）
#8.11新增看资讯任务和闯关,多号换行隔开,ua换成自己的（User-Agent）
#需要提5块设一次定时弄在任务本前面
#一天运行2-3次
#cron 0 0,7,15 * * *
money = "5"  # 提现金额，默认5
ua = "Mozilla/5.0 (Linux; Android 10; SEA-AL10 Build/HUAWEISEA-10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.5 Mobile Safari/537.36"

ck = os.getenv("llkck")
ck1 = ck.split("\n")
log_content = ''


class LoggerWriter:
    def __init__(self, level):
        self.level = level

    def write(self, message):
        global log_content
        self.level.write(message)
        log_content += message

    def flush(self):
        return None


sys.stdout = LoggerWriter(sys.stdout)

# 登录


print("当前执行【乐乐看PRO提现】 v1.4")
for b in range(len(ck1)):
    fg = ck1[b].split("#")
    device = fg[0]
    auth = fg[1]

    print("\n----------不才提醒您，账号" + str(b + 1) + "运行中----------")
    # user

    url1 = "https://apillkpro.cengaw.cn/api/v2/member/profile"
    #提现
    url2 ="https://apillkpro.cengaw.cn/api/v2/cash/exchange"
    #视频次数
    url3 = "https://apillkpro.cengaw.cn/api/v2/video/coin?ticket=eyJ0eXAiOiJKV1MiLCJhbGciOiJIUzUxMiJ9.eyJleHAiOjE2ODc0MTg4OTYsImlhdCI6MTY4NzQxNTI5NiwibmJmIjoxNjg3NDE1MzExLCJzdWIiOiJ2aWRlbyIsImF1ZCI6MTI3ODc4MywianRpIjoiNjQ5M2VhMDA0MjhjNyJ9.ZmQ2Mzk5OWMzNmY0ZjI3Mjk3NDgxN2FiZGRjZmE2NjE1YTgwODIwMzM3YzJmZDBiNDI3MjIzMTE4ZWQ1NTQ3OWI5OWY4MjZlNmE5YTJiYjg4NDcwMmUxMGMwNDk4MTA2NjYwMzI3ZjdiZGU1NjI3NDE3NTk0ODgzODgxZjNkZmQ"
    #开启视频红包
    url4 = "https://apillkpro.cengaw.cn/api/v2/video/redenv"

    data2 = 'gate=wechat&amount=' + money + '&lat=&lng=&root=0&sim=1&debug=1&model=V2055A&power=0&vpn=0'
    headers2 = {
        'accept': 'application/json',
        'device': device,
        'oaid': device,
        'store': 'baidu',
        'version': '105',
        'platform': '1',
        'Authorization': "Bearer " + auth,
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': ua,
        'Host': 'apillkpro.cengaw.cn',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'Content-Length': '79',

    }
    headers1 = {
        'accept': 'application/json',
        'device': device,
        'oaid': device,
        'store': 'baidu',
        'version': '105',
        'platform': '1',
        'Authorization': f'Bearer {auth}',
        'User-Agent': ua,
        'Host': 'apillkpro.cengaw.cn',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip'

    }
    headers3 = {
        'accept': 'application/json',
        'device': device,
        'oaid': device,
        'store': 'baidu',
        'version': '105',
        'platform': '1',
        'Authorization': f'Bearer {auth}',
        'User-Agent': ua,
        'Host': 'apillkpro.cengaw.cn',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'Content-Length': '12'

    }
    headers4 = {
        'accept': 'application/json',
        'device': device,
        'oaid': device,
        'store': 'baidu',
        'version': '105',
        'platform': '1',
        'Authorization': f'Bearer {auth}',
        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 13; V2055A Build/TP1A.220624.014)',
        'Host': 'apillkpro.cengaw.cn',
        'Connection': 'Keep-Alive',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    i = b + 1
    res1 = requests.request("GET", url1, headers=headers1)
    if res1.status_code == 200:
        user = res1.json().get("result")
        if res1.json().get("code") == 0:
            print(f"[账号{i}]:{user.get('nickname')}  总余额:{user.get('balance')}  提现券:{user.get('ticket')}")
            # 开始提现
            print(f"•••开始提现{money}元•••")
            time.sleep(2)
            for b in range(3):
                res2 = requests.request("POST", url2, headers=headers2, data=data2)
                if res2.status_code == 200:
                    qg = json.loads(res2.text)
                    qg1 = qg.get("message")
                    qg2 = qg.get("result")
                    if qg.get("success") == True and qg != None:
                        qg3 = qg2.get("title")
                        qg4 = qg2.get("message")
                        print(f"{qg2}\n{qg4}")
                        time.sleep(2)
                    else:
                        print(qg1)
                        time.sleep(2)
                        break
                else:
                    print(res2.json())
                    break
            # video
            if 1 <= datetime.datetime.now().hour <= 23:
                print("---开始看视频资讯  1-23点运行任务")
                time.sleep(2)
                for i in range(22):

                    res3 = requests.request("GET", url3, headers=headers4)
                    if res3.json().get("code") == 0:
                        data = res3.json().get("result")
                        counttotal = data.get("today_video_total")
                        count = data.get("count")
                        print(f"看视频赚钱第{count}次")
                        if count == 6:
                            print(f"已看满6次，开启红包,今日任务进度{counttotal}/20")
                            time.sleep(2)
                            res4 = requests.request("GET", url4, headers=headers1)
                            data1 = res4.json().get("result")
                            if res4.json().get("code") == 0:
                                print(f"红包开启成功，获得金币：{data1.get('reward')},获得提现券：{data1.get('coupon')}")
                            elif res4.json().get("code") == 40301:
                                print(f"{res4.json().get('message')}")
                                break
                        if counttotal >= 21:
                            url6 = "https://apillkpro.cengaw.cn/api/v2/zhuan/done"
                            headers6 = {
                                'accept': 'application/json',
                                'device': device,
                                'oaid': device,
                                'store': 'baidu',
                                'version': '105',
                                'platform': '1',
                                'Authorization': f'Bearer {auth}',
                                'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 13; V2055A Build/TP1A.220624.014)',
                                'Host': 'apillkpro.cengaw.cn',
                                'Connection': 'Keep-Alive',
                                'Content-Type': 'application/x-www-form-urlencoded'
                            }
                            res6 = requests.request("POST", url6, headers=headers6, data="id=7")
                            if res6.json().get("code") == 40302:
                                print(f"已经领取过了，{res6.json().get('message')}")
                                break
                            elif res6.json().get("code") == 0:
                                print(
                                    f"今日视频资讯已完成,获得金币：{res6.json().get('result').get('coin')},提现券：{res6.json().get('result').get('coupon')}")
                                break
                            else:
                                print("可能完成了", res6.json())
                                break
                    elif res3.json().get("code") == 40301:
                        print(res3.json().get("message"))
                        break

                    time.sleep(15)
                print("---开始闯关")
                time.sleep(2)

                for i in range(7):
                    headers5 = {
                        'accept': 'application/json',
                        'device': device,
                        'oaid': device,
                        'store': 'baidu',
                        'version': '105',
                        'platform': '1',
                        'Authorization': f'Bearer {auth}',
                        'User-Agent': ua,
                        'Host': 'apillkpro.cengaw.cn',
                        'Connection': 'Keep-Alive',
                        'Content-Type': 'application/x-www-form-urlencoded'
                    }
                    data5 = f"no={i + 1}&ticket="
                    res8 = requests.request("GET", 'https://apillkpro.cengaw.cn/api/v2/reward/barrier/index',
                                            headers=headers5)
                    res5 = requests.request("POST", 'https://apillkpro.cengaw.cn/api/v2/reward/barrier/index',
                                            headers=headers5, data=f"no={i + 1}&ticket=")
                    data3 = res5.json().get("result")

                    if res5.json().get("code") == 0:
                        print(
                            f"闯关换手机第{i + 1}关，获得金币：{data3.get('coin')} 获得提现券：{data3.get('coupon')} 获得碎片：{data3.get('fragment')}")
                    elif res5.json().get("code") == 40301:
                        print(f"第{i + 1}关，{res5.json().get('message')}")


                    else:
                        print(res5.json())
                    time.sleep(15)

            else:
                print("---不在1-23点跳过任务执行")



    else:
        print("未知错误，请检查数据,可能封号了")
send("乐乐看pro提现",log_content)




