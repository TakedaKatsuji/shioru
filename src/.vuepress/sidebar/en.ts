import { sidebar } from "vuepress-theme-hope";

export const enSidebar = sidebar({
  "/": [
    "",
    {
      text: "Articles",
      icon: "book",
      prefix: "posts/",
      children: [
        {
          text: "統計検定1級 統計数理",
          icon: "meteor-icons:folder",
          prefix: "grade1_1/",
          collapsible: true,
          children: "structure"
        },
        {
          text: "確率分布",
          icon: "meteor-icons:folder",
          prefix: "probability_distribution/",
          collapsible: true,
          children: "structure"
        },
        {
          text: "多次元分布",
          icon: "meteor-icons:folder",
          prefix: "multivariate_distribution/",
          collapsible: true,
          children: "structure"
        },
      ],
    },
    "intro"
  ],
});
