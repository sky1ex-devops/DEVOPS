FROM ubuntu:latest

RUN apt-get update && apt-get install -y openssh-server
RUN apt install -y libgeoip-dev && apt install -y libgd-dev && apt install -y libxslt-dev && apt install -y zlib1g zlib1g-dev && apt install -y openssl libssl-dev && apt install -y libpcre3 libpcre3-dev
RUN apt install -y nano && apt install -y mc && apt install -y make && apt install -y dpkg-dev && apt install -y git && mkdir /etc/nginx && apt install -y wget

RUN mkdir -p /src/nginx
WORKDIR /src/nginx
RUN cd /src/nginx && wget http://nginx.org/download/nginx-1.25.3.tar.gz && tar -xzvf nginx-1.25.3.tar.gz
RUN cd nginx-1.25.3 && git clone https://github.com/sky1ex-devops/ngx_http_proxy_connect_module.git && ls -lah
#RUN cd nginx-1.25.3 && patch -p1 < /src/nginx/nginx-1.25.3/ngx_http_proxy_connect_module/patch/proxy_connect_rewrite_102101.patch

RUN cd nginx-1.25.3 && ./configure \
--user=www \
--group=www \
--prefix=/etc/nginx \
--with-http_ssl_module \
--with-http_stub_status_module \
--with-http_realip_module \
--with-threads \
--with-stream \
--with-stream_ssl_preread_module \
--with-stream_ssl_module
RUN cd nginx-1.25.3 && make install

RUN cd nginx-1.25.3 && cp objs/nginx /etc/nginx/sbin/nginx
RUN groupadd -g 1001 www
RUN adduser -gid 1001 www

RUN mkdir /var/run/sshd
RUN echo 'root:toor' | chpasswd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
