# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KdkCurrentStockPriceItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    buying_volume= scrapy.Field()
    buying_price = scrapy.Field()
    selling_volume= scrapy.Field()
    selling_price = scrapy.Field()
    
