#! /bin/bash

cd /home/ec2-user/python_data_analysis_stock/scrapy_develop/tops
scrapy crawl topsbots

cd /home/ec2-user/python_data_analysis_stock/scrapy_develop/PSH_institut_stock_one
scrapy crawl institutbots

cd /home/ec2-user/python_data_analysis_stock/scrapy_develop/foreign_stock_one
scrapy crawl stockbots
