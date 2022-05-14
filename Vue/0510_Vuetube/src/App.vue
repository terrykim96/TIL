<template>
  <div>
    <h1>Vuetube</h1>
    <TheSearchBar @on-search="onSearch" />

    <VideoDetail v-if="Object.keys(video).length"
      :video="video"
    />

    <VideoList 
      :videos="videos"
      @on-click-video="onClickVideo"
    />
  </div>
</template>

<script>
import TheSearchBar from '@/components/TheSearchBar.vue'
import VideoList from '@/components/VideoList.vue'
import VideoDetail from '@/components/VideoDetail.vue'


import axios from 'axios'


export default {
  name: 'App',
  components: {
    TheSearchBar,
    VideoList,
    VideoDetail,
  },
  data: function() {
    return {
      videos: [],
      video: {}, // VideoListItem에서 클릭한 비디오를 저장할 데이터
    }
  },
  methods: {
    async onSearch(keyword) {

      const YOUTUBE_SEARCH_BASE_URL = 'https://www.googleapis.com/youtube/v3/search'
      const YOUTUBE_API_KEY = 'AIzaSyDLggjbmWBJTvSmXQostJVAPvd_RcOBr0g'

      const params = {
        key : YOUTUBE_API_KEY,
        part : 'snippet',
        q: keyword,
      }

      const response = await axios.get(YOUTUBE_SEARCH_BASE_URL, {params})
      // GET http://..../search?key=...&part=snippet&q=...
      const videos = response.data.items
      this.videos = videos
      console.log(this.videos)
    },
    onClickVideo(video) {
      this.video = video
    }
  },
}
</script>

<style>

</style>