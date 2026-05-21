import api from './axiosInstance';

export const getPKashData = async () => {
  const response = await api.get('/pkash');
  return response.data;
};
