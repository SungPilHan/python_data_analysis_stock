import scrapy

class TopsbotsSpider(scrapy.Spider):
    name = 'topsbots'
    allowed_domains = ['finance.naver.com']
    start_urls = ['https://finance.naver.com/sise/sise_market_sum.nhn']

    def parse(self, response):
        tops_list = response.xpath('//*[@id="contentarea"]/div[3]/table[1]/tbody/tr/td[2]/a/@href').extract()
        with open('tops.txt','w') as tops_f:
            for idx in range(10):
                tops_f.write(tops_list[idx].split('=')[1].strip()+'\n')
