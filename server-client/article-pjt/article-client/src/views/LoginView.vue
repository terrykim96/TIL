<template>
  <div>
    <h1>Login</h1>

    <form @submit.prevent="onSubmit">
      <input type="text" name="username" v-model="loginInfo.username">
      <input type="text" name="password" v-model="loginInfo.password">
      <input type="text" name="email" v-model="loginInfo.email">
      <button>로그인</button>
    </form>
  </div>
</template>

<script>
import { login } from '@/api/index.js'

export default {
  name: 'LoginView',
  data() {
    return {
      loginInfo : {
        username: '',
        password: '',
        email: '',
      },
    }
  },
  method: {
    async onSubmut () {
      // 1. API 서버로 로그인 요청
      const res = await login(this.loginInfo)
      console.log(res)

      // 2. 요청 성공 => 토큰을 state/localStorage에 저장
      const token = res.data.key
      this.$store.commit('setAuthToken', token)

      // 3. 실패 => 에러 처리

    }
  }

}
</script>

<style>

</style>