import json

import requests
from werkzeug.security import generate_password_hash

token = generate_password_hash('qk')
def paid(order_ids, token):
    for orderid in order_ids:
        # 回传支付完成给财务系统
        data = {
            'order_no': [str(orderid)],
            'token': token
        }
        print(data)
        headers = {'Content-Type': 'application/json'}
        data = json.dumps(data)
        # reslut = requests.post(url='http://172.18.10.19:8008/api/purchase/pay_status/', data=data)
        reslut = requests.post(url='http://192.168.1.234:8008/api/purchase/pay_status/', data=data, headers=headers)
        print('财务系统返回信息:', reslut.text)

if __name__ == '__main__':
    # ,103871,103872,103901,103902
    order_ids = [103871,103872,103901,103902]
    paid(order_ids, token)
