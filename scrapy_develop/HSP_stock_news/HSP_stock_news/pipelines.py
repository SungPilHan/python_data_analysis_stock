# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from kafka import KafkaProducer
from json import dumps
import time
import pymysql

class HspStockNewsPipeline:
    def __init__(self):
        self.producer = KafkaProducer(acks=0,
            compression_type='gzip',
            bootstrap_servers=['54.144.39.228:9092'],
            value_serializer=lambda x: dumps(x).encode('utf-8'))
        try:
            conn = pymysql.connect(host='skuser55-instance.c1aoapfinmy7.us-east-1.rds.amazonaws.com',port=3306,user='admin',password='y1syitq0is',db='mydb')
            cursor = conn.cursor()
            cursor.execute('TRUNCATE TABLE my_topic_news_table')
        except:
            pass

    def process_item(self, item, spider):
        data = {"schema":{"type":"struct","fields":[{"type":"int32","optional":"false","field":"id"},{"type":"string","optional":"false","field":"stock_code"},{"type":"string","optional":"false","field":"article_title"},{"type":"string","optional":"false","field":"article_url"},{"type":"string","optional":"false","field":"article_author"},{"type":"string","optional":"false","field":"article_date"},{"type":"int64","optional":"true","name":"org.apache.kafka.connect.data.Timestamp","version":1,"field":"create_at"}],"optional":"false","name":"news_table"},"payload":{"id":0,"stock_code":item.get('stock_code'),"article_title":item.get('article_title'),"article_url":item.get('article_url'),"article_author":item.get('article_author'),"article_date":item.get('article_date'),"create_at":int(time.time())*1000}}
        self.producer.send('my_topic_news_table', value=data)
        time.sleep(0.3)
        self.producer.flush()
        return item
