import scrapy
from KDK_current_stock_price.items import KdkCurrentStockPriceItem
from scrapy.http import Request

class PricebotsSpider(scrapy.Spider):
    name = 'pricebots'
    allowed_domains = ['finance.naver.com']
    start_urls = ['http://https://finance.naver.com/item/sise.nhn?code=005930']

    def __init__(self):
        base_url = 'https://finance.naver.com/item/sise.nhn?code={0}&page={1}'
        start_page = 1
        with open('./stock_list.txt', 'r') as stock_list:
            for stock in stock_list:
                for p in range(1):
                    temp_url = base_url.format(stock, start_page + p)
                    self.start_urls.append(temp_url)

    def parse(self, response):
        seling_prices = response.xpath('//*[@id="content"]/div[2]/div[2]/table[1]/tbody/tr/td[2]/span/text()').extract()
        seling_volumes = response.xpath('//*[@id="content"]/div[2]/div[2]/table[1]/tbody/tr/td[1]/span/text()').extract()
        buying_prices = response.xpath('//*[@id="content"]/div[2]/div[2]/table[1]/tbody/tr/td[4]/span/text()').extract()
        buying_volumes = response.xpath('//*[@id="content"]/div[2]/div[2]/table[1]/tbody/tr/td[5]/span/text()').extract()
        items = []
        print(seling_prices,seling_volumes,buying_prices,buying_volumes)
        for idx in range(len(seling_volumes)):#len
            item = KdkCurrentStockPriceItem()
            item['seling_price'] = seling_prices[idx].strip()
            item['seling_volume'] = seling_volumes[idx].strip()
            item['buying_price'] = buying_prices[idx].strip()
            item['buying_volume'] = buying_volumes[idx].strip()#매수 잔량
            items.append(item)
        return items
