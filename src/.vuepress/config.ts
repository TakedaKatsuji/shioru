import { defineUserConfig } from "vuepress";
import { markdownContainerPlugin } from '@vuepress/plugin-markdown-container'


import theme from "./theme.js";

const boxes = [
  ["def","定義"],
  ["expl","解説"],
  ["hint","ヒント"],
  ["plan","方針"],
  ["note","注意"],
  ["ex","例"],
  ["sum","まとめ"],
  ["calc","計算"],
  ["ans","解答"],
  ["proof","証明"],
  ["term","用語"],
  ["ref","参考"],
] as const

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

  plugins: boxes.map(([type, label]) =>
    markdownContainerPlugin({ type, locales: { "/": { defaultInfo: label } } })
  ),
  theme,
});
