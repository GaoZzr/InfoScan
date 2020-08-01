#封装一些通用的请求方法

from config import *

import requests
import re
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()    #避免访问https网站时显示警告信息

# get请求方法
def http_requests_get(url, allow_redirects = allow_redirects):
    try:
        result = requests.get(
            url = url,
            headers = headers,
            timeout = timeout,
            allow_redirects = allow_redirects,
            verify = allow_ssl_verify
        )
        return result.text
    except Exception as e:
        return e

# POST 请求方法
def http_requests_post(url, data,allow_redirects = allow_redirects):
    try:
        result = requests.post(
            url = url,
            headers = headers,
            data = data,
            timeout = timeout,
            allow_redirects = allow_redirects,
            verify = allow_ssl_verify
        )
        return result.text
    except Exception as e:
        return e


# 判断是否是网址

def is_domain(domain):
    pattern = re.compile(
        r'^(([a-zA-Z]{1})|([a-zA-Z]{1}[a-zA-Z]{1})|'
        r'([a-zA-Z]{1}[0-9]{1})|([0-9]{1}[a-zA-Z]{1})|'
        r'([a-zA-Z0-9][-_.a-zA-Z0-9]{0,61}[a-zA-Z0-9]))\.'
        r'([a-zA-Z]{2,13}|[a-zA-Z0-9-]{2,30}.[a-zA-Z]{2,3})$'
    )
    return True if pattern.match(domain) else False

# 列表写入文件方法
def write(result):
    with open('result.txt','a') as f:
        for line in result:
            f.write(line + '\n')
        f.close()

# 整合列表结果
resultall = []
def result_end(result):
    #if result:
    for j in result:
        resultall.append(j)
    return resultall

# 打印列表结果
def print_result(result):
    for i in result:
        print(i)

# 打印时的异常处理
def print_try(res):
    try:
        print(res)
    except "TypeError: object of type 'IndexError' has no len()":
        pass