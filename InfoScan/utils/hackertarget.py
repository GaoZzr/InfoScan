import re
from common import *

class Hackertarget(object):
    def __init__(self,domain):
        self.domain = domain
        self.url = "https://api.hackertarget.com/hostsearch/?q="
        self.result = []
    def run(self):
        print("[*]正在通过hackertarget查询域名[*]")
        url = self.url+self.domain
        try:
            res = http_requests_get(url=url)
            res2 = re.findall('\n(.*),',res)
            for result in res2:  # 循环写入
                if is_domain(result):  # 判断是否为域名
                    self.result.append(result)  # 将结果添加到列表中
            print_try("hackertarget查询完成,共" + str(len(self.result)) + "个域名")
            return list(set(self.result))  # 去重
        except Exception as e:
            return self.result



