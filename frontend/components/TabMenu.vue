<template lang="pug">
div
  b-nav-item-dropdown#my-nav-dropdown(text="Каталог")
    b-tabs(vertical, no-nav-style, no-fade, lazy)
      div(v-for="rootCategory of categories", :key="rootCategory.id")
        b-tab.ml-2(:title="rootCategory.name")
          ul.list-unstyled(
            v-for="subCategory of rootCategory.children",
            :key="subCategory.id"
          )
            .sub-category-name {{ subCategory.name }}
            li.my-2(
              v-for="subSubCategory of subCategory.children",
              :key="subSubCategory.id"
            )
              NuxtLink(
                :to="{ name: 'categories-slug', params: { slug: subSubCategory.slug } }"
              ) {{ subSubCategory.name }}
</template>


<script>
import { BIconCaretRightFill } from "bootstrap-vue";
export default {
  components: {
    BIconCaretRightFill,
  },
  async fetch() {
    const response = await this.$axios.$get("/categories/");
    const categories = JSON.parse(response);
    this.categories = categories;
  },
  data() {
    return {
      categories: {},
    };
  },
};
</script>


