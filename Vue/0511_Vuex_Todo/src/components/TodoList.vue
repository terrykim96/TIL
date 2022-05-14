<template>
  <div>
    <TodoListItem 
      v-for="todo in todoList" 
      :key="todo.id" 
      :todo="todo"
    />
  </div>
</template>

<script>
import TodoListItem from '@/components/TodoListItem'

export default {
  name: 'TodoList',
  components: {
    TodoListItem,
  },
  computed: {
    todoList() {
      return this.$store.state.todoList
    },
  }
}
</script>

<style scoped>
</style>