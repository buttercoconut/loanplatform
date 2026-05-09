import { createStore } from 'vuex';

const store = createStore({
  state() {
    return {
      loanApplication: null,
    };
  },
  mutations: {
    setLoanApplication(state, payload) {
      state.loanApplication = payload;
    },
  },
  actions: {
    updateLoanApplication({ commit }, payload) {
      commit('setLoanApplication', payload);
    },
  },
  getters: {
    getLoanApplication(state) {
      return state.loanApplication;
    },
  },
});

export default store;
