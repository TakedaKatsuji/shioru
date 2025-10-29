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

**確率密度関数のグラフ**

<div style="display: flex; gap: 10px; justify-content: center;">
  <img src="/assets/images/probability_distribution/chi2/chi2.png" style="max-width: 48%; height: auto;">
  <img src="/assets/images/probability_distribution/chi2/chi2.gif" style="max-width: 48%; height: auto;">
</div>

カイ二乗分布の確率密度関数は定義域が0以上で ==自由度が大きくなるにつれて山が右にシフト== していきます.


==確率密度関数の導出には2種類あります.==
- 標準正規分布の二乗和の定義から導出
- ガンマ分布の再生性から導出

両方ともなかなか歯ごたえのある導出になるので別記事で紹介することとします.


## 2. 累積分布関数
:::def
累積分布関数は不完全ガンマ関数(ガンマ積分の不定積分)で表します.

第１種不完全ガンマ関数 $\gamma(a, x)$
$$
\begin{align}
\gamma(a, x) = \int_0^x t^{a-1}e^{-t}dt
\end{align}
$$
を用いて.
$$
\begin{align}
F(x) &= \frac{\gamma(\frac{n}{2}, \frac{x}{2})}{\Gamma(\frac{n}{2})}
\end{align}
$$
と表せる.
:::

::: details 導出の手順はこちら
::: def 導出
$$
\begin{align}
f(u) &= \frac{1}{2^{n/2}\Gamma(\frac{n}{2})}u^{\tfrac{n}{2}-1}e^{-\tfrac{u}{2}} \\[6pt]
F(x) &= \int_0^x f(u)\,du \\[6pt]
&= \frac{1}{2^{n/2}\Gamma(\frac{n}{2})}
\int_0^x u^{\tfrac{n}{2}-1}e^{-\tfrac{u}{2}}\, du
\end{align}
$$

$u = 2t$ で置換積分を行う.

$$
\begin{align}
F(x) &= \frac{1}{2^{n/2}\Gamma(\frac{n}{2})}
\int_0^{x/2} (2t)^{\tfrac{n}{2}-1}e^{-t}2\,dt \\[6pt]
&= \frac{\gamma(\frac{n}{2}, \frac{x}{2})}{\Gamma(\frac{n}{2})}
\end{align}
$$
:::

## 3. 期待値
::: def 期待値
$$
\mathbb{E}[X] = n
$$
:::

::: details 導出の手順はこちら
::: def 導出
自由度 $n$ のカイ二乗分布 $X \sim \chi^2(n)$ の密度は
$$
f(x)=\frac{1}{2^{n/2}\Gamma\!\left(\tfrac{n}{2}\right)}\,x^{\tfrac{n}{2}-1}e^{-x/2}\quad(x>0)
$$
であるから，
$$
\begin{align}
\mathbb{E}[X]
&=\int_0^\infty x f(x)\,dx \\[6pt]
&=\frac{1}{2^{n/2}\Gamma\!\left(\tfrac{n}{2}\right)}
\int_0^\infty x^{\tfrac{n}{2}} e^{-x/2}\,dx
\end{align}
$$

ここで $x=2t$ とおくと $dx=2\,dt$，
$$
\begin{align}
\mathbb{E}[X]
&=\frac{1}{2^{n/2}\Gamma\!\left(\tfrac{n}{2}\right)}
\int_0^\infty (2t)^{\tfrac{n}{2}} e^{-t}\,2\,dt \\[6pt]
&=\frac{2^{\tfrac{n}{2}+1}}{2^{n/2}\Gamma\!\left(\tfrac{n}{2}\right)}
\int_0^\infty t^{\tfrac{n}{2}} e^{-t}\,dt \\[6pt]
&=\frac{2\,\Gamma\!\left(\tfrac{n}{2}+1\right)}{\Gamma\!\left(\tfrac{n}{2}\right)}
=2\cdot \frac{n}{2}=n
\end{align}
$$
:::

::: info 別視点（ガンマ分布）
$\chi^2(n)$ は $\mathrm{Gamma}(\alpha=\tfrac{n}{2},\,\theta=2)$ に等価であり，ガンマ分布の期待値 $\mathbb{E}[X]=\alpha\theta$ からも $n$ が得られる.
:::


## 4. 分散
::: def 分散
$$
\mathrm{V}[X] = 2n
$$
:::

::: details 導出の手順はこちら
::: def 導出
自由度 $n$ のカイ二乗分布 $X \sim \chi^2(n)$ の密度
$$
f(x)=\frac{1}{2^{n/2}\Gamma\!\left(\tfrac{n}{2}\right)}x^{\tfrac{n}{2}-1}e^{-x/2}\quad(x>0)
$$
より
$$
\mathbb{E}[X^2]
=\frac{1}{2^{n/2}\Gamma\!\left(\tfrac{n}{2}\right)}
\int_{0}^{\infty} x^{\tfrac{n}{2}+1} e^{-x/2}\,dx.
$$

$x=2t$ とおくと $dx=2\,dt$ だから
$$
\begin{align}
\mathbb{E}[X^2]
&=\frac{1}{2^{n/2}\Gamma\!\left(\tfrac{n}{2}\right)}
\int_{0}^{\infty} (2t)^{\tfrac{n}{2}+1} e^{-t}\,2\,dt \\[4pt]
&=\frac{2^{\tfrac{n}{2}+2}}{2^{n/2}\Gamma\!\left(\tfrac{n}{2}\right)}
\int_{0}^{\infty} t^{\tfrac{n}{2}+1} e^{-t}\,dt \\[4pt]
&=\frac{4\,\Gamma\!\left(\tfrac{n}{2}+2\right)}{\Gamma\!\left(\tfrac{n}{2}\right)}
=4\left(\tfrac{n}{2}+1\right)\tfrac{n}{2}
=n(n+2).
\end{align}
$$

よって
$$
\mathrm{V}[X]
=\mathbb{E}[X^2]-\{\mathbb{E}[X]\}^2
=n(n+2)-n^2
=2n.
$$
:::

::: info 別視点（ガンマ分布）
$\chi^2(n)\equiv \mathrm{Gamma}(\alpha=\tfrac{n}{2},\theta=2)$ なので $\mathrm{V}[X]=\alpha\theta^2=(\tfrac{n}{2})\cdot 4=2n$ でも得られる.
:::

## 5. 積率母関数
::: def 積率母関数
$$
M_X(t)=(1-2t)^{-\tfrac{n}{2}}\quad(t<\tfrac{1}{2})
$$
:::

::: details 導出の手順はこちら
::: def 導出
自由度 $n$ のカイ二乗分布 $X\sim\chi^2(n)$ の密度
$$
f(x)=\frac{1}{2^{n/2}\Gamma\!\left(\tfrac{n}{2}\right)}x^{\tfrac{n}{2}-1}e^{-x/2}\quad(x>0)
$$
から
$$
\begin{align}
M_X(t)
&=\int_0^\infty e^{tx}f(x)\,dx \\[6pt]
&=\frac{1}{2^{n/2}\Gamma(\tfrac{n}{2})}\int_0^\infty x^{\tfrac{n}{2}-1}e^{-(\tfrac{1}{2}-t)x}\,dx \\[6pt]
\end{align}
$$

置換 $u=(1-2t)x\ \ (t<\tfrac12)$ を用いると，$x=\dfrac{u}{1-2t},\ dx=\dfrac{du}{1-2t}$ なので
$$
\begin{align}
M_X(t)
&=\frac{1}{2^{n/2}\Gamma(\tfrac{n}{2})}
\int_0^\infty \Big(\frac{u}{1-2t}\Big)^{\tfrac{n}{2}-1}
e^{-u/2}\,\frac{du}{1-2t}\\[6pt]
&=\frac{1}{(1-2t)^{n/2}}\cdot
\frac{1}{2^{n/2}\Gamma(\tfrac{n}{2})}
\int_0^\infty u^{\tfrac{n}{2}-1}e^{-u/2}\,du\\[6pt]
&= \frac{1}{(1-2t)^{n/2}}\cdot
\frac{1}{2^{n/2}\Gamma(\tfrac{n}{2})}\,2^{n/2}\Gamma\!\Big(\tfrac{n}{2}\Big)\\[6pt]
&=(1-2t)^{-n/2}.
\end{align}
$$

ゆえに
$$
M_X(t)=(1-2t)^{-\tfrac{n}{2}}\quad (t<\tfrac12).
$$
:::

::: info チェック（平均と分散）
$$
M_X'(0)=n,\qquad M_X''(0)-\{M_X'(0)\}^2=2n.
$$
:::

## 6. 再生性

:::def
再生性は積率母関数を使うと簡単に証明できます.
確率変数 $X, Y$は独立に自由度 $n, m$ のカイ二乗分布に従うとき,
$$
\begin{align}
X \sim \chi2(n)\quad, Y \sim \chi2(m)
\end{align}
$$

$Z = X + Y$, それぞれの積率母関数 $M_X(t), M_Y(t), M_Z(t)$ として
積率母関数の性質より $X,Y$ が独立のとき
$$
\begin{align}
M_Z(t) &= M_X(t) \cdot M_Y(t) \\[6pt]
&= \left(1-2t\right)^{-\frac{n}{2}} \cdot \left(1-2t\right)^{-\frac{m}{2}} \\[6pt]
&= \left(1-2t\right)^{-\frac{n+m}{2}}
\end{align}
$$ 

これは自由度 $n+m$ のカイ二乗分布の積率母関数であり, ==積率母関数の一意性から==,
$$
\begin{align}
Z \sim \chi2(n+m)
\end{align}
$$
同様に $m$ 個の独立な $\chi2(k_i)$ の和も $\chi2\!\left(\sum_{i=1}^m k_i\right)$ に従う.
:::

