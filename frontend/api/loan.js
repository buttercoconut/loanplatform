// API communication module using Axios
import axios from 'axios'

const apiClient = axios.create({
  baseURL: process.env.VUE_APP_API_BASE_URL || 'http://localhost:8000',
  timeout: 5000,
})

export async function applyLoan(payload) {
  const response = await apiClient.post('/loans/apply', payload)
  return response.data
}
