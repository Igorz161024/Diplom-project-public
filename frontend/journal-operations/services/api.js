const mockData = [
  {
    date: "03.04.2026",
    doc: "Реалізація товарів №15",
    num: "15",
    client: "ТОВ 'Клієнт'",
    sum: "10 000,00 грн",
    status: "Проведено"
  },
  {
    date: "03.04.2026",
    doc: "Прибутковий касовий ордер №7",
    num: "7",
    client: "ТОВ 'Клієнт'",
    sum: "10 000,00 грн",
    status: "Проведено"
  },
  {
    date: "03.04.2026",
    doc: "Акт списання товарів №5",
    num: "5",
    client: "Собівартість",
    sum: "7 000,00 грн",
    status: "Проведено"
  }
];

// функція для отримання даних (імітація API-запиту)
export const fetchJournalData = () => {
  return Promise.resolve(mockData);
};
