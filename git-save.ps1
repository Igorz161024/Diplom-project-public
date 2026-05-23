param([string]$message = "Автоматичний коміт")

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
chcp 65001 > $null

git add .
git commit -m "$message"

# Пуш у приватний репозиторій
git push origin master

# Пуш у публічний репозиторій
git push public master

Write-Output "Зміни збережено у приватному та публічному репозиторіях (гілка master)"
git status




