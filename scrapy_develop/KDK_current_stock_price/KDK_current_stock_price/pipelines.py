# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter


# class KdkCurrentStockPricePipeline:
#     def process_item(self, item, spider):
#         return item
# 54.144.39.228
from kafka import KafkaProducer
from json import dumps
import time

# dict -> object
# str -> string

producer = KafkaProducer(acks=0,compression_type='gzip',bootstrap_servers=['54.144.39.228:9092'],value_serializer=lambda x: dumps(x).encode('utf-8'))

start = time.time()

# for i in range(10):
#     data = {'name': 'Dowon-' + str(i)}
#     producer.send('test', value=data)
#     producer.flush()

class KdkCurrentStockPricePipeline:
    def __init__(self):
        self.producer = KafkaProducer(acks=0,compression_type='gzip',bootstrap_servers=['54.144.39.228:9092'],value_serializer=lambda x: dumps(x).encode('utf-8'))
    def process_item(self, item, spider):
        data = {"schema":{"type":"struct","fields":[{"type":"int32","optional":"false","field":"id"},{"type":"string","optional":"false","field":"stock_name"},{"type":"string","optional":"false","field":"buying_price"},{"type":"string","optional":"false","field":"buying_volume"},{"type":"int64","optional":"true","name":"org.apache.kafka.connect.data.Timestamp","version":1,"field":"create_at"}],"optional":"false","name":"price_buy_table"},"payload":{"id":0,"stock_name":item.get('stock_name'),"buying_price":item.get('buying_price'),"buying_volume":item.get('buying_volume'),"create_at":int(time.time())*1000}}
        self.producer.send('my_topic_price_buy_table', value=data)
        time.sleep(0.3)
        self.producer.flush()

        data1 = {"schema":{"type":"struct","fields":[{"type":"int32","optional":"false","field":"id"},{"type":"string","optional":"false","field":"stock_name"},{"type":"string","optional":"false","field":"selling_price"},{"type":"string","optional":"false","field":"selling_volume"},{"type":"int64","optional":"true","name":"org.apache.kafka.connect.data.Timestamp","version":1,"field":"create_at"}],"optional":"false","name":"price_sell_table"},"payload":{"id":0,"stock_name":item.get('stock_name'),"selling_price":item.get('selling_price'),"selling_volume":item.get('selling_volume'),"create_at":int(time.time())*1000}}
        self.producer.send('my_topic_price_sell_table', value=data1)
        time.sleep(0.3)
        self.producer.flush()
        return item