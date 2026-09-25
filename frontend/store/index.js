import { createStore } from 'vuex'

export default createStore({
  state: {
    loans: [],
  },
  mutations: {
    setLoans(state, loans) {
      state.loans = loans
    },
  },
  actions: {
    fetchLoans({ commit }) {
      // placeholder for future API call
      commit('setLoans', [])
    },
  },
})
