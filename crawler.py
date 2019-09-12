#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 10:43:04 2019

@author: Amy
"""

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class HorseSpider(CrawlSpider):
    
    name = 'Whirlaway'
    
    allowed_domains = ['treehouse-projects.github.io']
    
    start_urls = ['http://treehouse-prohects.github.io/horse-land']
    
    rules = [Rule(LinkExtractor(allow=r'.*'),
                  callback='parse_horses',
                  follow=True)]
    
    def parse_horse(self, response):
        url = response.url
        title = response.css('title')
        print('Page URL: {}'.format(url))
        print('Page title: {}'.format(title))
    
    