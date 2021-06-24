<template lang="pug">
div
  b-button(
    :to="{ name: 'categories-slug', params: { slug: this.$route.params.slug } }",
    variant="primary",
    squared,
    block
  ) Сбросить

  div(v-for="(filterGroup, index) of filterSet.items", :key="index")
    .filter-group-name {{ filterGroup.name }}
    b-form-checkbox-group(
      :options="filterGroup.values",
      v-model="selectedFilters[filterGroup.slug]",
      text-field="name",
      value-field="slug",
      disabled-field="disabled",
      stacked,
      @change="updateQuery"
    )
</template>

<script>
export default {
  props: {
    filterSet: {
      type: Object,
      required: true,
    },
    selectedFilters: {
      type: Object,
      required: true,
    },
  },

  methods: {
    updateQuery() {
      this.$router.push({ query: this.selectedFilters });
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