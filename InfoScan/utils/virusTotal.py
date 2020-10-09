from common import *
import json
class Virus(object):
    def __init__(self,domain):
        self.domain = domain
        self.url = "https://www.virustotal.com/vtapi/v2/domain/report?apikey=e3ce6d7c072b832b91392dd57e8124c0a16775b80e04081c9827a74b5f79abe1&domain="
        self.result = []

    def run(self):
        print("[*]正在通过virusTotal查询域名[*]")
        url = self.url + self.domain
        try:
            virusTotalContent =  http_requests_get(url = url)
            for virusTotalSub in json.loads(virusTotalContent)['subdomains']:
                self.result.append(virusTotalSub)
            print_try("virusTotal查询完成,共" + str(len(self.result)) + "个域名")
            return list(set(self.result))  # 去重
        except Exception as e:
            return self.result