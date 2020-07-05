# class MaoyanSpider(scrapy.Spider):
#     name = 'MaoYan'
#     allowed_domains = ['maoyan.com']
#     start_urls = ['https://maoyan.com/films?showType=3']

#     def parse(self, response):
#         pass



# -*- coding: utf-8 -*-
import scrapy
from Spiders.items import SpidersItem
# from bs4 import BeautifulSoup
from scrapy.selector import Selector


class DoubanSpider(scrapy.Spider):
    # 定义爬虫名称
    name = 'MaoYan'
    allowed_domains = ['maoyan.com']
    # 起始URL列表
    start_urls = ['https://maoyan.com/films?showType=3']

#   注释默认的parse函数
#   def parse(self, response):
#        pass


    # 爬虫启动时，引擎自动调用该方法，并且只会被调用一次，用于生成初始的请求对象（Request）。
    # start_requests()方法读取start_urls列表中的URL并生成Request对象，发送给引擎。
    # 引擎再指挥其他组件向网站服务器发送请求，下载网页
    # def start_requests(self):
    #     # for i in range(0, 10):
    #         # i=0
    #         # url = f'https://movie.douban.com/top250?start={i*25}'
    #         url = f'https://maoyan.com/films?showType=3'
    #         yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)
            # url 请求访问的网址
            # callback 回调函数，引擎回将下载好的页面(Response对象)发给该方法，执行数据解析
            # 这里可以使用callback指定新的函数，不是用parse作为默认的回调参数

    # 解析函数
    def parse(self, response):
        try:
            for Selector in response.xpath('//div[@class="movie-hover-info"]')[:10]:
                item = SpidersItem()
                item['title'] = Selector.xpath('./div[1]/span[1]/text()').extract_first()
                item['movie_type'] = Selector.xpath('./div[2]/text()[2]').extract_first().strip()
                item['time'] = Selector.xpath('./div[4]/text()[2]').extract_first().strip()
                yield item
        except Exception as f:
            self.logger.error(f)
            
            
