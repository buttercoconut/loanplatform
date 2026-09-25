import { createRouter, createWebHistory } from 'vue-router'
import LoanApplicationView from '../views/LoanApplicationView.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: LoanApplicationView
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
