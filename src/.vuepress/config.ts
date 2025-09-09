import { defineUserConfig } from "vuepress";

import theme from "./theme.js";

export default defineUserConfig({
  base: "/shioru/",

  locales: {
    "/": {
      lang: "ja-JP",
      title: "Blog Demo",
      description: "A blog demo for vuepress-theme-hope",
    },
    "/zh/": {
      lang: "zh-CN",
      title: "博客演示",
      description: "vuepress-theme-hope 的博客演示",
    },
  },

  theme,

  // Enable it with pwa
  // shouldPrefetch: false,
});
