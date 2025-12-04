---
date: 2025-12-03
icon: meteor-icons:feather
category:
  - 統計数理
  - 確率分布
tag:
  - 尤度関数
  - スコア関数
  - 確率密度関数
cover: "/assets/images/probability_distribution/fisher/thumbnail.png"
---

<!-- more -->

# スコア関数
スコア関数は対数尤度関数の微分で定義されます.
:::def
確率変数 $X = (X_1, \dots, X_n)$ の同時確率密度関数を $f(x|\theta)$ とする.
また $\theta$ は一次元のパラメータとします.

- 尤度関数を $L_n(\theta|x) = f(x|\theta)$
- 対数尤度関数 $l(\theta|x) = \log{L_n(\theta|x)} = \log{f(x|\theta)}$

スコア関数 $S(\theta, x)$ は
$$
\begin{align}
S_n(\theta, x) := \frac{\partial}{\partial \theta} \log{f(x|\theta)}
\end{align}
$$
で定義される.
:::

==**スコア関数は対数尤度関数の勾配(傾き)**== を表しています.
スコア関数は対数尤度の傾きを表すので、
- $S_n(\theta, x)>0$ → $\theta$ を増加させれば対数尤度増加
- $S_n(\theta, x)<0$ → $\theta$ を減少させれば対数尤度増加

<div style="display: flex; gap: 10px; justify-content: center;">
  <img src="/assets/images/probability_distribution/score/score.png" style="max-width: 100%; height: auto;">
</div>

##  スコア関数の期待値

:::expl
微分積分が交換可能（正則条件）のもとで
$$
\begin{align}
\mathbb{E}[S_n(\theta, x)] = 0
\end{align}
$$
:::

:::proof

$$
\begin{align}
\mathbb{E}[S_n(\theta, x)] &= \mathbb{E}[\tfrac{\partial}{\partial \theta}\log{f(x|\theta)}] \\[6pt]
&= \int_x f(x|\theta) \frac{\partial}{\partial \theta} \log{f(x|\theta)} \, dx \\[6pt]
&= \int_x f(x|\theta) \frac{1}{f(x|\theta)} \frac{\partial}{\partial \theta} f(x|\theta) \, dx \\[6pt]
&= \int_x \frac{\partial}{\partial \theta} f(x|\theta) \, dx \\[6pt]
&= \frac{\partial}{\partial \theta}\int_x  f(x|\theta) \, dx \\[6pt]
&= \frac{\partial}{\partial \theta} \cdot 1\\[6pt]
&= 0
\end{align}
$$
:::