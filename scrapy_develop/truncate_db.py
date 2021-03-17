import pymysql

conn = pymysql.connect(host='skuser55-instance.c1aoapfinmy7.us-east-1.rds.amazonaws.com',port=3306,user='admin',password='y1syitq0is',db='mydb')
cursor = conn.cursor()
sql = 'TRUNCATE TABLE my_topic_foreign_table'
sql1 = 'TRUNCATE TABLE my_topic_institut_table'
sql2 = 'TRUNCATE TABLE my_topic_news_table'
sql3 = 'TRUNCATE TABLE my_topic_price_buy_table'
sql4 = 'TRUNCATE TABLE my_topic_price_sell_table'
cursor.execute(sql)
cursor.execute(sql1)
cursor.execute(sql2)
cursor.execute(sql3)
cursor.execute(sql4)