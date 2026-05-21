// roles.js
export const rolesConfig = {
  Admin: ["/users", "/products", "/journal", "/pkash", "/legal", "/purchases", "/sales", "/hr"],
  Buchgalter: ["/journal", "/pkash", "/products"],
  HR: ["/hr", "/users"],
  Legal: ["/legal"],
  Sales: ["/sales", "/products"],
  Purchases: ["/purchases", "/products"]
};

// функція перевірки доступу
export function hasAccess(role, path) {
  const allowed = rolesConfig[role] || [];
  return allowed.includes(path);
}
