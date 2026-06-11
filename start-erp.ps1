# Запуск ERP системи
Write-Host "🚀 Запускаю ERP..." -ForegroundColor Green

# Перехід у корінь проєкту
Set-Location "C:\Users\igorz\Projects\Diplom-project"

# Підняти контейнери (бекенд + база + фронтенд)
docker-compose up -d

# Перевірити статус контейнерів
docker ps

# Відкрити фронтенд у браузері
Start-Process "http://localhost:3000"

# Відкрити бекенд у браузері
Start-Process "http://localhost:8000"

Write-Host "✅ ERP запущено! Фронтенд і бекенд відкриті у браузері." -ForegroundColor Cyan


