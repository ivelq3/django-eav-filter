<template lang="pug">
a-card.h-100(hoverable)
  n-link(:to="{ name: 'products-slug', params: { slug: product.slug } }")
    img.img-fluid(:src="mainImage")
  .product-name {{ product.name }}
  .product-price {{ product.price }} &#8381;

  a-row.pt-4
    a-col(span="21")
      a-button В корзину
    a-col(span="3")
      a-icon(type="heart", style="font-size: 20px; padding-top: 6px")
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
<style>
.product-name {
  height: 70px;
}

.product-price {
  padding-bottom: 15px;
}
</style>