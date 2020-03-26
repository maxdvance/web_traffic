# Browser = User-Agent
import requests
import time
import random

url = ['https://www.google.com', 'https://www.github.com']

headers = {
    'cookie': 'uuid_tt_dd=3844871280714138949_20171108; kd_user_id=e61e2f88-9c4f-4cf7-88c7-68213cac17f7; UN=qq_40963426; BT=1521452212412; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=1788*1*PC_VC; smidV2=20180626144357b069d2909d23ff73c3bc90ce183c8c57003acfcec7f57dd70; __utma=17226283.14643699.1533350144.1533350144.1534431588.2; __utmz=17226283.1533350144.1.1.utmcsr=zhuanlan.zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/p/39165199/edit; TY_SESSION_ID=f49bdedd-c1d4-4f86-b254-22ab2e8f02f6; ViewMode=contents; UM_distinctid=165471259cb3e-02c5602643907b-5d4e211f-100200-165471259cc86; dc_session_id=10_1534471423488.794042; dc_tos=pdlzzq; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1534515139,1534515661,1534515778,1534515830; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1534515830; ADHOC_MEMBERSHIP_CLIENT_ID1.0=d480c872-d4e9-33d9-d0e5-f076fc76aa83',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
count = 1
countUrl = len(url)  # Visit count
while 1:
    for i in range(countUrl):
        try:
            response = requests.get(url[i], headers=headers)
            print(url[i])
            if 200 <= response.status_code < 400:
                print(response.status_code)
                print('Success ' + str(count), 'times')
                count = count + 1
                time.sleep(1+random.randint(0,3))
        except Exception:  # exception
            print(url[i])
            print('Failed and Retry')
            time.sleep(7)
