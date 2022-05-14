<template>
  <div>
    <div class="max-w-2xl mx-auto my-10 relative z-100">
      <SearchForm class="mb-5" />
      <AlbumList />
      <DarkModeButton />
    </div>
  </div>
</template>

<script>
import SearchForm from '@/components/SearchForm'
import AlbumList from '@/components/AlbumList'
import DarkModeButton from '@/components/DarkModeButton'

export default {
  name: 'App',
  components: {
    SearchForm,
    AlbumList,
    DarkModeButton,
  },
}
</script>

<style>

</style>