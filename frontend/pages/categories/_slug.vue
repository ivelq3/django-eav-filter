<template lang="pug">
div
  a-row
    a-col.pt-4
      a-breadcrumb.pt-2(separator=">")
        a-breadcrumb-item Главная
        a-breadcrumb-item Каталог
        a-breadcrumb-item {{ categoryName }}
  a-row
    a-col
      h1 {{ categoryName }}
  a-row(gutter=20)
    a-col(span=4)
      ProductFilter(
        :filterSet="filterSet",
        :selectedFilters="selectedFilters",
        :minPrice="minPrice",
        :maxPrice="maxPrice",
        :selectedMinAndMaxPrice="selectedMinAndMaxPrice"
      ) 
    a-col(span=20)
      a-row(type="flex", justify="space-between")
        a-col
          a-select(
            v-model="selectedOrderBy",
            :options="orderByOptions",
            @change="handleOrderBy"
          ) 
        a-col
          a-pagination(
            v-model="currentPage",
            :defaultPageSize="perPage",
            :total="productsCount",
            @change="paginate"
          )

      a-row
        a-col
          .tags(v-for="tag of selectedFilters", :key="tag")
            a-tag(closable, color="blue") {{ tag }}

      a-row.product-list(type="flex", :gutter="[20, 20]")
        a-col.ant-col-55(v-for="product of products", :key="product.id")
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
  async asyncData({ $axios, route, error }) {
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
  },
  data() {
    return {
      // array<{value, label, [disabled, key, title]}>
      currentPage: this.$route.query.page || 1,
      orderByOptions: [
        { value: "price", label: "Сначала дешевые" },
        { value: "-price", label: "Сначала дорогие" },
      ],
    };
  },
  watch: {
    "$route.query": "loadData",
  },
  methods: {
    async loadData() {
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

<style>
.product-list {
  padding-top: 20px;
}

.tags {
  display: inline-block;
  padding-top: 20px;
}

.pt-2 {
  padding-top: 20px;
}
</style>