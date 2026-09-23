"""
API wrapper using Axios.
"""
import axios from 'axios';

const api = axios.create({
  baseURL: process.env.VUE_APP_API_URL || 'http://localhost:8000',
});

export const applyLoan = async (payload) => {
  const response = await api.post('/loans/apply', payload);
  return response.data;
};
