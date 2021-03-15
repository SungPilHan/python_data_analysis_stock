import scrapy


class NewsbotsSpider(scrapy.Spider):
    name = 'newsbots'
    allowed_domains = ['https://finance.naver.com/item/news.nhn?code=005930']
    start_urls = ['http://https://finance.naver.com/item/news.nhn?code=005930/']

    def parse(self, response):
        pass
