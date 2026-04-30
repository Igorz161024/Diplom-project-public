import axios from './axiosInstance';

export const getSalesData = async () => {
  const response = await axios.get('/sales');
  return response.data;
};
