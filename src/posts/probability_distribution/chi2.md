---
date: 2025-10-08
icon: meteor-icons:feather
category:
  - 統計数理
  - 確率分布
tag:
  - カイ二乗分布
  - ヤコビアン
  - 確率密度関数
  - 連続型
  - ベータ関数
  - ガンマ関数
---

# カイ二乗分布の性質

<div style="display: flex; gap: 10px; justify-content: center;">
  <img src="/assets/images/probability_distribution/chi2/thumbnail.png" style="max-width: 100%; height: auto;">
</div>

:::def
カイ二乗分布は独立に[標準正規分布](/posts/probability_distribution/standard_normal1.md)に従う確率変数の二乗の和が従う分布です.

つまり $Z_i \overset{i.i.d.}{\sim} \mathcal{N}(0,1)$ のとき,
$$
\begin{align}
X = \sum_{i=1}^n Z_i^2 \sim \chi ^2(n)
\end{align}
$$
統計量 $X$ は自由度 $n$ のカイ二乗分布に従います.

:::

==カイ二乗分布は様々な**性質・関係**が学べる分布== であり, 以下の表ように他分布と関連しています.

|確率分布|関係|式|
|:----:|:----:|:--:|
|**カイ二乗分布**|標準正規分布の二乗和|$X=\sum_{i=1}^{n} Z_i^2,\ \ Z_i\sim\mathcal N(0,1)$|
|t分布|標準正規分布と**カイ二乗分布**の比|$T=\dfrac{Z}{\sqrt{X/n}},\ \ Z\sim\mathcal N(0,1),\ X\sim\chi^2(n)$|
|F分布|**カイ二乗分布**の比|$F=\dfrac{X_1/d_1}{X_2/d_2},\ \ X_1\sim\chi^2(d_1),\ X_2\sim\chi^2(d_2)$|

他にも**ベータ関数・ガンマ関数**, **変数変換**, **再生性**など統計検定で重要な性質の宝庫です.

## 1. 確率密度関数
::: def
自由度 $n$ , $x>0$ に対して
$$
\begin{align}
f(x) = \frac{1}{2^{n/2}\Gamma(\frac{n}{2})}x^{\tfrac{n}{2}-1}e^{-\tfrac{x}{2}}
\end{align}
$$
:::
## 2. 累積分布関数
## 3. 期待値
## 4. 分散
## 5. 積率母関数
## 6. 特性関数

執筆中...