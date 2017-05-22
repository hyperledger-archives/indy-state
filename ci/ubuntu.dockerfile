# Development
FROM ubuntu:16.04

ARG uid=1000

# Install environment
RUN apt-get update && apt-get install -y \
	git \
	wget \
	autoconf \
	build-essential \
	libtool-bin \
	zlib1g-dev \
	libbz2-dev \
	pkg-config \
	python3.5 \
	python3-pip \
	python3-dev \
	python-setuptools
RUN pip3 install -U \ 
	pip \ 
	setuptools \
	Cython \
	virtualenv

RUN useradd -ms /bin/bash -u $uid sovrin
USER sovrin

WORKDIR /home/sovrin
RUN git clone https://github.com/evernym/snappy.git
WORKDIR /home/sovrin/snappy
RUN ./autogen.sh && ./configure && cat ./README.md > ./README
RUN make
USER root
RUN make install

USER sovrin
WORKDIR /home/sovrin
RUN git clone https://github.com/evernym/rocksdb.git
WORKDIR /home/sovrin/rocksdb
RUN make EXTRA_CFLAGS="-fPIC" EXTRA_CXXFLAGS="-fPIC" static_lib

USER root
RUN make install

USER sovrin
WORKDIR /home/sovrin
RUN git clone https://github.com/evernym/python-rocksdb.git
WORKDIR /home/sovrin/python-rocksdb
RUN python3 setup.py build
USER root
RUN python3 setup.py install
RUN ldconfig

USER sovrin
RUN virtualenv -p python3.5 /home/sovrin/test
USER root
RUN ln -sf /home/sovrin/test/bin/python /usr/local/bin/python
RUN ln -sf /home/sovrin/test/bin/pip /usr/local/bin/pip
USER sovrin
WORKDIR /home/sovrin
