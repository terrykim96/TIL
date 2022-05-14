import Vue from 'vue'
import VueRouter from 'vue-router'
import TheLunch from '@/views/TheLunch'
import LottoView from '@/views/LottoView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/lunch',
    name: 'lunch',
    component: TheLunch,
  },
  {
    path: 'lotto/:lottoNum',
    name: 'lotto',
    component: LottoView,
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
