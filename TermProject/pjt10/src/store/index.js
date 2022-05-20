import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movieList: [],
    responses: [],
    popularIds: []
  },
  getters: {
  },
  mutations: {
    addMovie(state, newTitle) {
      state.movieList.push(newTitle)
    },

    movieInfo(state, responses) {
      state.responses = responses
    },

    popularMovieId(state, popularIds) {
      state.popularIds = popularIds
    }

  },
  actions: {
    async popularMovies(context) {
      let popularIds = []

      const POPULAR_MOVIE_GET_URL = `https://api.themoviedb.org/3/movie/popular`
      const API_KEY = '96b45c1f564c7459d2fdf0183eb0070a'
  
      const popParams = {
        api_key: API_KEY,
        language: 'ko',
      }
  
      const popResponses = await axios.get(POPULAR_MOVIE_GET_URL, { params:popParams })
  
      for (const popResponse of popResponses.data.results) {
        popularIds.push(popResponse.id)
      }

      context.commit('popularMovieId', popularIds)
    },

    async movieNums(context, movieNums) {
      let responses = []
      console.log(movieNums)
      for (const movieNum of movieNums) {
        const MOVIE_GET_URL = `https://api.themoviedb.org/3/movie/${ movieNum }`
        const API_KEY = '96b45c1f564c7459d2fdf0183eb0070a'

        const params = {
          api_key: API_KEY,
          language: 'ko',
        }

        const response = await axios.get(MOVIE_GET_URL, { params })
        responses.push(response)
      }
      console.log(responses)
      context.commit('movieInfo', responses)
    }
  },
  modules: {
  }
})
