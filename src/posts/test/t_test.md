---
icon: meteor-icons:file-lines
date: 2025-09-30
category:
  - 統計検定1級
  - 統計数理
  - 仮説検定
tag:
  - t検定
  - 対応のないt検定
  - 対応のないt検定
  - ウェルチのt検定
  - パラメトリック
  - 正規分布
---


# t検定について概要解説

<div style="display: flex; gap: 10px; justify-content: center;">
  <img src="/assets/images/test/t_test/thumbnail.png" style="max-width: 100%; height: auto;">
</div>

統計検定の過去問題でt検定は頻出します.t検定には複数種類がありますが本質は ==**母平均に関する検定**== であるということです.

::: expl 記事紹介
本記事では $T$ 分布, カイ二乗分布を使用します.詳しくはこちらから！
<div class="vp-card-container">
<VPCard
  title="Ｔ分布の性質"
  desc="定義"
  link="/posts/probability_distribution/t.html"
/>
<VPCard
  title="カイ二乗分布の性質"
  desc="再生性"
  link="/posts/probability_distribution/chi2.html"
/>
</div>
:::

またt検定には仮定が存在します.

::: expl 仮定
- データが ==正規分布== に従っている
- データの ==分散が未知== である (既知の場合は**Z検定**) 
:::

またt検定の種類として
::: expl t検定の種類
- 1標本t検定 (平均はこの値であってるのか？)

- 2標本(**対応あり**)
  たとえば ==「手術前後の同一患者の歩行速度に差はあるか」== のように組が作れるもの
  2標本の差 $z_i = y_i - x_i$ をとって差の母平均を検定する1標本t検定に帰着


- 2標本(**対応ない**)
  たとえば ==「都市部校と農村部校のテスト得点平均」== のように独立しているもの
  - 2標本t検定（二つの**分散が等しい**集団の平均に差はあるか？ ）
  - ウェルチのt検定 (二つの**分散が異なる**集団の平均に差はあるか？)

:::

などがありますが、すべて ==1標本t検定の派生== と考えられるでしょう.

ではt検定の種類を具体例とともに見ていきます.

## 1標本のt検定

::: expl 問題設定
$\{X_i\}_{i=1}^n$ は独立同分布の正規分布に従い, 分散 $\sigma^2$ は未知とする.
$$
X_1,\dots,X_n \sim \mathcal{N}(\mu,\sigma^2).
$$
:::

::: expl 仮説
帰無仮説 $H_0:\ \mu=\mu_0$.
対立仮説 $H_1:\ \mu\ne\mu_0$（両側）. (片側は $\mu>\mu_0$ または $\mu<\mu_0$.)
:::

::: expl 統計量
- 標本平均 $\bar X=\frac1n\sum_{i=1}^n X_i$
- 不偏分散 $S^2=\frac1{n-1}\sum_{i=1}^n (X_i-\bar X)^2$

をもちいて==統計量 $T$ は帰無仮説のもと==で,
$$
T=\frac{\bar X-\mu_0}{S/\sqrt n}\ \stackrel{H_0}{\sim}\ t_{n-1}.
$$
で表せる.
:::

## T統計量が自由度 $n-1$の $t$ 分布になることの証明

公式を暗記しているとこんな疑問がでてきます。==公式では $n$ しかないのに、自由度は$n-1$です.==
結論から言うとこの $n-1$ は==不偏分散==からでてきたものです。
では流れを踏まえて丁寧に証明していきましょう

:::hint 方針
1. **$t$ 分布の定義**の形を目指す
2. **標準正規分布**を作成
3. **カイ二乗分布**を作成
4. 公式を作成
:::

### 1. **$t$ 分布の定義**の形を目指す
$t$ 分布の定義は,

$$
\begin{align}
T = \frac{Z}{\sqrt{X/n}} \sim t(n)
\end{align}
$$

ただし $Z \sim \mathcal{N}(0, 1), X \sim \chi2(n)$ .

つまり ==**分母のカイ二乗分布の自由度が全体のt分布の自由度と一致**== します.

### 2. 標準正規分布の作成

$\{X_i\}_{i=1}^n$ は独立同分布の正規分布に従い, 分散 $\sigma^2$ は未知とする.
$$
X_1,\dots,X_n \sim \mathcal{N}(\mu,\sigma^2).
$$
したがって $\bar X \sim \mathcal{N}(\mu, \sigma^2/n)$

これを標準化すると
$$
\begin{align}
Z &= \frac{\bar X - \mu}{\sqrt{\sigma^2/n}} \sim \mathcal{N}(0, 1)
\end{align}
$$

### 3. カイ二乗分布の作成
不偏分散を $S^2$ とする
$$
\begin{align}
S^2 &= \frac{1}{n-1}\sum^{n}_{i=1}(X_i - \bar X)^2 \\[6pt]
(n-1)S^2 &= \sum^{n}_{i=1}(X_i - \bar X)^2 \\[6pt]
(n-1)S^2 &= \sum^{n}_{i=1}\left\{(X_i - \mu) - (\bar X - \mu)\right\}^2 \\[6pt]
(n-1)S^2 &= \sum^{n}_{i=1}\left\{(X_i - \mu)^2 -2(X_i-\mu)(\bar X -\mu)+(\bar X - \mu)^2\right\} \\[6pt]
(n-1)S^2 &= \sum^{n}_{i=1}(X_i - \mu)^2 -2(\bar X -\mu)\sum^{n}_{i=1}(X_i-\mu)+\sum^{n}_{i=1}(\bar X - \mu)^2 \\[6pt]
(n-1)S^2 &= \sum^{n}_{i=1}(X_i - \mu)^2 -n(\bar X - \mu)^2 \\[6pt]
\end{align}
$$
ここで両辺を $\sigma^2$で割ると,
$$
\begin{align}
\frac{(n-1)S^2}{\sigma^2} &= \sum^{n}_{i=1}\left(\frac{X_i - \mu}{\sigma}\right)^2 -n\left(\frac{\bar X - \mu}{\sigma} \right)^2 \\[6pt]
\frac{(n-1)S^2}{\sigma^2} &= \sum^{n}_{i=1}\left(\frac{X_i - \mu}{\sigma}\right)^2 -\left(\frac{\bar X - \mu}{\sqrt{\sigma^2/n}} \right)^2 \\[6pt]
\end{align}
$$
ここで,
$$
\begin{align}
Z_i &= \frac{X_i - \mu}{\sigma} \sim \mathcal{N}(0, 1) \\[6pt]
Z &= \frac{\bar X - \mu}{\sqrt{\sigma^2/n}} \sim \mathcal{N}(0, 1)
\end{align}
$$
であるから, $Z_i^2, Z^2$ は自由度 $1$のカイ二乗分布に従い,
$$
\begin{align}
\frac{(n-1)S^2}{\sigma^2} &= \sum^{n}_{i=1}Z_i^2 -Z^2 \\[6pt]
\end{align}
$$
右辺第一項は再生性より $\chi^2(n)$. よって **コクランの定理**から
$$
\begin{align}
\frac{(n-1)S^2}{\sigma^2} \sim \chi2(n-1)
\end{align}
$$
::: hint
コクランの定理を簡単に説明すると
分解されたカイ二乗分布は自由度を足し引きできるということです。

イメージ:
$$
\begin{align}
\sum^{n}_{i=1}Z_i^2 &= \frac{(n-1)S^2}{\sigma^2} + Z^2 \\[6pt]
\chi2(n) &= \chi2(\nu) + \chi2(1) \\[6pt]
n &= \nu + 1 \\[6pt]
\nu &= n - 1
\end{align}
$$
:::

### 4. T統計量の公式の導出
上記の1~3から $T$ 統計量を導出すると
$$
\begin{align}
T &= \frac{Z}{\sqrt{\frac{(n-1)S^2}{\sigma^2}/(n-1)}} \sim t(n-1)\\[6pt]
&= \frac{Z}{\sqrt{\frac{S^2}{\sigma^2}}} \\[6pt]
&= \frac{Z}{S/\sigma} \\[6pt]
&= Z \cdot \frac{\sigma}{S} \\[6pt]
&= \frac{\bar X - \mu}{\sigma/\sqrt{n}} \cdot \frac{\sigma}{S} \\[6pt]
&= \frac{\bar X - \mu}{S/\sqrt{n}}
\end{align}
$$

:::sum
==自由度が $n-1$ になるのは, **不偏分散**の分母 $n-1$== に対応しています.

また不偏分散を利用すると==きれいに**未知分散 $\sigma^2$** が消えて==、
推定・検定できる形になります.
:::

## 例題

### 1. 両側検定

::: expl 問題設定
外来高血圧患者の平均収縮期血圧がガイドライン基準 $\mu_0=140$ mmHg と異なるか検定する.  
標本サイズ $n=25$, 標本平均 $\bar x=134.0$ mmHg, 標本標準偏差 $s=10.0$ mmHg.  
母分散は未知, 各測定は正規分布からの独立標本と仮定する.
:::

::: expl 仮説
$H_0:\ \mu=140 \quad vs \quad H_1:\ \mu\ne140 \quad$（有意水準 $\alpha=0.05$）.
:::

::: expl 検定統計量
$$
\begin{align}
t&=\frac{\bar x-\mu_0}{s/\sqrt{n}} \\[6pt]
&=\frac{134.0-140}{10.0/\sqrt{25}} \\[6pt]
&=\frac{-6.0}{2.0} \\[6pt]
&=-3.0.
\end{align}
$$
自由度は $\nu=n-1=24$
:::

::: expl 判定
自由度24の $t$ 分布臨界値は $t_{0.975}\approx 2.064$.  
$|t|=3.0>2.064$ より $H_0$ を棄却.
:::

::: ans 結論
平均収縮期血圧は $140$ mmHg と有意に異なる（本標本では平均で低い）.
:::

### 2. 片側検定
::: expl 問題設定
糖尿病外来の集団で平均HbA1cがガイドライン基準 $\mu_0=7.0\%$ より高いかを検定する.  
標本サイズ $n=30$, 標本平均 $\bar x=7.4\%$, 標本標準偏差 $s=0.7\%$. 母分散は未知, 各測定は正規分布からの独立標本.
:::

::: expl 仮説
$H_0:\ \mu=7.0 \quad vs \quad H_1:\ \mu>7.0 \quad$（有意水準 $\alpha=0.05$）.
:::

::: expl 検定統計量
$$
t=\frac{\bar x-\mu_0}{s/\sqrt{n}}
=\frac{7.4-7.0}{0.7/\sqrt{30}}
=\frac{0.4}{0.1278}\approx 3.13,\quad \nu=n-1=29.
$$
:::

::: expl 判定
臨界値 $t_{0.95}\approx 1.699$.  
$t=3.13>1.699$ より $H_0$ を棄却
:::

::: ans 結論
平均HbA1cは $7.0\%$ より有意に高い.
:::