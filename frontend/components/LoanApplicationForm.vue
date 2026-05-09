<template>
  <div class="loan-application-form">
    <h2>대출 신청서</h2>
    <form @submit.prevent="handleSubmit">
      <div class="form-group">
        <label for="name">이름</label>
        <input v-model="form.name" id="name" type="text" required />
      </div>
      <div class="form-group">
        <label for="email">이메일</label>
        <input v-model="form.email" id="email" type="email" required />
      </div>
      <div class="form-group">
        <label for="income">연간 소득 (원)</label>
        <input v-model.number="form.income" id="income" type="number" required />
      </div>
      <div class="form-group">
        <label for="debt">현재 부채 (원)</label>
        <input v-model.number="form.debt" id="debt" type="number" required />
      </div>
      <div class="form-group">
        <label for="amount">대출 금액 (원)</label>
        <input v-model.number="form.amount" id="amount" type="number" required />
      </div>
      <div class="form-group">
        <label for="term">대출 기간 (개월)</label>
        <input v-model.number="form.term" id="term" type="number" required />
      </div>
      <button type="submit" :disabled="loading">제출</button>
    </form>
    <div v-if="message" class="message">
      {{ message }}
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue';
import { submitLoanApplication } from '../api/loan.js';
import { useStore } from 'vuex';

const store = useStore();
const loading = ref(false);
const message = ref('');

const form = reactive({
  name: '',
  email: '',
  income: 0,
  debt: 0,
  amount: 0,
  term: 0,
});

const handleSubmit = async () => {
  loading.value = true;
  message.value = '';
  try {
    const result = await submitLoanApplication({
      name: form.name,
      email: form.email,
      income: form.income,
      debt: form.debt,
      loan_amount: form.amount,
      loan_term_months: form.term,
    });
    store.dispatch('updateLoanApplication', result);
    message.value = '신청이 접수되었습니다! 심사 결과는 곧 알려드립니다.';
  } catch (err) {
    message.value = '신청 중 오류가 발생했습니다. 다시 시도해주세요.';
  } finally {
    loading.value = false;
  }
};
</script>

<style scoped>
.loan-application-form {
  max-width: 500px;
  margin: 0 auto;
  padding: 1rem;
  border: 1px solid #ccc;
  border-radius: 8px;
}
.form-group {
  margin-bottom: 1rem;
}
label {
  display: block;
  margin-bottom: 0.5rem;
}
input {
  width: 100%;
  padding: 0.5rem;
  box-sizing: border-box;
}
button {
  padding: 0.75rem 1.5rem;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
button[disabled] {
  background-color: #aaa;
}
.message {
  margin-top: 1rem;
  font-weight: bold;
}
</style>
