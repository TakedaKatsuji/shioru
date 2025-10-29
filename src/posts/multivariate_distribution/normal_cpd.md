---
date: 2025-09-24
icon: meteor-icons:feather
category:
  - 統計数理
  - 確率分布
tag:
  - 標準正規分布
  - 正規分布
  - 確率密度関数
  - 連続型
  - 条件付き分布
cover: "/assets/images/multivariate_distribution/normal_cpd/thumbnail.png" 
---

<!-- more -->

# 2次元正規分布の条件付き分布

統計検定1級では**2次元正規分布の条件付き分布**がよく出てきます.  

しかし公式を丸暗記しようとすると、平均や分散の形を間違えやすく、苦労する人も多いと思います.  

そこで本記事では ==「標準正規分布」から「一般の正規分布」へ変数変換する流れ==を押さえることで、  

公式をシンプルに導出する手順をご紹介します. 

<div style="display: flex; gap: 10px; justify-content: center;">
  <img src="/assets/images/multivariate_distribution/normal_cpd/cpd.gif" style="max-width: 100%; height: auto;">
</div>

::: hint ポイント
- ==標準正規分布での結果を **「そのままスケール・シフト」** するだけで一般形が出る==  
- ==覚えるべきは「標準正規の条件付き分布」の形だけ==

これを押さえると、統計検定の条件付き分布問題もスッキリ解けます！
:::

## 1. $X,Y$ が標準正規分布の場合

$(X,Y)$ が平均ベクトル $\mathbf{0}$, 分散共分散行列
$$
\Sigma =
\begin{pmatrix}
1 & \rho \\
\rho & 1
\end{pmatrix}
$$
に従うとする：
$$
(X,Y) \sim \mathcal{N}\!\left(
\begin{pmatrix}0 \\ 0\end{pmatrix},
\begin{pmatrix}1 & \rho \\ \rho & 1\end{pmatrix}
\right)
$$

::: def 条件付き分布
$X=x$ のときの $Y$ の条件付き分布は
$$
Y \mid X=x \sim \mathcal{N}\!\big(\rho x, \; 1-\rho^2\big)
$$
:::

::: details 導出の手順はこちら
::: hint 導出
2次元正規分布の同時確率密度関数は
$$
f(x,y) = \frac{1}{2\pi\sqrt{1-\rho^2}}
\exp\!\left[
-\frac{1}{2(1-\rho^2)}(x^2 - 2\rho xy + y^2)
\right]
$$

$X=x$ のときの条件付き分布は
$$
f_{Y|X}(y|x) = \frac{f(x,y)}{f_X(x)}
$$

まず $X$ の周辺分布は $X \sim \mathcal{N}(0,1)$ なので
$$
f_X(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}
$$

したがって
$$
\begin{align}
f_{Y|X}(y|x)
&= \frac{ \dfrac{1}{2\pi\sqrt{1-\rho^2}}
\exp\!\left[-\tfrac{1}{2(1-\rho^2)}(x^2 - 2\rho xy + y^2)\right]}
{ \dfrac{1}{\sqrt{2\pi}} e^{-x^2/2} } \\[8pt]
&= \frac{1}{\sqrt{2\pi(1-\rho^2)}}
\exp\!\left\{ -\frac{1}{2(1-\rho^2)}\Big(y^2 - 2\rho xy + \rho^2 x^2\Big) \right\}
\end{align}
$$

指数の中を整理すると
$$
y^2 - 2\rho xy + \rho^2 x^2 = (y-\rho x)^2
$$

したがって
$$
f_{Y|X}(y|x) = \frac{1}{\sqrt{2\pi(1-\rho^2)}}
\exp\!\left(-\frac{(y-\rho x)^2}{2(1-\rho^2)}\right)
$$

これは平均 $\rho x$, 分散 $1-\rho^2$ の正規分布の密度関数である.
:::


## 2. $X,Y$ が一般の正規分布の場合

標準正規分布からの変数変換を用いると，一般の場合も同様に導ける.  

例えば
$$
\begin{align}
X &= \mu_X + \sigma_X Z_X, \\
Y &= \mu_Y + \sigma_Y Z_Y,
\end{align}
$$
ただし $(Z_X, Z_Y)$ が相関係数 $\rho$ を持つ標準2次元正規に従うとする.  

このとき $(X,Y)$ は
$$
(X,Y) \sim \mathcal{N}\!\left(
\begin{pmatrix}\mu_X \\ \mu_Y\end{pmatrix},
\begin{pmatrix}\sigma_X^2 & \rho \sigma_X\sigma_Y \\
\rho \sigma_X\sigma_Y & \sigma_Y^2\end{pmatrix}
\right)
$$

::: def 条件付き分布
$X=x$ のときの $Y$ の条件付き分布は
$$
Y \mid X=x \sim \mathcal{N}\!\Big(
\mu_Y + \rho \frac{\sigma_Y}{\sigma_X}(x-\mu_X), \;
\sigma_Y^2 (1-\rho^2)
\Big)
$$
:::

::: details 導出の手順はこちら
::: hint 導出
1. **標準化**  
標準化した変数を
$$
Z_X = \frac{X-\mu_X}{\sigma_X}, \quad 
Z_Y = \frac{Y-\mu_Y}{\sigma_Y}
$$
とすると，$(Z_X,Z_Y)$ は標準正規ベクトルで相関係数 $\rho$ を持つ：
$$
(Z_X,Z_Y) \sim \mathcal{N}\!\left(
\begin{pmatrix}0 \\ 0\end{pmatrix},
\begin{pmatrix}1 & \rho \\ \rho & 1\end{pmatrix}
\right)
$$

2. **標準正規の場合の条件付き分布**  
すでに導出した結果より
$$
Z_Y \mid Z_X=z_x \sim \mathcal{N}(\rho z_x,\; 1-\rho^2)
$$

3. **元の変数に戻す**  
$X=x$ に対応する $Z_X = \tfrac{x-\mu_X}{\sigma_X}$.  
したがって
$$
Z_Y \mid X=x \sim \mathcal{N}\!\Big(
\rho \frac{x-\mu_X}{\sigma_X},\; 1-\rho^2
\Big)
$$

4. **$Y$ の変換**  
$Y = \mu_Y + \sigma_Y Z_Y$ なので，条件付き分布は
$$
Y \mid X=x \sim \mathcal{N}\!\Big(
\mu_Y + \rho \frac{\sigma_Y}{\sigma_X}(x-\mu_X),\;
\sigma_Y^2 (1-\rho^2)
\Big)
$$

以上で導出完了.
:::

---

## 参考文献
<AffiliateBook id="takemura_gen_stats"/>