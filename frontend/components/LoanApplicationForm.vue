<template>
  <div class="loan-form">
    <h2>대출 신청</h2>
    <form @submit.prevent="onSubmit">
      <label>
        이름:
        <input v-model="form.name" required />
      </label>
      <label>
        소득(원):
        <input type="number" v-model.number="form.income" required />
      </label>
      <label>
        부채(원):
        <input type="number" v-model.number="form.debt" required />
      </label>
      <label>
        대출 금액(원):
        <input type="number" v-model.number="form.amount" required />
      </label>
      <button type="submit">제출</button>
    </form>
  </div>
</template>

<script>
import { mapActions } from 'vuex';
import api from '../api/loan';

export default {
  name: 'LoanApplicationForm',
  data() {
    return {
      form: {
        name: '',
        income: 0,
        debt: 0,
        amount: 0,
      },
    };
  },
  methods: {
    ...mapActions(['submitApplication']),
    async onSubmit() {
      const payload = { ...this.form };
      try {
        const res = await api.submitApplication(payload);
        this.submitApplication(res.data);
        alert('신청이 접수되었습니다!');
      } catch (e) {
        console.error(e);
        alert('오류가 발생했습니다.');
      }
    },
  },
};
</script>

<style scoped>
.loan-form {
  max-width: 400px;
  margin: auto;
}
label {
  display: block;
  margin-bottom: 10px;
}
</style>
