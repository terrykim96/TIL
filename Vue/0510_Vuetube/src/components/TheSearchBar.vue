<template>
  <form @submit.prevent="onSearch">
    <input type="text" v-model="keyword">
  </form>
</template>

<script>
export default {
  name: 'TheSearchBar',
  data: function() {
    return {
      keyword: '',
    }
  },
  methods: {
    onSearch() {
      this.$emit('on-search', this.keyword)
      this.keyword = '' // 입력창 초기화
    },
  },
}
</script>

<style>

</style>