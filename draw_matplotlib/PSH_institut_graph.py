import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pymysql
from pandas import DataFrame
from datetime import datetime
import matplotlib.font_manager as fm
import os

class InstitutPlot:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    def __init__(self,num):
        plt.style.use('ggplot')
        self.conn = pymysql.connect(host='skuser55-instance.c1aoapfinmy7.us-east-1.rds.amazonaws.com',port=3306,user='admin',password='y1syitq0is',db='mydb')
        self.cursor = self.conn.cursor()
        self.num=num
        self.draw_graph()

    def newtime(self, x):
        return x.strftime('%Y-%m-%d %H:%M:%S')
    
    def strtoint(self, x):
        return int(x.replace(",", ""))

    def time_day(self, x):
        return x.split(' ')[0]

    def save_data(self):
        show_db = '''SELECT * FROM my_topic_institut_table ORDER BY stock_date DESC'''
        self.cursor.execute(show_db)
        data = self.cursor.fetchall()
        pddata = pd.DataFrame(data, columns=["id","stock_name","stock_code","stock_date","institut_trading_volume","create_at"])

        pddata["institut_trading_volume"] = pddata["institut_trading_volume"].map(lambda x: self.strtoint(x))

        pddata["create_at"] = pddata["create_at"].map(lambda x: self.newtime(x))
        pddata["time_day"] = pddata["stock_date"].map(lambda x: self.time_day(x))
        return pddata

    def insert_path(self, code, num):
        sql = '''INSERT graph_path(stock_code, path) VALUES(%s, %s)'''
        self.cursor.execute(sql,(code, '/media/institut/{}/{}.png'.format(num, code)))
        self.conn.commit()

    def draw_graph(self):
        
        pddata = self.save_data()
        stocks = set()

        for i in pddata["stock_code"]:
            stocks.add(i)
        stocks = list(stocks)
        for i in stocks:
            newpddata = pddata[pddata["stock_code"]==i]
            plt_index = range(len(newpddata[:self.num]))
            fig = plt.figure(figsize=(12,6))
            ax1 = fig.add_subplot(1, 1, 1)


            ax1.bar(plt_index, newpddata['institut_trading_volume'][:self.num], color='darkblue')
            
            plt.xticks(plt_index, newpddata['time_day'][:self.num], rotation=45, fontsize='small')
            plt.ticklabel_format(axis='y', style='plain')      
            ax1.xaxis.set_ticks_position('bottom')
            ax1.yaxis.set_ticks_position('left')
            ax1.set_title(i +'_institut_stock')
            
            plt.xlabel('day')
            plt.ylabel('volume')
            plt.savefig(self.BASE_DIR+'/../restapi/media/institut/{}/{}'.format(self.num,i), dpi=400, bbox_inches='tight')
            ax1.set_xlim(ax1.get_xlim()[::-1])
            plt.close()
            self.insert_path(i, self.num)

if __name__ == '__main__':
    InstitutPlot(5)


