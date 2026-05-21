param([string]$message = "Автоматичний коміт")

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
chcp 65001 > $null

git add .
git commit -m "$message"
git push origin master

Write-Output "Зміни збережено на GitHub (гілка master)"
git status



