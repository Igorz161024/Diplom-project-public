# ERP Deployment Guide

## ✅ Вимоги
- Windows 10/11 з WSL2 (Ubuntu 22.04)
- Docker Desktop
- Node.js + npm
- Git

---

## 📥 Клонування репозиторію (PowerShell)
git clone https://github.com/igorz2005/Diplom-project.git
cd Diplom-project

---

## 🗄️ Підняття бази даних (PowerShell)
cd C:\Users\igorz\Projects\Diplom-project
docker-compose up -d

> Контейнер PostgreSQL створиться з ім’ям erp_db.

---

## ⚙️ Запуск бекенду (WSL2 Ubuntu)
cd ~/Diplom-project/backend
uvicorn main:app --reload

> Бекенд буде доступний на http://localhost:8000

---

## 🎨 Запуск фронтенду (PowerShell)
cd C:\Users\igorz\Projects\Diplom-project\frontend
npm install
npm start

> Фронтенд буде доступний на http://localhost:3000

---

## 🔎 Перевірка API (WSL2 Ubuntu)
curl http://localhost:8000/
curl -X POST http://localhost:8000/add_entry -H "Content-Type: application/json" -d '{"date":"2026-06-09","operation":"income","status":"confirmed","amount":1000}'
curl http://localhost:8000/balance

---

## 📌 Нотатки
- Створіть файл .env з параметрами:
  DATABASE_URL=postgresql://user:password@localhost:5432/erp_diplom
  JWT_SECRET=your_secret_key

- Ініціалізація таблиць:
  alembic upgrade head

