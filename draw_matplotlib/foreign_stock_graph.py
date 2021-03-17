import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pymysql
from pandas import DataFrame
from datetime import datetime
import matplotlib.font_manager as fm

plt.rcParams['axes.unicode_minus'] = False
font_name=fm.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()

plt.rc('font', family=font_name)
plt.style.use('ggplot')

class Mdproject3:
    def __init__(self):
        self.conn = pymysql.connect(host='skuser55-instance.c1aoapfinmy7.us-east-1.rds.amazonaws.com',port=3306,user='admin',password='y1syitq0is',db='mydb_test')
        self.cursor = self.conn.cursor()
        self.plt_show()
    def newtime(self, x):
        return x.strftime('%Y-%m-%d %H:%M:%S')
    def strtoint(self, x):
        return int(x.replace(",", ""))
    def time_day(self, x):
        return x.split(' ')[0]
    def time_second(self, x):
        return x.split(' ')[1].split(":")[2]
    def save_data(self):
        show_db = '''SELECT * FROM my_topic_foreign_table'''
        self.cursor.execute(show_db)
        data = self.cursor.fetchall()
        pddata = pd.DataFrame(data, columns=["id","stock_name","stock_date","foreign_trading_volume","foreign_rate","create_at"])
        pddata["foreign_trading_volume"] = pddata["foreign_trading_volume"].map(lambda x: self.strtoint(x))
        pddata["create_at"] = pddata["create_at"].map(lambda x: self.newtime(x))
        pddata["time_day"] = pddata["stock_date"].map(lambda x: self.time_day(x))
        pddata["time_second"] = pddata["create_at"].map(lambda x: self.time_second(x))
        return pddata
    def plt_show(self):
        pddata = self.save_data()
        stocks = set()
        for i in pddata["stock_name"]:
            stocks.add(i)
        stocks = list(stocks)
        print(stocks)
        for i in stocks:
            newpddata = pddata[pddata["stock_name"]==i]
            plt_index = range(len(newpddata[:60]))
            fig = plt.figure(figsize=(12,6))
            ax1 = fig.add_subplot(1, 1, 1)
            ax1.bar(plt_index, newpddata['foreign_trading_volume'][:60], color='darkblue')
            ax1.plot(plt_index,newpddata['foreign_trading_volume'][:60],color='red')
            plt.xticks(plt_index, newpddata['time_day'][:60], rotation=70, fontsize='small')
            plt.ticklabel_format(axis='y', style='plain')      
            ax1.xaxis.set_ticks_position('bottom')
            ax1.yaxis.set_ticks_position('left')
            ax1.set_title(i+'_foreign_stock')
            plt.xlabel('day')
            plt.ylabel('volume')
            plt.savefig('foreign_plot {}.png'.format(i), dpi=400, bbox_inches='tight')
            ax1.set_xlim(ax1.get_xlim()[::-1])

if __name__ == '__main__':
    Mdproject3()