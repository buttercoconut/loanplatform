<template>
  <div class="loan-application-form">
    <h2>대출 신청서</h2>
    <form @submit.prevent="onSubmit">
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
        <label for="loanAmount">대출 금액 (원)</label>
        <input v-model.number="form.loanAmount" id="loanAmount" type="number" required />
      </div>
      <div class="form-group">
        <label for="loanTerm">상환 기간 (개월)</label>
        <input v-model.number="form.loanTerm" id="loanTerm" type="number" required />
      </div>
      <button type="submit">신청하기</button>
    </form>
    <div v-if="status" class="status">
      <p>신청 상태: {{ status }}</p>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import loanApi from '../api/loan'

const form = reactive({
  name: '',
  email: '',
  income: 0,
  loanAmount: 0,
  loanTerm: 12
})
const status = ref('')

const onSubmit = async () => {
  try {
    const response = await loanApi.submitApplication(form)
    status.value = '신청 접수 완료. ID: ' + response.data.id
  } catch (err) {
    status.value = '오류: ' + err.message
  }
}
</script>

<style scoped>
.loan-application-form {
  max-width: 400px;
  margin: 0 auto;
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
  background: #42b983;
  color: white;
  border: none;
  cursor: pointer;
}
.status {
  margin-top: 1rem;
  font-weight: bold;
}
</style>
