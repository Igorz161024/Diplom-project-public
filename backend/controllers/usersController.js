// Контролер для роботи з користувачами

// Повертає список користувачів (поки що тестові дані)
exports.getAllUsers = (req, res) => {
  res.status(200).json([
    { id: 1, name: 'Test User' },
    { id: 2, name: 'Another User' },
    { id: 3, name: 'ERP Admin' }
  ]);
};

