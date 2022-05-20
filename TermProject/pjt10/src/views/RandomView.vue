<template>
  <div>
    <p
      v-for="response in responses"
      :key="response.data.id"
      :response="response"
    >
    {{ response.data.title }}
    </p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'RandomView',
  computed: {
    responses() {
      return this.$store.state.responses
    }
  },
  methods: {
    getRandomMovie: async function() {
      await this.$store.dispatch('popularMovies')

      const selectedMovieNums = _.sampleSize(
        this.$store.state.popularIds,
        1
      )
      await this.$store.dispatch('movieNums', selectedMovieNums)
    },
  },
  created() {
    this.getRandomMovie()
  },
}
</script>

<style scoped>

</style>