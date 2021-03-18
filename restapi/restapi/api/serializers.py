from restapi.api.models import MyTopicForeign, MyTopicInstitut, MyTopicPriceBuy, MyTopicPriceSell, MyTopicNews
from rest_framework import serializers

class MyTopicInstitutSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyTopicInstitut
        fields = ['stock_name', 'stock_code', 'stock_date', 'institut_trading_volume']
        read_only_fields = ('stock_name', 'stock_date', 'institut_trading_volume')

class MyTopicForeignSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyTopicForeign
        fields = ['stock_name', 'stock_code', 'stock_date', 'foreign_trading_volume', 'foreign_rate']
        read_only_fields = ('stock_name', 'stock_date', 'foreign_trading_volume', 'foreign_rate')

class MyTopicPriceBuySerializer(serializers.ModelSerializer):
    class Meta:
        model = MyTopicPriceBuy
        fields = ['stock_name', 'stock_code', 'buying_price', 'buying_volume']
        read_only_fields = ('stock_name', 'stock_code', 'buying_price', 'buying_volume')

class MyTopicPriceSellSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyTopicPriceSell
        fields = ['stock_name', 'stock_code', 'selling_price', 'selling_volume']
        read_only_fields = ('stock_name', 'stock_code', 'selling_price', 'selling_volume')

class MyTopicNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyTopicNews
        fields = ['stock_code','article_title','article_url','article_author','article_date']
        read_only_fields = ('stock_code','article_title','article_url','article_author','article_date')