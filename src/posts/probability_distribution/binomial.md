---
date: 2025-09-25
icon: meteor-icons:feather
category:
  - 統計数理
  - 確率分布
tag:
  - 二項分布
  - 確率密度関数
  - 離散型
---

# 二項分布の性質

<div style="display: flex; gap: 10px; justify-content: center;">
  <img src="/assets/images/probability_distribution/binomial/binom_to_normal_line.gif" style="max-width: 100%; height: auto;">
</div>

::: expl
試行回数を $n$、成功確率を $p$ とする独立ベルヌーイ試行の和 $X\sim\mathrm{Bin}(n,p)$ を扱う. 
二項分布は離散型なので ==確率質量関数 (PMF)== を用いる.
:::

## 1. 確率質量関数
::: def 確率質量関数 (PMF)
$$
\mathbb{P}(X=k)=\binom{n}{k}p^{\,k}(1-p)^{\,n-k},\qquad k=0,1,\dots,n.
$$
:::

**確率質量関数のグラフ**

<div style="display: flex; gap: 10px; justify-content: center;">
  <img src="/assets/images/probability_distribution/binomial/pmf_multi_line.png" style="max-width: 80%; height: auto;">
</div>


## 2. 累積分布関数
::: def 累積分布関数 (CDF)
$$
F(k)=\mathbb{P}(X\le k)=\sum_{j=0}^{\lfloor k\rfloor}\binom{n}{j}p^{\,j}(1-p)^{\,n-j}.
$$
:::

**累積分布関数のグラフ**

<div style="display: flex; gap: 10px; justify-content: center;">
  <img src="/assets/images/probability_distribution/binomial/cdf.png" style="max-width: 70%; height: auto;">
</div>

## 3. 期待値
::: def 期待値
$$
\mathbb{E}[X]=np.
$$
:::

::: details 導出の手順はこちら
::: calc 導出
$$
X=\sum_{i=1}^n I_i,\ \ I_i\;\overset{\mathrm{i.i.d.}}{\sim} \mathrm{Bernoulli}(p).
$$
$$
\begin{align}
\mathbb{E}[X]&=\sum_{i=1}^n\mathbb{E}[I_i]\\[6pt]
&=\sum_{i=1}^n p \\[6pt]
&=np.
\end{align}
$$
:::

## 4. 分散
::: def 分散
$$
\mathrm{V}[X]=np(1-p).
$$
:::

::: details 導出の手順はこちら
::: calc 導出
独立より $\mathrm{Cov}[I_i,I_j]=0\ (i\ne j)$、かつ $\mathrm{V}[I_i]=p(1-p)$.
$$
\mathrm{V}[X]=\sum_{i=1}^n\mathrm{V}[I_i]=np(1-p).
$$
:::

## 5. 積率母関数
::: def 積率母関数 (MGF)
$$
M_X(t)=\mathbb{E}[e^{tX}]=(1-p+pe^{t})^{n}.
$$
:::

::: details 導出の手順はこちら
::: calc 導出
独立性と $I_i\in\{0,1\}$ から
\begin{align}
M_X(t)&=\mathbb{E}\!\left[e^{t\sum I_i}\right]=\prod_{i=1}^n\mathbb{E}[e^{t I_i}]
=\bigl((1-p)+p e^{t}\bigr)^n.
\end{align}
:::

## 6. 特性関数
::: def 特性関数 (CF)
$$
\varphi_X(\omega)=\mathbb{E}[e^{i\omega X}]=(1-p+pe^{i\omega})^{n}.
$$
:::

::: details 導出の手順はこちら
::: calc 導出
MGF と同様に
$$
\varphi_X(\omega)=\prod_{i=1}^n\mathbb{E}[e^{i\omega I_i}]
=\bigl((1-p)+p e^{i\omega}\bigr)^n.
$$
:::
