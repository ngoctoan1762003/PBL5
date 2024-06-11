import path from 'path';
import fs from 'fs';
const pkg = require('./package');

export default {
  ssr: false, // Set to false for SPA mode

  // Global page headers: https://go.nuxtjs.dev/config-head
  // Uncomment and configure server for HTTPS if needed
  // server: {
  //   https: {
  //     key: fs.readFileSync(path.resolve(__dirname, 'server.key')),
  //     cert: fs.readFileSync(path.resolve(__dirname, 'server.crt'))
  //   }
  // },
  devServer: {
    proxy: {
      '/ws': {
        target: 'ws://localhost:5000',
        ws: true,
        changeOrigin: true
      }
    }
  },

  head: {
    title: 'Forum',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
    script: [
      { src: 'https://apis.google.com/js/platform.js', async: true, defer: true }
    ]
  },

  css: [
    '~/assets/css/main.css',
    '~/assets/css/quill.css',
    'quill/dist/quill.snow.css',
    // 'vue3-datepicker/dist/vue3-datepicker.css' // Uncomment if needed
  ],

  loading: { color: '#fff' },

  middleware: [
    'cors'
  ],

  styleResources: {
    scss: [
      '~/assets/scss/variables.scss'
    ]
  },

  plugins: [
    { src: '~plugins/vue-quill-editor.js', ssr: false },
    '~/plugins/vue-notification.js',
    '~/plugins/axios-interceptor.js',
    '~/plugins/Behavior/scrollToTop.js',
    // { src: '~/plugins/google-auth.js', ssr: false },
    // { src: '~/plugins/google-signin.js', ssr: false },
    // '~/plugins/socket.js',
    // '~/plugins/server.js'
  ],

  components: true,

  build: {
    transpile: ['chartist'],
    extend(config, { isDev, isClient }) {
      if (isClient) {
        config.module.rules.push({
          test: /\.mjs$/,
          include: /node_modules/,
          type: 'javascript/auto'
        });
      }
      config.node = {
        fs: 'empty'
      }
    }
  },

  buildModules: [
    '@nuxtjs/eslint-module',
    '@nuxtjs/tailwindcss',
    // 'nuxt-vite' // Uncomment if needed
  ],

  modules: [
    '@nuxtjs/axios',
    '@nuxtjs/pwa',
    '@nuxtjs/auth-next',
    'nuxt-socket-io',
  ],

  axios: {
    baseURL: 'https://e518-42-116-158-46.ngrok-free.app',
  },

  router: {
    middleware: ['middleware-auth', 'middleware-admin']
  },

  pwa: {
    manifest: {
      lang: 'en'
    }
  },

  io: {
    // Socket.io module configuration
    sockets: [{
      name: 'main',
      url: 'http://localhost:5000',
      default: true,
      vuex: {
        actions: [],
        mutations: []
      }
    }]
  }
}
