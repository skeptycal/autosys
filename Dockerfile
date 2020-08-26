FROM python/python:3.9

# For Python3 compact
RUN apt-get -y update && apt-get -y install python3-setuptools && \
	apt-get -y clean

WORKDIR /app
ADD . /app
RUN python3 setup.py install && python3 setup.py test

RUN python3 -m autosys
