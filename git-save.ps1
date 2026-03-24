git add .
git commit -m "Автоматичний коміт" --allow-empty
git push private master
git push public master
git push both master
Write-Output "Зміни збережено на GitHub (приватний та публічний репозиторії)"
git status