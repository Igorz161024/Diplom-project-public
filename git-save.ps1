[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
chcp 65001 > $null

git add .
git commit -m "Автоматичний коміт" --allow-empty

git push private owner
git push public owner

Write-Output "Зміни збережено на GitHub (приватний та публічний репозиторії)"
git status
