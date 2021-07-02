export const state = () => ({
  products: [],
  filterSet: {},
})

export const mutations = {
  setProducts(state, products) {
    state.products = products
  },
  setFilterSet(state, filterSet) {
    state.filterSet = filterSet
  },
}

export const actions = {
  async loadCategory({ commit }, payload) {
    const response = await this.$axios.$get(`/categories/${payload.slug}`, { params: payload.query })
    commit('setProducts', response.products)
    commit('setFilterSet', response.filterSet)
  },
}

