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
  - 大数の弱法則
cover: "/assets/images/probability_distribution/weak_law_of_large_numbers/thumbnail.png"
---

<!-- more -->

# 大数の弱法則

:::expl
大数の弱法則とは，**たくさんの試行を平均すると，本当の平均（母平均）に近づく** という性質です．  
たとえばサイコロを何度も振って出た目の平均をとると，回数を増やすほど理論上の平均 3.5 に近づきます．  
つまり「偶然のブレ」は試行回数が多いほど平均で打ち消される，という直感を数学的に示した定理です．
:::

:::def
**大数の弱法則（Weak Law of Large Numbers）**

独立同分布な確率変数列 $X_1, X_2, \dots, X_n$ が存在し，  
それぞれの期待値が $\mathbb{E}[X_i] = \mu$，分散が $\mathrm{V}[X_i] = \sigma^2 < \infty$ であるとする．  
このとき，標本平均
$$
\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i
$$
は確率的に母平均 $\mu$ に収束する．すなわち
$$
\forall \varepsilon > 0,\quad
\lim_{n \to \infty} \Pr\left(|\bar{X}_n - \mu| \ge \varepsilon\right) = 0.
$$

これを **確率収束** と呼び，
$$
\bar{X}_n \xrightarrow{p} \mu
$$
と書く．
::: 

:::warning
大数の弱法則は，各確率変数が **期待値と分散をもつ** ことを仮定しています .
これが成立しない場合，標本平均が母平均に確率収束するとは限りません.
:::


## 大数の弱法則の証明
:::expl
大数の弱法則は定義の左辺から類推できるように ==**チェビシェフの不等式**== から証明できます.
:::

<div class="vp-card-container">

<VPCard
  title="チェビシェフの不等式"
  desc="チェビシェフの不等式の証明"
  link="/posts/probability_distribution/chebyshev.html"
/>

</div>

:::proof
独立同分布 $X_1,\dots,X_n$ に対し，$\mathbb{E}[X_i]=\mu$，$\mathrm{V}[X_i]=\sigma^2<\infty$ とする．
標本平均 $\bar X_n=\frac{1}{n}\sum_{i=1}^n X_i$ の期待値と分散は
$$
\mathbb{E}[\bar X_n]=\mu,\qquad \mathrm{V}[\bar X_n]=\frac{\sigma^2}{n}.
$$
チェビシェフの不等式より任意の $\varepsilon>0$ について
$$
\Pr\big(|\bar X_n-\mu|\ge \varepsilon\big)
\le \frac{\mathrm{V}[\bar X_n]}{\varepsilon^2}
= \frac{\sigma^2}{n\varepsilon^2}\xrightarrow[n\to\infty]{}0.
$$
よって $\bar X_n \xrightarrow{p} \mu$．これが大数の弱法則．
:::

## シミュレーションで確認
先ほど説明したように期待値が存在しない場合大数の弱法則は成立しません.
これをシミュレーションで確認してみましょう.

$t$ 分布は自由度2のとき期待値が$0$ですが、自由度が1のとき(コーシー分布)では期待値が存在しません.

<div class="vp-card-container">
<VPCard
  title="t分布"
  desc="PDF・CDF・期待値・分散"
  link="/posts/probability_distribution/t.html"
/>
</div>

### t分布の確率密度関数

:::expl 確率密度関数
$$
\begin{align}
f(t;1) &= \frac{1}{\pi (1+t^2)} \\[6pt]
f(t;2) &= \left(2+t^2\right)^{-\frac{3}{2}} \\[6pt]
\end{align}
$$
<div style="display: flex; gap: 10px; justify-content: center;">
  <img src="/assets/images/probability_distribution/weak_law_of_large_numbers/t_pdf.png" style="max-width: 100%; height: auto;">
</div>
:::

### シミュレーション

横軸にそれぞれの分布からのサンプル数, 縦軸にそのサンプルの平均をとります.


<div style="display: flex; gap: 10px; justify-content: center;">
  <img src="/assets/images/probability_distribution/weak_law_of_large_numbers/weaklaw.gif" style="max-width: 100%; height: auto;">
</div>

:::expl
シミュレーションの結果から，**期待値が存在しない分布では標本平均が安定せず収束していない** ことが確認できます．  
コーシー分布（自由度1）は裾が非常に重く，まれに極端に大きな値が出現するため，平均値が収束しません．  
そのためサンプルを増やしても平均が一定値に近づかず，グラフ上でも大きく揺れ動いたままになります．  

一方で，$t$ 分布（自由度2）は期待値が $0$ で存在するため，サンプル数を増やすにつれて平均が $0$ に収束していきます．  
:::

## 参考文献
<AffiliateBook id="official1"/>
<AffiliateBook id="takemura_gen_stats"/>