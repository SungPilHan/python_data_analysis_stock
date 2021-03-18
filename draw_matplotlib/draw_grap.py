import foreign_stock_graph as foreign
import PSH_institut_graph as institut
import pymysql

conn = pymysql.connect(host='skuser55-instance.c1aoapfinmy7.us-east-1.rds.amazonaws.com',port=3306,user='admin',password='y1syitq0is',db='mydb')
cursor = conn.cursor()
cursor.execute('TRUNCATE TABLE graph_path')

foreign.Mdproject3(5)
foreign.Mdproject3(30)
foreign.Mdproject3(60)

institut.InstitutPlot(5)
institut.InstitutPlot(30)
institut.InstitutPlot(60)