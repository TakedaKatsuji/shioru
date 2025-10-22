---
date: 2025-10-20
icon: meteor-icons:feather
category:
  - 統計数理
  - 確率分布
tag:
  - 多項分布
  - 最尤推定量
  - ラグランジュの未定乗数法
  - 確率密度関数
  - 連続型

---

# 多項分布の最尤推定量
:::def
==多項分布の確率質量関数==
$$
\begin{align}
f(x_1,\dots,x_m;\,n,\boldsymbol\theta)
= \frac{n!}{x_1!\cdots x_m!}\prod_{i=1}^m \theta_i^{\,x_i},
\qquad
\sum_{i=1}^m x_i = n,\ \ \theta_i\ge 0,\ \ \sum_{i=1}^m \theta_i=1.
\end{align}
$$
:::

:::expl 最尤推定量の求め方
1. 尤度 $L(\boldsymbol\theta)=\dfrac{n!}{\prod_i x_i!}\prod_i \theta_i^{x_i}$
2. 制約 $\sum_i \theta_i=1$ の下で 対数尤度 を最大化（==ラグランジュの未定乗数法==）
:::

多項分布の最尤推定量は少し特殊な求め方をします。
パラメータ $\theta_i$ には制約があり $\theta_1 + \dots + \theta_m = 1$ を満たします。
このように制約下での最大値は ==**ラグランジュの未定乗数法**== を使用します。
<br>

:::ans
多項分布の尤度関数 $L(\theta_1, \dots, \theta_m)$ は
$$
L(\theta_1, \dots, \theta_m) = \frac{n!}{x_1!x_2!\dots x_n!}\theta_1^{x_1}\theta_2^{x_2}\dots\theta_m^{x_n}
$$

対数尤度関数は
$$
\begin{align}
\log{L(\theta_1, \dots, \theta_m)} &= \log{\frac{n!}{x_1!x_2!\dots x_n!}\theta_1^{x_1}\theta_2^{x_2}\dots\theta_m^{x_n}} \\[6pt]
&= \log{\frac{n!}{x_1!x_2!\dots x_n!}} + \sum_{i=1}^m \log{\theta_i^{x_i}} \\[6pt]
&= \log{\frac{n!}{x_1!x_2!\dots x_n!}} + \sum_{i=1}^m x_i\log{\theta_i}
\end{align}
$$

対数尤度関数から**ラグランジュの未定乗数法**を用いて最尤推定量を求めます.

ラグランジュ関数は
$$
H(\theta_1, \dots, \theta_m) = \log{L(\theta_1,\dots,\theta_m)} - \lambda \sum_{i=1}^m\theta_i \\[6pt]
$$

ここで $\theta_i \, (i \in \set{1,\dots,m})$ で偏微分すると,
$$
\begin{align}
&\frac{\partial}{\partial \theta_i}H(\theta_1, \dots, \theta_m) \\[6pt]
&=  \frac{\partial}{\partial \theta_i}\log{L(\theta_1, \dots, \theta_m)} - \lambda\frac{\partial}{\partial \theta_i}\sum_{i=1}^m\theta_i \\[6pt]
&= \frac{x_i}{\theta_i} - \lambda

\end{align}
$$

したがって $\frac{\partial}{\partial \theta_i}H(\theta_1, \dots, \theta_m) = 0$ を解くと,
$$
\begin{align}
\theta_i = \frac{x_i}{\lambda}
\end{align}
$$
また, $\sum_{i=1}^m\theta_i=1$ より,


$$
\begin{align}
\sum_{i=1}^m\theta_i &= \sum_{i=1}^m \frac{x_i}{\lambda} \\[6pt]
1 &= \frac{1}{\lambda}\sum_{i=1}^m x_i \\[6pt]
1 &= \frac{n}{\lambda} \\[6pt]
n &= \lambda

\end{align}
$$

したがって最尤推定量 $\hat \theta_i$ は,
$$
\hat \theta_i = \frac{x_i}{n}
$$
:::