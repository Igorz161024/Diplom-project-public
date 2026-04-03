[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

# Додаємо всі зміни
git add .

# Коміт з повідомленням (порожній коміт дозволений)
git commit -m "Автоматичний коміт" --allow-empty

# Пушимо у приватний репозиторій, гілка Владелец
git push private Владелец

# Пушимо у публічний репозиторій, гілка Владелец
git push public Владелец

Write-Output "Зміни збережено на GitHub (приватний та публічний репозиторії)"
git status


