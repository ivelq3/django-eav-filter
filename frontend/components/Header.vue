<template lang="pug">
div
  b-navbar(toggleable="lg", type="light", variant="light")
    b-navbar-brand.font-weight-bold(:to="{ name: 'index' }") Home
    b-navbar-toggle(target="nav-collapse")
    b-collapse#nav-collapse(is-nav)
      MainMenu.ml-4
      b-navbar-nav.ml-auto
        b-nav-form
          b-form-input.rounded-0(placeholder="Название товара")
          b-button(variant="primary", squared) Поиск

</template>
<script>
import MainMenu from "@/components/MainMenu";
export default {
  components: {
    MainMenu
  },
};
</script>

