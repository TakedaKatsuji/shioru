---
date: 2025-09-22
icon: meteor-icons:feather
category:
  - 統計数理
  - 確率分布
tag:
  - 正規分布
  - 確率密度関数
  - 連続型
---

# 正規分布の性質

<div style="display: flex; gap: 10px; justify-content: center;">
  <img src="/assets/images/probability_distribution/normal/thumbnail.png" style="max-width: 100%; height: auto;">
</div>

::: expl
正規分布は **線形変換で閉じている分布** です.  
$$
Z \sim \mathcal{N}(0, 1)
$$
のとき, 変数変換 $X = \mu + \sigma Z$ により  
$$
X \sim \mathcal{N}(\mu, \sigma^2)
$$
が成り立ちます.  

したがって正規分布の多くの性質は ==標準正規分布の変数変換== によって導出可能です（計算が容易になる）.


  ::: details 正規分布が線形変換で閉じている証明
  標準正規分布 $Z \sim \mathcal{N}(0,1)$ の確率密度関数は
  $$
  f_Z(z) = \frac{1}{\sqrt{2\pi}} e^{-z^2/2}
  $$

  変数変換 $X = \mu + \sigma Z$ を考える.  

  逆変換は $z = \tfrac{x-\mu}{\sigma}$ で，ヤコビアンは $\tfrac{dz}{dx} = \tfrac{1}{\sigma}$.  

  したがって $X$ の密度関数は
  $$
  \begin{align}
  f_X(x) &= f_Z\!\left(\frac{x-\mu}{\sigma}\right) \cdot \frac{1}{|\sigma|} \\[6pt]
  &= \frac{1}{\sqrt{2\pi}} 
  \exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)\cdot \frac{1}{\sigma} \\[6pt]
  &= \frac{1}{\sqrt{2\pi\sigma^2}} 
  \exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)
  \end{align}
  $$

  これは平均 $\mu$, 分散 $\sigma^2$ の正規分布 $\mathcal{N}(\mu,\sigma^2)$ の確率密度関数に一致する.  
  :::


はじめに 👉 [標準正規分布の性質](/posts/probability_distribution/standard_normal1.md) を確認することをおすすめします.

## 1. 確率密度関数
::: def 確率密度関数 (PDF)
平均 $\mu$, 分散 $\sigma^2$ の正規分布 $X \sim \mathcal{N}(\mu,\sigma^2)$ の確率密度関数は  
$$
f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)
$$
:::

**確率密度関数のグラフ**

<div style="display: flex; gap: 10px; justify-content: center;">
  <img src="/assets/images/probability_distribution/normal/pdf.png" style="max-width: 48%; height: auto;">
  <img src="/assets/images/probability_distribution/normal/pdf.gif" style="max-width: 48%; height: auto;">
</div>

## 2. 累積分布関数
::: def 累積分布関数 (CDF)
$$
F(x) = \int_{-\infty}^x f(t)\,dt
$$
閉じた形は存在せず，誤差関数 $\operatorname{erf}$ で表される.  
$$
F(x) = \frac{1}{2}\left[1+\operatorname{erf}\!\left(\frac{x-\mu}{\sqrt{2\sigma^2}}\right)\right]
$$
:::

::: def 誤差関数
積分を直接解くことはできないため，誤差関数 $\operatorname{erf}$ を導入する.  
$$
\operatorname{erf}(z) = \frac{2}{\sqrt{\pi}} \int_0^z e^{-t^2}\,dt
$$
:::

**累積分布関数のグラフ**

<div style="display: flex; gap: 10px; justify-content: center;">
  <img src="/assets/images/probability_distribution/normal/cdf.png" style="max-width: 70%; height: auto;">
</div>

## 3. 期待値
::: def 期待値
$$
\mathbb{E}[X] = \mu
$$
:::

::: details 導出の手順はこちら
::: def 導出
平均 $\mu$, 分散 $\sigma^2$ の正規分布 $X \sim \mathcal{N}(\mu,\sigma^2)$ に対して，  

$$
f(x) = \frac{1}{\sqrt{2\pi\sigma^2}}
\exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)
$$

なので，
$$
\begin{align}
\mathbb{E}[X] 
&= \int_{-\infty}^\infty x f(x)\,dx \\[6pt]
&= \int_{-\infty}^\infty 
x \cdot \frac{1}{\sqrt{2\pi\sigma^2}}
\exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right) dx
\end{align}
$$

ここで変数変換を行う.  
$$
y = \frac{x-\mu}{\sigma}, \quad x = \mu + \sigma y, \quad dx = \sigma dy
$$

これを代入すると
$$
\begin{align}
\mathbb{E}[X]
&= \int_{-\infty}^\infty 
(\mu + \sigma y) \cdot \frac{1}{\sqrt{2\pi\sigma^2}}
\exp\!\left(-\frac{(\sigma y)^2}{2\sigma^2}\right)\sigma dy \\[6pt]
&= \int_{-\infty}^\infty 
(\mu + \sigma y) \cdot \frac{1}{\sqrt{2\pi\sigma^2}}
\exp\!\left(-\frac{y^2}{2}\right)\sigma dy \\[6pt]
&= \int_{-\infty}^\infty 
(\mu + \sigma y) \cdot \frac{1}{\sqrt{2\pi}}
\exp\!\left(-\frac{y^2}{2}\right) dy
\end{align}
$$

積分を分けると
$$
\begin{align}
\mathbb{E}[X]
&= \mu \int_{-\infty}^\infty \frac{1}{\sqrt{2\pi}}
\exp\!\left(-\frac{y^2}{2}\right) dy
+ \sigma \int_{-\infty}^\infty 
\frac{y}{\sqrt{2\pi}}\exp\!\left(-\frac{y^2}{2}\right) dy
\end{align}
$$

前者は標準正規分布の全確率で $=1$，後者は奇関数の積分で $=0$.  
したがって
$$
\mathbb{E}[X] = \mu
$$
:::
---

## 4. 分散
::: def 分散
$$
\mathrm{V}[X] = \sigma^2
$$
:::

::: details 導出の手順はこちら
::: def 導出
正規分布 $X \sim \mathcal{N}(\mu,\sigma^2)$ に対して，分散は

$$
\mathrm{V}[X] = \mathbb{E}[(X-\mu)^2]
= \int_{-\infty}^\infty (x-\mu)^2 f(x)\,dx
$$

である.  
確率密度関数は
$$
f(x) = \frac{1}{\sqrt{2\pi\sigma^2}}
\exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)
$$

なので，

$$
\begin{align}
\mathrm{V}[X] &= \int_{-\infty}^\infty (x-\mu)^2
\cdot \frac{1}{\sqrt{2\pi\sigma^2}}
\exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right) dx
\end{align}
$$

変数変換を行う.  
$$
y = \frac{x-\mu}{\sigma}, \quad x = \mu + \sigma y, \quad dx = \sigma dy
$$

代入すると，

$$
\begin{align}
\mathrm{V}[X]
&= \int_{-\infty}^\infty (\sigma y)^2 \cdot
\frac{1}{\sqrt{2\pi\sigma^2}}
\exp\!\left(-\frac{(\sigma y)^2}{2\sigma^2}\right)\sigma dy \\[6pt]
&= \int_{-\infty}^\infty \sigma^2 y^2 \cdot
\frac{1}{\sqrt{2\pi\sigma^2}}
\exp\!\left(-\frac{y^2}{2}\right)\sigma dy \\[6pt]
&= \int_{-\infty}^\infty \sigma^2 y^2 \cdot
\frac{1}{\sqrt{2\pi}}
\exp\!\left(-\frac{y^2}{2}\right) dy
\end{align}
$$

ここで
$$
\int_{-\infty}^\infty \frac{y^2}{\sqrt{2\pi}}
\exp\!\left(-\frac{y^2}{2}\right) dy = 1
$$
である（標準正規分布の二次モーメント）.  

したがって
$$
\mathrm{V}[X] = \sigma^2
$$
:::

---

## 5. 積率母関数
::: def 積率母関数 (MGF)
$$
M_X(t) = \mathbb{E}[e^{tX}] = \exp\!\left(\mu t + \tfrac{1}{2}\sigma^2 t^2\right)
$$
:::

::: details 導出の手順はこちら
::: def 導出
標準正規分布 $Z \sim \mathcal{N}(0,1)$ の[積率母関数](/posts/probability_distribution/standard_normal1.html#_5-積率母関数)は

$$
M_Z(s) = \mathbb{E}[e^{sZ}] = \exp\!\left(\tfrac{1}{2}s^2\right)
$$

である.  

いま $X \sim \mathcal{N}(\mu,\sigma^2)$ を  
$$
X = \mu + \sigma Z
$$
と標準正規分布 $Z$ を使って表す.  

すると
$$
M_X(t) = \mathbb{E}[e^{tX}]
= \mathbb{E}[e^{t(\mu + \sigma Z)}]
$$

指数を分けると
$$
M_X(t) = e^{\mu t}\,\mathbb{E}[e^{(\sigma t)Z}]
$$

ここで $\mathbb{E}[e^{(\sigma t)Z}]$ は $Z$ のMGFを $s=\sigma t$ とおいたものだから
$$
\mathbb{E}[e^{(\sigma t)Z}] = M_Z(\sigma t) = \exp\!\left(\tfrac{1}{2}(\sigma t)^2\right)
$$

したがって
$$
M_X(t) = e^{\mu t}\,\exp\!\left(\tfrac{1}{2}\sigma^2 t^2\right)
= \exp\!\left(\mu t + \tfrac{1}{2}\sigma^2 t^2\right)
$$

これで導出が完了する.
:::


---

## 6. 特性関数
::: def 特性関数 (CF)
$$
\varphi_X(t) = \mathbb{E}[e^{itX}] = \exp\!\left(i\mu t - \tfrac{1}{2}\sigma^2 t^2\right)
$$
:::

::: details 導出の手順はこちら
::: def 導出
MGFと同様の積分を行い，$t$ を $it$ に置換して導出できる.  
$$
\varphi_X(t) = M_X(it) = \exp\!\left(i\mu t - \tfrac{1}{2}\sigma^2 t^2\right)
$$
:::
