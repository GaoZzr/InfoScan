# 备案信息
import re
from common import http_requests_get, is_domain, write

class Beian(object):      #定义一个类
    def __init__(self,domain):     #初始化
        self.domain = domain    # 接受域名信息
        self.site = "http://icp.bugscaner.com/host_"
        self.result = []    # 定义一个列表，接受返回结果
    def run(self):
        url = self.site+self.domain+'.html'
        try:
            res = http_requests_get(url = url)      #发起请求
            res1 = re.findall('主办单位性质</div><div class="line-value">(.*?)</div></div><div',res)
            res2 = re.findall('网站备案号</div><div class="line-value">(.*?)</div></div><div', res)
            res3 = re.findall('首页网址</div><div class="line-value">(.*?)</div></div><div', res)
            res_3 = re.findall('">(.*?)</a><br>', res3[0])

            res4 = re.findall('备案域名</div><div class="line-value">(.*?)</div></div><div', res)
            res5 = re.findall('审核时间</div><div class="line-value">(.*?)</div></div><div', res)
            res6 = re.findall('数据更新于</div><div class="line-value">(.*?)</div></div><div', res)

            res = re.findall('html" title="(.*?)">', res)
            return "主办单位性质: " + str(res1[0])+'\n'+"主办单位名称: " + res[5]+'\n'+"主办单位备案号: " + res[6]+'\n'+"网站名称: " + res[7]+'\n'+"网站备案号: " + str(res2[0])+'\n'+"首页网址: " + str(res_3[0])+'\n'+"备案域名: " + str(res4[0])+'\n'+"审核时间: " + str(res5[0])+'\n'+"数据更新于: " + str(res6[0])
        except Exception as e:
            return e