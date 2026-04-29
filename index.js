const express = require('express');
const app = express();
const PORT = 5000;

// Підключення маршруту користувачів
const usersRoutes = require('./backend/routes/users');
app.use('/api/users', usersRoutes);

// Підключення маршруту фінансів
const financeRoutes = require('./backend/routes/finance');
app.use('/api/finance', financeRoutes);

// Тестовий кореневий маршрут
app.get('/', (req, res) => {
  res.send('ERP server is running');
});

// Запуск сервера
app.listen(PORT, () => {
  console.log(`ERP backend started on port ${PORT}`);
});

