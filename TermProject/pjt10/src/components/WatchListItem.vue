<template>
  <div>
    <p
      v-for="movie in movieList"
      :key="movie.id"
      :movie="movie"
    >
    {{ movie.title }}
    </p>
  </div>
</template>

<script>
export default {
  name: 'WatchListItem',
  computed: {
    movieList() {
      return this.$store.state.movieList
    },
  }
}
</script>

<style scoped>

</style>