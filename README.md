# 2020.8.15
## InfoScan
一个可进行备案信息查询，指纹信息查询，子域名爆破的工具
可自己在utils文件夹下添加其他模块

## 文件结构
![](3.jpg)

## 使用方法
python3 InfoScan.py 域名  线程

## 效果截图
![](1.jpg)
![](2.jpg)

# 2020.10.09
**增加了更多查询接口，精简代码**
## crt查询结果
   yumingco查询
   ip138查询
   hackertarget查询
   virustotal查询
   Cesuyun查询

# 2020.10.13
## 增加命令行参数
![](123.png)
## 增加批量查询子域名和批量爆破子域名功能
单个url
```shell
root@kali:~/桌面/tools/InfoScan/InfoScan# python3 InfoScan.py  -u runoob.com -t 20

 ___        __      ____                  
|_ _|_ __  / _| ___/ ___|  ___ __ _ _ __  
 | || '_ \| |_ / _ \___ \ / __/ _` | '_ \ 
 | || | | |  _| (_) |__) | (_| (_| | | | |
|___|_| |_|_|  \___/____/ \___\__,_|_| |_|
                               By:CyzCc
                               Data:2020.08.12
        
Use: python3 InfoScan.py domain Thread
Example: python3 InfoScan.py -u baidu.com -t 100
Example: python3 InfoScan.py -f url.txt -t 100
当前域名runoob.com
[*]正在进行指纹识别[*]
指纹识别完成
[*]正在进行备案信息查询[*]
备案信息查询完成
[*]正在通过crt查询域名[*]
crt查询完成,共83个域名
[*]正在通过yumingco查询域名[*]
yumingco查询完成,共3个域名
[*]正在通过ip138查询域名[*]
ip138查询完成,共7个域名
[*]正在通过hackertarget查询域名[*]
hackertarget查询完成,共1个域名
[*]正在通过virusTotal查询域名[*]
virusTotal查询完成,共7个域名
[*]正在通过cesuyun查询域名[*]
cesuyun查询完成,共4个域名

[*]整合结果中(去重)[*]
[*]整合完成，共9个域名[*]
查询结果：

======备案信息======
主办单位性质: 个人
主办单位名称: 陈巧梅
主办单位备案号: 闽ICP备15012807号
网站名称: 菜鸟网
网站备案号: 闽ICP备15012807号-1
首页网址: www.runoob.com
备案域名: runoob.com
审核时间: 2015-06-30
数据更新于: 2015-07-01</div>

======指纹信息======
 status : 99
 Programming Languages : [ PHP ]
 url :  runoob.com 
 status_code : 200
 CDN : [ AliyunCdn 
 阿里云cdn缓存命中 ]
 Web Servers : [ Tengine ]
 Font Scripts : [ Font Awesome ]
 ip :  61.155.221.217 
 JavaScript Frameworks : [ jQuery 2.0.3 ]
 address :  江苏省苏州市昆山市 电信 
 CMS : [ WordPress ]

======子域名======
ww.runoob.com
c.runoob.com
www.runoob.com
cdn.static.runoob.com
static.runoob.com
tool.runoob.com
t.runoob.com
runoob.com
m.runoob.com
基础爬取完成，Q/q:保存查询结果并退出，B/b:继续爆破子域名:b
正在准备子域名爆破

[*]正在对runoob.com进行子域名爆破,请稍等[*]
[*]ALL: 33 | Thread: 20 | Schedule: 29 | Complete: 87.88% | Found: 1

爆破完成,共爆破出3个域名

ww.runoob.com
c.runoob.com
www.runoob.com
cdn.static.runoob.com
static.runoob.com
tool.runoob.com
t.runoob.com
runoob.com
m.runoob.com
所有子域名结果保存至result/runoob.com.txt
root@kali:~/桌面/tools/InfoScan/InfoScan# 

```


批量url扫描
```shell
root@kali:~/桌面/tools/InfoScan/InfoScan# python3 InfoScan.py -f subdomain.txt -t 20

 ___        __      ____                  
|_ _|_ __  / _| ___/ ___|  ___ __ _ _ __  
 | || '_ \| |_ / _ \___ \ / __/ _` | '_ \ 
 | || | | |  _| (_) |__) | (_| (_| | | | |
|___|_| |_|_|  \___/____/ \___\__,_|_| |_|
                               By:CyzCc
                               Data:2020.08.12
        
Use: python3 InfoScan.py domain Thread
Example: python3 InfoScan.py -u baidu.com -t 100
Example: python3 InfoScan.py -f url.txt -t 100
当前域名runoob.com
[*]正在进行指纹识别[*]
指纹识别完成
[*]正在进行备案信息查询[*]
备案信息查询完成
[*]正在通过crt查询域名[*]
crt查询完成,共83个域名
[*]正在通过yumingco查询域名[*]
yumingco查询完成,共3个域名
[*]正在通过ip138查询域名[*]
ip138查询完成,共7个域名
[*]正在通过hackertarget查询域名[*]
hackertarget查询完成,共1个域名
[*]正在通过virusTotal查询域名[*]
virusTotal查询完成,共7个域名
[*]正在通过cesuyun查询域名[*]
cesuyun查询完成,共4个域名

[*]整合结果中(去重)[*]
[*]整合完成，共9个域名[*]
查询结果：

======备案信息======
主办单位性质: 个人
主办单位名称: 陈巧梅
主办单位备案号: 闽ICP备15012807号
网站名称: 菜鸟网
网站备案号: 闽ICP备15012807号-1
首页网址: www.runoob.com
备案域名: runoob.com
审核时间: 2015-06-30
数据更新于: 2015-07-01</div>

======指纹信息======
 status : 99
 Programming Languages : [ PHP ]
 url :  runoob.com 
 status_code : 200
 CDN : [ AliyunCdn 
 阿里云cdn缓存命中 ]
 Web Servers : [ Tengine ]
 Font Scripts : [ Font Awesome ]
 ip :  61.155.221.217 
 JavaScript Frameworks : [ jQuery 2.0.3 ]
 address :  江苏省苏州市昆山市 电信 
 CMS : [ WordPress ]

======子域名======
runoob.com
static.runoob.com
tool.runoob.com
m.runoob.com
t.runoob.com
c.runoob.com
www.runoob.com
ww.runoob.com
cdn.static.runoob.com
所有子域名结果保存至result/runoob.com.txt
当前域名freebuf.com
[*]正在进行指纹识别[*]
指纹识别完成
[*]正在进行备案信息查询[*]
备案信息查询完成
[*]正在通过crt查询域名[*]
crt查询完成,共0个域名
[*]正在通过yumingco查询域名[*]
yumingco查询完成,共18个域名
[*]正在通过ip138查询域名[*]
ip138查询完成,共9个域名
[*]正在通过hackertarget查询域名[*]
hackertarget查询完成,共16个域名
[*]正在通过virusTotal查询域名[*]
virusTotal查询完成,共27个域名
[*]正在通过cesuyun查询域名[*]
cesuyun查询完成,共19个域名

[*]整合结果中(去重)[*]
[*]整合完成，共30个域名[*]
查询结果：

======备案信息======
主办单位性质: 企业
主办单位名称: 上海斗象信息科技有限公司
主办单位备案号: 沪ICP备13033796号
网站名称: 黑客与极客
网站备案号: 沪ICP备13033796号-1
首页网址: www.freebuf.com
备案域名: freebuf.com
审核时间: 2019-03-17
数据更新于: 2019-03-18</div>

======指纹信息======
 status : 99
 status_code : 200
 address :  北京市 阿里云BGP数据中心 
 url :  freebuf.com 
 ip :  123.56.129.169 
 JavaScript Frameworks : [ React 
 Nuxt.js 
 Vue.js 
 Ant Design ]
 CMS :  未知 
 CDN : [ Fireblade ]

======子域名======
zhuanlan.freebuf.com
www.freebuf.com
bar.freebuf.com
socket.freebuf.com
chat.freebuf.com
zhaopin.freebuf.com
company.freebuf.com
freebuf.com
user.freebuf.com
live.freebuf.com
fit.freebuf.com
product.freebuf.com
shop.freebuf.com
wittest.freebuf.com
my.freebuf.com
job.freebuf.com
m.freebuf.com
api.freebuf.com
push.freebuf.com
wit.freebuf.com
hackpwn.freebuf.com
freetalk.freebuf.com
search.freebuf.com
prize.freebuf.com
ai.freebuf.com
cis.freebuf.com
pay.freebuf.com
open.freebuf.com
static.freebuf.com
geekpwn.freebuf.com
所有子域名结果保存至result/freebuf.com.txt
当前域名zhihu.com
[*]正在进行指纹识别[*]
[*]正在进行备案信息查询[*]
备案信息查询完成
[*]正在通过crt查询域名[*]
crt查询完成,共34个域名
[*]正在通过yumingco查询域名[*]
yumingco查询完成,共51个域名
[*]正在通过ip138查询域名[*]
ip138查询完成,共35个域名
[*]正在通过hackertarget查询域名[*]
hackertarget查询完成,共14个域名
[*]正在通过virusTotal查询域名[*]
virusTotal查询完成,共100个域名
[*]正在通过cesuyun查询域名[*]
cesuyun查询完成,共52个域名

[*]整合结果中(去重)[*]
[*]整合完成，共131个域名[*]
查询结果：

======备案信息======
主办单位性质: 企业
主办单位名称: 北京智者天下科技有限公司
主办单位备案号: 京ICP备13052560号
网站名称: 知乎
网站备案号: 京ICP备13052560号-1
首页网址: www.zhihu.com
备案域名: zhihu.com
审核时间: 2017-05-31
数据更新于: 2017-06-01</div>

======指纹信息======
'ConnectTimeout' object has no attribute 'replace'

======子域名======
oauth.zhihu.com
mail.zhihu.com
video.zhihu.com
sms.zhihu.com
www4.zhihu.com
crash2.zhihu.com
news.at.zhihu.com
dudu.zhihu.com
sos.zhihu.com
static.daily.zhihu.com
zhuanlan.zhihu.com
crash.zhihu.com
mail-p2.newsletter.zhihu.com
push.zhihu.com
udd1i5.zhihu.com
mail-p4.newsletter.zhihu.com
newsletter2.zhihu.com
2fwww.zhihu.com
apply.zhihu.com
d0j1o9.zhihu.com
oia.zhihu.com
xg.zhihu.com
mail-p1.newsletter.zhihu.com
api2.zhihu.com
2019.zhihu.com
vpn.in.zhihu.com
lc-explore-push.zhihu.com
e.zhihu.com
lb-pkx01-offline.zhihu.com
s.zhihu.com
planets-cats.zhihu.com
gslb-pek01.zhihu.com
2014.zhihu.com
daily.zhihu.com
trends.zhihu.com
tencent-adn.zhihu.com
event.zhihu.com
wwww.zhihu.com
apilive.zhihu.com
api.zhihu.com
www2.zhihu.com
mqtt-app.zhihu.com
www-quic.zhihu.com
dispatcher.zhihu.com
upload.zhihu.com
postbox-callback.zhihu.com
coreuserbiz.zhihu.com
meteor.zhihu.com
comet.zhihu.com
planets-catb.zhihu.com
messaging.zhihu.com
c7wxky4x.zhihu.com
appcloud.zhihu.com
pu.zhihu.com
at.zhihu.com
www.zhihu.com
zhstatic.zhihu.com
z.zhihu.com
account.zhihu.com
eclipse2.zhihu.com
ad.zhihu.com
appcloud2.zhihu.com
link.zhihu.com
newsletter.zhihu.com
planets-catc.zhihu.com
adx-audit.zhihu.com
gslb-dsa-ali.zhihu.com
mqtt-web.zhihu.com
vpn.zhihu.com
m.zhihu.com
walletpay.zhihu.com
planets-cata.zhihu.com
analytics.zhihu.com
north.zhihu.com
nalendar.zhihu.com
mail-p1.mail.zhihu.com
zhi.zhihu.com
liukanshan.zhihu.com
baozipu.zhihu.com
bao.zhihu.com
solarflare03.zhihu.com
aidatatest.zhihu.com
pay.zhihu.com
earth.zhihu.com
promotion.zhihu.com
blog.zhihu.com
eclipse.zhihu.com
gslb-dsa-tc.zhihu.com
static.zhihu.com
static.analytics.zhihu.com
dudulogin.zhihu.com
2016.zhihu.com
zhihu-web-analytics.zhihu.com
promo.zhihu.com
zhihu.com
zhihu-analytics.zhihu.com
mail-p5.newsletter.zhihu.com
open.zhihu.com
worldcup2014.zhihu.com
2017.zhihu.com
mail-p3.newsletter.zhihu.com
club.zhihu.com
beacon.zhihu.com
dsa-tencent.zhihu.com
mqtt.zhihu.com
notification.zhihu.com
adx.zhihu.com
v.zhihu.com
status.zhihu.com
zhihu-app-analytics.zhihu.com
wwwwwwwwwww.zhihu.com
mail2.zhihu.com
activity.zhihu.com
club2014.zhihu.com
adstatic.zhihu.com
openapi.zhihu.com
beta.zhihu.com
lc-push.zhihu.com
mail-p6.newsletter.zhihu.com
gslb-dsa.zhihu.com
ms.zhihu.com
game002.zhihu.com
tmail.zhihu.com
tghd.zhihu.com
world.zhihu.com
lens.zhihu.com
news-at.zhihu.com
sugar.zhihu.com
bespoke.zhihu.com
web2.zhihu.com
unpkg.zhihu.com
所有子域名结果保存至result/zhihu.com.txt
批量爬取完成，Q/q:保存批量查询结果并退出，B/b:继续爆破子域名:b
正在准备子域名爆破

[*]正在对runoob.com进行子域名爆破,请稍等[*]
[*]ALL: 33 | Thread: 20 | Schedule: 33 | Complete: 100.0% | Found: 1

爆破完成,共爆破出3个域名

www.runoob.com
所有子域名结果保存至result/runoob.com.txt

[*]正在对freebuf.com进行子域名爆破,请稍等[*]
[*]ALL: 33 | Thread: 20 | Schedule: 33 | Complete: 100.0% | Found: 1

爆破完成,共爆破出3个域名

www.freebuf.com
所有子域名结果保存至result/freebuf.com.txt

[*]正在对zhihu.com进行子域名爆破,请稍等[*]
[*]ALL: 33 | Thread: 20 | Schedule: 31 | Complete: 93.94% | Found: 1

爆破完成,共爆破出12个域名

www.zhihu.com
所有子域名结果保存至result/zhihu.com.txt
[*]程序运行完成，是否将所有结果汇总到result.txt并去重[Y/N]:y
result/runoob.com.txt

result/freebuf.com.txt

result/zhihu.com.txt

处理完成！结果保存至result/result.txt
root@kali:~/桌面/tools/InfoScan/InfoScan# 

```
![]456.png
