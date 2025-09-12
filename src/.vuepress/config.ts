import { defineUserConfig } from "vuepress";

import theme from "./theme.js";

export default defineUserConfig({
  base: "/shioru/",

  locales: {
    "/": {
      lang: "ja-JP",
      title: "栞る数理統計",
      description: "A blog demo for vuepress-theme-hope",
    },
  },

  theme,
  // head: [
  //   ["link", { rel: "icon", href: "/logo.png" }],  // faviconの指定
  // ],
  // Enable it with pwa
  // shouldPrefetch: false,
});
