#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__author__ = 'Kandy.Ye'
__mtime__ = '2017/4/12'
"""

import re
import logging
import json
import requests
from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import Request
#from items import *
from selenium import webdriver
import time
import urllib2

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


key_word = ['book', 'e', 'channel', 'mvd', 'list']
Base_url = 'https://list.jd.com'
price_url = 'https://p.3.cn/prices/mgets?skuIds=J_'
comment_url = 'https://club.jd.com/comment/productPageComments.action?productId=%s&score=0&sortType=5&page=%s&pageSize=10'
favourable_url = 'https://cd.jd.com/promotion/v2?skuId=%s&area=1_72_2799_0&shopId=%s&venderId=%s&cat=%s'


allNum = 0


wantList = [
            "手机", 
            "家用电器", 
            "数码", 
            "电脑办公", 
            #"钟表"
            ]

smallNotWantList = [
                    "选号中心",
                    "装宽带",
                    "办套餐",
                    "手机贴膜",
                    "数据线",
                    "手机保护套",
                    "创意配件",
                    "手机饰品",
                    "酒柜",
                    "冲印服务",
                    "手机电池",
                    "延保服务",
                    "杀毒软件",
                    "积分商品",
                    
                    "组装电脑",
                    "纸类",
                    "办公文具",
                    "学生文具",
                    "财会用品",
                    "文件管理",
                    "本册/便签",
                    "笔类",
                    "画具画材",
                    "刻录碟片/附件",
                    "上门安装",
                    "延保服务",
                    "维修保养",
                    "电脑软件",
                    "办公家具"
                    ]



class HandBookSpider(Spider):

    name = "HandBookSpider"
    allowed_domains = ["jd.com", "haier.com"]
    start_urls = [
        'https://www.jd.com/allSort.aspx'
    ]
    logging.getLogger("requests").setLevel(logging.ERROR)  # 将requests的日志级别设成WARNING

    tampleUrl = "http://www.haier.com/was5/web/search?channelid=249897&searchword="

    searchList = ["EG8014BDX59SDU1"]
    
    
    body = {
                "query": {
                    "bool": {
                        "must": [{
                            "term": {
                                "brand": ["海尔（Haier）", "海尔", "海尔 Haier"]
                            }
                        }],
                        "must_not": [{
                            "term": {
                                "model": "unknown"
                            }
                        }]
                    }
                }
            }

    
    
    def __init__(self):
        
        self.driver = webdriver.PhantomJS(executable_path=r"E:\phantomjs-2.1.1-windows\bin\phantomjs.exe")
        #self.driver2 = webdriver.PhantomJS(executable_path=r"E:\phantomjs-2.1.1-windows\bin\phantomjs.exe")

    def start_requests(self):
        


#         headersLocal = {
#               "Date":"Wed, 16 May 2018 08:30:00 GMT",
#               "Server":"QTWS",
#               "Content-Type":"text/html;charset=UTF-8",
#               "Transfer-Encoding": "chunked",
#               "Set-Cookie": "JSESSIONID=280171E1000219818A2C242C15C081A4; Path=/was5",
#               "Expires": "Wed, 31 Dec 1969 23:59:59 GMT",
#               "max-age": "Thu, 01 Jan 1970 00:00:00 GMT",
#               "Set-Cookie": "cn_was_fuseatch=EG8014BDX59SDU1; Expires=Wed, 16-May-2018 09:29:59 GMT",
#               "Set-Cookie": "sto-id-20480-web_8080=ANLPJPAKJABP; Expires=Sat, 13-May-2028 08:35:19 GMT; Path=/",
#               "X-Via": "1.1 jszjsx47:6 (Cdn Cache Server V2.0), 1.1 PSbjsjqwtxu192:8 (Cdn Cache Server V2.0)",
#               "Connection": "close",
#               "X-Dscp-Value": 0,
#               "Cookie": "cn_was_fuseatch=EG8014BDX59SDU1; JSESSIONID=25DE3988CE91D10912F972BA96777FE8; sto-id-20480-web_8080=AKLPJPAKJABP; sto-id-36895-haierhudong_8080=FFLPJPAKJABP; _trs_uv=jh68irce_259_o7z; _trs_ua_s_1=jh8v4777_259_f75t; hn_app_num=0; hn_active_num=0; hn_shuomingshu_num=0; hn_service_num=0; hn_drive_num=0; hn_product_num=13; hn_bbs_num=45; _h_cur_co_inv=1df18473f7554af3b8dcc186ef544558-15264604035314720; h_trs_frequency_1=1"
#             }
        
        for item in self.searchList:
            
            
            
            requestUrl = self.tampleUrl+item
            
            #print requestUrl
            
            #driver = webdriver.PhantomJS(executable_path=r"E:\phantomjs-2.1.1-windows\bin\phantomjs.exe")

            #responseStr = response.read()
            
            meta = {}
            #meta["str"] = responseStr
            meta["keyWord"] = item
            
            ret = es.search(index="jd-classify",doc_type="event",body=body)
            
            
            print ret
            #yield Request(url=requestUrl, callback=self.parse_search_ret, meta=meta)
            
            
            
    def parse_search_ret(self, response):
        
        meta =  response.meta
        
        #body = '<html><body><span>good</span></body></html>'
        
        #print meta["str"]
        
        requestUrl = response.url
        
        print requestUrl
        
        self.driver.get(requestUrl)
        time.sleep(5)
        responseStr = self.driver.page_source
        
        keyWord = meta["keyWord"]
        
        #print "^^^^^^^^"+keyWord
        
        selector = Selector(text = responseStr)
        
        #print selector
        
        try:
            texts = selector.xpath('//*[@id="productlist"]/div[@class="hs-sr-display"]/div[@class="hn_probox"]/ul[@class="js_prolist"]/li[@class="repost_js_prostyleimg"]/div[@class="cont js_prostyleimg cur"]/h2/a').extract()
            
            
            
            #texts = selector.xpath('//*[@id="productlist"]').extract()
            
            #print texts
            
            for text in texts:
                #print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
                #print text
                keyItems = re.findall(r'href="(.*?)">(.*?)<span style="color:#f00">(.*?)</span>', text)
                #if text == keyWord:
                #print keyItems

                if len(keyItems) > 0:
                
                   hrefUrl = "http:"+keyItems[0][0]
                   searchText = keyItems[0][2]
                   retKeyword = keyItems[0][1]
                   
                   #print "$$$$$$$$"+retKeyword
                   
                   if keyWord == searchText:
                
                       print hrefUrl
                       print searchText
                       
                       yield Request(url=hrefUrl, callback=self.parse_support)
                   
                   #print selector
                
                    
            
            
        except Exception as e:
            print('error:', e)
            

    
    
    def parse_support(self, response):
        hrefUrl = response.url
        self.driver.get(hrefUrl)
        time.sleep(5)
        responseStr = self.driver.page_source
                   
        selector = Selector(text = responseStr)
        
        print selector
        
        try:
            texts = selector.xpath('//*[@id="salesSupport"]/div[@class="content"]/div[@class="side_l"]/div[@class="hn_pro_service"]/table/tbody/tr[2]/td/a').extract()
            
            for text in texts:
                print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
                print text
                
                keyItems = re.findall(r'href="(.*?)"', text)
                
                print keyItems
                if len(keyItems) > 0:
                    hrefUrl = "http:"+keyItems[0].strip()
                    if "%" in hrefUrl:
                        
                        hrefUrl = hrefUrl[0:hrefUrl.index('%')]
                        #hrefUrl = hrefUrl.subString(0, hrefUrl.index('%'))
                        
            
        except Exception as e:
            print('error:', e)
