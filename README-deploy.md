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
git clone https://github.com/Igorz161024/Diplom-project.git
cd Diplom-project
git clone git@github.com:Igorz161024/Diplom-project.git
cd Diplom-project

### 🌍 Інструкція для користувачів
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
.\start-erp.ps1

### Linux/WSL
bash start-erp.sh

> **Примітка:** файл `start-erp.sh` запускає Docker‑контейнери, бекенд (FastAPI) та фронтенд (React) автоматично.  
> Після виконання скрипта система буде доступна за адресами:  
> - Фронтенд → http://localhost:3000  
> - Бекенд → http://localhost:8000  

---

## 🗄️ Відновлення бази даних
Приклад команди для відновлення з дампу:
psql -U postgres -d erp_diplom < backups/erp_diplom_2026-06-11_09-13.sql

---

## 📘 Документація API
Swagger доступний за адресою:  
http://localhost:8000/docs  

Основні модулі:  
- /api/journal  
- /api/finance  
- /api/sales  
- /api/purchases  
- /api/inventory  
- /api/legal
