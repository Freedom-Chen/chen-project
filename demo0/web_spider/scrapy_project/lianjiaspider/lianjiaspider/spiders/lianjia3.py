# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.linkextractors import LinkExtractor
from lianjiaspider.items import LianjiaspiderItem
from scrapy.spiders import Rule


class Lianjia3Spider(RedisCrawlSpider):
    name = 'lianjia3'
    redis_key = 'lianjia3:start_urls'

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(Lianjia3Spider, self).__init__(*args, **kwargs)

    pagelink = LinkExtractor(restrict_xpaths=('//div[@class="page-box house-lst-page-box"]/a[text()="下一页"]'))
    contentlink = LinkExtractor(restrict_xpaths=('//a[@class="noresultRecommend img LOGCLICKDATA"]'))

    rules = [
        Rule(pagelink, follow=True),
        Rule(contentlink, follow=True, callback='parse_item')
    ]

    def parse_item(self, response):

        title = response.xpath('//h1[@class="main"]/text()')[0].extract().strip()
        print('title：', title)
        total = response.xpath('//span[@class="total"]/text()')[0].extract().strip()
        print('total：', total)
        price = response.xpath('//span[@class="unitPriceValue"]/text()')[0].extract().strip()
        print('price:', price)
        area = response.xpath('//div[@class="houseInfo"]/div[@class="area"]/div[@class="mainInfo"]/text()[last()]')[
            0].extract().strip()
        print('area:', area)
        hx = response.xpath('//div[@class="mainInfo"]/text()[1]')[0].extract().strip()
        print('hx:', hx)
        number = response.xpath('//div[@class="houseRecord"]/span[@class="info"]/text()')[0].extract().strip()
        print('number:', number)
        item = LianjiaspiderItem()
        item['title'] = title
        item['total'] = total
        item['price'] = price
        item['area'] = area
        item['hx'] = hx
        item['number'] = number

        yield item
