import scrapy


class StockbotsSpider(scrapy.Spider):
    name = 'stockbots'
    allowed_domains = ['https://finance.naver.com/item/frgn.nhn?code=005930']
    start_urls = ['http://https://finance.naver.com/item/frgn.nhn?code=005930/']

    def parse(self, response):
        pass
