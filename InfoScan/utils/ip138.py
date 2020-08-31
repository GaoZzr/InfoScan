# 通过yumingco.com第三方网站获取子域名
import re
from common import http_requests_get, is_domain, write

class Ip138(object):      #定义一个类
    def __init__(self,domain):     #初始化
        self.domain = domain    # 接受域名信息
        self.site = "https://site.ip138.com/"
        self.result = []    # 定义一个列表，接受返回结果
    def run(self):
        url = self.site+self.domain+"/domain.htm"
        try:
            res = http_requests_get(url = url)      #发起请求
            r1 = re.findall('target="_blank"\>(.*?)\</a\>\</p\>', res)
            #return r1
            for result in  r1:       #循环写入
                if is_domain(result):       # 判断是否为域名
                    self.result.append(result)    # 将结果添加到列表中
            #write(list(set(self.result)))
            return list(set(self.result))   #去重
        except Exception as e:
            return self.result
