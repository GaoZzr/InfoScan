# 通过yumingco.com第三方网站获取子域名
import re
from common import http_requests_get, is_domain, print_try

class Yumingco(object):      #定义一个类
    def __init__(self,domain):     #初始化
        self.domain = domain    # 接受域名信息
        self.site = "http://www.yumingco.com/sub/?subdomain="
        self.result = []    # 定义一个列表，接受返回结果
    def run(self):
        print("[*]正在通过yumingco查询域名[*]")
        url = self.site+self.domain
        try:
            res = http_requests_get(url = url)      #发起请求
            r1 = re.findall('main:(.*)\<br\>', res)
            r = re.findall('(.*?)\<br\>',"".join(r1))
            #return res.text
            #return r
            for result in  r:       #循环写入
                if is_domain(result):       # 判断是否为域名
                    self.result.append(result)    # 将结果添加到列表中
            print_try("yumingco查询完成,共"+str(len(self.result))+"个域名")
            return list(set(self.result))   #去重
        except Exception as e:
            return self.result