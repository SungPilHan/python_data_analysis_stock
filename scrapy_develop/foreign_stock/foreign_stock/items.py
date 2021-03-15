# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ForeignStockItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    stock_name = scrapy.Field()
    stock_date = scrapy.Field()
    foreign_trading_volume = scrapy.Field()
    foreign_rate = scrapy.Field()
