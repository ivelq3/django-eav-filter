<template lang="pug">
div
  b-navbar(toggleable="lg", type="light", variant="light")
    b-navbar-brand(:to="{ name: 'index' }") Home
    b-navbar-toggle(target="nav-collapse")
    b-collapse#nav-collapse(is-nav)
      b-navbar-nav
        b-nav-item-dropdown(text="Категории")
          b-dropdown-item(
            v-for="category of categories",
            :key="category.id",
            :to="{ name: 'categories-slug', params: { slug: category.slug } }"
          ) {{ category.name }}

      b-navbar-nav.ml-auto
        b-nav-form
          b-form-input.rounded-0(placeholder="Название товара")
          b-button(variant="primary", squared) Поиск
</template>

<script>
export default {
  async fetch() {
    this.categories = await this.$axios.$get("/categories/");
  },

  data() {
    return {
      categories: {},
    };
  },
};
</script>

