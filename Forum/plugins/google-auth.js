import { defineNuxtConfig } from 'nuxt/config'

export default defineNuxtConfig({
    modules: [
        'nuxt-vue3-google-signin'
    ],
    googleSignIn: {
        clientId: '924458972373-8fjviiu7k2dqkn3uo6ob1ab3seom2fob.apps.googleusercontent.com'
    }
 })