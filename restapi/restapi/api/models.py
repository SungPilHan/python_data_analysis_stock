from django.db import models

class MyTopicForeign(models.Model):
    stock_name = models.TextField(db_column='stock_name')
    stock_code = models.TextField(db_column='stock_code')
    stock_date = models.TextField(db_column='stock_date')
    foreign_trading_volume = models.TextField(db_column='foreign_trading_volume')
    foreign_rate=models.TextField(db_column='foreign_rate')
    create_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table='my_topic_foreign_table'

class MyTopicInstitut(models.Model):
    stock_name = models.TextField(db_column='stock_name')
    stock_code = models.TextField(db_column='stock_code')
    stock_date = models.TextField(db_column='stock_date')
    institut_trading_volume = models.TextField(db_column='institut_trading_volume')
    create_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table='my_topic_institut_table'

class MyTopicPriceBuy(models.Model):
    stock_name = models.TextField(db_column='stock_name')
    stock_code = models.TextField(db_column='stock_code')
    buying_price = models.TextField(db_column='buying_price')
    buying_volume = models.TextField(db_column='buying_volume')
    create_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table='my_topic_price_buy_table'

class MyTopicPriceSell(models.Model):
    stock_name = models.TextField(db_column='stock_name')
    stock_code = models.TextField(db_column='stock_code')
    selling_price = models.TextField(db_column='selling_price')
    selling_volume = models.TextField(db_column='selling_volume')
    create_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table='my_topic_price_sell_table'

class MyTopicNews(models.Model):
    stock_code = models.TextField(db_column='stock_code')
    article_title = models.TextField(db_column='article_title')
    article_url = models.TextField(db_column='article_url')
    article_author = models.TextField(db_column='article_author')
    article_date = models.TextField(db_column='article_date')
    create_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table='my_topic_news_table'