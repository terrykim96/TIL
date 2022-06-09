<template>
  <div>
    <h1>Signup</h1>
    <form @submit.prevent="onSubmit">
      <input type="text" name="username" v-model="signupInfo.username">
      <input type="text" name="password1" v-model="signupInfo.password1">
      <input type="text" name="password2" v-model="signupInfo.password2">
      <input type="text" name="email" v-model="signupInfo.email">
      <button>회원가입</button>
    </form>
  </div>
</template>

<script>
import { signup } from '@/api/index.js'

export default {
  name: 'SignupView',
  data() {
    return {
      signupInfo: {
        username: '',
        password1: '',
        password2: '',
        email: '',
      },
    }
  },
  methods: {
    async onSubmit() {
      // 1. API 서버로 회원가입 요청
      
      try {
        await signup(this.signupInfo)
        // 2. 성공 시, 로그인 페이지로 이동
        this.$router.push('/login')
      } catch(err) {
        // 3. 실패 시, alert
        alert(`
          문제가 발생하였습니다. ${err}
          관리자에게 문의해주세요.

          - 원재호: 010-1234-2134.
        `)
      }
    },
  },
}
</script>

<style>

</style>