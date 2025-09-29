---
icon: meteor-icons:file-lines
date: 2025-09-29
category:
  - 統計検定1級
  - 統計数理
  - 検定
tag:
  - 検定
  - 正規近似
  - 連続修正
---

## 半整数補正

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
- Exact(正確確率)
- Non CC(正規近似・半整数補正なし)
- CC（正規近似・半整数補正あり）
の3種類値を比較していきます.
:::

<執筆中...>
