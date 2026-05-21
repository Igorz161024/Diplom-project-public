import api from './axiosInstance';

export const getHRData = async () => {
  const response = await api.get('/hr');
  return response.data;
};
