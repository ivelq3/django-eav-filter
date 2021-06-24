<template lang="pug">
.card.h-100
  b-link(:to="{ name: 'products-slug', params: { slug: product.slug } }")
    img.img-fluid(:src="mainImage")
  .card-body
    .product-price {{ product.price }} &#8381;
    .product-name {{ product.name }}
  .card-footer
    b-button(variant="primary", squared, block) В корзину
</template>

<script>
const noImage = require("@/assets/noImage.png");
export default {
  props: {
    product: {
      required: true,
      type: Object,
    },
  },

  computed: {
    mainImage() {
      return this.product.main_image || noImage;
    },
  },
};
</script>

<style scoped>
.card-footer,
.card-header {
  background-color: #fff;
  border: none;
}

.product-price {
  font-size: 18px;
  font-weight: bold;
}

.card {
  box-shadow: 0 10px 20px rgb(0 0 0 / 19%), 0 6px 6px rgb(0 0 0 / 23%);
}
</style>