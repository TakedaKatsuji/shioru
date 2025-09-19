import { navbar } from "vuepress-theme-hope";
import type { NavbarOptions } from "vuepress-theme-hope";

export const enNavbar: NavbarOptions = navbar([
  "/",
  {
    text: "記事",
    icon: "meteor-icons:folder",
    prefix: "/posts/",
    children: [
      {
        text: "統計検定1級-数理統計",
        icon: "meteor-icons:folder",
        prefix: "grade1_1/",
        children: [
          { text: "2013", icon: "meteor-icons:folder",link: "2013/1.md"},
        ],
      },
      {
        text: "確率分布",
        icon: "meteor-icons:folder",
        prefix: "probability_distribution/",
        children: [
          { text: "一様分布", icon: "meteor-icons:folder",link: "uniform.md"},
        ],
      },
    ],
  },
]);
