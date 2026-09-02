<template>
  <div class="loan-form">
    <h2>Loan Application</h2>
    <form @submit.prevent="submitForm">
      <div>
        <label>Applicant ID</label>
        <input v-model.number="form.applicant_id" required />
      </div>
      <div>
        <label>Loan Product ID</label>
        <input v-model.number="form.loan_product_id" required />
      </div>
      <div>
        <label>Amount</label>
        <input v-model.number="form.amount" type="number" required />
      </div>
      <div>
        <label>Income</label>
        <input v-model.number="form.income" type="number" required />
      </div>
      <div>
        <label>Debt Ratio</label>
        <input v-model.number="form.debt_ratio" type="number" step="0.01" required />
      </div>
      <div>
        <label>Credit Score</label>
        <input v-model.number="form.credit_score" type="number" required />
      </div>
      <button type="submit">Apply</button>
    </form>
    <p v-if="message">{{ message }}</p>
  </div>
</template>

<script>
import { applyLoan } from "@/api/loan.js";
export default {
  name: "LoanApplicationForm",
  data() {
    return {
      form: {
        applicant_id: 0,
        loan_product_id: 0,
        amount: 0,
        income: 0,
        debt_ratio: 0,
        credit_score: 0,
      },
      message: "",
    };
  },
  methods: {
    async submitForm() {
      try {
        const res = await applyLoan(this.form);
        this.message = `Application submitted: ${JSON.stringify(res)}`;
      } catch (e) {
        this.message = `Error: ${e.response?.data?.detail || e.message}`;
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
.loan-form div {
  margin-bottom: 10px;
}
</style>
