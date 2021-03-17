# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PshInstitutStockItem(scrapy.Item):
    stock_name = scrapy.Field()
    stock_code = scrapy.Field()
    stock_date = scrapy.Field()
    institut_trading_volume = scrapy.Field()
