# Етап 1: збірка React/Material UI
FROM node:18-alpine AS build

WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Етап 2: nginx для продакшн
FROM nginx:alpine

# Копіюємо наш власний конфіг nginx
COPY nginx/default.conf /etc/nginx/conf.d/default.conf

# Копіюємо білд фронтенду
COPY --from=build /app/build /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

