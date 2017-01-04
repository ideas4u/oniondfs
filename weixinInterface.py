# -*- coding: utf-8 -*-
import hashlib
import web
import lxml
import time
import os
import urllib2, json
from lxml import etree

class WeixinInterface:
	def __init__(self):
		self.app_root = os.path.dirname(__file__)
		self.templates_root = os.path.join(self.app_root,'templates')
		self.render = web.template.render(self.templates_root)

	def GET(self):
		#get the input paramater
		data = web.input()
		signature = data.signature
		timestamp = data.timestamp
		nonce = data.nonce
		echostr = data.echostr

		# your token
		token = "xxx" # here change to ur wechar platform token
		# dict sort
		list=[token,timestamp,nonce]
		list.sort()
		sha1 = hashlib.sha1()
		map(sha1.update,list)
		hashcode = sha1.hexdigest()

		# sha1 recode athgridem

		# if the request is from wechar ,then reply echostr
		if hashcode == signature:
			return echostr
	def POST(self):
		str_xml = web.data() # get the data from post
		xml = etree.fromstring(str_xml) # XML process
		content = xml.find("Content").text # get the content user input
		msgType = xml.find("MsgType").text
		fromUser = xml.find("FromUserName").text
		toUser = xml.find("ToUserName").text
		return self.render.reply_text(fromUser,toUser,int(time.time()),u"it is develeping, nothing more function, you just said: " + content)

