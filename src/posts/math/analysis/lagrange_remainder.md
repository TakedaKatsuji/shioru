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
:::info 複数回微分表記
$f$ の $n$ 回微分を $f^{(n)}$ と表記しています
:::

<br>

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
### マクローリン展開
$f$ を区間 $[0, x]$ で $n+1$ 回連続微分可能であるとき,
$f$をマクローリン展開すると,
$$
\begin{align}
f(x) &= \sum^{\infty}_{k=0}\frac{f^{(k)}(0)}{k!}x^k \\[6pt]
\end{align}
$$
ここで
$$
\begin{align}
P_n(x) &:= \sum^{n}_{k=0}\frac{f^{(k)}(0)}{k!}x^k \\[6pt]
R_n(x) &:= f(x) - P_n(x)
\end{align}
$$
とする.

---
### 補助関数
これ以降便宜上 $x$ を $c_0$ で書く.

ここで補助関数 $g(t)$を定数 $A$ を用いて, $g(c_0) = 0$ となるように定義する.
$$
\begin{align}
g(t) = f(t) - P_n(t) - At^{n+1}
\end{align}
$$
$g(c_0) = 0$より,
$$
\begin{align}
g(c_0) &= f(c_0) - P_n(c_0) - Ac_0^{n+1} = 0 \\[6pt]
A &= \frac{f(c_0) - P_n(c_0)}{c_0^{n+1}}
\end{align}
$$
したがって,
$$
\begin{align}
g(t) = f(t) - P_n(t) - \frac{f(c_0) - P_n(c_0)}{c_0^{n+1}}t^{n+1}
\end{align}
$$

また $f(0) = P_n(0)$ より $g(0)=0$, したがって $g(t)$ は区間 $[0,c_0]$ に対して,
$$
\begin{align}
g(0) &= 0, \quad g(c_0) = 0  
\end{align}
$$

---

### ロルの定理

$f^{(n)}(0) = P_n^{(n)}(0)$ より常に $g^{(n)}(0)=0$

$g(t)$ の $1$ 階微分 $g^{(1)}(t)$ は,
$$
\begin{align}
g^{(1)}(t) = f^{(1)}(t) - P_n^{(1)}(t) - \frac{n+1}{c_0^{n+1}}(f(c_0)-P_n(c_0))t^n
\end{align}
$$
とかける.

ロルの定理より $\exists\,c_1 \in (0,c_0), \quad g^{(1)}(c_1)=0$

したがって $g^{(1)}(t)$ は区間 $[0,c_1]$ に対して,
$$
\begin{align}
g^{(1)}(0) &= 0, \quad g^{(1)}(c_1) = 0
\end{align}
$$

これを $g^{(n+1)}$ まで繰り返す. 簡潔に表にすると,

|関数|区間|ロルの定理|$c_j$ の範囲|
|:---:|:---:|:---:|:---:|
|$g^{(1)}(t)$|$[0,c_0]$|$g^{(1)}(c_1)=0$|$0<c_1<c_0$|
|$g^{(2)}(t)$|$[0,c_1]$|$g^{(2)}(c_2)=0$|$0<c_2<c_1$|
|$\vdots$|$\vdots$|$\vdots$|$\vdots$|
|$g^{(n)}(t)$|$[0,c_{n-1}]$|$g^{(n)}(c_n)=0$|$0<c_n<c_{n-1}$|
|$g^{(n+1)}(t)$|$[0,c_{n}]$|$g^{(n+1)}(c_{n+1})=0$|$0<c_{n+1}<c_n$|

読み方は, ==**[関数]**== は ==**[区間]**== に ==**[ロルの定理]**== を満たす $c_j$ が ==**[ $c_j$ の範囲]**== に存在する

$c_{n+1}$ は $0<c_{n+1}<c_n<\cdots<c_0=x$ より $0<c_{n+1}<x$
$c_{n+1}=\xi, \, c_0 = x$ とする.
$$
\begin{align}
g^{(n+1)}(\xi) &= f^{(n+1)}(\xi) -  P_n^{(n+1)}(\xi) - \frac{(n+1)!}{x^{n+1}}(f(x)-P_n(x))
\end{align}
$$
ここで $P_n(t)$ は $n$ 次多項式より $P^{(n+1)}_n(t)=0$

また $R_n(x) = f(x) - P_n(x)$ より
$$
\begin{align}
g^{(n+1)}(\xi) &= f^{(n+1)}(\xi) - \frac{(n+1)!}{x^{n+1}}R_n(x) = 0\\
R_n(x) &= \frac{f^{(n+1)}(\xi)}{(n+1)!}x^{n+1}
\end{align}
$$

これで証明終了.
:::

## 参考文献
<AffiliateBook id="official1"/>
<AffiliateBook id="takemura_gen_stats"/>
<AffiliateBook id="fullscalemath"/>