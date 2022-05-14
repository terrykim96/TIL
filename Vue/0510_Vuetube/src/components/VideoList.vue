<template>
  <div>
    <VideoListItem 
      v-for="video in videos"
      :key="video.id.videoId"
      :video="video"
      @on-click-video="(video) => $emit('on-click-video', video)"
    />
  </div>
</template>

<script>
import VideoListItem from '@/components/VideoListItem.vue'


export default {
  name: 'VideoList',
  components : {
    VideoListItem,
  },
  props: {
    videos: {
      type: Array,
      required: false,
    },
  },

  data: function() {
    return {}
  },
}
</script>

<style scoped>

</style>