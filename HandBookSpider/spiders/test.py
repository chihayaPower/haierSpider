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
from elasticsearch import Elasticsearch
import datetime
import urllib2
import httplib
from selenium import webdriver
import time




if __name__ == '__main__':
    
    url = "http://www.haier.com/was5/web/search?channelid=249897&searchword=EG8014BDX59SDU1"
    
#     handler=urllib2.HTTPHandler(debuglevel=1) 
#     opener = urllib2.build_opener(handler) 
#     urllib2.install_opener(opener) 
#     
#     response = urllib2.urlopen(url)
#     print response.read()

    driver = webdriver.PhantomJS(executable_path=r"E:\phantomjs-2.1.1-windows\bin\phantomjs.exe")
    driver.get(url)
    time.sleep(3)
    body = driver.page_source
    print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$44"
    print body
    #print res
