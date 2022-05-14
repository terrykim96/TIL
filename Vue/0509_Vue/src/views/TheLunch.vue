<template>
  <div>
    <h1>The Lunch</h1>
    <button @click="pickLunch">Pick Lunch</button>
    {{ pickedOne }}
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLunch',
  data: function() {
    return {
      menuList: ['햄버거', '초밥'],
      pickedOne: '',
    }
  },
  methods: {
    pickLunch() {
      this.pickedOne = _.sample(this.menuList)
    }
  }
}
</script>

<style>

</style>