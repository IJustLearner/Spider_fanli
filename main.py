#coding=utf-8

import re
import sys
import time
import requests
from bs4 import BeautifulSoup

from Spider import spider_
from Format import format_


#在当前目录下保存
soure_html=".\\ReadMe.html"
soure_text=".\\ReadMe.txt"

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

            output = "\n#"+str(counts)+" >>"+str(title)+"\n#链接："+str(fanly_soure)+str(links)
            
            print(output)
            html_lists.append(output)
        self.list = html_lists
        return html_lists

    def checksToHtml(self):
        text = BeautifulSoup(self.html,'lxml')
        print("Title:",text.title.string)
        #print(text)
        #for x in range(1,10):
        #    element = text.find_all(attrs={'id' : x})[0].get_text()
        #    print(x," >> ",element)
       
        element = text.find_all('div',class_='zdm-list-item J-item-wrap')
        print(len(element))

        counts = 0
        html_lists = []
        for documents in element: 
            counts = counts + 1
            links = documents.find_all("a",attrs={"class":"J-item-track nodelog"})[0].get('href')
            documents = documents.find_all("a",attrs={"class":"J-item-track nodelog"})[0].get_text() 

            #a = documents.a

            #a['href'] = str(fanly_soure + links)
            #print("\n",counts,">>",documents)
            #print("\n链接：",fanly_soure+links)
            output = "##"+str(counts)+". ["+str(documents)+"]("+str(fanly_soure)+str(links)+")    "
            
            #print(output)
            html_lists.append(output)

        return documents      
   
if __name__ == "__main__":

    #抓取10页信息
    html = spider_().get_html(url=fanly_url , end_page=1 , max_time=0)

    #提取需要信息
    md = refine(html)

    #提取文档，规整数据，输出打印并写入本地
    data = md.checksToText()
    try:
        with open(soure_text,'a',encoding='utf-8') as file:

            format_.print_s(time.asctime( time.localtime(time.time()) ),file_name=file)
            format_.print_s(data,file_name=file)
            #file.write(str(data))
    except IOError as e:
        print('File Error:' + str(ioerr))
