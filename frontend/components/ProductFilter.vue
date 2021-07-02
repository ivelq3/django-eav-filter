<template lang="pug">
div
  b-button(
    :to="{ name: 'categories-slug', params: { slug: this.$route.params.slug } }",
    variant="primary",
    squared,
    block
  ) Сбросить
  .filter-group-name.pb-5 Цена
  vue-slider(
    :value="selectedMinAndMaxPrice",
    :dotSize="19",
    :contained="true",
    :tooltip="'always'",
    :process-style="{ backgroundColor: '#007bff' }",
    :tooltip-style="{ backgroundColor: '#007bff', borderColor: '#007bff' }",
    :lazy="true",
    :min="minPrice",
    :max="maxPrice",
    @change="changePriceHandler"
  )
  div(v-for="(filterGroup, index) of filterSet.items", :key="index")
    .filter-group-name {{ filterGroup.name }}
    b-form-checkbox-group(
      :options="filterGroup.values",
      v-model="selectedFilters[filterGroup.slug]",
      text-field="name",
      value-field="slug",
      disabled-field="disabled",
      stacked,
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

<style scoped>
.filter-group-name {
  font-size: 16px;
  padding: 10px 0px;
  font-weight: bolder;
}
</style>