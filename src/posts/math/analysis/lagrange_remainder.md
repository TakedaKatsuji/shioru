---
date: 2025-10-30
icon: meteor-icons:feather
category:
  - 解析学
tag:
  - マクローリン展開
  - テイラー展開
  - ラグランジュの剰余項
cover: "/assets/images/math/analysis/lagrange_remainder/thumbnail.png"
---

<!-- more -->

# ラグランジュの剰余項
## ラグランジュの剰余項の定義
:::expl
統計学で行われる近似手法ではマクローリン展開・テイラー展開後に $n+1$ 次以降を ==**剰余項**== で書くことがあります.
$n+1$ 次以降を ==**剰余項**== といい,　この記事ではそのなかでも ==**ラグランジュの剰余項**== を紹介します.

$$
\begin{align}
f(x) &= \sum_{k=0}^{\infty} \frac{f^{(k)}(0)}{k!}x^k \\[6pt]
&= \sum_{k=0}^n \frac{f^{(k)}(0)}{k!}x^k + \sum_{k=n+1}^{\infty} \frac{f^{(k)}(0)}{k!}x^k \\[6pt]
&= P_n(x) + R_n(x) \\[6pt]
\end{align}
$$
$R_n(x)$ を剰余項という.
==**$P_n(x)$ は $f(x)$ の近似式, $R_n(x)$ はその誤差として考えるとわかりやすいです.**==

:::

:::def ラグランジュの剰余項の定義
$f$ は区間 $[0, x]$ で $n+1$ 回連続微分可能とする.
$$
\begin{align}
P_n(x) &= \sum_{k=0}^n \frac{f^{(k)}(0)}{k!}x^k \\[6pt]
R_n(x)&= f(x) - P_n(x) \\[6pt]
\end{align}
$$

$\exists\,\xi \in (0, x)$ のとき,
$$
\begin{align}
R_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!}x^{n+1}
\end{align}
$$

$R_n(x)$ を ==**ラグランジュの剰余項**== という.
:::

## オーダー表記とラグランジュの剰余項

:::expl
ラグランジュの剰余項は
$$
R_n(x)=\frac{f^{(n+1)}(\xi)}{(n+1)!}\,x^{n+1}, \qquad \xi\in(0,x)
$$
と表される.

このとき $|f^{(n+1)}(\xi)|$ が有界なら
$$
|R_n(x)| \le \frac{M}{(n+1)!}\,|x|^{n+1}
$$
が成り立ち,
$$
R_n(x)=O(|x|^{n+1})
$$
と書ける.

つまり ==**$x$ が $0$ に近づくとき, 誤差 $R_n(x)$ は $|x|^{n+1}$ に定数倍かけた程度以下**== になるということです.

:::

## ラグランジュの剰余項の証明
:::proof
執筆中...
:::

## 参考文献
<AffiliateBook id="official1"/>
<AffiliateBook id="takemura_gen_stats"/>
<AffiliateBook id="fullscalemath"/>