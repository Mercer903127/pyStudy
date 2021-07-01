#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import json
from requests.api import post

if __name__ == "__main__":
	#UA偽装
	headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
	}

	post_url = 'https://fanyi.baidu.com/sug'

	word = 'new'
	data = {
		'kw':word
	}

	response = requests.post(url=post_url,data=data,headers=headers)

	dic_obj = response.json()

	fileName = word + '.json'
	fp = open(fileName,'w',encoding='utf-8')
	json.dump(dic_obj,fp=fp,ensure_ascii=False)

	print('DONE!')