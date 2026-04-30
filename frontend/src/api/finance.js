import api from './axiosInstance';

export const getFinanceData = async () => {
  const response = await api.get('/finance');
  return response.data;
};
