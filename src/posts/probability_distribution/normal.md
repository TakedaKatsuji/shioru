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

## 1. 確率密度関数
::: info 確率密度関数 (PDF)
平均 $\mu$, 分散 $\sigma^2$ の正規分布 $X \sim \mathcal{N}(\mu,\sigma^2)$ の確率密度関数は  
$$
f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)
$$
:::

**確率密度関数のグラフ**

---

## 2. 累積分布関数
::: info 累積分布関数 (CDF)
$$
F(x) = \int_{-\infty}^x f(t)\,dt
$$
閉じた形は存在せず，誤差関数 $\operatorname{erf}$ で表される.  
$$
F(x) = \frac{1}{2}\left[1+\operatorname{erf}\!\left(\frac{x-\mu}{\sqrt{2\sigma^2}}\right)\right]
$$
:::

::: tip 誤差関数
積分を直接解くことはできないため，誤差関数 $\operatorname{erf}$ を導入する.  
$$
\operatorname{erf}(z) = \frac{2}{\sqrt{\pi}} \int_0^z e^{-t^2}\,dt
$$
:::

**累積分布関数のグラフ**

---

## 3. 期待値
::: info 期待値
$$
\mathbb{E}[X] = \mu
$$
:::

::: details 導出の手順はこちら
::: tip 導出
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
::: info 分散
$$
\mathrm{V}[X] = \sigma^2
$$
:::

::: details 導出の手順はこちら
::: tip 導出
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
::: info 積率母関数 (MGF)
$$
M_X(t) = \mathbb{E}[e^{tX}] = \exp\!\left(\mu t + \tfrac{1}{2}\sigma^2 t^2\right)
$$
:::

::: details 導出の手順はこちら
::: tip 導出
正規分布 $X \sim \mathcal{N}(\mu,\sigma^2)$ の確率密度関数を使う：

$$
f(x) = \frac{1}{\sqrt{2\pi\sigma^2}}
\exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)
$$

積率母関数は
$$
M_X(t) = \int_{-\infty}^\infty e^{tx} f(x)\,dx
$$

これを代入して
$$
\begin{align}
M_X(t) &= \int_{-\infty}^\infty 
e^{tx} \cdot \frac{1}{\sqrt{2\pi\sigma^2}}
\exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right) dx \\[6pt]
&= \frac{1}{\sqrt{2\pi\sigma^2}}
\int_{-\infty}^\infty 
\exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2} + tx\right) dx
\end{align}
$$

指数部を整理する.  
まず $tx$ を $\mu t$ と $(x-\mu)$ に分解：
$$
tx = t\mu + t(x-\mu)
$$

したがって
$$
-\frac{(x-\mu)^2}{2\sigma^2} + tx 
= -\frac{(x-\mu)^2}{2\sigma^2} + t(x-\mu) + \mu t
$$

ここで $(x-\mu)$ を変数とし，平方完成を行う：
$$
-\frac{1}{2\sigma^2}(x-\mu)^2 + t(x-\mu) 
= -\frac{1}{2\sigma^2}\Big[(x-\mu)^2 - 2\sigma^2 t (x-\mu)\Big]
$$

$$
= -\frac{1}{2\sigma^2}\Big[(x-\mu - \sigma^2 t)^2 - (\sigma^2 t)^2\Big]
$$

したがって
$$
-\frac{(x-\mu)^2}{2\sigma^2} + tx
= -\frac{(x-\mu - \sigma^2 t)^2}{2\sigma^2}
+ \frac{\sigma^2 t^2}{2} + \mu t
$$

積分に戻すと
$$
\begin{align}
M_X(t) &= \frac{1}{\sqrt{2\pi\sigma^2}}
\int_{-\infty}^\infty 
\exp\!\left(-\frac{(x-\mu - \sigma^2 t)^2}{2\sigma^2}\right)
\exp\!\left(\frac{\sigma^2 t^2}{2} + \mu t\right) dx
\end{align}
$$

ここで $\exp\!\left(\frac{\sigma^2 t^2}{2} + \mu t\right)$ は $x$ に依存しないので外に出す：
$$
M_X(t) = \exp\!\left(\mu t + \tfrac{1}{2}\sigma^2 t^2\right)
\cdot \frac{1}{\sqrt{2\pi\sigma^2}}
\int_{-\infty}^\infty 
\exp\!\left(-\frac{(x-\mu - \sigma^2 t)^2}{2\sigma^2}\right) dx
$$

右側の積分は正規分布の積分で $=1$ となる.  

したがって
$$
M_X(t) = \exp\!\left(\mu t + \tfrac{1}{2}\sigma^2 t^2\right)
$$
:::

---

## 6. 特性関数
::: info 特性関数 (CF)
$$
\varphi_X(t) = \mathbb{E}[e^{itX}] = \exp\!\left(i\mu t - \tfrac{1}{2}\sigma^2 t^2\right)
$$
:::

::: details 導出の手順はこちら
::: tip 導出
MGFと同様の積分を行い，$t$ を $it$ に置換して導出できる.  
$$
\varphi_X(t) = M_X(it) = \exp\!\left(i\mu t - \tfrac{1}{2}\sigma^2 t^2\right)
$$
:::
