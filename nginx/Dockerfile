FROM nginx:alpine
RUN rm /etc/nginx/config.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]