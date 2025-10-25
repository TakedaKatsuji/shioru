---
date: 2025-10-24
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

# マルコフの不等式

<div style="display: flex; gap: 10px; justify-content: center;">
  <img src="/assets/images/probability_distribution/markov/thumbnail.png" style="max-width: 100%; height: auto;">
</div>

## マルコフの不等式の証明

:::def
確率変数 $X$ が可積分（$\mathbb{E}[|X|]<\infty$）であるとする.  
任意の $a>0$ に対して次が成り立つ:
$$
P(|X|\ge a) \le \frac{\mathbb{E}[|X|]}{a}.
$$
:::

:::proof
確率変数 $Y$ を次で定義する:
$$
Y =
\begin{cases}
a, & \text{if } |X|\ge a,\\
0, & \text{if } |X|<a.
\end{cases}
$$

このとき $Y \le |X|$ が成り立つ.  
したがって期待値をとると
$$
\mathbb{E}[Y] \le \mathbb{E}[|X|].
$$

一方で $Y=a$ となるのは $|X|\ge a$ のときのみなので,
$$
\mathbb{E}[Y] = a\,P(|X|\ge a).
$$

以上より
$$
a\,P(|X|\ge a) \le \mathbb{E}[|X|].
$$

両辺を $a$ で割って
$$
P(|X|\ge a) \le \frac{\mathbb{E}[|X|]}{a}.
$$

証明完了.
:::

## マルコフの不等式の意味
::: expl
マルコフの不等式には解釈しやすい形があります. $k=\frac{a}{\mathbb{E}[|X|]}$ とおくと,
$$
\begin{align}
P(|X|\ge k\mathbb{E}[|X|]) \le \frac{1}{k}
\end{align}
$$

つまり,  ==**期待値の $k$ 倍以上になる確率は $\frac{1}{k}$ 以下**==
:::

たとえばマルコフの不等式を使用すると、==**平均年収が500万円のとき、年収が1000万以上となる確率は50%以下**== ということがわかります。
ちなみに実際の日本の年収で1000万以上は5~6%程と言われていますので, マルコフの不等式はかなり大雑把に上から抑えています.

## マルコフの不等式の可視化
$X \sim \mathcal{N}(0,1)$ とすると,マルコフの不等式は
$$
\begin{align}
P(|X|\ge k\mathbb{E}[|X|]) \le \frac{1}{k}
\end{align}
$$
この左辺を赤、右辺を青でプロットした図がこちらです.

<div style="display: flex; gap: 10px; justify-content: center;">
  <img src="/assets/images/probability_distribution/markov/markov.png" style="max-width: 100%; height: auto;">
</div>

グラフからもわかるように常に $\frac{1}{k}$ で上から抑えられています.

## 参考文献
<AffiliateBook id="takemura_gen_stats"/>