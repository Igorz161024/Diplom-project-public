import api from './axiosInstance';

export const getProductsData = async () => {
  const response = await api.get('/products');
  return response.data;
};
