#!/bin/bash
# 🚀 Запуск ERP системи (Linux/WSL)

echo "🚀 Запускаю ERP..."

# Перехід у корінь проєкту (Windows шлях у WSL)
cd /mnt/c/Users/igorz/Projects/Diplom-project || { echo "❌ Не знайдено директорію /mnt/c/Users/igorz/Projects/Diplom-project"; exit 1; }

# Підняти контейнери (бекенд + база + фронтенд)
docker-compose up -d

# Перевірити статус контейнерів
docker ps

# Запустити бекенд (FastAPI)
cd backend || { echo "❌ Не знайдено директорію backend"; exit 1; }
nohup uvicorn main:app --reload --host 0.0.0.0 --port 8000 > backend.log 2>&1 &

# Запустити фронтенд (React)
cd ../frontend || { echo "❌ Не знайдено директорію frontend"; exit 1; }
npm install
nohup npm start > frontend.log 2>&1 &

echo "✅ ERP запущено! Фронтенд → http://localhost:3000, бекенд → http://localhost:8000"
