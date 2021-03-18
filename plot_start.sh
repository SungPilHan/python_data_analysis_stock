#! /bin/bash

chmod 755 draw_jobs.sh

cat <(crontab -l) <(echo "50 8 * * * /home/ec2-user/python_data_analysis_stock/draw_jobs.sh") | sudo crontab -u ec2-user -
