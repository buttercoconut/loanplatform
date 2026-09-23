"""
Vue component for loan application form.
"""
<template>
  <div class="loan-form">
    <h2>대출 신청</h2>
    <form @submit.prevent="submitForm">
      <label>고객 ID</label>
      <input v-model="form.customer_id" type="number" required />

      <label>상품 ID</label>
      <input v-model="form.product_id" type="number" required />

      <label>대출 금액</label>
      <input v-model="form.amount" type="number" required />

      <label>기간(개월)</label>
      <input v-model="form.term_months" type="number" required />

      <label>소득</label>
      <input v-model="form.income" type="number" required />

      <label>부채</label>
      <input v-model="form.debt" type="number" required />

      <label>신용 점수</label>
      <input v-model="form.credit_score" type="number" required />

      <button type="submit">신청</button>
    </form>
    <div v-if="response">
      <h3>결과</h3>
      <pre>{{ response }}</pre>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { applyLoan } from "@/api/loan";

const form = ref({
  customer_id: 0,
  product_id: 0,
  amount: 0,
  term_months: 0,
  income: 0,
  debt: 0,
  credit_score: 0,
});
const response = ref(null);

const submitForm = async () => {
  try {
    const res = await applyLoan(form.value);
    response.value = res;
  } catch (e) {
    console.error(e);
    response.value = { error: e.message };
  }
};
</script>

<style scoped>
.loan-form {
  max-width: 400px;
  margin: auto;
}
label {
  display: block;
  margin-top: 10px;
}
input {
  width: 100%;
}
button {
  margin-top: 15px;
}
</style>
