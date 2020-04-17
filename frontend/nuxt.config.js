
export default {
  mode: 'universal',
  /*
  ** Headers of the page
  */
  head: {
    title: process.env.npm_package_name || '',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: process.env.npm_package_description || '' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      {
        rel: "stylesheet",
        href: "https://fonts.googleapis.com/css?family=Open+Sans"
      }
    ]
  },
  /*
  ** Customize the progress-bar color
  */
 loading: { color: "#fa923f", height: "4px", duration: 5000 },
 loadingIndicator: {
   name: "circle",
   color: "#fa923f"
 },
  /*
  ** Global CSS
  */
 css: ["~assets/styles/main.css"],
  /*
  ** Plugins to load before mounting the App
  */
  plugins: [
    "~/plugins/core-components.js"

  ],
  /*
  ** Nuxt.js dev-modules
  */
  buildModules: [
  ],
  /*
  ** Nuxt.js modules
  */
  modules: [
    // Doc: https://github.com/nuxt-community/modules/tree/master/packages/bulma
    '@nuxtjs/bulma',
    // Doc: https://axios.nuxtjs.org/usage
    '@nuxtjs/axios',
    '@nuxtjs/pwa',
    // Doc: https://github.com/nuxt-community/dotenv-module
    '@nuxtjs/dotenv',
  ],
  /*
  ** Axios module configuration
  ** See https://axios.nuxtjs.org/options
  */
  axios: {
    proxy: true
  },

  proxy: {
    '/api/':{
      target: 'http://localhost:8000',
      pathRewrite: { '^/api/': '' }
    }
  },
  /*
  ** Build configuration
  */
  build: {
    postcss: {
      preset: {
        features: {
          customProperties: false
        }
      }
    },
    /*
    ** You can extend webpack config here
    */
    extend (config, ctx) {
    }
  },
  env:{
    validatorURL: process.env.VALIDATOR_URL || "http://192.168.0.14:4004"
  },
  transition:{
    name: "fade",
    mode: "out-in"
  }
}
