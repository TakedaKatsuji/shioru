---
date: 2025-09-21
category:
  - 統計数理
  - 多次元分布
tag:
  - 共分散
  - 期待値
  - 分散共分散行列
  - 独立
icon: meteor-icons:feather
---

# 共分散の性質まとめ

<div style="display: flex; gap: 10px; justify-content: center;">
  <img src="/assets/images/multivariate_distribution/covariance/thumbnail.png" style="max-width: 100%; height: auto;">
</div>

## 共分散の定義
::: def
確率変数 $X, Y$ に対して
$$
\mathrm{Cov}[X, Y] = \mathbb{E}[(X-\mathbb{E}[X])(Y-\mathbb{E}[Y])]
$$

公式として以下の形もよく利用されます.
$$
\mathrm{Cov}[X, Y] = \mathbb{E}[XY] - \mathbb{E}[X]\mathbb{E}[Y]
$$
:::

## 分散共分散行列の定義

::: def
確率ベクトル $\mathbf{X} = (X_1, X_2, \dots, X_p)^\top$ の平均ベクトルを  
$$
\mu = \mathbb{E}[\mathbf{X}] = 
\begin{pmatrix}
\mathbb{E}[X_1] \\ \mathbb{E}[X_2] \\ \vdots \\ \mathbb{E}[X_p]
\end{pmatrix}
$$
とすると, 分散共分散行列は次で定義される.  
$$
\begin{align}
\Sigma 
&= \mathrm{Cov}[\mathbf{X}] \\[6pt]
&= \mathbb{E}\big[(\mathbf{X}-\mu)(\mathbf{X}-\mu)^\top\big] \\[6pt]
&=
\begin{pmatrix}
\mathrm{V}[X_1] & \mathrm{Cov}[X_1,X_2] & \cdots & \mathrm{Cov}[X_1,X_p] \\
\mathrm{Cov}[X_2,X_1] & \mathrm{V}[X_2] & \cdots & \mathrm{Cov}[X_2,X_p] \\
\vdots & \vdots & \ddots & \vdots \\
\mathrm{Cov}[X_p,X_1] & \mathrm{Cov}[X_p,X_2] & \cdots & \mathrm{V}[X_p]
\end{pmatrix}
\end{align}
$$

:::

## 共分散の基本性質

::: expl 1. 対称性
$\mathrm{Cov}[X, Y] = \mathrm{Cov}[Y, X]$
:::

::: expl 2. 線形性
$\mathrm{Cov}[aX+b, Y] = a\mathrm{Cov}[X, Y]$

**線形性を利用した重要な公式**

この公式は統計検定では頻出です. 証明までできるようにしましょう. 

- $\mathrm{Cov}[X+Y, Z] = \mathrm{Cov}[X,Z] + \mathrm{Cov}[Y,Z]$

- 特に $\mathrm{Cov}[X+Y, Y] = \mathrm{Cov}[X,Y] + \mathrm{Var}[Y]$

::: details 証明
::: proof
まず線形性を確認する.   
$$
\begin{align}
\mathrm{Cov}[aX+b, Y]
&= \mathbb{E}[(aX+b - \mathbb{E}[aX+b])(Y-\mathbb{E}[Y])]\\[6pt]
&= \mathbb{E}[(aX+b - (a\mathbb{E}[X]+b))(Y-\mathbb{E}[Y])]\\[6pt]
&= \mathbb{E}[a(X-\mathbb{E}[X])(Y-\mathbb{E}[Y])]\\[6pt]
&= a\,\mathrm{Cov}[X,Y]
\end{align}
$$

したがって一次式の係数は外に出せる.   

次に和に関する性質：  
$$
\begin{align}
\mathrm{Cov}[X+Y, Z]
&= \mathbb{E}[(X+Y-\mathbb{E}[X+Y])(Z-\mathbb{E}[Z])]\\[6pt]
&= \mathbb{E}[(X-\mathbb{E}[X])(Z-\mathbb{E}[Z])] + \mathbb{E}[(Y-\mathbb{E}[Y])(Z-\mathbb{E}[Z])]\\[6pt]
&= \mathrm{Cov}[X,Z] + \mathrm{Cov}[Y,Z]\\[6pt]
\end{align}

$$
特に $Z=Y$ とすると  
$$
\mathrm{Cov}[X+Y, Y] = \mathrm{Cov}[X,Y] + \mathrm{V}[Y]
$$
:::

::: expl 3. 独立性
$X, Y$ が独立なら $\mathrm{Cov}[X,Y] = 0$

==ただし逆は必ずしも成立しません.==

正規分布の場合は独立性と無相関性は同値です. 

::: details 証明
::: proof
公式より,
$$
\mathrm{Cov}[X, Y] = \mathbb{E}[XY] - \mathbb{E}[X]\mathbb{E}[Y]
$$
$X, Y$ が独立のとき, $\mathbb{E}[XY] = \mathbb{E}[X]\mathbb{E}[Y]$ より

$$
\begin{align}
\mathrm{Cov}[X, Y]
&= \mathbb{E}[XY] - \mathbb{E}[X]\mathbb{E}[Y] \\[6pt]
&= \mathbb{E}[X]\mathbb{E}[Y] - \mathbb{E}[X]\mathbb{E}[Y]\\[6pt]
&= 0
\end{align}
$$
:::

## 例題

- 例題1: 独立な確率変数
$X, Y \sim U(0,1)$ 独立のとき、$\mathrm{Cov}[X,Y]$ を求めよ. 

::: details 解答
::: ans
独立なら $\mathrm{Cov}[X,Y]=0$ が成り立つ.   
実際に計算すると：

$$
\begin{align}
\mathrm{Cov}[X,Y] &= \mathbb{E}[XY] - \mathbb{E}[X]\mathbb{E}[Y] \\[6pt]
\mathbb{E}[X] &= \mathbb{E}[Y] = \tfrac{1}{2} \\[6pt]
\mathbb{E}[XY] &= \left(\int_0^1 x\,dx\right)\left(\int_0^1 y\,dy\right) = \tfrac{1}{4} \\[6pt]
\mathrm{Cov}[X,Y] &= \tfrac{1}{4} - \tfrac{1}{2}\cdot\tfrac{1}{2} = 0
\end{align}
$$
:::

---

- 例題2: 線形結合 ([2013年統計数理問1 改](/posts/grade1_1/2013/1.md))
$X \sim U(0,1)$ とし、$Y = 1 - X$ のとき、$\mathrm{Cov}[X,Y]$ を求めよ. 

::: details 解答
::: ans
$$
\begin{align}
\mathrm{Cov}[X,Y] &= \mathrm{Cov}[X,1-X] \\[6pt]
&= \mathrm{Cov}[X,1] - \mathrm{Cov}[X,X] \\[6pt]
&= 0 - \mathrm{V}[X] \\[6pt]
&= -\tfrac{1}{12}
\end{align}
$$
:::

---

- 例題3: 共分散行列
$X,Y \sim U(0,1)$ 独立のとき、ベクトル $\mathbf{Z} = (X,Y)^\top$ の共分散行列を求めよ. 

::: details 解答
::: ans
$$
\begin{align}
\Sigma &= 
\begin{pmatrix}
\mathrm{V}[X] & \mathrm{Cov}[X,Y] \\
\mathrm{Cov}[Y,X] & \mathrm{V}[Y]
\end{pmatrix} \\[6pt]
&=
\begin{pmatrix}
\tfrac{1}{12} & 0 \\
0 & \tfrac{1}{12}
\end{pmatrix}
\end{align}
$$
:::
