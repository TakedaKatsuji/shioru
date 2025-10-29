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
        text: "統計検定1級 統計数理 過去問解説",
        icon: "meteor-icons:folder",
        prefix: "grade1_1/",
        children: [
          { text: "2013", icon: "meteor-icons:folder",link: "2013/1.md"},
        ],
      },
      {
        text: "数理統計学",
        icon: "meteor-icons:folder",
        prefix: "",
        children: [
          { text: "確率分布", icon: "meteor-icons:folder",link: "probability_distribution/README.md"},
          { text: "多次元分布", icon: "meteor-icons:folder",link: "multivariate_distribution/README.md"},
          { text: "仮説検定手法", icon: "meteor-icons:folder",link: "test/README.md"},
        ],
      },
    ],
  },
]);
