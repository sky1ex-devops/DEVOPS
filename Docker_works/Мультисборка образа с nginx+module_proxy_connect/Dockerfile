# Мультисборка образа с nginx+module_proxy_connect
# Первый этап сборки

FROM ubuntu:latest as build

RUN apt-get update && apt-get install -y openssh-server
RUN apt install -y libgeoip-dev && apt install -y libgd-dev && apt install -y libxslt-dev && apt install -y zlib1g zlib1g-dev && apt install -y openssl libssl-dev && apt install -y libpcre3 libpcre3-dev
RUN apt install -y nano && apt install -y mc && apt install -y make && apt install -y dpkg-dev && apt install -y git && mkdir /etc/nginx && apt install -y wget

RUN mkdir /src
WORKDIR /src/nginx
RUN cd /src/nginx && wget http://nginx.org/download/nginx-1.25.3.tar.gz && tar -xzvf nginx-1.25.3.tar.gz
RUN cd nginx-1.25.3 && git clone https://github.com/sky1ex-devops/ngx_http_proxy_connect_module.git && ls -lah
RUN cd nginx-1.25.3 && patch -p1 < /src/nginx/nginx-1.25.3/ngx_http_proxy_connect_module/patch/proxy_connect_rewrite_102101.patch

RUN cd /src/nginx/nginx-1.25.3 && ./configure \
--user=www \
--group=www \
--prefix=/etc/nginx \
--with-http_ssl_module \
--with-http_stub_status_module \
--with-http_realip_module \
--with-threads \
--add-module=/src/nginx/nginx-1.25.3/ngx_http_proxy_connect_module

RUN cd nginx-1.25.3 && make install

RUN apt install -y wget
RUN mkdir /src/nginx/nginx-1.25.3/init
RUN wget -O /src/nginx/nginx-1.25.3/init/nginx https://gist.github.com/sairam/5892520/raw/b8195a71e944d46271c8a49f2717f70bcd04bf1a/etc-init.d-nginx


# Второй этап сборки

FROM ubuntu:latest as prod

COPY --from=build /src/nginx/nginx-1.25.3 /etc/nginx/nginx-1.25.3
COPY --from=build /usr/lib/x86_64-linux-gnu/libpcre.a /usr/lib/x86_64-linux-gnu/libpcre.a
COPY --from=build /usr/lib/x86_64-linux-gnu/libpcre.so.3.13.3 /etc/nginx/usr/lib/x86_64-linux-gnu/libpcre.so.3.13.3
COPY --from=build /usr/lib/x86_64-linux-gnu/libpcre.so.3 /usr/lib/x86_64-linux-gnu/libpcre.so.3

WORKDIR /etc/nginx
RUN cd /etc/nginx && cp -r nginx-1.25.3/conf /etc/nginx/conf
RUN cp nginx-1.25.3/objs/nginx /etc/nginx
RUN cp nginx-1.25.3/init/nginx /etc/init.d/nginx
RUN chmod +x /etc/init.d/nginx
RUN groupadd www && useradd -m -g www www
RUN mkdir /etc/nginx/logs && touch /etc/nginx/logs/error.log && touch /etc/nginx/logs/access.log

#RUN apt update && apt install -y libpcre3

CMD ["/bin/bash"] 