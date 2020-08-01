# InfoScan
一个可进行备案信息查询，指纹信息查询，子域名爆破的工具
可自己在utils文件夹下添加其他模块

# 文件结构
>  ├─InfoScan
   │  common.py       #定义一些通用的方法
   │  config.py       #定义全局的变量
   │  InfoScan.py     #主程序文件
   │
   ├─dict
   │      dict.txt    #子域名爆破字典
   │
   ├─utils
      │  beian.py     #备案信息查询
      │  brutedomain.py     #子域名爆破
      │  cms.py       #网站指纹信息查询
      │  crt.py       #通过crt.sh网站进行子域名收集
      │  yumingco.py    #通过yumingco.com网站进行子域名收集
      │  __init__.py

# 使用方法
python3 InfoScan.py 域名  线程

# 效果截图
![](1.jpg)
![](2.jpg)
