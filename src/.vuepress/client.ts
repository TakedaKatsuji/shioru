import { defineClientConfig } from 'vuepress/client'
import AffiliateBook from './components/AffiliateBook.vue'

export default defineClientConfig({
  enhance({ app }) {
    app.component('AffiliateBook', AffiliateBook)
  },
})
