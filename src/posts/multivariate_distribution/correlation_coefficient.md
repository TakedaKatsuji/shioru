---
date: 2025-09-22
icon: meteor-icons:feather
category:
  - 統計数理
  - 多次元分布
tag:
  - 相関係数
  - 偏相関係数
  - 共分散
cover: "/assets/images/multivariate_distribution/correlation_coefficient/thumbnail.png" 
---

<!-- more -->

# 相関係数の性質まとめ

::: expl
相関係数とは二つ以上の確率変数の間にある関係の強弱を表す指標で、$-1 \leq \rho \leq 1$ を満たします.

1に近づけば==正の相関==があるといい、確率変数 $X$ が増えれば $Y$ も増える関係にあります.

逆に-1に近ければ==負の相関==確率変数 $X$ が増えるとき $Y$ は減る関係にあります.[下図参照]

相関係数と言われればピアソンの積率相関係数を表すのが一般的です.

<div style="display: flex; gap: 10px; justify-content: center;">
  <img src="/assets/images/multivariate_distribution/correlation_coefficient/correlation_color_animation.gif" style="max-width: 48%; height: auto;">
</div>

<div style="display: flex; gap: 10px; justify-content: center;">
  <img src="/assets/images/multivariate_distribution/correlation_coefficient/correlation_scatter_plots.png" style="max-width: 100%; height: auto;">
</div>
:::

## 相関係数の定義
::: def 定義
確率変数 $X, Y$ の**ピアソンの積率相関係数**は次で定義されます.

$$
\rho_{X,Y} = \frac{\mathrm{Cov}[X,Y]}{\sqrt{\mathrm{V}[X]} \, \sqrt{\mathrm{V}[Y]}}
$$

ここで，
- $\mathrm{Cov}[X,Y]$ は共分散
- $\mathrm{V}[X], \mathrm{V}[Y]$ は分散  

を表します.
:::

---

## 性質
- $-1 \leq \rho_{X,Y} \leq 1$

- $\rho_{X,Y} = 0$ のとき $X, Y$ は**無相関**と呼ばれる  
  （ただし独立とは限らない点に注意）

- 線形変換に対して不変  
  $X' = aX + b, Y' = cY + d$ としても $\rho_{X',Y'} = \rho_{X,Y}$ が成り立つ  

- $\rho_{X,Y} = \pm 1$ のとき，$Y$ は $X$ の完全な線形関数

---

## サンプル相関係数
::: def
有限のデータ $(x_i, y_i) \; (i=1,\dots,n)$ から計算する場合，**標本相関係数**は

$$
r = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}
{\sqrt{\sum_{i=1}^n (x_i - \bar{x})^2} \, \sqrt{\sum_{i=1}^n (y_i - \bar{y})^2}}
$$

で与えられます.

ここで $\bar{x}, \bar{y}$ は標本平均です.

:::

## 例題

- **例題1: 線形結合**  
([2013年統計数理問1 改](/posts/grade1_1/2013/1.md))  

$X \sim \mathrm{Uniform}(0,1)$ とし，$Y = 1 - X$ のとき，確率変数 $X, Y$ の相関係数を求めよ.

::: details 解答

  ::: ans
  まず，$X$ の基本的な統計量は

  $$
  \mathbb{E}[X] = \tfrac{1}{2}, \quad \mathrm{V}[X] = \tfrac{1}{12}
  $$

  です.  

  次に $Y = 1 - X$ なので，

  $$
  \mathbb{E}[Y] = 1 - \mathbb{E}[X] = \tfrac{1}{2}, \quad 
  \mathrm{V}[Y] = \mathrm{V}[1 - X] = \mathrm{V}[X] = \tfrac{1}{12}
  $$

  となります.  

  共分散は
  $$
  \begin{align}
  \mathrm{Cov}[X,Y]
  &= \mathbb{E}[XY] - \mathbb{E}[X]\mathbb{E}[Y] \\[6pt]
  &= \mathbb{E}[X(1-X)] - \tfrac{1}{2}\cdot\tfrac{1}{2} \\[6pt]
  &= \mathbb{E}[X - X^2] - \tfrac{1}{4}
  \end{align}
  $$

  ここで

  $$
  \mathbb{E}[X] = \tfrac{1}{2}, \quad \mathbb{E}[X^2] = \frac{1}{3}
  $$

  だから
  $$
  \begin{align}
  \mathbb{E}[X - X^2] &= \tfrac{1}{2} - \tfrac{1}{3} = \tfrac{1}{6}, \\[6pt]
  \mathrm{Cov}[X,Y] &= \tfrac{1}{6} - \tfrac{1}{4} = -\tfrac{1}{12}
  \end{align}
  $$

  したがって，相関係数は
  $$
  \begin{align}
  \rho_{X,Y}
  &= \frac{\mathrm{Cov}[X,Y]}{\sqrt{\mathrm{V}[X]}\sqrt{\mathrm{V}[Y]}} \\[6pt]
  &= \frac{-\tfrac{1}{12}}{\sqrt{\tfrac{1}{12}} \cdot \sqrt{\tfrac{1}{12}}} \\[6pt]
  &= \frac{-\tfrac{1}{12}}{\tfrac{1}{12}} \\[6pt]
  &= -1
  \end{align}
  $$

  よって，$X, Y$ は**完全な負の相関**を持つ.
  :::

::: ans 別解
[共分散の**線形性**](/posts/multivariate_distribution/covariance.md)を使うとより簡単に計算できます.
$$
\begin{align}
\mathrm{Cov}[X, Y] 
&= \mathrm{Cov}[X, 1 - X] \\[6pt]
&= \mathrm{Cov}[X, 1] + \mathrm{Cov}[X, -X] \\[6pt]
&= 0 - \mathrm{V}[X] \\[6pt]
&= -\tfrac{1}{12}
\end{align}
$$
よって相関係数は
$$
\begin{align}
\rho_{X,Y}
= \frac{\mathrm{Cov}[X,Y]}{\sqrt{\mathrm{V}[X]}\sqrt{\mathrm{V}[Y]}}
= \frac{-\tfrac{1}{12}}{\tfrac{1}{12}}
= -1
\end{align}
$$

計算量が一気に減り，**線形性を使うのが有効**であることが分かります.
:::

## 参考文献
<AffiliateBook id="takemura_gen_stats"/>