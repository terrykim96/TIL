<template>
  <form class="w-3/4 mx-auto" @submit.prevent>
    <input
      type="text"
      class="border border-slate-500 rounded-sm w-full px-2 py-2"
      placeholder="가수 및 앨범명을 입력해주세요"
      @input="onSearchDebounce"
    >
  </form>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'SearchForm',
  methods: {
    onSearchDebounce: _.debounce(function(event) {
      const keyword = event.target.value
      this.$store.dispatch('fetchAlbums', keyword)
    }, 500),
    // onSearch(event) {
    //   const keyword = event.target.value
    //   this.$store.dispatch('fetchAlbums', keyword)
    // },
  },
}
</script>

<style scoped>

</style>