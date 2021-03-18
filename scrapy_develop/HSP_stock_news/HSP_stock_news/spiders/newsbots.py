import scrapy
from HSP_stock_news.items import HspStockNewsItem
import os
import platform

class NewsbotsSpider(scrapy.Spider):
    name = 'newsbots'
    allowed_domains = ['finance.naver.com']
    start_urls = []
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    def __init__(self):
        base_url = 'https://finance.naver.com/item/news_news.nhn?code={0}&page={1}&sm=title_entity_id.basic&clusterId='
        start_page = 1

        if platform.system() == 'Windows':
            stock_list_path = self.BASE_DIR+'\\..\\..\\..\\stock_list.txt'
        else:
            stock_list_path = self.BASE_DIR+'/../../../stock_list.txt'

        with open(stock_list_path, 'r') as stock_list:
            for stock in stock_list:
                for p in range(2):
                    temp_url = base_url.format(stock, start_page + p)
                    self.start_urls.append(temp_url)

    def parse(self, response):
        article_titles = response.xpath('/html/body/div/table[1]/tbody/tr/td[1]/a/text()').extract()
        article_urls = response.xpath('/html/body/div/table[1]/tbody/tr/td[1]/a/@href').extract()
        article_authors = response.xpath('/html/body/div/table[1]/tbody/tr/td[2]/text()').extract()
        article_dates = response.xpath('/html/body/div/table[1]/tbody/tr/td[3]/text()').extract()

        items = []
        for idx in range(len(article_titles)):
            item = HspStockNewsItem()
            item['stock_code'] = str(response).split('?')[1].split('&')[0].split('=')[1].strip()
            item['article_title'] = article_titles[idx].strip()
            item['article_url'] = 'https://finance.naver.com' + article_urls[idx].strip()
            item['article_author'] = article_authors[idx].strip()
            item['article_date'] = article_dates[idx].strip().split(' ')[0].strip().replace('.','-')
            items.append(item)
        return items
