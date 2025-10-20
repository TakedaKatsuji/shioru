export type Book = {
  title: string
  author?: string
  img: string
  amazon?: string
  rakuten?: string
  desc?: string
}

export const BOOKS: Record<string, Book> = {
  takemura_gen_stats: {
    title: "新装改訂版　現代数理統計学",
    author: "竹村 彰通",
    img: "https://thumbnail.image.rakuten.co.jp/@0_mall/book/cabinet/8601/9784780608601.jpg?_ex=240x240",
    amazon: "https://amzn.to/46UzNM9",
    rakuten: "https://a.r10.to/h54IFF",
    desc: "統計検定1級対策に定番の書籍 難易度は高めだが演習問題も豊富"
  },
  official_1: {
    title: "増訂版 日本統計学会公式認定 統計検定１級対応 統計学",
    author: "日本統計学会",
    img: "https://thumbnail.image.rakuten.co.jp/@0_mall/book/cabinet/4016/9784489024016_1_2.jpg?_ex=240x240",
    amazon: "https://amzn.to/48zzS9h",
    rakuten: "https://a.r10.to/hPi4TD",
    desc: "統計検定1級公式教本 網羅的に記述してあるので辞書的に使うことをおすすめします"
  },
  kakomon1213: {
    title: "日本統計学会公式認定 統計検定 1級 公式問題集[2012〜2013年]",
    author: "日本統計学会",
    img: "https://m.media-amazon.com/images/I/61GHu8G0tgL._SY425_.jpg",
    amazon: "https://amzn.to/4nYPlV8",
    desc: "過去問2012年・2013年"
  },
  kakomon1415: {
    title: "日本統計学会公式認定 統計検定 1級 公式問題集[2014〜2015年]",
    author: "日本統計学会",
    img: "https://m.media-amazon.com/images/I/611hH61A9zL._SY425_.jpg",
    amazon: "https://amzn.to/3KXI1dG",
    desc: "過去問2014年・2015年"
  },
  kakomon1618: {
    title: "日本統計学会公式認定 統計検定 1級 公式問題集[2016〜2018年]",
    author: "日本統計学会",
    img: "https://m.media-amazon.com/images/I/41sWMgbd-aL._SY445_SX342_ControlCacheEqualizer_.jpg",
    amazon: "https://amzn.to/4nXXTvv",
    desc: "過去問2016年・2017年・2018年"
  },
  kakomon1922: {
    title: "日本統計学会公式認定 統計検定 1級 公式問題集[2019〜2022年]",
    author: "日本統計学会",
    img: "https://m.media-amazon.com/images/I/611ZI5RBsyL._SY425_.jpg",
    amazon: "https://amzn.to/42LCoFB",
    rakuten: "https://a.r10.to/h5S3kH",
    desc: "過去問2019年・2020年・2021年・2022年"
  },
  kakomon2224: {
    title: "日本統計学会公式認定 統計検定 1級 公式問題集[2022〜2024年]",
    author: "日本統計学会",
    img: "https://thumbnail.image.rakuten.co.jp/@0_mall/book/cabinet/5588/9784788925588_1_7.jpg?_ex=288x288",
    amazon: "https://amzn.to/43qAD0K",
    rakuten: "https://a.r10.to/hP62u7",
    desc: "過去問2022年・2023年・2024年"
  },
}