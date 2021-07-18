<template lang="pug">
div
  b-button(v-b-toggle.mainMenuSidebar, variant="primary") Каталог
  b-sidebar#mainMenuSidebar(title="Категории", shadow)
    b-nav(vertical)
      div(v-for="rootCategory of categories", :key="rootCategory.id")
        b-nav-item(v-b-toggle="'root-' + rootCategory.id")
          span {{ rootCategory.name }}
          BIconCaretRightFill.float-right(scale="0.6", variant="dark")
        b-collapse(:id="'root-' + rootCategory.id")
          div(
            v-for="subCategory of rootCategory.children",
            :key="subCategory.id"
          )
            b-nav-item(v-b-toggle="'sub-' + subCategory.id")
              span(
                :to="{ name: 'categories-slug', params: { slug: subCategory.slug } }"
              ) {{ subCategory.name }}
              BIconCaretRightFill.float-right(
                v-if="subCategory.children",
                scale="0.6",
                variant="dark"
              )
            b-collapse(:id="'sub-' + subCategory.id")
              div(
                v-for="subSubCategory of subCategory.children",
                :key="subSubCategory.id"
              )
                b-nav-item
                  b-link(
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
    this.categories = JSON.parse(response);
  },
  data() {
    return {
      categories: {},
    };
  },
};
</script>
