# -*- coding: utf-8 -*-
# @Author: ijustlearner.github.io
# @Date:   2019-08-09 17:46:04
# @Last Modified by:   Administrator
# @Last Modified time: 2019-08-13 18:27:17

import time
import random
import requests

class spider_():
    """爬取网页"""
    def __init__(self):
        #设置User-Agent
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}
        #设置cookie
        self.cookie = {    }
        #设置代理
        self.proxies = {
                        #"http": "http://10.10.1.10:3128",
                        #"https": "http://10.10.1.100:4444",
        }
        #保存爬取的页面数据
        self.html = []

    def get_html(self,url,start_page=1,end_page=1,mini_time=0,max_time=2):
        """爬取指定网页，返回html页面
		url:待爬取网页链接
		start_page:爬取的起始页,默认为第一页
		end_page:爬取的结束页,默认为第一页
		mini_time:爬取网页时的最小休眠时间,默认为0
		max_time:爬取网页时的最大休眠时间，默认为2
        """
        if start_page<1:
            return "#页码输入错误"
        elif end_page>100:
            return "#页码超出范围，请输入1-100的整数!"
        time_start1 = time.time()
        for i in range(start_page,end_page+1):
            time_start2 = time.time()
            try:
                url_sourse = url+str(i)
                r = requests.get(url_sourse,headers=self.header,timeout=10)
                r.encoding = 'utf-8'  
                #print(r.headers)
                r.raise_for_status()  # 如果响应状态码不是 200，就主动抛出异常
                #data = str(r)
                self.html.append(r.text) #将爬取的多个页面合并

                time_end2=time.time()   
                print("#GET:",url_sourse," status_code:",r.status_code," encode:",r.encoding,"\t#Cost time:",round(time_end2-time_start2,2),"s" )

                time.sleep(random.uniform(mini_time, max_time))	#随机休眠mini_time~max_time秒

            except requests.RequestException as e:
                print("#ERROR:拒绝连接！")	

        time_end1=time.time()
        print("#Total time:",round(time_end1-time_start1,2),"s" )
        return str(self.html)
