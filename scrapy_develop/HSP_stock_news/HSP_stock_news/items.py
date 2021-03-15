# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HspStockNewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    article_title = scrapy.Field()
    article_url = scrapy.Field()
    article_author = scrapy.Field()
    article_date = scrapy.Field()
