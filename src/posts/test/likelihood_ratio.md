---
icon: meteor-icons:file-lines
date: 2025-09-30
category:
  - 統計検定1級
  - 統計数理
  - 仮説検定
tag:
  - 尤度比検定
  - カイ二乗分布
  - 尤度比
  - 最尤推定量
cover: "/assets/images/test/likelihood_ratio/thumbnail.png" 
---

<!-- more -->

# 尤度比検定について徹底解説

## 尤度比検定の定義と内容

==**尤度比検定は統計検定1級で頻出の仮説検定手法です.**==

尤度比統計量が従う確率分布や検定方法について一つずつ整理していきましょう.


:::def 尤度比統計量
観測 $x$, パラメータ空間 $\Theta$

- 帰無仮説 $H_0:\theta\in\Theta_0\subset\Theta$
- 対立仮説 $H_1:\theta\in\Theta_1 = \Theta_0 \backslash \Theta$

尤度関数 $L(\theta)=f(x\mid\theta)$ に対し，
$$
\begin{align}
\Lambda &= \frac{\sup_{\theta\in\Theta_0} L(\theta)}{\sup_{\theta\in\Theta} L(\theta)} \\[6pt]
D &\equiv-2\log\Lambda
\end{align}
$$

**Wilksの定理**（漸近）より標本数が十分大きいとき

$$
D\ \xrightarrow{d}\ \chi^2(n),\qquad n=\dim(\Theta)-\dim(\Theta_0).
$$
:::

### 尤度比の分子と分母の意味
- **分子** $\sup_{\theta\in\Theta_0} L(\theta)$：制約下（$H_0$）での最大尤度  
- **分母** $\sup_{\theta\in\Theta} L(\theta)$：制約なし（フルモデル）での最大尤度

==**制約なしの最大尤度に対して，制約下の最大尤度の相対的な大きさを測る**== のが尤度比.
<br>

:::expl 尤度比の範囲
$\Theta_0\subset\Theta$ のとき $\sup_{\theta \in \Theta_0}L(\theta)\le \sup_{\theta \in \Theta}L(\theta)$ なので

$$
0<\Lambda\le 1,\qquad D=-2\log\Lambda\ge 0.
$$

==**$\Lambda$ が小さい $\Rightarrow$ $D$ が大きい $\Rightarrow$ 上側確率が小さくなる $\Rightarrow$ $H_0$を棄却しやすい**==
<div style="display: flex; gap: 10px; justify-content: center;">
  <img src="/assets/images/test/likelihood_ratio/pdf_with_D.png" style="max-width: 100%; height: auto;">
</div>
:::

## 例題 過去問2013年統計数理[5]の類題
<AffiliateBook id="kakomon1213"/>

:::expl 問題
離散型確率変数 $\{X_i\}_{i=1}^4$ は $\sum_{i=1}^4 X_i = 200$ であり，パラメータ $\boldsymbol{\theta}=(\theta_1,\theta_2,\theta_3,\theta_4)$ の多項分布に従うとする．  
観測度数は $(x_1,x_2,x_3,x_4)=(52,41,63,44)$ とする．

帰無仮説と対立仮説を
$$
\begin{align}
H_0&:\ \boldsymbol{\theta_0}=\left(\theta_{01}, \theta_{02}, \theta_{03},\theta_{04}\right) \quad \theta_{0i} = \tfrac{1}{4},\\[6pt]
H_1&:\ \boldsymbol{\theta}\neq\boldsymbol{\theta_0}
\end{align}
$$
とおく．有意水準 $5\%$ での棄却可否を答えよ．
:::

:::hint
==**尤度比検定の手順**==
1. 帰無仮説下の尤度を求める $L(\theta\mid H_0)$
2. 対立仮説下の最大尤度を求める（最尤推定量の尤度） $L(\hat\theta\mid H_1)$
3. 自由度を求める $n=\dim(\Theta)-\dim(\Theta_0)$
4. 尤度比検定統計量 $D=-2\log\Lambda=-2\log\!\left(\dfrac{L(\theta\mid H_0)}{L(\hat\theta\mid H_1)}\right)$ を計算
5. 漸近分布を用いる: $D\ \overset{H_0}{\sim}\ \chi^2(n)$
6. 有意水準 $\alpha$ で判定: $D>\chi^2_{1-\alpha}(n)$ なら $H_0$ を棄却, それ以外は棄却しない
:::


:::ans
手順にしたがって解説していきます.

1. **帰無仮説下の尤度**

多項分布の確率質量関数は
$$
\begin{align}
f(\boldsymbol{x}\mid\boldsymbol{\theta})
&=\frac{n!}{x_1!\,x_2!\,x_3!\,x_4!}\,
\theta_1^{x_1}\theta_2^{x_2}\theta_3^{x_3}\theta_4^{x_4},\qquad
\sum_{i=1}^4 \theta_i=1
\end{align}
$$

帰無仮説下 ($\theta_{0i}=1/4$) の尤度は
$$
\begin{align}
L(\boldsymbol{\theta_0})
= f(\boldsymbol{x}\mid\boldsymbol{\theta_0})
= \frac{n!}{x_1!\,x_2!\,x_3!\,x_4!}\prod_{i=1}^4 \left(\tfrac14\right)^{x_i}.
\end{align}
$$

2. **対立仮説下の最大尤度**

多項分布の最尤推定量は $\hat\theta_i=x_i/n$. よって

<div class="vp-card-container">

<VPCard
  title="多項分布の最尤推定量"
  desc="最尤推定量・オイラーラグランジュの未定乗数法"
  link="/posts/probability_distribution/multinomial_likelihood.md"
/>
</div>

$$
\begin{align}
L(\hat{\boldsymbol{\theta}})
= \frac{n!}{x_1!\,x_2!\,x_3!\,x_4!}\prod_{i=1}^4 \left(\frac{x_i}{n}\right)^{x_i}.
\end{align}
$$

3. **自由度**

制約なしの $\Theta$ は次元 $3$（総和 $1$ の制約で $4-1$）. 帰無仮説下は点仮説で次元 $0$. よって
$$
n=\dim(\Theta)-\dim(\Theta_0)=3.
$$

4. **尤度比と検定統計量**

両者の比で多項係数が相殺される:
$$
\begin{align}
\Lambda
&=\frac{L(\boldsymbol{\theta_0})}{L(\hat{\boldsymbol{\theta}})}
=\prod_{i=1}^4
\left(\frac{\tfrac14}{x_i/n}\right)^{x_i}
=\prod_{i=1}^4
\left(\frac{n\,\theta_{0i}}{x_i}\right)^{x_i}.
\end{align}
$$

$$
\begin{align}
D
&=-2\log\Lambda
=2\sum_{i=1}^4 x_i \log\!\left(\frac{x_i}{n\theta_{0i}}\right).
\end{align}
$$

本データでは $n=200,\ \boldsymbol{x}=(52,41,63,44),\ n\theta_{0i}=50$ より
$$
\begin{align}
D
&=2\Big[
52\log\!\left(\tfrac{52}{50}\right)
+41\log\!\left(\tfrac{41}{50}\right)
+63\log\!\left(\tfrac{63}{50}\right)
+44\log\!\left(\tfrac{44}{50}\right)
\Big] \\[4pt]
&\approx 5.677.
\end{align}
$$

5. **漸近分布と $p$ 値**

Wilks の定理より $D\ \overset{H_0}{\sim}\ \chi^2(3)$（大標本近似）

6. **判定（有意水準 $5\%$）**

臨界値は $\chi^2_{0.95}(3)=7.81$. $D=5.677<7.81$ より

> **結論:** $H_0$ は棄却しない.
:::

## 参考文献

<AffiliateBook id="official1"/>
<AffiliateBook id="takemura_gen_stats"/>
