# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KdkCurrentStockPriceItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    buying_volumes= scrapy.Field()
    buying_price = scrapy.Field()
    seling_volume= scrapy.Field()
    seling_price = scrapy.Field()
    
