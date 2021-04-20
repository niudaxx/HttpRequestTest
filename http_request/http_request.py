# @Time:2021/4/20 17:50
# @Author:testDa
# @File:http_request.py
# @Reason: 接口测试用例类

import unittest
from http_request import base_request
from http_request.get_cookie import getCookie
baseReq = base_request.BaseRequest()
class Http_Request(unittest.TestCase):

    def __init__(self,methodName,url,data,http_type):
        super(Http_Request,self).__init__(methodName)
        self.url = url
        self.data = data
        self.http_type = http_type


    @classmethod
    def setUpClass(cls) -> None:
        baseReq.login_Request(url='http://localhost:8080/sisqp-web/j_spring_security_check',
                          data={'j_username': 'admin_1_12', 'userName': 'admin', 'j_password': 'f', 'companyId': '1',
                                'departmentId': '12'})

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_case(self):
        result = baseReq.Http_Request(self.url,self.data,self.http_type,cookies=getattr(getCookie,'cookie'),headers=getattr(getCookie,'headers'))
        print(result)




