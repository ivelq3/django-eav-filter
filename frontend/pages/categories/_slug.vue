<template lang="pug">
div
  .row
    .col-12
      h1 Категория: {{ categoryName }}

  .row
    .col-2
      ProductFilter(:filterSet="filterSet", :selectedFilters="selectedFilters") 

    .col-10
      .row.row-cols-5
        .col.mb-4(v-for="product of products", :key="product.id")
          ProductListItem(:product="product")
</template>

<script>
import ProductFilter from "@/components/ProductFilter";
import ProductListItem from "@/components/ProductListItem";
export default {
  components: {
    ProductFilter,
    ProductListItem,
  },

  watchQuery: true,

  async asyncData({ $axios, route }) {
    const response = await $axios.$get(`/categories/${route.params.slug}`, {
      params: route.query,
    });

    return {
      products: response.products,
      filterSet: response.filterSet,
      categoryName: response.categoryName,
      selectedFilters: response.selectedFilters,
    };
  },
};
</script>