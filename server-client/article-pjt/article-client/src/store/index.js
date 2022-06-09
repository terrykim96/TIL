import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    authToken: JSON.parse(localStorage.getItem('authToken')) || '',
    // userInfo : null,
  },
  getters: {
    isLoggedIn(state) {
      return state.authToken ? true : false
    }
  },
  mutations: {
    setAuthToken(state, authToken) {
      state.authToken = authToken
      localStorage.setItem('authToken', JSON.stringify(authToken))
    },
  },
  actions: {
  },
  modules: {
  }
})
