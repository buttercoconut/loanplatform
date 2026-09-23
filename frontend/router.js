"""
Vue router.
"""
import { createRouter, createWebHistory } from 'vue-router';
import LoanForm from '@/components/LoanForm.vue';

const routes = [
  { path: '/', component: LoanForm },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
