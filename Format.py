# -*- coding: utf-8 -*-
# @Author: ijustlearner.github.io
# @Date:   2019-08-09 17:46:04
# @Last Modified by:   Administrator
# @Last Modified time: 2019-08-13 12:10:39

import	sys

class format_():
	"""格式化输出"""
	def __init__(self, arg):
		super(format_, self).__init__()
		self.arg = arg

	def print_s(the_list, level=0, d='\t', indent=False, file_name=sys.stdout):  
		'''函数print_s， 使用递归的方式输出一个可能嵌套有其他列表的列表  
		参数the_list， 是需要输出的列表  
		参数level， 是整形，表示缩进级别，默认值为0  
		参数d， 是字符串，表示缩进符号，默认值为制表符  
		参数indent， 是一个布尔值，表示是否进行缩进，默认为否 
		参数file_name, 为需要写入的文件名，默认为不写入任何文件直接输出'''    

		for each_item in the_list:    
		    if isinstance(each_item, list):    
		        print_s(each_item, level+1, file_name)    
		    else:    
		        if indent:  
		            for tab_stop in range(level):  
		                print(d, end = '', file = file_name)    
		    print(each_item, file = file_name)