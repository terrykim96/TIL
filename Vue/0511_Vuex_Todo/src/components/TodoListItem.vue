<template>
  <div 
    class="todo-item"
  >
    <input 
      type="checkbox" 
      :value="todo.completed"
      @input="onCheck"
    >
    <p :class="{ 'todo-item--completed': todo.completed }">
      제목: {{ todo.content }}
    </p>
    <button @click="deleteTodo">삭제</button>
  </div>
</template>

<script>
export default {
  name: 'TodoListItem',
  props: {
    todo: {
      type: Object,
      required: true,
    },
  },
  methods: {
    deleteTodo() {
      this.$store.commit('deleteTodo', this.todo)
    },
    onCheck() {
      // update todo ... 
      this.$store.commit('updateTodo', this.todo)
    },
  },
}
</script>

<style scoped>
.todo-item {
  display: flex;
  align-items: center;
}

.todo-item--completed {
  text-decoration: line-through;
  color: gray;

}
</style>