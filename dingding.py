import json

import requests


def ding_talk():
    # print(reponse)
    # if not reponse:
    #     return
    # date_response = json.loads(reponse.text)
    error = '失败'
    print (str(error))
    text = {"msgtype": "text", "text": {"content": 'orderid: %s, currentStatus: %s, 消息处理成功: %s' % ('hello', 2, 3)}}
    url = 'https://oapi.dingtalk.com/robot/send?access_token=bb9aa6fdac0b01bf47fbfa087840b5fff2e3ea9eff8face980ad17f5332d8815'
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data = json.dumps(text)
    info1 = requests.post(url=url, data=data, headers=headers).content
    print (info1)

if __name__ == '__main__':
   ding_talk()