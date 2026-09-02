import axios from 'axios';
const API_URL = process.env.VUE_APP_API_URL || 'http://localhost:8000';

export async function applyLoan(data) {
  const response = await axios.post(`${API_URL}/loans/apply`, data);
  return response.data;
}

export async function getLoanStatus(appId) {
  const response = await axios.get(`${API_URL}/loans/status/${appId}`);
  return response.data;
}
