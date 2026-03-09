param(
    [string]$Message = "Автоматичний коміт"
)

# Додаємо всі зміни
git add .

# Робимо коміт з повідомленням
git commit -m $Message

# Пушимо у приватний та публічний репозиторії
git push both master

# Виводимо повідомлення про успіх
Write-Host "✅ Зміни збережено на GitHub (приватний та публічний репозиторії)" -ForegroundColor Green