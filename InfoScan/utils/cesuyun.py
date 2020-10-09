from common import *
class Cesuyun(object):
    def __init__(self,domain):
        self.domain = domain
        self.url = "http://ce.baidu.com/index/getRelatedSites?site_address="
        self.result = []

    def run(self):
        print("[*]正在通过cesuyun查询域名[*]")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'
        }
        url = self.url + self.domain
        try:
            CesuyunContent =  requests.get(url = url,headers = headers).text
            res = re.findall('{"domain":"(.*?)","score":',CesuyunContent)
            #print(res)
            for CesuyunSub in res:
                self.result.append(CesuyunSub)
            print_try("cesuyun查询完成,共" + str(len(self.result)) + "个域名\n")
            return list(set(self.result))  # 去重
        except Exception as e:
            return self.result