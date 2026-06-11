# ERP Deployment Guide

## ✅ Вимоги
- Windows 10/11 з WSL2 (Ubuntu 22.04)
- Docker Desktop
- Node.js + npm
- Git
- Visual Studio Code (рекомендовано для зручності)
- Розширення Docker Dev Containers (для інтеграції з VS Code)

---

## 📥 Клонування репозиторію

### 🔒 Приватний (для власної роботи)
git clone https://github.com/Igorz161024/Diplom-project.git
cd Diplom-project
git clone git@github.com:Igorz161024/Diplom-project.git
cd Diplom-project

### 🌍 Публічний (для викладача / перевірки)
git clone https://github.com/Igorz161024/Diplom-project-public.git
cd Diplom-project-public
git clone git@github.com:Igorz161024/Diplom-project-public.git
cd Diplom-project-public

---

## ⚙️ Налаштування середовища
cp .env.example .env
nano .env   # або notepad .env у Windows
docker-compose up --build

---

## 🗄️ Підняття бази даних (PowerShell)
cd C:\Users\igorz\Projects\Diplom-project
docker-compose up -d
docker ps

---

## ⚙️ Запуск бекенду (WSL2 Ubuntu)
cd ~/Diplom-project/backend
uvicorn main:app --reload

---

## 🎨 Запуск фронтенду (PowerShell)
cd C:\Users\igorz\Projects\Diplom-project\frontend
npm install
npm start

---

## 🔎 Перевірка API (WSL2 Ubuntu)
curl http://localhost:8000/
curl -X POST http://localhost:8000/add_entry -H "Content-Type: application/json" -d '{"date":"2026-06-09","operation":"income","status":"confirmed","amount":1000}'
curl http://localhost:8000/balance
curl -H "Authorization: Bearer <your_token>" http://localhost:8000/protected_endpoint

---

## 🚀 Автоматичний запуск
### Windows (PowerShell)
.\start.ps1

### Linux/WSL
bash start.sh

---

## 📌 Нотатки
- Створіть файл .env з параметрами:
  DATABASE_URL=postgresql://user:password@localhost:5432/erp_diplom
  JWT_SECRET=your_secret_key
- Ініціалізація таблиць:
  alembic upgrade head
- Для збереження змін використовуйте:
  .\git-save.ps1
- Для подвійного пушу в приватний і публічний репозиторії:
  ./git-double-push.sh
