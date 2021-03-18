#! /bin/bash

__conda_setup="$('/home/ec2-user/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
        eval "$__conda_setup"
else
        if [ -f "/home/ec2-user/anaconda3/etc/profile.d/conda.sh" ]; then
                . "/home/ec2-user/anaconda3/etc/profile.d/conda.sh"
        else
                export PATH="/home/ec2-user/anaconda3/bin:$PATH"
        fi
fi
unset __conda_setup

cd /home/ec2-user/python_data_analysis_stock/scrapy_develop/tops
scrapy crawl topsbots

cd /home/ec2-user/python_data_analysis_stock/scrapy_develop/PSH_institut_stock_one
scrapy crawl institutbots

cd /home/ec2-user/python_data_analysis_stock/scrapy_develop/foreign_stock_one
scrapy crawl stockbots
