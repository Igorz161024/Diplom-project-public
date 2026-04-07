[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
chcp 65001 > $null

git add .
git commit -m "Автоматичний коміт"
git push private owner
git push public owner
git push private master
git push public master

Write-Output "Зміни збережено на GitHub (гілки owner та master)"
git status
