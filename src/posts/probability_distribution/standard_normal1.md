---
date: 2025-09-22
icon: meteor-icons:feather
category:
  - 統計数理
  - 確率分布
tag:
  - 標準正規分布
  - 正規分布
  - 確率密度関数
  - 連続型

---


# 標準正規分布の性質

この記事では標準正規分布の $t$ 次モーメントを既知とします。

詳しく知りたい方は[➡標準正規分布の $t$ 次モーメント](/posts/probability_distribution/standard_normal2.md)をご覧ください。

正規分布のうち，平均が $0$，分散が $1$ の場合を特に **標準正規分布** といいます．  

::: info 定義
一般の正規分布 $X \sim \mathcal{N}(\mu, \sigma^2)$ に対し，  
変数変換
$$
Z = \frac{X - \mu}{\sigma}
$$
を行うと，
$$
Z \sim \mathcal{N}(0,1)
$$
となる．
:::

正規分布の多くの性質は，この標準化によって **標準正規分布の性質から導出** できます．  

そのため，標準正規分布に関する積分公式や累積分布関数を整理しておくと，他の正規分布の性質も容易に導けます．



## 1. 確率密度関数
::: info 確率密度関数 (PDF)
標準正規分布 $Z \sim \mathcal{N}(0,1)$ の確率密度関数は  
$$
f(z) = \frac{1}{\sqrt{2\pi}} \exp\!\left(-\frac{z^2}{2}\right)
$$
:::

**確率密度関数のグラフ**

<div style="display: flex; gap: 10px; justify-content: center;">
  <img src="/assets/images/probability_distribution/standard_normal/pdf.png" style="max-width: 80%; height: auto;">
</div>



## 2. 累積分布関数
::: info 累積分布関数 (CDF)
$$
F(z) = \int_{-\infty}^z f(t)\,dt
= \frac{1}{2}\left[1+\operatorname{erf}\!\left(\frac{z}{\sqrt{2}}\right)\right]
$$
:::

::: tip 誤差関数
閉じた形での積分は存在しないため，誤差関数 $\operatorname{erf}$ を用いる：  
$$
\operatorname{erf}(u) = \frac{2}{\sqrt{\pi}} \int_0^u e^{-t^2}\,dt
$$
:::

**累積分布関数のグラフ**

<div style="display: flex; gap: 10px; justify-content: center;">
  <img src="/assets/images/probability_distribution/standard_normal/cdf.png" style="max-width: 80%; height: auto;">
</div>


## 3. 期待値
::: info 期待値
$$
\mathbb{E}[Z] = 0
$$
:::

::: details 導出の手順はこちら
::: tip 導出
$$
\begin{align}
\mathbb{E}[Z] &= \int_{-\infty}^\infty z f(z)\,dz \\[6pt]
&= \int_{-\infty}^\infty 
z \cdot \frac{1}{\sqrt{2\pi}}
\exp\!\left(-\frac{z^2}{2}\right) dz
\end{align}
$$

被積分関数は奇関数なので，
$$
\mathbb{E}[Z] = 0
$$
:::



## 4. 分散
::: info 分散
$$
\mathrm{V}[Z] = 1
$$
:::

::: details 導出の手順はこちら
::: tip 導出
$$
\begin{align}
\mathrm{V}[Z] &= \mathbb{E}[Z^2] - (\mathbb{E}[Z])^2 \\[6pt]
&= \int_{-\infty}^\infty z^2 f(z)\,dz - 0^2 \\[6pt]
&= \int_{-\infty}^\infty 
z^2 \cdot \frac{1}{\sqrt{2\pi}}
\exp\!\left(-\frac{z^2}{2}\right) dz
\end{align}
$$

既知の標準正規分布の二次モーメントより
$$
\int_{-\infty}^\infty \frac{z^2}{\sqrt{2\pi}} e^{-z^2/2}\,dz = 1
$$

したがって
$$
\mathrm{V}[Z] = 1
$$
:::



## 5. 積率母関数
::: info 積率母関数 (MGF)
$$
M_Z(t) = \exp\!\left(\tfrac{1}{2}t^2\right)
$$
:::

::: details 導出の手順はこちら
::: tip 導出
$$
M_Z(t) = \int_{-\infty}^\infty e^{tz} f(z)\,dz
= \frac{1}{\sqrt{2\pi}} \int_{-\infty}^\infty 
\exp\!\left(-\frac{z^2}{2} + tz\right) dz
$$

指数部を平方完成する：
$$
-\frac{z^2}{2} + tz
= -\frac{1}{2}(z^2 - 2tz)
= -\frac{1}{2}\big[(z-t)^2 - t^2\big]
$$

よって
$$
M_Z(t) =  \int_{-\infty}^\infty
\frac{1}{\sqrt{2\pi}} \exp\!\left(-\frac{(z-t)^2}{2}\right) dz \cdot e^{t^2/2}
$$

積分は正規分布の全積分で $=1$ だから
$$
M_Z(t) = e^{t^2/2}
$$
:::



## 6. 特性関数
::: info 特性関数 (CF)
$$
\varphi_Z(t) = \exp\!\left(-\tfrac{1}{2}t^2\right)
$$
:::

::: details 導出の手順はこちら
::: tip 導出
積率母関数 $M_Z(t) = e^{t^2/2}$ の $t \mapsto it$ 置換で得られる：  
$$
\varphi_Z(t) = M_Z(it) = \exp\!\left(-\tfrac{1}{2}t^2\right)
$$
:::
