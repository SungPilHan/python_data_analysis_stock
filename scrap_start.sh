#! /bin/bash

chmod 755 daily_jobs.sh hourly_jobs.sh every_minute_jobs.sh

cd /home/ec2-user/python_data_analysis_stock/scrapy_develop/tops
scrapy crawl topsbots

python /home/ec2-user/python_data_analysis_stock/scrapy_develop/truncate_db.py

cd /home/ec2-user/python_data_analysis_stock/scrapy_develop/HSP_stock_news
scrapy crawl newsbots

cd /home/ec2-user/python_data_analysis_stock/scrapy_develop/KDK_current_stock_price
scrapy crawl pricebots

cd /home/ec2-user/python_data_analysis_stock/scrapy_develop/PSH_institut_stock
scrapy crawl institutbots

cd /home/ec2-user/python_data_analysis_stock/scrapy_develop/foreign_stock
scrapy crawl stockbots

cat <(crontab -l) <(echo "30 8 * * * /home/ec2-user/python_data_analysis_stock/daily_jobs.sh") | sudo crontab -u ec2-user -
cat <(crontab -l) <(echo "0 * * * * /home/ec2-user/python_data_analysis_stock/hourly_jobs.sh") | sudo crontab -u ec2-user -
cat <(crontab -l) <(echo "*/5 9-16 * * * /home/ec2-user/python_data_analysis_stock/every_minute_jobs.sh") | sudo crontab -u ec2-user -
