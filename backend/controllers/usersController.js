// Тестові дані користувачів
let users = [
  { id: 1, name: 'Ivan Petrenko', role: 'HR Manager' },
  { id: 2, name: 'Olena Shevchenko', role: 'Accountant' }
];

// Отримати всіх користувачів
exports.getAllUsers = (req, res) => {
  res.json(users);
};

// Отримати користувача за ID
exports.getUserById = (req, res) => {
  const user = users.find(u => u.id === parseInt(req.params.id));
  user ? res.json(user) : res.status(404).json({ message: 'User not found' });
};

// Створити нового користувача
exports.createUser = (req, res) => {
  const newUser = { id: users.length + 1, ...req.body };
  users.push(newUser);
  res.status(201).json(newUser);
};

// Оновити користувача
exports.updateUser = (req, res) => {
  const idx = users.findIndex(u => u.id === parseInt(req.params.id));
  if (idx !== -1) {
    users[idx] = { ...users[idx], ...req.body };
    res.json(users[idx]);
  } else {
    res.status(404).json({ message: 'User not found' });
  }
};

// Видалити користувача
exports.deleteUser = (req, res) => {
  users = users.filter(u => u.id !== parseInt(req.params.id));
  res.json({ message: 'User deleted' });
};

