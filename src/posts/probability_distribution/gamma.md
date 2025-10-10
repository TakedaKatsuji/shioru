---
date: 2025-10-10
icon: meteor-icons:feather
category:
  - 統計数理
  - 確率分布
tag:
  - ガンマ分布
  - ヤコビアン
  - 確率密度関数
  - 連続型
  - ベータ関数
  - ガンマ関数
---

# ガンマ二乗分布の性質

<div style="display: flex; gap: 10px; justify-content: center;">
  <img src="/assets/images/probability_distribution/gamma/thumbnail.png" style="max-width: 100%; height: auto;">
</div>

::: expl
==ガンマ分布は**指数分布の和**で定義されます。==

独立同分布な待ち時間 $T_i\sim \mathrm{Exp}(\lambda)$（率 $\lambda>0$）とする. 尺度は $\theta=1/\lambda$.

このとき，和
$$
\begin{align}
T_k &= \sum_{i=1}^k T_i \sim \mathrm{Gamma}(k,\ \theta=1/\lambda)
\end{align}
$$
となる. ここで $k$ は形状パラメータ，$\theta$ は尺度パラメータ.

例えば  
「外来患者の到着が一定率のポアソン過程で $\lambda=1/\theta$ とする. このとき $k$ 人目までの累積待ち時間 $T_k$ は $\mathrm{Gamma}(k,\theta)$ に従う.」

$\lambda$ を使う流儀と　$\theta = \frac{1}{\lambda}$ を使う流儀があります。混乱するので気を付けましょう。個人的には $\theta$ 派です.(統計検定では $\lambda$ が多いような...)
:::

## 1. 確率密度関数
::: def
形状 $k>0$, 尺度 $\theta>0$, $x>0$ に対して
$$
\begin{align}
f(x)
&= \frac{1}{\Gamma(k)\,\theta^{k}}\,x^{k-1} e^{-x/\theta}
\end{align}
$$
:::

**確率密度関数のグラフ**

<div style="display: flex; gap: 10px; justify-content: center;">
  <img src="/assets/images/probability_distribution/gamma/pdf1.gif" style="max-width: 48%; height: auto;">
  <img src="/assets/images/probability_distribution/gamma/pdf2.gif" style="max-width: 48%; height: auto;">
</div>


## 2. 累積分布関数
::: def
$x>0$ に対して
$$
\begin{align}
F(x)
&= \Pr(X\le x)
= \frac{\gamma\!\left(k,\, x/\theta\right)}{\Gamma(k)}
\end{align}
$$
ここで $\gamma(k,z)=\int_{0}^{z} t^{k-1}e^{-t}\,dt$ は第一種不完全ガンマ関数.
:::

## 3. 期待値

:::def 期待値
$$
\mathbb{E}[X] = k\,\theta
$$
:::

::: details 導出の手順はこちら
:::def 導出
ガンマ分布 $X\sim\mathrm{Gamma}(k,\theta)$ の密度は
$$
f(x)=\frac{1}{\Gamma(k)\,\theta^{k}}x^{k-1}e^{-x/\theta}\quad(x>0)
$$
より，
$$
\begin{align}
\mathbb{E}[X]
&=\int_{0}^{\infty} x\,f(x)\,dx
= \frac{1}{\Gamma(k)\,\theta^{k}}\int_{0}^{\infty} x^{k}e^{-x/\theta}\,dx
\end{align}
$$
と書ける．$u=x/\theta$ とおくと $x=\theta u,\ dx=\theta\,du$ で
$$
\begin{align}
\mathbb{E}[X]
&=\frac{1}{\Gamma(k)\,\theta^{k}}
\int_{0}^{\infty} (\theta u)^{k} e^{-u}\,\theta\,du \\[6pt]
&=\frac{\theta^{k+1}}{\Gamma(k)\,\theta^{k}}
\int_{0}^{\infty} u^{k} e^{-u}\,du \\[6pt]
&= \theta \cdot \frac{\Gamma(k+1)}{\Gamma(k)} \\[6pt]
&= \theta \cdot k \\[6pt]
&= k\,\theta \\[6pt]
\end{align}
$$
:::

## 4. 分散
::: def 分散
$$
\mathrm{V}[X] = k\,\theta^2
$$
:::

::: details 導出の手順はこちら
::: def 導出
ガンマ分布 $X\sim\mathrm{Gamma}(k,\theta)$ に対して
$$
\mathrm{V}[X] = \mathbb{E}[X^2] - \{\mathbb{E}[X]\}^2
$$
より，まず $\mathbb{E}[X^2]$ を計算する.

$$
\begin{align}
\mathbb{E}[X^2]
&= \int_{0}^{\infty} x^2 f(x)\,dx \\[4pt]
&= \frac{1}{\Gamma(k)\,\theta^{k}}
    \int_{0}^{\infty} x^{k+1}e^{-x/\theta}\,dx
\end{align}
$$

$u=x/\theta$ とおく. すると $x=\theta u,\ dx=\theta\,du$.  

$$
\begin{align}
\mathbb{E}[X^2]
&= \frac{1}{\Gamma(k)\,\theta^{k}}
    \int_{0}^{\infty} (\theta u)^{k+1} e^{-u}\,\theta\,du \\[4pt]
&= \frac{\theta^{k+2}}{\Gamma(k)\,\theta^{k}}
    \int_{0}^{\infty} u^{k+1} e^{-u}\,du \\[4pt]
&= \theta^{2}\,\frac{\Gamma(k+2)}{\Gamma(k)} \\[4pt]
&= \theta^{2}\,\frac{k(k+1)\Gamma(k)}{\Gamma(k)} \\[4pt]
&= \theta^{2}\,k(k+1).
\end{align}
$$

一方で $\mathbb{E}[X]=k\theta$ なので

$$
\begin{align}
\mathrm{V}[X]
&= \theta^{2}\,k(k+1) - (k\theta)^2 \\[4pt]
&= \theta^{2}\,\bigl[k(k+1) - k^2\bigr] \\[4pt]
&= k\,\theta^{2}.
\end{align}
$$
:::

## 5. 積率母関数
::: def 積率母関数
$$
M_X(t)=\mathbb{E}[e^{tX}]=(1-\theta t)^{-k}\quad (t<1/\theta)
$$
:::

::: details 導出の手順はこちら
::: def 導出
ガンマ分布 $X\sim\mathrm{Gamma}(k,\theta)$ の密度
$$
f(x)=\frac{1}{\Gamma(k)\,\theta^{k}}x^{k-1}e^{-x/\theta}\quad(x>0)
$$
より
$$
\begin{align}
M_X(t)
&=\int_{0}^{\infty} e^{tx} f(x)\,dx \\[4pt]
&=\frac{1}{\Gamma(k)\,\theta^{k}}
  \int_{0}^{\infty} x^{k-1}\exp\!\left(-\Bigl(\tfrac{1}{\theta}-t\Bigr)x\right)\,dx,
\end{align}
$$
ここで $t<1/\theta$ を仮定する.

$u=\left(\tfrac{1}{\theta}-t\right)x$ とおく.  
すると $x=\dfrac{u}{\tfrac{1}{\theta}-t}$, $dx=\dfrac{du}{\tfrac{1}{\theta}-t}$.

$$
\begin{align}
M_X(t)
&=\frac{1}{\Gamma(k)\,\theta^{k}}
  \int_{0}^{\infty}
  \left(\frac{u}{\tfrac{1}{\theta}-t}\right)^{k-1}
  e^{-u}\,\frac{du}{\tfrac{1}{\theta}-t} \\[6pt]
&=\frac{1}{\Gamma(k)\,\theta^{k}}
  \left(\frac{1}{\tfrac{1}{\theta}-t}\right)^{k}
  \int_{0}^{\infty} u^{k-1} e^{-u}\,du \\[6pt]
&=\frac{1}{\Gamma(k)\,\theta^{k}}
  \left(\frac{1}{\tfrac{1}{\theta}-t}\right)^{k}\Gamma(k) \\[6pt]
&=\left(\frac{1}{1-\theta t}\right)^{k} \\[6pt]
&=(1-\theta t)^{-k}.
\end{align}
$$
:::


## 6. 特性関数
::: def 特性関数
$$
\varphi_X(s)=\mathbb{E}[e^{isX}]=(1-i\theta s)^{-k}\quad (s\in\mathbb{R})
$$
:::

::: details 導出の手順はこちら
::: def 導出
積率母関数が $M_X(t)=(1-\theta t)^{-k}$（$t<1/\theta$）なので，
$$
\varphi_X(s)=M_X(is)=(1-i\theta s)^{-k}.
$$
:::

## 7. 再生性
:::warning 注意
**ガンマ分布は尺度パラメータが共通の場合のみ再生性があります.**
:::

:::def
再生性は積率母関数を使うと簡単に証明できます。  
確率変数 $X, Y$ は独立に $X\sim \mathrm{Gamma}(k_1,\theta)$, $Y\sim \mathrm{Gamma}(k_2,\theta)$ とする（同一の尺度 $\theta$）.

$Z = X + Y$ とおく。積率母関数 $M_X(t), M_Y(t), M_Z(t)$ について，独立性より
$$
\begin{align}
M_Z(t)
&= M_X(t)\,M_Y(t) \\[6pt]
&= (1-\theta t)^{-k_1}\,(1-\theta t)^{-k_2} \\[6pt]
&= (1-\theta t)^{-(k_1+k_2)} \qquad (t<1/\theta)
\end{align}
$$

これは $\mathrm{Gamma}(k_1+k_2,\theta)$ の積率母関数であり，==積率母関数の一意性から==，
$$
\begin{align}
Z \sim \mathrm{Gamma}(k_1+k_2,\theta)
\end{align}
$$
同様に $m$ 個の独立な $\mathrm{Gamma}(k_i,\theta)$ の和も $\mathrm{Gamma}\!\left(\sum_{i=1}^m k_i,\theta\right)$ に従う.
:::

