<template>
  <div>
    <h1>My Movie List</h1>
    
    <form @submit.prevent="onSubmit">
      <input
        v-model="movieTitle"
        type="text" 
        placeholder="시청한 영화 제목을 입력해주세요."
        autofocus
      >
      <button>Add</button>
    </form>

  </div>
</template>

<script>
export default {
  name: 'WatchListForm',
  data: function() {
    return {
      movieTitle: '',
    }
  },
  methods : {
    onSubmit() {
      const newTitle = {
        id: new Date().getMilliseconds(),
        title : this.movieTitle,
      }

      this.$store.commit('addMovie', newTitle)
      this.movieTitle = ''
    },
  },
}
</script>

<style scoped>

</style>