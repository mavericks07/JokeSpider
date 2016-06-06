# -*- coding: UTF-8 -*-
"""
Created on 2016/6/2

@author: mavericks
"""

from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request
from ..items import JokespiderItem
import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class jSpider(CrawlSpider):
    name = "j"
    #redis_key = "j:start_urls"
    start_urls = ['http://www.jokeji.cn/list43_1.htm', #冷笑话
                  'http://www.jokeji.cn/list13_1.htm', #社会
                  'http://www.jokeji.cn/list5_1.htm',  #校园
                  'http://www.jokeji.cn/list1_1.htm',  #夫妻
                  'http://www.jokeji.cn/list7_1.htm',  #儿童
                  'http://www.jokeji.cn/list16_1.htm', #职场
                  ''
                  ]
    main = 'http://www.jokeji.cn'

    def parse(self, response):
        selector = Selector(response)
        all = selector.xpath('/html/body/div[3]/div[1]/div[2]/ul/li/b/a')
        last_page = selector.xpath('//div[@class="next_page"]/a[last()]/@href').extract()[0]
        list_num = re.findall('(.*_)\d*\.htm', last_page)[0]
        last_num = int(re.findall('.*_(\d*)\.htm', last_page)[0])
        for i in xrange(2, last_num):
            link = self.main + '/' + list_num + str(i) + '.htm'
            yield Request(link, callback=self.parse_link)
        for each in all:
            item = JokespiderItem()
            url = self.main + each.xpath('@href').extract()[0]
            item['title'] = each.xpath('text()').extract()[0]
            yield Request(url, callback=self.parse_content, meta={'item': item})

    def parse_link(self, response):
        selector = Selector(response)
        all = selector.xpath('/html/body/div[3]/div[1]/div[2]/ul/li/b/a')
        for each in all:
            item = JokespiderItem()
            url = self.main + each.xpath('@href').extract()[0]
            item['title'] = each.xpath('text()').extract()[0]
            yield Request(url, callback=self.parse_content, meta={'item': item})

    def parse_content(self, response):
        selector = Selector(response)
        item = response.meta['item']
        all = selector.xpath('//p').extract()
        type = selector.xpath('/html/body/div/div/div/h1/a[2]/text()').extract()[0]
        item['type'] = type
        content = ''
        for each in all:
            each = str(each).replace('<br>', '\n').replace('<p>', '').replace('</p>', '')\
                .replace('<font face="Verdana">', '').replace('</font>', '')
            # each = re.sub('<.*>', '', each).strip()
            content += each + '\n'
        item['content'] = content
        yield item



