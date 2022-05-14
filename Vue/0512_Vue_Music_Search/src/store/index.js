import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    albums: [],
    isFetching: false,
  },
  getters: {
  },
  mutations: {
    updateAlbums(state, albums) {
      state.albums = albums
    },
    toggleFetchingStatus(state) {
      state.isFetching = !state.isFetching
    },
  },
  actions: {
    async fetchAlbums(context, keyword) {
      if (!keyword) {
        return context.commit('updateAlbums', [])
      }

      const LAST_FM_ALBUM_SEARCH_URL = 'https://ws.audioscrobbler.com/2.0/'
      const API_KEY = '9ab32563c64cf303b42cfbe59cdb63f8'
      const params = {
        api_key: API_KEY,
        album: keyword,
        method: 'album.search',
        format: 'json',
      }

      context.commit('toggleFetchingStatus')
      const response = await axios.get(LAST_FM_ALBUM_SEARCH_URL, { params })
      context.commit('toggleFetchingStatus')
      
      const albums = response.data.results.albummatches.album
      console.log(albums)
      context.commit('updateAlbums', albums)
    },
  },
})
