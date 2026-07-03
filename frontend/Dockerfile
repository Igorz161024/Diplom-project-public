# Етап 1: збірка React
FROM node:20-alpine AS build

WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install
COPY . .
RUN npm run build

# Етап 2: Nginx для віддачі збірки
FROM nginx:latest

# Копіюємо збірку у стандартну директорію Nginx
COPY --from=build /app/build /usr/share/nginx/html

# Копіюємо свій конфіг
COPY ./nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
