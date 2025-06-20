from ast import literal_eval

import requests
import random
import json
import string
import io


class APICall:
    def __init__(self,base_url,auth_token):
        self.base_url = base_url
        # Auth token
        self.headers = {"Authorization":auth_token,"Content-Type": "application/json"}



    def get_request(self,url_):
        url = self.base_url + url_
        response = requests.get(url)
        assert response.status_code == 200
        return response
    def post_request(self,url_,data):
        url = self.base_url + url_
        response = requests.post(url,json=data,headers=self.headers)
        assert  response.status_code == 201
        return response
    def put_request(self,url_,data):
        url = self.base_url + url_
        response = requests.put(url,json=data,headers=self.headers)
        assert  response.status_code == 200
        return response
    def delete_request(self,url_):
        url = self.base_url + url_
        response = requests.delete(url,headers=self.headers)
        assert response.status_code == 204
    @staticmethod
    def get_auth_token():
        request_url = "https://api-dev.technica.vn/api/auth/v1/login"
        data = {
                   "username":"sale1",
                   "password":"123456"
               }
        json_object = json.dumps(data, indent=4)
        response = requests.post(url=request_url,data=json_object,headers = {"Content-Type": "application/json"})
        content = response.content
        s = json.load(io.BytesIO(content))
        aut_tocken = s['data']['jwtToken']
        return aut_tocken






