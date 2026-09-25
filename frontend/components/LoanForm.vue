<template>
  <div class="loan-form">
    <h2>대출 신청</h2>
    <form @submit.prevent="submitForm">
      <label>고객 ID:</label>
      <input v-model.number="form.customer_id" type="number" required />

      <label>상품 ID:</label>
      <input v-model.number="form.product_id" type="number" required />

      <label>금액:</label>
      <input v-model.number="form.amount" type="number" required />

      <label>기간(개월):</label>
      <input v-model.number="form.term_months" type="number" required />

      <label>소득:</label>
      <input v-model.number="form.income" type="number" required />

      <label>부채비율:</label>
      <input v-model.number="form.debt_ratio" type="number" step="0.01" required />

      <label>신용점수:</label>
      <input v-model.number="form.credit_score" type="number" required />

      <button type="submit">제출</button>
    </form>
    <div v-if="response">
      <h3>결과</h3>
      <pre>{{ response }}</pre>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from "vue"
import { submitLoanApplication } from "@/api/loanApi"

const form = reactive({
  customer_id: 0,
  product_id: 0,
  amount: 0,
  term_months: 0,
  income: 0,
  debt_ratio: 0,
  credit_score: 0,
})
const response = ref(null)

async function submitForm() {
  try {
    const res = await submitLoanApplication(form)
    response.value = res
  } catch (e) {
    response.value = { error: e.message }
  }
}
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
