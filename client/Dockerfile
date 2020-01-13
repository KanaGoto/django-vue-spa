# ビルド環境
FROM node:11.14.0-alpine
RUN mkdir app
#ADD package*.json /app/
ADD . /app/
WORKDIR /app
RUN npm install -g npm @vue/cli
RUN npm run build


# 本番環境
FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
