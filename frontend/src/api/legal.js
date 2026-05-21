import axios from './axiosInstance';

export const getLegalData = async () => {
  const response = await axios.get('/legal');
  return response.data;
};
