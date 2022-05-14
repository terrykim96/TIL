import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    // == data
    // - 컴포넌트에서 활용할 때: this.$store.state 
    todoList: [],
  },
  getters: {
    // == computed
    // - 컴포넌트에서 활용할 때: this.$store.getters
  },
  mutations: {
    // == methods
    // - 첫번째 인자: state
    // - 두번째 인자: 컴포넌트에서 넘기는 데이터
    // - 컴포넌트에서 활용할 때: this.$store.commit('뮤테이션명', 데이터)
    addTodo(state, newTodo) {
      state.todoList.push(newTodo)
    },
    deleteTodo(state, targetTodo) {
      state.todoList = state.todoList.filter(todo => {
        return todo.id !== targetTodo.id
      })
    },
    updateTodo(state, targetTodo) {
      state.todoList = state.todoList.map(todo => {
        if (todo.id === targetTodo.id) {
          todo.completed = !todo.completed
        }
        return todo
      })
    },
  },
  actions: {
    // == methods (비동기 처리 담당)
    // 외부 네트워크 API 호출 등에 사용
    // - 컴포넌트에서 활용할 때: this.$store.dispatch('액션명', 데이터)
  },
})
