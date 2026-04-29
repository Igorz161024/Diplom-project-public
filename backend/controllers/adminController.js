exports.getAllAdmins = (req, res) => {
  res.json([
    { id: 1, username: 'admin1', role: 'SuperAdmin', active: true },
    { id: 2, username: 'admin2', role: 'Moderator', active: false }
  ]);
};
