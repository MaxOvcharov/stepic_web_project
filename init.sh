#sudo rm /etc/nginx/sites-enabled/default
#sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
#sudo /etc/init.d/nginx restart
#sudo /etc/init.d/mysql start
#sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
#sudo ln -sf /home/box/web/etc/django.py /etc/gunicorn.d/django.py
#sudo /etc/init.d/gunicorn start
sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE USER 'box'@'localhost'"
mysql -uroot -e "SET PASSWORD FOR 'box'@'localhost' = PASSWORD('121212')"
mysql -uroot -e "CREATE DATABASE stepic_web"
mysql -uroot -e "GRANT ALL ON stepic_web.* TO 'box'@'localhost'"