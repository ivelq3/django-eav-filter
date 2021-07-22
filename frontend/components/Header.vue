<template lang="pug">
.main-menu-top
  a-row
    a-col(span="2")
      n-link(to="/")
        .logo Home
    a-col(span="3")
      //- a-button Каталог
        //- a-icon(type="menu")
      a-dropdown(trigger="click")
        a-menu(slot="overlay")
          a-menu-item(
            key="1",
            v-for="category of categories",
            :key="category.id"
          )
            n-link(
              :to="{ name: 'categories-slug', params: { slug: category.slug } }"
            ) {{ category.name }}
        a-button Каталог
          a-icon(type="down")

    a-col(span="14")
      a-input-search(placeholder="Поиск")
    a-col(span="2")

    a-col(span="1")
      a-icon(type="user", style="font-size: 24px")
    a-col(span="1")
      a-badge(count="5")
        a-icon(type="heart", style="font-size: 24px")
    a-col(span="1")
      a-badge(count="2")
        a-icon(type="shopping-cart", style="font-size: 26px")

  a-row.bottom
    a-col(span="2") Оплата
    a-col(span="2") Оплата
    a-col(span="2") Оплата
    a-col(span="2") Оплата
    a-col(span="2") Оплата
    a-col(span="2") Оплата
    a-col(span="2") Оплата
    a-col(span="2") Оплата
    a-col(span="2") Оплата
    a-col(span="2") Оплата
    a-col(span="2") Оплата
    a-col(span="2") Оплата
</template>

<script>
export default {
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



<style>
.bottom {
  box-shadow: 0 2px 0px 0 rgb(0 0 0 / 6%);
  padding-top: 25px;
  padding-bottom: 25px;
}
.logo {
  font-size: 20px;
  font-weight: bold;
}

.main-menu-top {
  padding-top: 30px;
}

.gray {
  background-color: gray;
}

.wr {
  width: 1200px;
  height: 600px;
}

.wrap {
  height: 100%;
  background-color: red;
}
</style>