<template lang="pug">
.wrapper
  a-row
    a-col
      Header
  a-row
    a-col
      Nuxt
</template>
<script>
import Header from "@/components/Header";
export default {
  components: {
    Header,
  },
};
</script>

<style>
.wrapper {
  max-width: 1440px;
  margin: 0 auto;
}
</style>