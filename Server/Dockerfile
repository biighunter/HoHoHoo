FROM ubuntu

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt install -y \
        nano \
	nginx \
	python3-certbot-nginx \
	cron  

COPY /conf.d/*.conf /etc/nginx/conf.d/
COPY nginx.conf /etc/nginx/nginx.conf
COPY /ssl-renew/renew_cert.sh /ssl-renew/renew_cert.sh
COPY renew_cert_job /etc/cron.d/
COPY /install-ssl/ssl.sh /install-ssl/ssl.sh

RUN chmod +x /install-ssl/ssl.sh
RUN chmod +x /ssl-renew/renew_cert.sh
RUN chmod 0644 /etc/cron.d/renew_cert_job

EXPOSE 80/tcp
EXPOSE 80/udp
EXPOSE 443/tcp
EXPOSE 443/udp

ENTRYPOINT ["nginx"]

CMD ["-g","daemon off;"]
