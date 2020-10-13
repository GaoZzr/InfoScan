import time
from utils.crt import Crt
from utils.yumingco import Yumingco
from utils.brutedomain import Brutedomain
from utils.cms import Cms
from utils.beian import Beian
from utils.ip138 import Ip138
from utils.hackertarget import Hackertarget
from utils.virusTotal import Virus
from utils.cesuyun import Cesuyun
from common import *
import sys

def main():
    print('当前域名'+get_domain_root(url))
    # # ============cms查询============== # #
    result_cms = Cms(domain = get_domain_root(url)).run()
    # # ============网站备案信息============== # #
    result_beian = Beian(domain=get_domain_root(url)).run()
    # # ============子域名收集============== # #
    result1 = Crt(domain = get_domain_root(url)).run()
    result2 = Yumingco(domain = get_domain_root(url)).run()
    result3 = Ip138(domain = get_domain_root(url)).run()
    result4 = Hackertarget(domain=get_domain_root(url)).run()
    result5 = Virus(domain = get_domain_root(url)).run()
    result6 = Cesuyun(domain = get_domain_root(url)).run()

    # 将所有列表合并，方便去重整理结果
    result_end(result1)   #crt查询结果
    result_end(result2)   #yumingco查询结果
    result_end(result3)   # ip138查询结果
    result_end(result4)   #hackertarget查询结果
    result_end(result5)   # virustotal查询
    result_end(result6)   #Cesuyun查询
    result_chaxun = list(set(resultall))    #去重后的结果

    print("[*]整合结果中(去重)[*]")
    print_try("[*]整合完成，共"+str(len(result_chaxun))+"个域名[*]")
    #time.sleep(2)

    print("查询结果：\n")
    print("======备案信息======")
    print(result_beian)
    print("\n======指纹信息======")
    print(result_cms)
    print("\n======子域名======")
    print_result(result_chaxun)
    return result_chaxun

def brute_main():

    # ============子域名爆破============== #

    result_baopo = Brutedomain(domain = get_domain_root(url),thread_count=args.thread).run()
    # 将所有列表合并，方便去重整理结果
    result_end(result_baopo)    #爆破结果
    result_all = list(set(resultall))    #去重后的结果
    print_result(result_all)
    Baocun(url,result_all)      #将最终的结果保存到**.**.**.txt文件中


if __name__ == '__main__':
    print('''
 ___        __      ____                  
|_ _|_ __  / _| ___/ ___|  ___ __ _ _ __  
 | || '_ \| |_ / _ \___ \ / __/ _` | '_ \ 
 | || | | |  _| (_) |__) | (_| (_| | | | |
|___|_| |_|_|  \___/____/ \___\__,_|_| |_|
                               By:CyzCc
                               Data:2020.08.12
        ''')
    print("Use: python3 InfoScan.py domain Thread")
    print("Example: python3 InfoScan.py baidu.com 100")
    print("Example: python3 InfoScan.py baidu.com 100 > result.txt")
    args = parse_args()
    if args.file == None:
        url = Url(args.url)
        main()
        user_input(url,list(set(resultall)))
        brute_main()
        exit()
    else:
        for i in open(args.file,'r'):
            url = i.replace('\n','')
            main()
            Baocun(url,list(set(resultall)))
            resultall.clear()       # 清空列表，方便保存下一个url域名
        user_input2()
        for j in open(args.file,'r'):
            url = j.replace('\n', '')
            brute_main()
            resultall.clear()
    End()
    exit()
