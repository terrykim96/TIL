<template>
  <div>
    <h1 class="text-center">Home</h1>
    <MovieCard
      v-for="response in responses"
      :key="response.data.id"
      :response="response"
    />
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard.vue'
import _ from 'lodash'

export default {
  name: 'HomeView',
  components: {
    MovieCard
  },
  computed: {
    responses() {
      return this.$store.state.responses
    },
  },
  methods: {
    getMovieNums: async function() {
      await this.$store.dispatch('popularMovies')

      const selectedMovieNums = _.sampleSize(
        this.$store.state.popularIds,
        10
      )
      await this.$store.dispatch('movieNums', selectedMovieNums)
    },

  },
  created() {
    this.getMovieNums()
  },

}
</script>

<style scoped>

</style>