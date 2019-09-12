#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 02:19:45 2019

@author: Amy
"""

import  scrapy
class HorseSpider(scrapy.Spider):
    
    name = 'ike'
    
    def start_requests(self):
        urls = ['https://treehouse-projects.github.io/horse-land/index.html',
                'https://treehouse-projects.github.io/horse-land/mustang.html']
        
        return [scrapy.Request(url=url, callback=self.parse) for url in urls]
    
    def parse(self, response):
        url = response.url
        page = url.split('/')[-1]
        filename = 'horse-%s' %page
        print('URL is: {}'.format(url))
        with open(filename,'wb') as file:
            file.write(response.body)
        print('Saved file %s' % filename)
    