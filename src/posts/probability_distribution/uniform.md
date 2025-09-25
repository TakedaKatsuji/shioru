---
date: 2025-09-16
icon: meteor-icons:feather
category:
  - 統計数理
  - 確率分布
tag:
  - 一様分布
  - 確率密度関数
  - 連続型
---

# 一様分布の性質

連続一様分布の重要な性質を解説します.

## 1. 確率密度関数

::: def 確率密度関数 (PDF)
区間 $[a,b]$ の一様分布の確率密度関数は次の通り：
$$
f(x) =
\begin{cases}
\dfrac{1}{b-a}, & a \le x \le b, \\
0, & \text{otherwise}.
\end{cases}
$$
:::

**確率密関数のグラフ**

<div style="display: flex; gap: 10px; justify-content: center;">
  <img src="/assets/images/probability_distribution/uniform/pdf.png" style="max-width: 48%; height: auto;">
  <img src="/assets/images/probability_distribution/uniform/pdf.gif" style="max-width: 48%; height: auto;">
</div>

## 2. 累積分布関数
::: def 累積分布関数 (CDF)
$$
F(x) =
\begin{cases}
0, & x < a, \\
\dfrac{x-a}{b-a}, & a \le x \le b, \\
1, & x > b.
\end{cases}
$$
:::

**累積分布関数のグラフ**
<div style="display: flex; gap: 10px; justify-content: center;">
  <img src="/assets/images/probability_distribution/uniform/cdf.png" style="max-width: 70%; height: auto;">
</div>

::: details **導出の手順はこちら**
::: calc 導出
累積分布関数は

$$
F(x) = P(X \leq x) = \int_{-\infty}^x f(t)\,dt
$$

で定義される. 区間 $[a,b]$ の一様分布について場合分けすると：

1. **$x < a$ のとき**

$$
F(x) = \int_{-\infty}^x f(t)\,dt = 0
$$

2. **$a \leq x \leq b$ のとき**

$$
\begin{align}
F(x) &= \int_a^x \frac{1}{b-a}\,dt \\[6pt]
&= \frac{x-a}{b-a}
\end{align}
$$

3. **$x > b$ のとき**

$$
F(x) = \int_{-\infty}^x f(t)\,dt = 1
$$

**結果**
$$
F(x) =
\begin{cases}
0, & x < a, \\
\dfrac{x-a}{b-a}, & a \le x \le b, \\
1, & x > b.
\end{cases}
$$
:::

## 3. 期待値
::: def 期待値
$$
\mathbb{E}[X] = \frac{a+b}{2}
$$

期待値は==区間の中点==を表しています.
:::

::: details 導出の手順はこちら
::: calc 導出
確率変数 $X \sim \mathrm{Uniform}(a,b)$ の場合，

$$
\mathbb{E}[X] = \int_a^b x \cdot f(x)\,dx
= \int_a^b x \cdot \frac{1}{b-a}\,dx
$$

積分すると，

$$
\mathbb{E}[X] = \frac{1}{b-a}\left[\frac{x^2}{2}\right]_a^b
= \frac{1}{b-a}\cdot \frac{b^2-a^2}{2}
= \frac{a+b}{2}.
$$
:::


## 4. 分散
::: def 分散
$$
\mathrm{Var}[X] = \frac{(b-a)^2}{12}
$$
:::

::: details 導出の手順はこちら
::: calc 導出
確率変数 $X \sim \mathrm{Uniform}(a,b)$ の場合，

$X^2$の期待値$\mathbb{E}[X^2]$は
$$
\begin{align}
\mathbb{E}[X^2] &= \int_a^b \frac{x^2}{b-a}\,dx \\[6pt]
&= \frac{1}{b-a}\left[\frac{x^3}{3}\right]_a^b \\[6pt]
&= \frac{b^3 - a^3}{3(b-a)} \\[6pt]
&= \frac{b^2 + ab + a^2}{3}
\end{align}
$$

したがって，

$$
\begin{align}
\mathrm{Var}[X] &= \mathbb{E}[X^2] - \mathbb{E}[X]^2 \\[6pt]
&= \frac{b^2 + ab + a^2}{3} - \frac{(b+a)^2}{4}\\[6pt]
&= \frac{(b-a)^2}{12}\\[6pt]
\end{align}
$$
:::



## 5. 積率母関数
::: def 積率母関数 (MGF)
$$
M_X(t) =
\begin{cases}
\dfrac{e^{bt} - e^{at}}{(b-a)t}, & t \ne 0, \\
1, & t = 0.
\end{cases}
$$
:::

::: details 導出の手順はこちら
::: calc 導出

積率母関数は

$$
M_X(t) = \mathbb{E}[e^{tX}] = \int_a^b e^{tx}\,\frac{1}{b-a}\,dx
$$

1. $t \ne 0$ の場合：

$$
M_X(t) = \frac{1}{b-a}\int_a^b e^{tx}\,dx
= \frac{1}{b-a}\left[\frac{1}{t}e^{tx}\right]_a^b
= \frac{e^{bt} - e^{at}}{(b-a)t}.
$$

2. $t = 0$ の場合：

$$
M_X(0) = \mathbb{E}[1] = 1.
$$
:::


## 6. 特性関数
::: def 特性関数 (CF)
$$
\varphi_X(t) =
\begin{cases}
\dfrac{e^{i b t} - e^{i a t}}{(b-a) i t}, & t \ne 0, \\
1, & t = 0.
\end{cases}
$$
:::

::: details 導出の手順はこちら
::: calc 導出
特性関数は

$$
\varphi_X(t) = \mathbb{E}[e^{itX}] 
= \int_a^b e^{itx}\,\frac{1}{b-a}\,dx
$$

1. $t \ne 0$ の場合：

$$
\varphi_X(t) 
= \frac{1}{b-a}\int_a^b e^{itx}\,dx
= \frac{1}{b-a}\left[\frac{1}{it}e^{itx}\right]_a^b
= \frac{e^{ibt} - e^{iat}}{(b-a)it}.
$$

2. $t = 0$ の場合：

$$
\varphi_X(0) = \mathbb{E}[1] = 1.
$$
:::