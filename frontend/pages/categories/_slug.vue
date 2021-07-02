<template lang="pug">
div
  .row
    .col-12
      h1 Категория: {{ categoryName }}
  .row
    .col-2
      ProductFilter(
        :filterSet="filterSet",
        :selectedFilters="selectedFilters",
        :minPrice="minPrice",
        :maxPrice="maxPrice",
        :selectedMinAndMaxPrice="selectedMinAndMaxPrice"
      ) 
    .col-10
      .row
        .col-12.d-flex.mb-3
          b-form-select.w-25(
            v-model="selectedOrderBy",
            :options="orderByOptions",
            value-field="item",
            text-field="name",
            @change="handleOrderBy"
          )
          .overflow-auto.ml-auto
            b-pagination(
              v-model="currentPage",
              :total-rows="productsCount",
              :per-page="perPage",
              @change="paginate"
            )

      .row.row-cols-5(v-if="products.length > 0")
        .col.mb-4(v-for="product of products", :key="product.id")
          ProductListItem(:product="product")
      .row(v-else)
        h1 Товаров в таком ценовом диапазоне не найденно
</template>
<script>
import ProductFilter from "@/components/ProductFilter";
import ProductListItem from "@/components/ProductListItem";
export default {
  components: {
    ProductFilter,
    ProductListItem,
  },
  async asyncData({ $axios, route, error }) {
    try {
      const response = await $axios.$get(`/categories/${route.params.slug}`, {
        params: route.query,
      });
      return {
        perPage: response.perPage,
        products: response.products,
        minPrice: response.minPrice,
        maxPrice: response.maxPrice,
        filterSet: response.filterSet,
        categoryName: response.categoryName,
        productsCount: response.productsCount,
        selectedFilters: response.selectedFilters,
        selectedOrderBy: response.selectedOrderBy,
        selectedMinAndMaxPrice: response.selectedMinAndMaxPrice,
      };
    } catch {
      error({ statusCode: 404 });
    }
  },
  data() {
    return {
      currentPage: this.$route.query.page || 1,
      orderByOptions: [
        { item: "price", name: "Сначала дешевые" },
        { item: "-price", name: "Сначала дорогие" },
      ],
    };
  },
  watch: {
    "$route.query": "loadData",
  },
  methods: {
    async loadData() {
      try {
        const response = await this.$axios.$get(
          `/categories/${this.$route.params.slug}`,
          {
            params: this.$route.query,
          }
        );
        this.perPage = response.perPage;
        this.products = response.products;
        this.minPrice = response.minPrice;
        this.maxPrice = response.maxPrice;
        this.filterSet = response.filterSet;
        this.categoryName = response.categoryName;
        this.productsCount = response.productsCount;
        this.selectedFilters = response.selectedFilters;
        this.selectedOrderBy = response.selectedOrderBy;
        this.selectedMinAndMaxPrice = response.selectedMinAndMaxPrice;
      } catch {
        return this.$nuxt.error({ statusCode: 404 });
      }
    },
    paginate(currentPage) {
      const query = { ...this.$route.query, page: currentPage };
      this.$router.push({ query });
    },
    handleOrderBy() {
      const query = { ...this.$route.query, order_by: this.selectedOrderBy };
      this.$router.push({ query });
    },
  },
};
</script>