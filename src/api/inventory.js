import axios from './axiosInstance';

export const getInventoryData = async () => {
  const response = await axios.get('/inventory');
  return response.data;
};
