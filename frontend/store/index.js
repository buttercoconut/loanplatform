import { createStore } from 'vuex';

export default createStore({
  state: {
    loans: [],
  },
  mutations: {
    setLoans(state, loans) {
      state.loans = loans;
    },
  },
  actions: {
    // placeholder for future actions
  },
  getters: {
    allLoans: (state) => state.loans,
  },
});
