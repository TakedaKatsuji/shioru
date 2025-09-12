import { defineUserConfig } from "vuepress";

import theme from "./theme.js";

export default defineUserConfig({
  base: "/",

  locales: {
    "/": {
      lang: "ja-JP",
      title: "栞る数理統計",
      description: "A blog demo for vuepress-theme-hope",
    },
  },

  head: [["link", { rel: "icon", href: "/favicon.png?v=1" }]],

  theme,
  // Enable it with pwa
  // shouldPrefetch: false,
});
