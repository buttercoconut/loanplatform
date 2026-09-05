# Frontend Vue3 component for loan application form
<template>
  <div class="loan-application">
    <h2>대출 신청</h2>
    <form @submit.prevent="submitForm">
      <label>금액: <input v-model.number="form.amount" type="number" required /></label>
      <label>기간(개월): <input v-model.number="form.termMonths" type="number" required /></label>
      <label>연소득: <input v-model.number="form.annualIncome" type="number" required /></label>
      <label>부채비율: <input v-model.number="form.debtToIncomeRatio" type="number" step="0.01" required /></label>
      <label>신용점수: <input v-model.number="form.creditScore" type="number" required /></label>
      <button type="submit">신청</button>
    </form>
    <div v-if="response">
      <h3>결과</h3>
      <pre>{{ response }}</pre>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { applyLoan } from '@/api/loan'

const form = ref({
  amount: 0,
  termMonths: 12,
  annualIncome: 0,
  debtToIncomeRatio: 0,
  creditScore: 0,
})
const response = ref(null)

async function submitForm() {
  try {
    const res = await applyLoan(form.value)
    response.value = res
  } catch (e) {
    response.value = { error: e.message }
  }
}
</script>

<style scoped>
.loan-application {
  max-width: 400px;
  margin: auto;
}
label {
  display: block;
  margin-bottom: 8px;
}
button {
  margin-top: 12px;
}
</style>
