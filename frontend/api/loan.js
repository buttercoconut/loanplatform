import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:8000/api', // Adjust to backend URL
  timeout: 5000,
});

export const submitLoanApplication = async (data) => {
  try {
    const response = await apiClient.post('/loan-applications/', data);
    return response.data;
  } catch (error) {
    console.error('Loan application submission error:', error);
    throw error;
  }
};
