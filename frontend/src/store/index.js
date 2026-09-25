import { createStore } from 'vuex'

export default createStore({
  state: {
    loanApplication: null
  },
  mutations: {
    setLoanApplication(state, payload) {
      state.loanApplication = payload
    }
  },
  actions: {
    submitLoanApplication({ commit }, payload) {
      commit('setLoanApplication', payload)
    }
  },
  getters: {
    getLoanApplication: (state) => state.loanApplication
  }
})
