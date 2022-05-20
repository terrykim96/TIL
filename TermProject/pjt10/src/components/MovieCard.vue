<template>
  <div>
    <p>{{ response.data.title }}</p>
  </div>
</template>

<script>
export default {
  name: 'MovieCard',
  props: {
    response: {
      type: Object,
      required: true,
    }
  }
}
</script>

<style scoped>

</style>