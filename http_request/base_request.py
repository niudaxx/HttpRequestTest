# @Time:2021/4/20 17:26
# @Author:testDa
# @File:base_request.py
# @Reason: 接口基础类

import requests
from http_request.get_cookie import getCookie
class BaseRequest():

    def login_Request(self,url,data):
        session = requests.session()
        session.get(url=url,data=data)
        setattr(getCookie, 'cookie', session.cookies)
        setattr(getCookie, 'headers', session.headers)

    def Http_Request(self,url,data,http_type,headers=None,cookies=None):
        result = None
        session = requests.session()
        try:
            if http_type=='get':
                result = session.get(url=url,data=data,headers=headers,cookies=cookies)
            elif http_type=='post':
                result = session.post(url=url,data=data,headers=headers,cookies=cookies)
            else:
                print('暂不支持其它httprequest请求方式')
        except Exception as e:
            print(e)

        return result