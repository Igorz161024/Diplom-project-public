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
curl -X POST http://localhost:8000/report -H "Content-Type: application/json" -d '{"from":"2026-06-01","to":"2026-06-15"}'
curl -X GET http://localhost:8000/plot -H "Authorization: Bearer <admin_token>"

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
psql -U postgres -d erp_diplom < backups/erp_diplom_2026-06-11_09-13.sql

---

## 📘 Документація API
Swagger доступний за адресою:  
http://localhost:8000/docs  

Основні модулі:  
- /api/accounts  
- /api/journal  
- /api/entry_lines  

Додаткові модулі:  
- /api/finance  
- /api/sales  
- /api/purchases  
- /api/inventory  
- /api/legal  

---

## 📑 Приклади JSON‑запитів
```json
{
  "date": "2026-06-09",
  "operation": "income",
  "status": "confirmed",
  "amount": 1000
}
{
  "account_id": 1
}
{
  "from": "2026-06-01",
  "to": "2026-06-15"
}
{
  "type": "line",
  "metric": "amount"
}
```
---

## 📝 CHANGELOG.md
- Додано `start-erp.sh` та `start-erp.ps1`.
- Оновлено `README-deploy.md` з прикладами JSON‑запитів.
- Перевірено API на чистій системі.
- Успішна інсталяція підтверджена.

---

## 🎨 Фронтенд інтеграція
- React + Material UI напряму працює з FastAPI.
- Node.js шлюз не використовується.
- Базова сторінка авторизації відображає дані з бекенду.

---

## 🧪 Тестування на чистій системі
1. Запустити новий WSL або VM.
2. Клонувати репозиторій.
3. Виконати `start-erp.sh` (Linux/WSL) або `start-erp.ps1` (Windows).
4. Переконатися, що база `erp_diplom` створюється і контейнер `erp_db` піднімається.
5. Відкрити Swagger (`http://localhost:8000/docs`) і протестувати модулі.
6. Додати результат у `CHANGELOG.md`.

---

## 📊 Додаткові перевірки
- Переконатися, що у базі є таблиці `accounts`, `journal`, `entry_lines`.
- У таблиці `journal` обов’язково: `id`, `date`, `operation`, `status`, `amount`.
- JWT авторизація працює для admin токена.
- Фронтенд коректно відображає дані з бекенду.
- README‑deploy.md не містить локальних шляхів (C:\Users\...).
- Скрипти запуску працюють без ручних правок.
