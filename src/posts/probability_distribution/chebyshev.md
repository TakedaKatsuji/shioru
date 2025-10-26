---
date: 2025-10-26
icon: meteor-icons:feather
category:
  - 統計数理
  - 確率分布
  - 極限定理
tag:
  - マルコフの不等式
  - 期待値
  - 極限定理
  - 中心極限定理
  - チェビシェフの不等式
---

# チェビシェフの不等式

<div style="display: flex; gap: 10px; justify-content: center;">
  <img src="/assets/images/probability_distribution/chebyshev/thumbnail.png" style="max-width: 100%; height: auto;">
</div>

:::def
**チェビシェフの不等式（Chebyshev’s inequality）**  
平均 $\mu=\mathbb{E}[X]$ と分散 $\sigma^2=\mathrm{V}[X]$ をもつ確率変数 $X$ と任意の $a>0$ に対して
$$
\Pr\big(|X-\mu|\ge a\big)\le \frac{\sigma^2}{a^2}.
$$
特に $a=k\sigma\ (k>0)$ とおくと
$$
\Pr\big(|X-\mu|\ge k\sigma\big)\le \frac{1}{k^2}.
$$
:::

## チェビシェフの不等式の証明
:::expl
チェビシェフの不等式は ==**平均値(期待値)から $k\sigma$ 以上ずれる確率は高々 $\frac{1}{k^2}$**== を表す不等式です。

期待値と分散がわかっていれば確率変数 $X$ の分布がわからなくても上から抑えることができます.

証明はマルコフの不等式から簡単に導けます.
:::

<div class="vp-card-container">

<VPCard
  title="マルコフの不等式"
  desc="マルコフの不等式の証明"
  link="/posts/probability_distribution/markov.html"
/>

</div>

:::proof
マルコフの不等式より，非負の確率変数 $Y \ge 0$ と $t>0$ に対して
$$
\Pr(Y \ge t) \le \frac{\mathbb{E}[Y]}{t}.
$$

ここで確率変数 $X$ の平均と分散を
$$
\mu = \mathbb{E}[X], \quad \sigma^2 = \mathrm{V}[X]
$$
とおく．

$Y = (X - \mu)^2 \ge 0$ とし，$t = a^2\ (a > 0)$ を代入すると，
$$
\Pr\!\left((X - \mu)^2 \ge a^2\right)
\le \frac{\mathbb{E}[(X - \mu)^2]}{a^2}
= \frac{\sigma^2}{a^2}.
$$

左辺は $\Pr(|X - \mu| \ge a)$ なので，
$$
\Pr(|X - \mu| \ge a) \le \frac{\sigma^2}{a^2}.
$$

これが **チェビシェフの不等式** である．

また別形式で $a = k\sigma$ とおくと,
$$
\begin{align}
\Pr(|X - \mu| \ge k\sigma) \le \frac{1}{k^2}.
\end{align}
$$
:::

## 実際のデータで確認
令和5年度の共通テスト数学Ⅱ・Bの点数分布をし使用してチェビシェフの不等式を確認します.

<a href="/data/r5_math2B.csv" download="r5_math2B.csv">
CSVデータをダウンロード
</a>


### 統計量
|総受験者数|平均|標準偏差|
|:----:|:----:|:----:|
|316728|61.48|20.18|

### 得点分布
横軸に得点、縦軸にその得点の人数のヒストグラム
<div style="display: flex; gap: 10px; justify-content: center;">
  <img src="/assets/images/probability_distribution/chebyshev/hist.png" style="max-width: 80%; height: auto;">
</div>

### チェビシェフの不等式

チェビシェフの不等式より, 平均値から $2\sigma$ 以上離れる確率は $\frac{1}{4}$ つまり$25$%以下

今回使用するデータでは, 

- $\mu = 61.48$
- $\sigma = 20.18$
- $\mu - 2\sigma = 21.13$
- $\mu + 2\sigma = 101.8$

点数の上限は100点のため101.8点以上の得点者は0人, 21.13点以下の人数は10971人なので全体の3.46%

==マルコフの不等式同様に粗い抑え方であることがわかります.==


## 参考文献
- データ
  - [共通テスト 令和５年度 試験情報データ（本試験）](https://www.dnc.ac.jp/kyotsu/hyouka/r5_hyouka/r5_data.html)
- 書籍
<AffiliateBook id="takemura_gen_stats"/>