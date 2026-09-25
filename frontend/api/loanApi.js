import axios from 'axios'

const API_BASE = process.env.VUE_APP_API_BASE || 'http://localhost:8000'

export async function submitLoanApplication(data) {
  const response = await axios.post(`${API_BASE}/loans/apply`, data)
  return response.data
}
