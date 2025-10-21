import { defineUserConfig } from "vuepress";
import { viteBundler } from "@vuepress/bundler-vite";
import { markdownContainerPlugin } from "@vuepress/plugin-markdown-container";
import { googleAnalyticsPlugin } from "@vuepress/plugin-google-analytics";

import theme from "./theme.js";

const boxes = [
  ["def", "定義"],
  ["expl", "解説"],
  ["hint", "ヒント"],
  ["plan", "方針"],
  ["note", "注意"],
  ["ex", "例"],
  ["sum", "まとめ"],
  ["calc", "計算"],
  ["ans", "解答"],
  ["proof", "証明"],
  ["term", "用語"],
  ["ref", "参考"],
] as const;

export default defineUserConfig({
  base: "/",

  locales: {
    "/": {
      lang: "ja-JP",
      title: "栞る数理統計",
      description: "A blog demo for vuepress-theme-hope",
    },
  },

  plugins: [
    ...boxes.map(([type, label]) =>
      markdownContainerPlugin({ type, locales: { "/": { defaultInfo: label } } })
    ),
    googleAnalyticsPlugin({ id: "G-8NJW3R4RJD" }),
  ],

  head: [
    ["link", { rel: "icon", href: "/favicon.png?v=1" }],

    // Fonts: preconnect + preload to avoid first-visit FOUC on home
    ["link", { rel: "preconnect", href: "https://fonts.googleapis.com" }],
    ["link", { rel: "preconnect", href: "https://fonts.gstatic.com", crossorigin: "" }],
    [
      "link",
      {
        rel: "preload",
        as: "style",
        href:
          "https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;600;700&display=swap",
        onload: "this.onload=null;this.rel='stylesheet'",
      },
    ],
    [
      "noscript",
      {},
      `<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;600;700&display=swap">`,
    ],

    // AdSense
    [
      "script",
      {
        async: "",
        src: "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7160116077446563",
        crossorigin: "anonymous",
      },
    ],

    // Optional: lock initial color scheme early to reduce FOUC
    [
      "script",
      {},
      `(function(){var m=localStorage.getItem('vuepress-color-scheme')||'light';document.documentElement.dataset.theme=m;})();`,
    ],
  ],

  // Bundle CSS as a single file to prevent home-only first-load style gaps
  bundler: viteBundler({
    viteOptions: {
      build: { cssCodeSplit: false },
    },
  }),

  theme,
});
