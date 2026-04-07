[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
chcp 65001 > $null

git add .
git commit -m "Автоматичний коміт"
git push origin master

Write-Output "Зміни збережено на GitHub (гілка master)"
git status
