const express = require("express");
const path = require("path");

const app = express();

// Приклад API‑маршруту бекенду
app.get("/api/hello", (req, res) => {
  res.json({ message: "Hello from backend!" });
});

// Віддавати статичні файли з React‑збірки
app.use(express.static(path.join(__dirname, "frontend/build")));

// Для будь‑якого маршруту, який не є API, віддавати index.html
app.get("*", (req, res) => {
  res.sendFile(path.join(__dirname, "frontend/build", "index.html"));
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});






