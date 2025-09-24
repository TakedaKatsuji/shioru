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
          { text: "一様分布", icon: "meteor-icons:feather",link: "uniform.md"},
          { text: "標準正規分布の性質", icon: "meteor-icons:feather",link: "standard_normal1.md"},
          { text: "標準正規分布の k 次モーメント", icon: "meteor-icons:feather",link: "standard_normal2.md"},
          { text: "正規分布", icon: "meteor-icons:feather",link: "normal.md"},
        ],
      },
      {
        text: "多次元分布",
        icon: "meteor-icons:folder",
        prefix: "multivariate_distribution/",
        children: [
          { text: "共分散", icon: "meteor-icons:feather",link: "covariance.md"},
          { text: "相関係数", icon: "meteor-icons:feather",link: "correlation_coefficient.md"},
          { text: "正規分布の条件付き分布", icon: "meteor-icons:feather",link: "normal_cpd.md"},
        ],
      },
    ],
  },
]);
