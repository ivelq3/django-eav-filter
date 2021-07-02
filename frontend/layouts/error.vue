<template lang="pug">
div
  h1(v-if="error.statusCode === 404") Страница не найденна
  h1(v-else) Что то пошло не так
</template>

<script>
  export default {
    props: ['error'],
  }
</script>