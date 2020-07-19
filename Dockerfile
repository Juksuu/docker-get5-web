FROM amd64/ubuntu:16.04

RUN apt-get update && apt-get upgrade -y && \
    apt-get install build-essential software-properties-common -y && \
    apt-get install python-dev python-pip apache2 libapache2-mod-wsgi -y && \
    apt-get install virtualenv libmysqlclient-dev -y && \
    apt-get install git -y && \
    cd /var/www && \
    git clone https://github.com/splewis/get5-web && \
    cd get5-web && \
    virtualenv venv && \
    . venv/bin/activate && \
    pip install --upgrade 'setuptools<45.0.0' && \
    pip install -r requirements.txt

COPY 000-default.conf /etc/apache2/sites-available/000-default.conf
COPY get5.wsgi /var/www/get5-web/get5.wsgi
COPY prod_config.py /var/www/get5-web/instance/prod_config.py

COPY entrypoint.sh /sbin/entrypoint.sh

RUN chmod +x /sbin/entrypoint.sh

EXPOSE 80

ENTRYPOINT ["/sbin/entrypoint.sh"]

