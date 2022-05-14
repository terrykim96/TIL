<template>
  <div>
    <h1>Todo App with Vuex</h1>
    <TodoForm/>
    <TodoList/>    
  </div>
</template>

<script>
import TodoForm from '@/components/TodoForm'
import TodoList from '@/components/TodoList'

export default {
  name: 'App',
  components: {
    TodoForm,
    TodoList,
  },
}
</script>

<style scoped>
</style>