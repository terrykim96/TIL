<template>
  <div id="app">
    <nav class="">
      <router-link to="/">Home</router-link> |
      <router-link to="/random">Random</router-link> |
      <router-link to="/watch-list">My Movie List</router-link>
    </nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
  
}
</script>

<style>

</style>
