import { createRouter, createWebHistory } from 'vue-router';
import LoanApplicationForm from '../components/LoanApplicationForm.vue';

const routes = [
  {
    path: '/',
    name: 'LoanApplication',
    component: LoanApplicationForm,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
