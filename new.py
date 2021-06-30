#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests



if __name__ == "__main__":
	#UA偽装
	headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
	}
	#urlを指定する
	url = 'httpS://www.sogou.com/web'

	#キーワード設定
	keyword = '古龙'

	param = {
		'query':keyword
	}

	#response
	response = requests.get(url=url,params=param,headers=headers)

	page_text = response.text

	#保存
	fileName = keyword + '.html'
	with open(fileName,'w',encoding='utf-8') as fp:
		fp.write(page_text)
	print('DONE!')