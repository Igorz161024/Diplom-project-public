import api from './axiosInstance';

export const getAdminData = async () => {
  const response = await api.get('/admin');
  return response.data;
};
