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
---

# 尤度比検定について徹底解説

<div style="display: flex; gap: 10px; justify-content: center;">
  <img src="/assets/images/test/likelihood_ratio/thumbnail.png" style="max-width: 100%; height: auto;">
</div>

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

:::expl 尤度比の範囲
$\Theta_0\subset\Theta$ のとき $\sup_{\theta \in \Theta_0}L(\theta)\le \sup_{\theta \in \Theta}L(\theta)$ なので

$$
0<\Lambda\le 1,\qquad D=-2\log\Lambda\ge 0.
$$

$\Lambda$ が小さいほど $D$ は大きく，$D\sim\chi^2(n)$より，上側確率が小さくなり $H_0$ を棄却しやすい.
:::

執筆中...

## 参考文献
- [現代数理統計学](https://amzn.to/46UzNM9)
- [現代数理統計学の基礎](https://amzn.to/3W6W3ME)
- [統計検定準1級対応 統計学実践ワークブック](https://amzn.to/46QExlU)