---
date: 2025-10-03
icon: meteor-icons:feather
category:
  - 統計数理
  - 確率分布
tag:
  - t分布
  - 確率密度関数
  - 連続型
---

# t分布の性質

<div style="display: flex; gap: 10px; justify-content: center;">
  <img src="/assets/images/probability_distribution/t/thumbnail.png" style="max-width: 100%; height: auto;">
</div>

**t分布**は ==分散が未知の場合の仮説検定でよく使用される分布== です。

t分布もしくは ==スチューデントのt分布== と言われます。

定義にある標準正規分布とカイ二乗分布との関係は必ず覚えた方がいいでしょう. (**統計検定には頻出！**)


::: def
$Z\sim\mathcal{N}(0,1)$, $W\sim\chi^2(n)$, かつ $Z\perp W$ (独立)のとき,

$$
T=\frac{Z}{\sqrt{W/n}} \sim t(n)
$$
は自由度 $n$ の $t$ 分布に従う.
ただし, $Z$ は標準正規分布, $W$ はカイ二乗分布を表す。
:::

## 1. 確率密度関数


::: def 確率密度関数 (PDF)
自由度 $n$ の $t$ 分布 $T \sim t(n)$ の確率密度関数は  
$$
f(t)=\frac{\Gamma\!\left(\frac{n+1}{2}\right)}{\sqrt{n\pi}\,\Gamma\!\left(\frac{n}{2}\right)}
\left(1+\frac{t^2}{n}\right)^{-\frac{n+1}{2}}
$$

また $n=1$　のとき,
$$
\begin{align}
f(t) &=\frac{\Gamma\!\left(1\right)}{\sqrt{\pi}\,\Gamma\!\left(\frac{1}{2}\right)}
\left(1+t^2\right)^{-1} \\[6pt]
&= \frac{1}{\pi(1+t^2)}

\end{align}
$$

これを特別に(標準) ==**コーシー分布**== という.

:::

### 確率密度関数のグラフ

<div style="display: flex; gap: 10px; justify-content: center;">
  <img src="/assets/images/probability_distribution/t/pdf.png" style="max-width: 48%; height: auto;">
  <img src="/assets/images/probability_distribution/t/pdf.gif" style="max-width: 48%; height: auto;">
</div>

:::expl
標準正規分布と非常によく似た形をしていて、自由度(degrees of freedom)が増えるにつれて

==標準正規分布と一致== するようすが確認できます.

特徴として、自由度が小さい場合, 標準正規分布より ==山が低く、裾が厚い== です.
:::


::: hint おすすめ
導出には**標準正規分布**と**カイ二乗分布**を使用します。二つの分布についてはこちらをご覧ください。
<div class="vp-card-container">
<VPCard
  title="標準正規分布の性質"
  desc="期待値・分散・導出"
  link="/posts/probability_distribution/standard_normal1.md"
/>
<VPCard
  title="カイ二乗分布の性質"
  desc="期待値・分散・導出"
  link="/posts/probability_distribution/chi.md"
/>
</div>
:::

## 2. 累積分布関数
::: def 累積分布関数 (CDF)
自由度 $n$ の $t$ 分布 $T\sim t(n)$ の累積分布関数は  
初等関数での閉じた形はなく，**正則不完全ベータ関数** $I$ で表す
(統計検定の範囲外なので紹介のみ)
$$
\begin{align}
F(t) = \int_{-\infty}^t f(u) du &=  1 - \frac{1}{2}I_{x(t)}\left(\frac{n}{2}, \frac{1}{2}\right)
\end{align}
$$
ただし $x(t) = \frac{n}{t^2+n}$
:::

**累積分布関数のグラフ**

<div style="display: flex; gap: 10px; justify-content: center;">
  <img src="/assets/images/probability_distribution/t/cdf.png" style="max-width: 48%; height: auto;">
  <img src="/assets/images/probability_distribution/t/cdf.gif" style="max-width: 48%; height: auto;">
</div>

## 3. 期待値

::: def 期待値 (Mean)
$t$ 分布 $T\sim t(n)$ の期待値は
$$
\mathbb{E}[T]=
\begin{cases}
0, & n>1,\\
\text{未定義}, & 0<n\le 1.
\end{cases}
$$
（対称性により存在すれば 0, 存在条件は $n>1$）

興味深いのは $0 < n \leq 1$ つまり ==コーシー分布のときでも期待値が定義されません。==
:::


::: details 導出の手順はこちら
::: def 導出
PDF を
$$
f(t)=C\left(1+\frac{t^2}{n}\right)^{-\frac{n+1}{2}},
\quad
C=\frac{\Gamma\!\left(\frac{n+1}{2}\right)}{\sqrt{n\pi}\,\Gamma\!\left(\frac{n}{2}\right)}
$$
とする.

対称性 $f(t)=f(-t)$ より，期待値が存在すれば $\mathbb{E}[T]=0$.

:::

## 4. 分散

::: def 分散
$t$ 分布 $T \sim t(n)$ の分散は
$$
\mathrm{V}[T]=
\begin{cases}
\dfrac{n}{\,n-2\,}, & n>2,\\[6pt]
\text{未定義（発散）}, & 1<n\le 2,\\[4pt]
\text{未定義}, & 0<n\le 1.
\end{cases}
$$
（$n\le 1$ は平均が未定義. $1<n\le 2$ は平均は 0 だが二乗積分が発散）
:::

::: details 導出の手順はこちら
::: def 導出
PDF を
$$
f(t)=C\left(1+\frac{t^2}{n}\right)^{-\frac{n+1}{2}},\quad
C=\frac{\Gamma\!\left(\frac{n+1}{2}\right)}{\sqrt{n\pi}\,\Gamma\!\left(\frac{n}{2}\right)}
$$
とする. 対称性より $n>1$ で $\mathbb{E}[X]=0$ なので $\mathrm{V}(X)=\mathbb{E}[X^2]$ を計算する.

$$
\mathbb{E}[T^2]
=2C\int_{0}^{\infty} t^2\!\left(1+\frac{t^2}{n}\right)^{-\frac{n+1}{2}} dt.
$$

$u=t^2/n$で置換すると,
- 逆変換 $t=\sqrt{nu}$
- 微分 $dt=\tfrac{\sqrt{n}}{2}u^{-1/2}du$
- 範囲 $t: 0 \to \infty, u: 0 \to \infty$
$$
\begin{align}
\mathbb{E}[T^2]
&= C n^{3/2}\!\int_{0}^{\infty} u^{1/2}(1+u)^{-\frac{n+1}{2}} du \\[6pt]
\end{align}
$$

ここで $z = \frac{u}{1+u}$ とおくと
- 逆変換 $u = \frac{z}{1-z}$
- 微分 $du = \frac{1}{(1-z)^2}dz$
- 範囲 $u: 0 \to \infty, z: 0 \to 1$
$$
\begin{align}
\mathbb{E}[T^2] 
&= C n^{3/2}\!\int_0^1 \left(\frac{z}{1-z}\right)^{\frac{1}{2}}\left(\frac{1}{1-z}\right)^{-\frac{n+1}{2}}\frac{1}{(1-z)^2}dz \\[6pt]
&= C n^{3/2}\!\int_0^1 z^{\frac{1}{2}}(1-z)^{\frac{n-4}{2}}dz \\[6pt]
&= C n^{3/2}\!\int_0^1 z^{\frac{3}{2}-1}(1-z)^{\frac{n-2}{2}-1}dz \\[6pt]
&= C n^{3/2}\mathrm{B}(\tfrac{3}{2}, \tfrac{n-2}{2})
\end{align}
$$

ただし $\mathrm{B}$ はベータ関数。


==ここから**ベータ関数とガンマ関数の性質**を使用するときれいに約分できます。==

- $\mathrm{B}(x, y) = \frac{\Gamma(x)\Gamma(y)}{\Gamma(x+y)}$
- $\Gamma(x+1) = x\Gamma(x)$

さて $C$ も代入して丁寧に整理していきましょう。

$$
\begin{align}
\mathbb{E}[T^2] 
&= \frac{\Gamma\!\left(\frac{n+1}{2}\right)}{\sqrt{n\pi}\,\Gamma\!\left(\frac{n}{2}\right)}\,
    n\sqrt{n}\,\mathrm{B}\!\left(\tfrac{3}{2}, \tfrac{n-2}{2}\right) \\[6pt]
&= \frac{n}{\sqrt{\pi}}\frac{\Gamma\!\left(\frac{n+1}{2}\right)}{\Gamma\!\left(\frac{n}{2}\right)}
    \,\mathrm{B}\!\left(\tfrac{3}{2}, \tfrac{n-2}{2}\right) \\[6pt]
&= \frac{n}{\sqrt{\pi}}\frac{\Gamma\!\left(\frac{n+1}{2}\right)}{\Gamma\!\left(\frac{n}{2}\right)}
   \frac{\Gamma\!\left(\frac{3}{2}\right)\Gamma\!\left(\frac{n-2}{2}\right)}{\Gamma\!\left(\frac{n+1}{2}\right)} \\[6pt]
&= \frac{n}{\sqrt{\pi}} \cdot \frac{\Gamma\!\left(\frac{3}{2}\right)\Gamma\!\left(\frac{n-2}{2}\right)}{\Gamma\!\left(\frac{n}{2}\right)} \\[6pt]
&= \frac{n}{\sqrt{\pi}} \cdot \frac{\tfrac{\sqrt{\pi}}{2}\,\Gamma\!\left(\tfrac{n-2}{2}\right)}{\Gamma\!\left(\tfrac{n}{2}\right)} \\[6pt]
&= \frac{n}{2}\cdot \frac{\Gamma\!\left(\tfrac{n-2}{2}\right)}{\Gamma\!\left(\tfrac{n}{2}\right)}\\[6pt]
&= \frac{n}{2}\cdot \frac{\Gamma\!\left(\tfrac{n-2}{2}\right)}{\Gamma\!\left(\tfrac{n}{2}-1 + 1\right)}\\[6pt]
&= \frac{n}{2}\cdot \frac{\Gamma\!\left(\tfrac{n-2}{2}\right)}{\tfrac{n-2}{2}\Gamma\!\left(\tfrac{n-2}{2}\right)}\\[6pt]
&= \frac{n}{2}\cdot \frac{1}{\tfrac{n-2}{2}} \\[6pt]
&= \frac{n}{n-2}\,.
\end{align}
$$

したがって,

$$
\mathbb{E}[T^2]=\frac{n}{n-2}\quad (n>2).
$$
ゆえに $n>2$ で $\mathrm{V}[T]=\dfrac{n}{n-2}$. 一方 $1<n\le2$ はベータ積分が発散し分散は未定義. $n\le1$ は平均も未定義.

:::