import api from './axiosInstance';

export const getPurchasesData = async () => {
  const response = await api.get('/purchases');
  return response.data;
};
