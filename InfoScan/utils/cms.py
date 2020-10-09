# 指纹识别

from config import *
from common import http_requests_post

class Cms(object):
    def __init__(self,domain):
        self.domain = domain
        self.site = 'http://whatweb.bugscaner.com/what.go'
        self.payload = {
            'url': domain,
            'location_capcha':'no'
        }
        self.result = []
    def run(self):
        print("[*]正在进行指纹识别[*]")
        try:
            res = http_requests_post(url = self.site, data = self.payload)
            res = res.replace(", ", "\n").replace("{", "").replace("}", "").encode('utf-8').decode('unicode_escape').replace('\"',' ')
            print('指纹识别完成')
            return res
        except Exception as e:
            return e
