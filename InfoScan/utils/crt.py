# 通过crt.sh证书查询子域名
import re
from common import *

class Crt(object):      #定义一个类
    def __init__(self,domain):     #初始化
        self.domain = domain    # 接受域名信息
        self.site = "https://crt.sh/?q="
        self.result = []    # 定义一个列表，接受返回结果
    def run(self):
        print("[*]正在通过crt查询域名[*]")
        url = self.site+self.domain
        try:
            res = http_requests_get(url = url)      #发起请求
            r = re.findall('</TD>\n    <TD>(.*?)</TD>\n    <TD><A', res)
            #return res.text
            for result in  r:       #循环写入
                if is_domain(result):       # 判断是否为域名
                    self.result.append(result)    # 将结果添加到列表中
            print_try("crt查询完成,共"+str(len(self.result))+"个域名")
            return list(set(self.result))
        except Exception as e:
            return self.result