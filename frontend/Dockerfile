FROM httpd:2.4

ENV PATH $PATH:/project/docs_manager/bin

RUN echo "\
\n\
ServerName doc_manager_app\n\
AddDefaultCharset utf-8\n\
LoadModule proxy_module modules/mod_proxy.so\n\
LoadModule proxy_http_module modules/mod_proxy_http.so\n\
ProxyPass /api http://docs-manager:8000\n\
ProxyPassReverse /api http://docs-manager-rest-api:8000\n\
\n\
" >>/usr/local/apache2/conf/httpd.conf

EXPOSE 80/tcp