import scrapy
from KDK_current_stock_price.items import KdkCurrentStockPriceItem
from scrapy.http import Request
import os

class PricebotsSpider(scrapy.Spider):
    name = 'pricebots'
    allowed_domains = ['finance.naver.com']
    start_urls = []
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    def __init__(self):
        base_url = 'http://finance.naver.com/item/sise.nhn?code={0}'
        start_page = 1
        with open(self.BASE_DIR + '/stock_list.txt', 'r') as stock_list:
            for stock in stock_list:
                for p in range(1):
                    temp_url = base_url.format(stock, start_page + p)
                    self.start_urls.append(temp_url)

    def parse(self, response):
        stock_names=response.xpath('//*[@id="middle"]/div[1]/div[1]/h2/a/text()').extract()
        stock_codes=response.xpath('//*[@id="middle"]/div[1]/div[1]/div/span[1]/text()').extract()
        buying_volume_nows=response.xpath('//*[@id="content"]/div[2]/div[2]/table[1]/tbody/tr[11]/td[5]/span/strong/text()').extract()
        buying_price_nows=response.xpath('//*[@id="content"]/div[2]/div[2]/table[1]/tbody/tr[11]/td[4]/span/strong/text()').extract()
        selling_volume_nows=response.xpath('//*[@id="content"]/div[2]/div[2]/table[1]/tbody/tr[7]/td[1]/span/strong/text()').extract()
        selling_price_nows=response.xpath('//*[@id="content"]/div[2]/div[2]/table[1]/tbody/tr[7]/td[2]/span/strong/text()').extract()
        selling_prices = response.xpath('//*[@id="content"]/div[2]/div[2]/table[1]/tbody/tr/td[2]/span/text()').extract()
        selling_volumes = response.xpath('//*[@id="content"]/div[2]/div[2]/table[1]/tbody/tr/td[1]/span/text()').extract()
        buying_prices = response.xpath('//*[@id="content"]/div[2]/div[2]/table[1]/tbody/tr/td[4]/span/text()').extract()
        
        buying_volumes = response.xpath('//*[@id="content"]/div[2]/div[2]/table[1]/tbody/tr/td[5]/span/text()').extract()
        items = []
        print(selling_prices,selling_volumes,buying_prices,buying_volumes)
        
        buying_volumes.append(buying_volume_nows[0].strip())
        buying_prices.append(buying_price_nows[0].strip())
        selling_volumes.append(selling_volume_nows[0].strip())
        selling_prices.append(selling_price_nows[0].strip())

        for idx in range(len(selling_volumes)):#len]
            item = KdkCurrentStockPriceItem()
            item['stock_name'] = stock_names[0].strip()
            item['stock_code'] = stock_codes[0].strip()
            item['selling_price'] = selling_prices[idx].strip()
            item['selling_volume'] = selling_volumes[idx].strip()
            item['buying_price'] = buying_prices[idx].strip()
            item['buying_volume'] = buying_volumes[idx].strip()
            items.append(item)
        
        return items
