INSERT INTO journal (date, operation, status, amount)
VALUES
(CURRENT_DATE, 'Оновлення даних', 'WARNING', 150),
(CURRENT_DATE, 'Видалення клієнта', 'ERROR', 0),
(CURRENT_DATE, 'Cash>Revenue', 'SUCCESS', 250);

SELECT * FROM journal;
