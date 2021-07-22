<template lang="pug">
.product-filter
  n-link(:to="{ name: 'categories-slug', params: { slug: this.$route.params.slug } }")
    a-button(block) Сбросить

  .filter-group-name.price-range Цена
  vue-slider(
    :value="selectedMinAndMaxPrice",
    :dotSize="16",
    :contained="true",
    :tooltip="'always'",
    :process-style="{ backgroundColor: '#1890ff' }",
    :tooltip-style="{ backgroundColor: '#1890ff', borderColor: '#1890ff' }",
    :lazy="true",
    :min="minPrice",
    :max="maxPrice",
    @change="changePriceHandler"
  )

  div(v-for="(filterGroup, index) of filterSet.items", :key="index")
    .filter-group-name {{ filterGroup.name }}
    a-checkbox-group(
      v-model="selectedFilters[filterGroup.slug]",
      :options="filterGroup.values",
      @change="changeFilterHandler"
    )
</template>
<script>
import VueSlider from "vue-slider-component/dist-css/vue-slider-component.umd.min";
import "vue-slider-component/dist-css/vue-slider-component.css";
import "vue-slider-component/theme/default.css";
export default {
  components: {
    "vue-slider": VueSlider,
  },
  props: {
    filterSet: {
      type: Object,
      required: true,
    },
    selectedFilters: {
      type: Object,
      required: true,
    },
    minPrice: { type: Number, required: true },
    maxPrice: { type: Number, required: true },
    selectedMinAndMaxPrice: { type: Array, required: true },
  },
  methods: {
    changePriceHandler(event) {
      const min = event[0];
      const max = event[1];
      const query = { ...this.$route.query, min_price: min, max_price: max };
      this.$router.push({ query });
    },
    changeFilterHandler() {
      const query = { ...this.$route.query };
      delete query.page;
      this.$router.push({ query: { ...query, ...this.selectedFilters } });
    },
  },
};
</script>

<style>
.filter-group-name {
  font-weight: bold;
  color: #282828;
  font-size: 14px;
  padding: 10px 0px;
}

.ant-checkbox-group-item {
  display: block;
  margin-right: 0;
}

.price-range {
  margin-bottom: 35px;
}
</style>