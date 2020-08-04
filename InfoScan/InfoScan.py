# 导入crt.py中的Crt对象
import time
from utils.crt import Crt
from utils.yumingco import Yumingco
from utils.brutedomain import Brutedomain
from utils.cms import Cms
from utils.beian import Beian
from utils.ip138 import Ip138
from common import *
import sys

def main():
    # ============cms查询============== #

    print("[*]正在进行指纹识别[*]")
    result5 = Cms(domain = sys.argv[1]).run()
    print('指纹识别完成')

    # ============网站备案信息============== #
    print("[*]正在进行备案信息查询[*]")
    result6 = Beian(domain=sys.argv[1]).run()
    print('备案信息查询完成')

    # ============子域名收集============== #

    print("[*]正在通过crt查询域名[*]")
    result1 = Crt(domain = sys.argv[1]).run()
    print_try("crt查询完成,共"+str(len(result1))+"个域名")

    print("[*]正在通过yumingco查询域名[*]")
    result2 = Yumingco(domain = sys.argv[1]).run()
    print_try("yumingco查询完成,共"+str(len(result2))+"个域名")

    print("[*]正在通过ip138查询域名[*]")
    result3 = Ip138(domain = sys.argv[1]).run()
    print_try("ip138查询完成,共"+str(len(result3))+"个域名\n")

    # 将所有列表合并，方便去重整理结果
    result_end(result1)   #crt查询结果
    result_end(result2)   #yumingco查询结果
    result_end(result3)   # ip138查询结果
    #result_end(result)    #爆破结果
    result4 = list(set(resultall))    #去重后的结果

    print("[*]整合结果中(去重)[*]")
    print_try("[*]整合完成，共"+str(len(result4))+"个域名[*]")
    time.sleep(3)

    print("查询结果：\n")
    print("======备案信息======")
    print(result6)
    print("\n======指纹信息======")
    print(result5)
    print("\n======子域名======")
    print_result(result4)

    # ============子域名爆破============== #
    user_input()
    print("\n[*]正在进行子域名爆破,预计用时3分钟[*]")
    result = Brutedomain(domain = sys.argv[1]).run()
    print_try("爆破完成,共"+str(len(result))+"个域名\n")

    # 将所有列表合并，方便去重整理结果
    result_end(result1)   #crt查询结果
    result_end(result2)   #yumingco查询结果
    result_end(result3)   # ip138查询结果
    result_end(result)    #爆破结果
    result9 = list(set(resultall))    #去重后的结果
    print(result9)
if __name__ == '__main__':
    print('''
 ___        __      ____                  
|_ _|_ __  / _| ___/ ___|  ___ __ _ _ __  
 | || '_ \| |_ / _ \___ \ / __/ _` | '_ \ 
 | || | | |  _| (_) |__) | (_| (_| | | | |
|___|_| |_|_|  \___/____/ \___\__,_|_| |_|
            
        ''')
    print("Use: python3 InfoScan.py domain Thread")
    print("Example: python3 InfoScan.py baidu.com 100")
    print("Example: python3 InfoScan.py baidu.com 100 > result.txt")
    main()
