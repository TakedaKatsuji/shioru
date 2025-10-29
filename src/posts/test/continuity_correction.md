---
icon: meteor-icons:file-lines
date: 2025-09-29
category:
  - 統計検定1級
  - 統計数理
  - 仮説検定
tag:
  - 検定
  - 正規近似
  - 連続修正
  - 半整数補正
cover: "/assets/images/test/continuity_crrection/thumbnail.png" 
---

<!-- more -->

# 半整数補正

半整数補正とは二項分布などの離散型分布を正規近似で連続型の分布に近似するときに==近似精度を上げる==方法です.
この記事ではグラフやアニメーションとともに、この近似がどの程度有効か議論していきたいと思います.

:::expl
二項分布 $X \sim \mathrm{Bin}(n, p)$ の正規近似は
$$
\begin{align}
X \sim \mathcal{N}\left(np, np(1-p)\right)
\end{align}
$$

今回 $\mathrm{Pr}(X \leq c)$ の値を
- 正確確率(Exact) オレンジ色の長方形の面積の和
- 正規近似・半整数補正なし(Non CC) 赤色の線より左側の曲線下面積
- 正規近似・半整数補正あり(CC) 緑色の線より左側の曲線下面積

この3種類値を比較していきます.

**3種類の面積のグラフ**
<div style="display: flex; gap: 10px; justify-content: center;">
  <img src="/assets/images/test/continuity_crrection/continuity_correction.png" style="max-width: 100%; height: auto;">
</div>

<div style="display: flex; gap: 10px; justify-content: center;">
  <img src="/assets/images/test/continuity_crrection/continuity_correction_zoom.png" style="max-width: 100%; height: auto;">
</div>
:::

## Exactとの差のアニメーション1
:::plan 設定
二項分布の ==確率 $p$ を固定して $n$ を増加== してExactとの差分をプロットします.

- 分布: $X\sim\mathrm{Bin}(n,p)$（$p=0.5$）  
- 片側: 左片側（$\,\Pr(X\le c)\,$）  
- しきい値: $c=\lfloor a n\rfloor$（本文では $a=0.35$）  
- $n$ の範囲: $n_{\min}=10,\ n_{\max}=100$

:::

::: expl
標準正規分布の分布関数を $\Phi$ とし，$\mu=np,\ \sigma=\sqrt{np(1-p)}$ とする.

- Exact のとき
$$
\Pr(X \le c)=\sum_{k=0}^{c}\binom{n}{k}p^{k}(1-p)^{n-k}\,.
$$

- 補正なしのとき
$$
\Pr(X \le c)_{NonCC}\approx \Phi\!\left(\frac{c-\mu}{\sigma}\right).
$$

- 半整数補正ありのとき
$$
\Pr(X \le c)_{CC}\approx \Phi\!\left(\frac{c+\tfrac{1}{2}-\mu}{\sigma}\right).
$$

差の可視化は
$$
\begin{align}
\Delta_{\text{Non CC}}(n)&=\Phi\!\left(\frac{c-\mu}{\sigma}\right)-\Pr(X\le c) \\[6pt]
\Delta_{\text{CC}}(n)&=\Phi\!\left(\frac{c+\tfrac{1}{2}-\mu}{\sigma}\right)-\Pr(X\le c).
\end{align}
$$

Non CC と CC で Exact との差をプロットすると以下になる.

<div style="display: flex; gap: 10px; justify-content: center;">
  <img src="/assets/images/test/continuity_crrection/cc_diff_convergence.gif" style="max-width: 100%; height: auto;">
</div>
:::

::: sum
左片側では小さな $n$ で $\Delta_{\text{Non CC}}<0$（過少推定）になりやすい傾向にあります.
一方で ==半整数補正は小さな $n$ でも差を大きく縮めている== ことがわかります.
:::

## Exactとの差のアニメーション2
:::plan 設定
二項分布の ==確率 $n$ を固定して $p$ を増加== してExactとの差分をプロットします.

- 分布: $X\sim\mathrm{Bin}(n,p)$ ($n=50$)
- 片側: 左片側（$\,\Pr(X\le c)\,$）  
- しきい値: $c=\lfloor a n\rfloor$（本文では $a=0.35$）  
- $p$ の範囲: $p_{\min}=0,\ p_{\max}=1$

:::

::: expl
$n=50$で固定し, $p \in [0,1]$ の範囲で動かす,
Non CC と CC で Exact との差をプロットすると以下になる.
<div style="display: flex; gap: 10px; justify-content: center;">
  <img src="/assets/images/test/continuity_crrection/cc_diff_over_p.gif" style="max-width: 100%; height: auto;">
</div>
:::

:::sum
- 本稿では $n=50$ を固定し，$p$ を $[0,1]$ で動かして左片側 $\Pr(X\le c)$ の近似誤差を比較しました．
- 近似なし（Non CC）は，$\mu=np$ が $c+\tfrac12$ に近づく付近で誤差が最大化しやすいことを確認しました．
- 半整数補正（CC）は，この最大誤差点付近でも誤差を大きく抑えられることを示しました．
- 例として $c=2$ の設定では，誤差は $p=(c+\tfrac12)/n=0.05$ 付近で最大化しやすく，CC による改善が明瞭に観察できます．
- 実務では 半整数補正を利用するのをお勧めします.
:::

## 参考文献
<AffiliateBook id="official1"/>
<AffiliateBook id="takemura_gen_stats"/>