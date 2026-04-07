const express = require('express');
const app = express();
const PORT = 3000;

// Підключення маршруту користувачів
const usersRoutes = require('./backend/routes/users');
app.use('/api/users', usersRoutes);

// Тестовий кореневий маршрут
app.get('/', (req, res) => {
  res.send('ERP server is running');
});

app.listen(PORT, () => {
  console.log(`Server started on port ${PORT}`);
});
