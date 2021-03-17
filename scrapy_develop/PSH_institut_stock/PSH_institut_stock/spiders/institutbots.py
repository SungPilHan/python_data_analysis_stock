import scrapy
from PSH_institut_stock.items import PshInstitutStockItem
from scrapy.http import Request
import os

class InstitutbotsSpider(scrapy.Spider):
    name = 'institutbots'
    allowed_domains = ['finance.naver.com']
    start_urls= []
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))


    def __init__(self):
        base_url = 'https://finance.naver.com/item/frgn.nhn?code={0}&page={1}'
        start_page = 1
        with open(self.BASE_DIR + '/stock_list.txt', 'r') as stock_list:
            for stock in stock_list:
                for p in range(3):
                    temp_url = base_url.format(stock, start_page + p)
                    self.start_urls.append(temp_url)

    def parse(self, response):
        stock_names = response.xpath('//*[@id="middle"]/div[1]/div[1]/h2/a/text()').extract()
        stock_codes = response.xpath('//*[@id="middle"]/div[1]/div[1]/div/span[1]/text()').extract()
        stock_dates = response.xpath('//*[@id="content"]/div[2]/table[1]/tr/td[1]/span/text()').extract()
        institut_trading_volumes = response.xpath('//*[@id="content"]/div[2]/table[1]/tr/td[6]/span/text()').extract()

        items = []
        for idx in range(len(stock_dates)):
            item = PshInstitutStockItem()
            item['stock_name'] = stock_names[0].strip()
            item['stock_code'] = stock_codes[0].strip()
            item['stock_date'] = stock_dates[idx].strip()
            item['institut_trading_volume'] = institut_trading_volumes[idx].strip()
            items.append(item)
        return items
