<template>
  <div>
    <h1>재생목록</h1> 

    <WatchListForm/>
    <WatchListItem/>
  </div>
</template>

<script>
import WatchListForm from '@/components/WatchListForm.vue'
import WatchListItem from '@/components/WatchListItem.vue'


export default {
  name: 'WatchListView',
  components :{
    WatchListForm,
    WatchListItem,
  }
}
</script>

<style scoped>

</style>