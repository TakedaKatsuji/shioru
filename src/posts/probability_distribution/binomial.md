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

cover: "/assets/images/probability_distribution/binomial/thumbnail.png" 
---

<!-- more -->

# 二項分布の性質


::: expl
二項分布は 試行回数 $n$、成功確率を $p$ とする独立ベルヌーイ試行の和で表されます.
これは成功回数の分布であり、==回数(カウント)の分布をモデル化== するときに頻繁に利用されます.

独立同分布のベルヌーイ分布に従う確率変数 $I_i$ とする.
二項分布は
$$
\begin{align}
I_i &\overset{i.i.d.}{\sim} \mathrm{Bern}(p)\\[6pt]

X &= \sum_i^n I_i \sim Bin(n, p)
\end{align}
$$
で表される.
:::

<div style="display: flex; gap: 10px; justify-content: center;">
  <img src="/assets/images/probability_distribution/binomial/binom_to_normal_line.gif" style="max-width: 100%; height: auto;">
</div>

## 1. 確率質量関数

::: def 確率質量関数 (PMF)
$$
\mathbb{P}(X=k)=\,{}_nC_k\,p^k(1-p)^{\,n-k},\quad k=0,1,\dots,n.
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

::: details 導出の手順はこちら　ベルヌーイ分布から
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

::: details 導出の手順はこちら 確率質量関数から
::: calc 導出

二項分布 $X \sim \mathrm{Bin}(n,p)$ に対して
$$
\mathbb{E}[X]=\sum_{k=0}^n k\,{}_nC_k\,p^k(1-p)^{n-k}.
$$

$_nC_k$ を階乗で展開し，$k$ と約分する:
$$
\begin{align}
k\,{}_nC_k
&=k \cdot \frac{n!}{k!(n-k)!} \\[4pt]
&=\frac{k}{k!}\cdot\frac{n!}{(n-k)!}
=\frac{1}{(k-1)!}\cdot\frac{n!}{(n-k)!} \\[4pt]
&=\frac{n\,(n-1)!}{(k-1)!\,(n-k)!}
= n \cdot \frac{(n-1)!}{(k-1)!\,\{(n-1)-(k-1)\}!} \\[4pt]
&= n \cdot {}_{\,n-1}C_{\,k-1}.
\end{align}
$$

これを元の和に代入し，$m=k-1$ と置換する:
$$
\begin{align}
\mathbb{E}[X]
&=\sum_{k=1}^n n\,{}_{\,n-1}C_{\,k-1}\,p^k(1-p)^{n-k} \\[4pt]
&= n p \sum_{k=1}^n {}_{\,n-1}C_{\,k-1}\,p^{k-1}(1-p)^{(n-1)-(k-1)} \\[4pt]
&= n p \sum_{m=0}^{n-1} {}_{\,n-1}C_{\,m}\,p^{m}(1-p)^{(n-1)-m}. 
\end{align}
$$

ここで $\sum_{m=0}^{n-1} {}_{\,n-1}C_{\,m}\,p^{m}(1-p)^{(n-1)-m}=1$（全確率）なので
$$
\mathbb{E}[X]=n p \cdot 1 = np.
$$

:::


## 4. 分散
::: def 分散
$$
\mathrm{V}[X]=np(1-p).
$$
:::

::: details 導出の手順はこちら ベルヌーイ分布から
::: calc 導出
独立より $\mathrm{Cov}[I_i,I_j]=0\ (i\ne j)$、かつ $\mathrm{V}[I_i]=p(1-p)$.
$$
\mathrm{V}[X]=\sum_{i=1}^n\mathrm{V}[I_i]=np(1-p).
$$
:::

::: details 導出の手順はこちら 確率質量関数から
::: calc 導出

$X \sim \mathrm{Bin}(n,p)$ の分散は
$$
\mathrm{V}[X] = \mathbb{E}[X^2]-\mathbb{E}[X]^2.
$$
ここでは $\mathbb{E}[X(X-1)]$ を先に求めてから
$\mathbb{E}[X^2]=\mathbb{E}[X(X-1)]+\mathbb{E}[X]$ を用いる.

まず二階階乗モーメント:
$$
\begin{align}
\mathbb{E}[X(X-1)]
&=\sum_{k=0}^n k(k-1)\,{}_nC_k\,p^k(1-p)^{n-k}.
\end{align}
$$

$_nC_k$ を階乗で展開し約分する:
$$
\begin{align}
k(k-1)\,{}_nC_k
&=k(k-1)\cdot \frac{n!}{k!(n-k)!} \\[4pt]
&=\frac{k(k-1)}{k!}\cdot \frac{n!}{(n-k)!}
=\frac{1}{(k-2)!}\cdot \frac{n!}{(n-k)!} \\[4pt]
&=\frac{n(n-1)\,(n-2)!}{(k-2)!\,(n-k)!} \\[4pt]
&= n(n-1)\cdot {}_{\,n-2}C_{\,k-2}.
\end{align}
$$

代入し，$m=k-2$ と置換する:
$$
\begin{align}
\mathbb{E}[X(X-1)]
&=\sum_{k=2}^n n(n-1)\,{}_{\,n-2}C_{\,k-2}\,p^k(1-p)^{n-k} \\[4pt]
&= n(n-1)\,p^2 \sum_{m=0}^{n-2} {}_{\,n-2}C_{\,m}\,p^{m}(1-p)^{(n-2)-m}.
\end{align}
$$

ここで $\sum_{m=0}^{n-2} {}_{\,n-2}C_{\,m}\,p^{m}(1-p)^{(n-2)-m}=1$（全確率）より
$$
\mathbb{E}[X(X-1)] = n(n-1)p^2.
$$

ゆえに
$$
\mathbb{E}[X^2]=\mathbb{E}[X(X-1)]+\mathbb{E}[X]
= n(n-1)p^2 + np,
$$
したがって
$$
\mathrm{V}[X]
= \bigl(n(n-1)p^2 + np\bigr) - (np)^2
= np(1-p).
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
