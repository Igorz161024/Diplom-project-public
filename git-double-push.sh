#!/bin/bash
# Автоматичний подвійний пуш у приватний та публічний репозиторії

# Запускаємо ssh-agent і додаємо ключ
eval "$(ssh-agent -s)" >/dev/null
ssh-add ~/.ssh/id_ed25519 >/dev/null

# Додаємо всі зміни
git add .

# Коміт з повідомленням (можна змінити текст)
git commit -m "Daily save"

# Пушимо у приватний
git push origin master

# Пушимо у публічний
git push public master
