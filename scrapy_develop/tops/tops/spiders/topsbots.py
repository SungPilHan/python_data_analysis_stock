import scrapy
import os
import platform

class TopsbotsSpider(scrapy.Spider):
    name = 'topsbots'
    allowed_domains = ['finance.naver.com']
    start_urls = ['https://finance.naver.com/sise/sise_market_sum.nhn']
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    def parse(self, response):
        tops_list = response.xpath('//*[@id="contentarea"]/div[3]/table[1]/tbody/tr/td[2]/a/@href').extract()
        if platform.system() == 'Windows':
            stock_list_path = self.BASE_DIR+'\\..\\..\\..\\stock_list.txt'
        else:
            stock_list_path = self.BASE_DIR+'/../../../stock_list.txt'
        with open(stock_list_path,'w') as tops_f:
            for idx in range(10):
                tops_f.write(tops_list[idx].split('=')[1].strip()+'\n')
