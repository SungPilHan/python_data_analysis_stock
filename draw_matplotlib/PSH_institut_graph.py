import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pymysql
from pandas import DataFrame
from datetime import datetime
import matplotlib.font_manager as fm
font_name=fm.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
plt.rcParams['axes.unicode_minus'] = False
plt.rc('font', family=font_name)
plt.style.use('ggplot')


class InstitutPlot:
    def __init__(self):
        self.conn = pymysql.connect(host='skuser55-instance.c1aoapfinmy7.us-east-1.rds.amazonaws.com',port=3306,user='admin',password='y1syitq0is',db='mydb_test')
        self.cursor = self.conn.cursor()
        # self.cursor.close()
        # self.connectdb.close()
        self.draw_graph()

    def newtime(self, x):
        return x.strftime('%Y-%m-%d %H:%M:%S')
    
    def strtoint(self, x):
        return int(x.replace(",", ""))

    def time_day(self, x):
        return x.split(' ')[0]

    def save_data(self):
        show_db = '''SELECT * FROM my_topic_institut_table'''
        self.cursor.execute(show_db)
        data = self.cursor.fetchall()
        pddata = pd.DataFrame(data, columns=["id","stock_name","stock_date","institut_trading_volume","create_at"])

        pddata["institut_trading_volume"] = pddata["institut_trading_volume"].map(lambda x: self.strtoint(x))

        pddata["create_at"] = pddata["create_at"].map(lambda x: self.newtime(x))
        pddata["time_day"] = pddata["stock_date"].map(lambda x: self.time_day(x))
        return pddata
          
    def draw_graph(self):
        pddata = self.save_data()
        stocks = set()

        for i in pddata["stock_name"]:
            stocks.add(i)
        stocks = list(stocks)
        for i in stocks:
            newpddata = pddata[pddata["stock_name"]==i]
            plt_index = range(len(newpddata[:60]))
            fig = plt.figure(figsize=(12,6))
            ax1 = fig.add_subplot(1, 1, 1)


            ax1.bar(plt_index, newpddata['institut_trading_volume'][:60], color='darkblue')
            ax1.plot(plt_index, newpddata['institut_trading_volume'][:60], color='red')
            
            plt.xticks(plt_index, newpddata['time_day'][:60], rotation=45, fontsize='small')
            plt.ticklabel_format(axis='y', style='plain')      
            ax1.xaxis.set_ticks_position('bottom')
            ax1.yaxis.set_ticks_position('left')
            ax1.set_title(i +'institut_stock')
            
            plt.xlabel('day')
            plt.ylabel('volume')
            plt.savefig('institut_plot {}.png'.format(i), dpi=400, bbox_inches='tight')
            plt.show()

if __name__ == '__main__':
    InstitutPlot()
