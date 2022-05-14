<template>
  <div>
    <form @submit.prevent="onSubmit">
      <input
        v-model="todoContent"
        type="text" 
        placeholder="할 일을 입력해주시오."
        autofocus
      >
      <button>추가하기</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'TodoForm',
  data: function() {
    return {
      todoContent: '',
    }
  },
  methods: {
    onSubmit() {
      const newTodo = {
        id: new Date().getMilliseconds(),
        content: this.todoContent, // 사용자 입력값
        completed: false,
      }

      this.$store.commit('addTodo', newTodo) 
      this.todoContent = ''
    },
  },
}
</script>

<style scoped>
</style>