import os
import platform

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if platform.system() == 'Windows':
    os.system('copy tops.txt {}'.format(BASE_DIR+'\\..\\foreign_stock\\foreign_stock\\spiders\\stock_list.txt'))
    os.system('copy tops.txt {}'.format(BASE_DIR+'\\..\\HSP_stock_news\\HSP_stock_news\\spiders\\stock_list.txt'))
    os.system('copy tops.txt {}'.format(BASE_DIR+'\\..\\KDK_current_stock_price\\KDK_current_stock_price\\spiders\\stock_list.txt'))
    os.system('copy tops.txt {}'.format(BASE_DIR+'\\..\\PSH_institut_stock\\PSH_institut_stock\\spiders\\stock_list.txt'))
else:
    os.system('cp tops.txt {}'.format(BASE_DIR+'/../foreign_stock/foreign_stock/spiders/stock_list.txt'))
    os.system('cp tops.txt {}'.format(BASE_DIR+'/../HSP_stock_news/HSP_stock_news/spiders/stock_list.txt'))
    os.system('cp tops.txt {}'.format(BASE_DIR+'/../KDK_current_stock_price/KDK_current_stock_price/spiders/stock_list.txt'))
    os.system('cp tops.txt {}'.format(BASE_DIR+'/../PSH_institut_stock/PSH_institut_stock/spiders/stock_list.txt'))