# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaspiderItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    total = scrapy.Field()
    price = scrapy.Field()
    hx = scrapy.Field()
    area = scrapy.Field()
    number = scrapy.Field()


