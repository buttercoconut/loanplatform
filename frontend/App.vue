<template>
  <div id="app">
    <LoanApplicationForm />
  </div>
</template>

<script>
import LoanApplicationForm from './components/LoanApplicationForm.vue';
export default {
  name: 'App',
  components: { LoanApplicationForm },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
