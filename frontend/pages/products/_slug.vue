<template lang="pug">
div
  .row
    .col-12
      h1 {{ product.name }}

  .row
    .col-4
      img.img-fluid(:src="mainImage")

    .col-8
      div(v-for="eav of product.eavs", :key="eav.id")
        span {{ eav.attribute.name }}:
        span(v-for="value of eav.values", :key="value.id")
          span {{ value.name }}
</template>

<script>
const noImage = require("@/assets/noImage.png");
export default {
  async asyncData({ $axios, route }) {
    const product = await $axios.$get(`/products/${route.params.slug}`);
    return { product };
  },

  computed: {
    mainImage() {
      return this.product.main_image || noImage;
    },
  },
};
</script>