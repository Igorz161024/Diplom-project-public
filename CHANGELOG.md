# Changelog
Усі значущі зміни цього проєкту документуються у цьому файлі.
Формат відповідає стандарту [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [1.0.1] – 2026-03-11
### Changed
- Перехід на PostgreSQL 18.3 (оновлення з 15‑ї версії).
- Налаштовано шлях до volume для коректного збереження даних.
- Відновлено інтеграцію FastAPI з новою базою (ендпоінти `/add_entry`, `/get_account_balance`).
- Домовлено про використання української латиниці для назв рахунків, таблиць та описів.
### Added
- Додано `.env.dev` та `.env.prod` для безпечного збереження конфігураційних даних.

---

## [1.0.2] – 2026-03-15
### Fixed
- Усунуто 9 проблем із конфігурацією Docker та бекенду.
- Виправлено проблеми з підключенням до PostgreSQL.
- Відновлено автоматичне підключення до FastAPI (`/` та `/add_entry`).
- Налагоджено відображення даних у PowerShell без помилок кодування.

---

## [1.0.3] – 2026-03-23
### Added
- Інтеграція React‑фронтенду з ERP‑системою.
- Нові компоненти для бухгалтерського обліку та управління персоналом.
### Changed
- Оновлено `main.py` для інтеграції фронтенду.
- Налаштовано маршрути FastAPI для UI.
### Fixed
- Виправлено некоректне відображення балансу при додаванні записів.
### Security
- JWT‑автентифікація перероблена для нових фронтенд‑завантажень.

---

## [1.0.4] – 2026-03-24
### Added
- Інтегровано базовий React‑frontend для ERP‑системи.
- Додано нові форми для бухгалтерів та HR.
### Changed
- Новий скрипт `git-save.ps1` з підтримкою UTF‑8.
- Змінено структуру фронтенду для більшої організації компонентів.
- Оптимізовано підтримку FastAPI для стабільної роботи з JWT.
### Fixed
- Усунуто проблему з некоректним відображенням даних у PowerShell.
- Успішно інтегровано Docker‑контейнери після додавання фронтенду.
### Security
- JWT‑токени перероблені для різних ролей користувачів.

---

## [1.0.5] – 2026-03-26
### Added
- Ініціалізація ERP‑проєкту.

---

## [1.0.6] – 2026-03-27
### Added
- Оновлення CI‑pipeline та управління форматом `CHANGELOG.md`.
- Додано шаблон для майбутніх записів (Added / Changed / Fixed / Security).
### Changed
- Приведено формат усіх попередніх записів до стандарту CI.
- `README.md` втрачено через конфлікт при ребейзі.
### Fixed
- CI підключено через видимість початкової секції у `CHANGELOG.md`.
### Security
- Перевірено, що `.env.dev` та `.env.prod` залишаються у `.gitignore`.

## [2026-03-28] – v0.2.0
### Added
- CRUD функції для таблиць `users` та `products` у `db.py`.
- Клас `Product` з інтеграцією до бази даних.
- Новий релізний тег `v0.2.0` у GitHub.

### Changed
- Оновлено імпорти у `users.py` для правильного шляху `backend.modules.db`.
- Оновлено `requirements.txt` для роботи з `psycopg2`.
- Dockerfile адаптовано для нових залежностей.
- Перейменовано основну гілку з `Владелец` на `owner`.
- Оновлено remote‑структуру: тепер використовується `private` (Diplom-project) та `public` (Diplom-project-public).

### Fixed
- Перевірено роботу CRUD‑операцій у REPL.
- Видалення користувачів та продуктів працює коректно.

### Security
- `.gitignore` блокує `.env.dev`, `.env.prod` та `config/.env`.
- Перевірено, що секрети не потрапляють у публічний репозиторій.

---

## [2026-04-03] – owner
### Changed
- Оновлено файл `git-save.ps1`: додано коректне кодування UTF‑8 та команда `chcp 65001`.
- Налаштовано подвійний пуш у приватний та публічний репозиторії.
### Fixed
- Усунуто помилку з некоректним refspec.
- Виправлено відображення кирилиці у повідомленнях комітів.

---

## [2026-04-07]
### Changed
- Force‑push локальної версії у приватний та публічний репозиторії.
- Видалено зайві гілки `owner` та `Владелец`.
- Стандартизовано remote: залишено лише `origin`.
- Переписано `git-save.ps1`: залишено лише пуш у origin/master.

---

## [2026-04-11]
### Added
- Додано компонент JournalTable у `frontend/src/components`.
- Додано стилі `journal.css` для операцій журналу.
### Changed
- Оновлено `App.js` для інтеграції JournalTable.
- Оновлено `package.json` та `package-lock.json` після додавання нового компонента.
### Fixed
- Виправлено конфігурацію `git-save.ps1` після чистки гілок.
- Оновлено CHANGELOG для узгодження з новим стандартом комітів.
### Security
- Перевірено `.gitignore` для виключення `node_modules`, `build` та `.env` файлів.

---

## [Unreleased]
### Added
- Створено файл `.env.prod` для конфігурації PostgreSQL (POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB).
- Додано підтримку запуску контейнерів через docker-compose.
### Changed
- Оновлено інструкції для запуску ERP‑проєкту у WSL2 (Node.js, npm, Docker, PostgreSQL).
### Fixed
- Виправлено помилку запуску контейнерів через відсутність `.env.prod`.
### Security
- Пароль для PostgreSQL винесено у `.env.prod` замість відкритого використання у `docker-compose.yml`.

---

## [2026-04-15]
### Added
- Створено файл `.env.prod` у корені проєкту для запуску ERP‑системи.
- Додано `.gitattributes`.
### Changed
- Налаштовано `docker-compose` для використання `.env.prod`.
- Оновлено backend (auth, database, main).
- Оновлено CHANGELOG.md.
### Fixed
- Виправлено помилку "env file not found" при запуску контейнерів.

## [2026-04-18] Backend & Frontend Fixes

### Backend
- Додано CORSMiddleware у FastAPI для дозволу запитів з фронтенду (вирішено проблему CORS).
- Оновлено ендпоінт `/api/journal` — тепер дані з бази коректно повертаються у JSON.
- Перезапущено бекенд із новим кодом, перевірено роботу через Docker/uvicorn.

### Frontend
- JournalTable.js тепер отримує дані з бекенду без помилок.
- DataGrid відображає записи (усунено проблему "No rows").
- Додано логування у Console: `Отримані рядки: Array(3)` для підтвердження отримання даних.
- Перевірено перемикання теми (light/dark) у таблиці.

### Git
- Виконано автоматичний коміт через `git-save.ps1`.
- Останній коміт: "Автоматичний коміт" успішно запушено у гілку master.
## [2026-04-20] Frontend & Nginx Fixes

### Backend / Nginx
- Перезаписано файл `/etc/nginx/conf.d/default.conf` у контейнері `erp_frontend`.
- Додано директиву `try_files $uri /index.html;` для коректної роботи SPA‑маршрутів.
- Перевірено синтаксис через `nginx -t` — конфігурація валідна.
- Перезапущено контейнер `frontend`, nginx стартує без помилок.

### Frontend
- Виправлено 404 при переході на `/journal`, `/users`, `/products`.
- Статичні ресурси (`CSS`, `JS`, `manifest.json`, `logo192.png`) віддаються коректно.
- Додано нові маршрути у `App.js`: `/finance`, `/hr`, `/admin`.
- Оновлено навігаційне меню з посиланнями на нові модулі.

### ERP Project Progress
- Фронтенд тепер стабільно працює як SPA.
- Підготовлено основу для наступного етапу: авторизація через токен та розмежування доступу за ролями.
## [2026-04-20] Dockerfile & Nginx Update

### Frontend / Dockerfile
- Оновлено Dockerfile для фронтенду.
- Додано копіювання власного конфігу nginx:
  COPY nginx/default.conf /etc/nginx/conf.d/default.conf
- Тепер при кожному docker-compose build конфіг nginx автоматично застосовується.

### Nginx
- Робочий default.conf витягнуто з контейнера та додано у репозиторій.
- Забезпечено збереження правок після rebuild.

### ERP Project Progress
- Фронтенд стабільно працює як SPA.
- Конфігурація тепер зберігається у вихідних файлах проєкту.
## [2026-04-21] Frontend build & ERP modules

- Додано базові компоненти-заглушки для модулів ERP:
  - Finance (Фінанси)
  - HR (Відділ кадрів)
  - Admin (Адміністратор)
  - Products (Продукти)
  - PKash (Каса)
- Успішно пересобрано образ фронтенду через `docker-compose build frontend`
- Запущено контейнер `erp_frontend` разом із `erp_backend` та `erp_db`
- Перевірено роботу nginx з локальним конфігом `frontend/nginx/default.conf`
- React/Material UI білд завершився успішно (`Compiled successfully`)
## [2026-04-21] Build & Network Fixes
- Пересоздано мережу diplom-project_erp_network (enable_ipv4 / enable_ipv6).
- Повна збірка backend (Python 3.12-slim) та frontend (Node 18-alpine + Nginx).
- Оптимізовано Dockerfile: requirements.txt → pip install, npm install → npm run build.
- Контейнери erp_db, erp_backend, erp_frontend успішно підняті у WSL2 без Docker Desktop.
### 2026-04-21
- Додано компонент ProtectedRoute.jsx для захисту маршрутів за ролями
- Оновлено App.jsx: додано маршрути для Finance, HR, Admin, Products, PKash
- Створено нові модулі: Inventory.jsx, Purchases.jsx, Sales.jsx, Legal.jsx
- Оновлено App.jsx: додано маршрути для Inventory, Purchases, Sales, Legal
- Підготовлено план робіт для бекенду (API ендпоінти та ролі)
## [2026-04-21] Backend Routers Init
- Створено базові роутери FastAPI:
  - /api/finance
  - /api/inventory
  - /api/purchases
  - /api/sales
  - /api/legal
- Додано мінімальні Pydantic‑моделі (FinanceEntry, InventoryItem, PurchaseContract, SaleRecord, LegalDoc).
- Підключено роутери у main.py.
- Додано заглушки JSON для тестових запитів.
- External Postgres port changed from 5432 to 5433
## [2026-04-23]
- Додано нові роутери у FastAPI: Finance, Inventory, Purchases, Sales, Legal
- Створено мінімальні Pydantic‑моделі для кожного модуля
- Підключено всі роутери у main.py
- Додано заглушки JSON для тестових ендпоінтів
### 2026-04-24
- Додано заглушки JSON для тестових ендпоінтів:
  - /api/finance → фінансові операції
  - /api/inventory → інвентаризація
  - /api/purchases → закупівлі
  - /api/sales → продажі
  - /api/legal → юридичні документи
- Виправлено дублювання префіксів у роутерах (prefix тепер задається тільки в main.py)
## [2026-04-26]
### Added
- Додано 9 ролей у JWT токен: Finance, HR, Admin, Products, PKash, Inventory, Purchases, Sales, Legal
- Додано ендпоінти для Products та PKash
### Changed
- Оновлено main.py: інтеграція всіх ролей, перевірка доступу через токен
### Fixed
- Виправлено дублювання ендпоінтів, залишено чисту структуру з роутерами
## [2026-04-27]
### Added
- Додано JWT‑авторизацію для 9 ролей (admin, accountant, hr, products, pkash, inventory, purchases, sales, legal).
- Додано колонку `amount` у таблицю journal для зберігання сум операцій.

### Changed
- Налаштовано SQL‑запити для вибірки та сортування даних по колонці `amount`.
- Оновлено інтеграцію `main.py` для перевірки доступу через токен.

### Fixed
- Виправлено помилки при виконанні SQL‑запитів у Bash (тепер використовується правильний контекст psql).
- Перевірено відмову доступу (403) для чужих модулів.

### Verified
- Перевірено отримання токенів для кожної ролі.
- Ендпоінти `/finance`, `/inventory`, `/sales`, `/legal` доступні відповідно до ролей.
- Ролі працюють коректно: користувачі бачать лише свої дані.

## [2026-04-29]
- Створено контролер usersController.js з CRUD‑операціями
- Налаштовано маршрути для Users, Finance, HR, Admin, Journal, Products, Purchases, PKash, Legal
- Видалено зайвий файл home.js, замінено на legal.js
- Переписано App.jsx з правильним використанням ProtectedRoute (requiredRole + currentRole)
- Підготовлено план інтеграції фронтенду з бекендом
## [2026-04-30]
- Перенесено всі робочі таблиці у frontend/src/components
- Видалено дублікати пустих файлів таблиць
- Переписано App.jsx: додано Material UI тему, меню навігації та ProtectedRoute для ролей
- Оновлено index.js для імпорту App.jsx
- Видалено App.js як дубль
## [2026-05-06]
- Додано компонент NavBar.jsx для UI навігації між модулями ERP.
- Підключено NavBar у App.jsx.
- Перевірено всі маршрути у App.jsx — модулі Finance, HR, Admin, Products, PKash, Inventory, Purchases, Sales, Legal.
- Закрито пункти 5 і 6 плану (маршрути та UI навігація).
- Встановлено axios у frontend для роботи з компонентами.
## [2026-05-07]
### Added
- Додано сервіс резервного копіювання бази даних у docker-compose.yml.
- Створено скрипт `backup.sh` для автоматичного щоденного дампу бази `erp_diplom`.

### Changed
- Оновлено конфігурацію `docker-compose.yml` для коректного запуску бекенду, фронтенду та бази у WSL2.
- Виправлено інтерполяцію команди у сервісі `backup`.

### Fixed
- Усунено помилку `Invalid interpolation format` у секції `backup`.
## [2026-05-13]
- Налаштовано розгортання контейнерів ERP‑проєкту через Docker Compose
- Виправлено проблеми із запуском фронтенду (контейнери не піднімалися)
- Перевірено роботу PostgreSQL контейнера (a7de60bac498_erp_db)
- Узгоджено запуск сервісів тільки з кореня проєкту (docker-compose.yml)
- Вимкнено pager у psql для зручної роботи
- Перевірено структуру таблиць accounts та entry_lines
- Створено таблицю journal з прив’язкою до entry_lines
- Перевірено всі констрейнти (accounts ↔ entry_lines ↔ journal)
## [2026-05-15]
### Added
- Додано модуль Journal (`backend/routers/journal_router.py`).
- Створено компонент JournalTable.jsx для фронтенду.
- Ініціалізовано init.sql для бази даних.
- Зроблено резервну копію `erp_diplom_2026-05-15_11-17.sql`.
### Changed
- Запущено бекенд FastAPI з модулем Journal.
- Запущено фронтенд React на порту 3000, успішна компіляція.
### Verified
- Перевірено роботу ендпоінта `/api/journal` — отримано коректний JSON з кирилицею.
- Виконано інтеграцію логіну з ролями через `/token`.

---

## [2026-05-21]
### Added
- Підключено `journal_router` через `backend.schemas`.
- Реалізовано CRUD‑ендпоінти для Journal (GET, POST, PUT, DELETE).
### Changed
- Перенесено `journal_router.py` у `backend/schemas/` для інтеграції з ORM та схемами.
- Основні роутери залишаються у `backend/routers/` для модульної архітектури.
### Verified
- CRUD‑операції для Journal перевірені через curl (GET/POST/PUT/DELETE).
- Підтверджено коректну відповідь JSON на всі CRUD‑операції.

---

## [2026-05-27]
### Added
- Виправлено циклічні імпорти у `backend/models/journal.py`.
- Переписано моделі Journal та Finance з чіткими колонками.
- Оновлено `backend/models/__init__.py` для коректного імпорту моделей.
- Переписано схеми Journal та Finance (Pydantic v2, from_attributes).
### Verified
- Запущено сервер на порту 8001 без конфліктів.
- Swagger UI: доступні CRUD‑ендпоінти для Journal та Finance, а також фінансові звіти (/add_entry, /balance, /report, /plot).
### Finance Module
- Пересобрано Docker‑контейнери (backend, frontend, db, backup).
- Перевірено структуру таблиці `finance` у БД `erp_diplom`.
- Додано колонки (`date`, `debit`, `credit`, `description`).
- Виконано тестовий INSERT → дані успішно збережені.
- CRUD‑операції Finance працюють коректно (POST, PUT, DELETE, GET).
- Особливість: поле `date` у схемі `FinanceUpdate` не оновлюється через PUT.

### Next Steps
- Протестувати спеціальні фінансові ендпоінти: `/add_entry`, `/balance`, `/report`, `/plot`.
- Підключити фронтенд (React + Material UI) для Journal і Finance.
## [2026-05-28]
- Завершено повний CRUD для модуля Journal (створення, читання, оновлення, видалення).
- Завершено повний CRUD для модуля Finance (створення, читання, оновлення, видалення).
- Перевірено роботу з кількома записами у Finance, включно з оновленням та видаленням.
- Підтверджено стабільність базових моделей Journal та Finance.
## [2026-05-31]
### Added
- Реалізовано ендпоінт `/api/finance/balance/{account_id}` для отримання балансу по рахунку.
- Переписано `finance_router.py` з повним CRUD для Finance та додатковим маршрутом `/balance/{id}`.
- Перевірено роботу ендпоінта через `curl` — повертає коректний результат.

### Fixed
- Усунено помилку `Internal Server Error` при виклику `/balance/{id}`.
## [2026-06-03]
### Backend
- Завершено повний цикл CRUD для всіх модулів:
  - Inventory (створення, читання, оновлення, видалення)
  - Purchases (з урахуванням поля country)
  - Sales (з урахуванням полів client та invoice)
  - Legal (з урахуванням полів contract та partner)
  - Finance (CRUD + баланс по рахунку)
- Переписано `finance_router.py`:
  - Додано спецмаршрути `/add_entry`, `/report`, `/plot`
  - Тепер підтримуються фінансові операції, звіти та побудова графіків
- Перевірено роботу всіх CRUD‑ендпоінтів — усі повертають коректні відповіді.
- Баланс‑ендпоінт працює стабільно, повертає суму по рахунку з урахуванням Journal.
### Status
✅ Бекенд‑частина ERP закрита повністю.

---

## [2026-06-04]
### Added
- Додано новий запис у journal через `/api/finance/add_entry` (account_id=1, income, completed, amount=1500).
- Додано нові компоненти у фронтенд: FinancePlot.jsx, FinanceReportTable.jsx.
- Створено резервні дампи бази у `backups/erp_diplom_2026-06-04_*.sql`.
### Verified
- Перевірено баланс по рахунку (account_id=1) — результат 3000.0.
- Згенеровано звіт за період 2026-06-01 → 2026-06-04, запис успішно відображається.
- Побудовано графік для account_id=1, точка відображається коректно.
- Налагоджено SSH‑автентифікацію для GitHub (id_ed25519), виконано успішний пуш у приватний репозиторій (master branch).

---

## [2026-06-07] Backend & DB стабілізація + ярлик запуску
### Changed
- Виправлено конфігурацію `docker-compose.yml` для Postgres 18 (правильний том `/var/lib/postgresql`).
- Пересобрано середовище: база `erp_diplom` піднята у статусі healthy.
- Бекенд (`erp_backend`) стартує стабільно, Uvicorn слухає на порту 8000.
- Фронтенд (`erp_frontend`) успішно збирається та працює на порту 3000.
### Verified
- Перевірено наявність таблиць у базі: accounts, finance, inventory, journal, legal, purchases, sales.
### Added
- Додано PowerShell‑скрипт `start-erp.ps1` для запуску ERP.
- Створено ярлик на робочому столі Windows, який виконує `start-erp.ps1` для швидкого доступу до ERP‑системи.

---

## [2026-06-11] Рефакторинг роутерів, main.py та підготовка інсталяції
### Changed
- Видалено параметр `prefix` у всіх файлах роутерів (journal, finance, inventory, purchases, sales, legal).
- Централізовано додано префікси у `main.py` для `/api/journal`, `/api/finance`, `/api/inventory`, `/api/purchases`, `/api/sales`, `/api/legal`.
- Спеціальні фінансові ендпоінти (`/add_entry`, `/balance/{id}`, `/report`, `/plot`) перенесено під єдиний шлях `/api/finance/...`.
### Added
- Створено файл `start-erp.ps1` для автоматичного запуску ERP‑системи на Windows.
- Налаштовано `docker-compose.yml` для підняття контейнера PostgreSQL (`erp_db`) з volume‑mount.
### Documentation
- Всі зміни документуються у `CHANGELOG.md` та пушаться через `git-double-push.sh` одночасно у приватний та публічний репозиторії.
- Підготовлено інструкції для сторонніх користувачів (клонування, запуск Docker, виконання `start-erp.ps1`, відкриття фронтенду та бекенду).
### Goal
- Уніфікація структури URL → всі ендпоінти тепер мають стабільний формат `/api/<module>/...`.
- Спрощення підтримки → префікси задаються лише в одному місці (`main.py`).
- Підготовка до використання третіми особами → будь‑який користувач може легко інсталювати та запустити ERP‑систему на власному ПК.

---

## [2026-06-16] Deployment Update
### Added
- Файл `start-erp.sh` для автоматичного запуску ERP у Linux/WSL.
- Інструкцію з відновлення бази даних у `README-deploy.md`.
- Блок документації API у `README-deploy.md` з посиланням на Swagger та переліком основних модулів.
### Changed
- Оновлено `README-deploy.md`: тепер він містить єдиний цілісний текст для користувачів.
- Замінено всі згадки “для викладача” на **“Інструкція для користувачів”**.

## [2026-06-19] Documentation Cleanup

### Changed
- Оновлено Deployment Guide (README-deploy.md): виправлено дублювання прикладів JSON‑запитів.
- Закрито всі блоки коду у секції "📑 Приклади JSON‑запитів" для коректного відображення Markdown.
- Перевірено структуру файлу (154 рядки) — підтверджено логічну послідовність розділів.

### Fixed
- Усунуто дублікати у CHANGELOG.txt (Unreleased, owner, 2026‑04‑07, 2026‑05‑15).
- Виправлено конфліктні записи після ребейзу, залишено лише унікальні зміни.
- Видалено помилковий запис про додавання `start-erp.sh` та `start-erp.ps1`, який не відповідав реальним діям.

### Verified
- Підтверджено, що документація відповідає стандарту [Keep a Changelog].
- Перевірено узгодженість між README‑deploy.md та CHANGELOG.md.
### Зміни за 02.07.2026
- Додано балансувальник у docker-compose для запуску кількох інстансів FastAPI.
- Створено `frontend/Dockerfile` з multi-stage build (React → Nginx).
- Створено `frontend/nginx.conf` для проксування запитів `/api/` на бекенд та віддачі фронтенду.
- Перевірено структуру таблиць у базі `erp_diplom` (accounts, journal).
- Вставлено тестові записи для перевірки зв’язку між accounts та journal.
- Виявлено проблему: Nginx показує дефолтну сторінку та блокує POST‑запити.
- Додано інструкцію `COPY ./nginx.conf /etc/nginx/nginx.conf` у `frontend/Dockerfile`.
- Зупинились на етапі перевірки та пересборки контейнера frontend, щоб Nginx підхопив кастомний конфіг і працював як reverse proxy для бекенду.
укцію `COPY ./nginx.conf /etc/nginx/nginx.conf` у `frontend/Dockerfile`.
- Зупинились на етапі перевірки та пересборки контейнера `frontend`, щоб Nginx підхопив кастомний конфіг і працював як reverse proxy для бекенду.
## 2026-07-03
- Перевірено авторизацію через /token
- CRUD у Journal: створення, оновлення, перегляд
- Accounts доступні (порожня таблиця)
- Finance, Inventory, Purchases, Sales, Legal — протестовано створення записів із required-полями
- CRUD підтверджено для всіх модулів
