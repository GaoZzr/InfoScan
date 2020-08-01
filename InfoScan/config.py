# 定义一些全局变量

import random
import sys
# 是否开启https服务器的证书校验
allow_ssl_verify=False

# ===============================
# requests配置项
# ===============================

# 多线程线程数
thread_count = sys.argv[2]

# 域名
domain = sys.argv[1]

# 超时时间
timeout = 10

# 是否允许url重定向
allow_redirects = True

# 是否允许继承http Request类 的Sess ion支持，在发出的所有请求之间保持cookies.
allow_http_session = True

# 是否允许随机User-Agent
allow_random_useragent = False

# 是否允许随机X-Forwarded-For
allow_random_x_forward = False

# 随机的HTTP头
USER_AGENTS= [
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8"
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36"
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36"
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36"
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36"
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36"
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36"
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36"
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36"
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36"

]

# 随机生成User-Agent
def random_useragent(condition = False):
    if condition:
        return random.choice(USER_AGENTS)
    else:
        return USER_AGENTS[0]

#随机X-Forwarded-For. 动态IP
def random_x_forwarded_for(condition = False):
    if condition:
        return '%d.%d.%d.%d' % (random.randint(1, 254),random.randint(1, 254),random.randint(1, 254),random.randint(1, 254))
    else:
        return '8.8.8.8'



# HTTP头设置
headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'User-Agent': random_useragent(allow_random_useragent),
    'Connection': 'keep-alive',
    'X_FORWARDED_FOR': random_x_forwarded_for(allow_random_x_forward)
}