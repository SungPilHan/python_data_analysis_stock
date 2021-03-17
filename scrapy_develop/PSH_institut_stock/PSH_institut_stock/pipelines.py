from itemadapter import ItemAdapter
from kafka import KafkaProducer
from json import dumps
import time
class PshInstitutStockPipeline:

    def __init__(self): 
        self.producer= KafkaProducer( acks=0, compression_type='gzip', bootstrap_servers=['54.144.39.228:9092'],value_serializer=lambda x : dumps(x).encode('utf-8'))      

    def process_item(self, item, spider):

        data = {"schema":{"type":"struct","fields":[{"type":"int32","optional":"false","field":"id"},{"type":"string","optional":"false","field":"stock_name"},{"type":"string","optional":"false","field":"stock_code"},{"type":"string","optional":"false","field":"stock_date"},{"type":"string","optional":"false","field":"institut_trading_volume"},{"type":"int64","optional":"true","name":"org.apache.kafka.connect.data.Timestamp","version":1,"field":"create_at"}],"optional":"false","name":"institut_table"},"payload":{"id":0,"stock_name":item.get('stock_name','').strip(),"stock_code":item.get('stock_code'),"stock_date":item.get('stock_date','').strip(),"institut_trading_volume":item.get('institut_trading_volume','').strip(),"create_at":int(time.time())*1000}}
        print("wait")
        time.sleep(0.3)
        self.producer.send('my_topic_institut_table', value=data)
        time.sleep(0.3)
        self.producer.flush()
        return item

