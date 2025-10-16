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
}
