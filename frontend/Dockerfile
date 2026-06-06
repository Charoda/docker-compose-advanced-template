# Nginx как обратный прокси и раздача статики
FROM nginx:1.25-alpine

# Убираем дефолтный конфиг и подставляем свой
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/
# Статика (стили) кладётся по пути, который ожидает nginx
COPY styles.css /usr/share/nginx/html/static/styles.css
