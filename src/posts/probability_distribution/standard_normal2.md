---
date: 2025-09-22
icon: meteor-icons:feather
category:
  - 統計数理
  - 確率分布
tag:
  - 標準正規分布
  - 正規分布
  - モーメント
  - 連続型
  - ガウス積分

---


# 標準正規分布の t 次モーメント

<div style="display: flex; gap: 10px; justify-content: center;">
  <img src="/assets/images/probability_distribution/standard_normal/thumbnail2.png" style="max-width: 100%; height: auto;">
</div>

ここでは，標準正規分布における $t$ 次モーメントを導出します．
::: def t 次モーメント
標準正規分布 $X \sim \mathcal{N}(0,1)$ に対して，
$$
\mathbb{E}[X^t] = \int_{-\infty}^{\infty} x^t \,\frac{1}{\sqrt{2\pi}} e^{-\frac{1}{2}x^2}\, dx
$$

$$
\mathbb{E}[X^t] =
\begin{cases}
1 & (t=0) \\
0 & (t \text{ が奇数}) \\
(2k-1)!! & (t=2k \geq 2)
\end{cases}
$$
:::

::: plan
導出の流れは次の通りです．
1. ガウス積分の確認  
2. $t$ 次モーメントの計算  
:::


## ガウス積分

**ガウス積分**とは，次の積分を指します．

$$
I = \int_{-\infty}^{\infty} e^{-ax^2}\, dx
$$

これは閉じた形で初等関数による評価はできませんが，極座標変換を用いることで  
$$
I = \sqrt{\frac{\pi}{a}}
$$
が得られることが知られています．  

この結果は正規分布の正規化やモーメント計算の基礎として重要です．

::: expl ガウス積分の諸公式
一般に
$$
I_n = \int_{-\infty}^{\infty} x^n e^{-ax^2}\, dx \quad (a>0)
$$
とおくと，$n$ の偶奇で結果が分かれます．

- $n$ が **奇数** のとき  
  integrand が奇関数となるため，
  $$
  I_n = 0
  $$

- $n$ が **偶数** のとき，$n=2k$ とおくと，
  $$
  I_{2k} = \frac{(2k-1)!!}{(2a)^k}\,\sqrt{\frac{\pi}{a}}
  $$
  ここで $(2k-1)!! = 1 \cdot 3 \cdot 5 \cdots (2k-1)$ は二重階乗を表す．

特に $k=0$ の場合，
$$
I_0 = \sqrt{\frac{\pi}{a}}
$$
が得られる．
:::

### 計算例
::: ex 例
$k=1$ のとき（$n=2$）  
$$
I_2=\int_{-\infty}^{\infty} x^2 e^{-a x^2}\,dx
$$

一般式
$$
I_{2k}=\frac{(2k-1)!!}{(2a)^k}\sqrt{\frac{\pi}{a}}
$$
より，
$$
I_2=\frac{(2\cdot1-1)!!}{(2a)^1}\sqrt{\frac{\pi}{a}}
=\frac{1}{2a}\sqrt{\frac{\pi}{a}}
$$
:::

## $t$ 次モーメントの計算
::: calc
標準正規分布 $X \sim \mathcal{N}(0,1)$ に対し，
$$
\mathbb{E}[X^t] = \int_{-\infty}^{\infty} x^t \frac{1}{\sqrt{2\pi}} e^{-x^2/2}\, dx
$$

**偶奇で場合分け**

- **$t$ が奇数のとき**  
  integrand は奇関数となるので
  $$
  \mathbb{E}[X^t] = 0
  $$

- **$t=2k$ が偶数のとき**  
  ガウス積分の公式を用いると
  $$
  \mathbb{E}[X^{2k}] = (2k-1)!!
  $$
  が得られる．  

  ここで $(2k-1)!! = 1 \cdot 3 \cdot 5 \cdots (2k-1)$ は二重階乗である．  

したがって，標準正規分布の $t$ 次モーメントは
$$
\mathbb{E}[X^t] =
\begin{cases}
1 & (t=0) \\
0 & (t \text{ が奇数}) \\
(2k-1)!! & (t=2k \geq 2)
\end{cases}
$$
で与えられる．
:::