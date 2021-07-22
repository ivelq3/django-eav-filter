export default {
  head: {
    title: 'frontend',
    htmlAttrs: {
      lang: 'en'
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: 'description' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },

  css: [
    '@/assets/css/main.css',
    'ant-design-vue/dist/antd.css'
  ],

  plugins: [
    '@/plugins/antd-ui',
    '@/plugins/axios.js',
  ],

  components: true,

  buildModules: [
  ],

  modules: [
    '@nuxtjs/axios',
  ],

  axios: {
    baseURL: 'http://localhost:8000/api',
    // baseURL: 'http://backend:8000/api',
    // browserBaseURL: '/api',
  },

  build: {
  },

  loading: true,
}