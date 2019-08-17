#coding=utf-8

import re
import sys
import time
import requests
from bs4 import BeautifulSoup

from Spider import spider_
from Format import format_


#在当前目录下保存
soure_path=".\\ReadMe.txt"

#抓取地址
fanly_url="https://zhide.fanli.com/p"
#源地址
fanly_soure="https://zhide.fanli.com"

class refine():
    """提取需要的内容"""

    def __init__(self,html):
        super(refine, self).__init__()
        self.html = html
        self.list = []
        
    def checksToText(self):
        """提炼需要的内容保存在html_lists列表中"""

        text = BeautifulSoup(self.html,'lxml')  
        element = text.find_all('div',class_='zdm-list-item J-item-wrap')
        print("------------------------------------------------------------------------------")
        print("#Title:",text.title.string)
        print("#Messages:",len(element))

        counts = 0
        html_lists = []
        #遍历数据
        for documents in element: 
            counts = counts + 1
            #获取链接
            links = documents.find_all("a",attrs={"class":"J-item-track nodelog"})[0].get('href')            
            #获取推荐人
            itme_user = documents.find_all("div",attrs={"class":"item-user"})[0].get_text()
            #获取标签分类
            tags = documents.find_all("a",attrs={"class":"nine"})[0].get_text()
            #获取发布时间
            time_info = documents.find_all("div",attrs={"class":"item-time"})[0].get_text()
            #获取点赞数量
            vote_yes = documents.find_all("a",attrs={"class":"l item-vote-yes J-item-vote-yes"})[0].get_text()
            #获取差评数量
            vote_no = documents.find_all("a",attrs={"class":"l item-vote-no J-item-vote-no"})[0].get_text()
            #获取标题
            title = documents.find_all("a",attrs={"class":"J-item-track nodelog"})[0].get_text()
            #按打印格式连接字符串
            output = "\n#"+str(counts)+" >>"+\
                    str(title)+"\n#链接："+str(fanly_soure)+str(links)+\
                    "\n#发布时间："+str(time_info)+"\t#分类："+str(tags)+"\t#"+str(itme_user)+\
                    "\n#值："+str(vote_yes)+"\t#呸："+str(vote_no)
            
            print(output)
            html_lists.append(output)

        self.list = html_lists

        return html_lists
       
if __name__ == "__main__":

    #抓取5页信息,设置爬取最大休眠时间为1秒
    html = spider_().get_html(url=fanly_url , end_page=5 , max_time=1)

    #提取需要信息
    md = refine(html)

    #提取文档，规整数据，输出打印并写入本地
    data = md.checksToText()
    try:
        with open(soure_path,'a',encoding='utf-8') as file:

            format_.print_s(data,file_name=file)

    except IOError as e:
        print('File Error:' + str(ioerr))
