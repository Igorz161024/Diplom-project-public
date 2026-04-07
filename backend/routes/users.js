const express = require('express');
const router = express.Router();
const usersController = require('../controllers/usersController');

// маршрут для отримання всіх користувачів
router.get('/', usersController.getAllUsers);

module.exports = router;
