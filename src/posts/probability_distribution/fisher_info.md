---
date: 2025-12-03
icon: meteor-icons:feather
category:
  - 統計数理
  - 確率分布
tag:
  - 尤度関数
  - フィッシャー情報量
  - 確率密度関数
cover: "/assets/images/probability_distribution/fisher_score/thumbnail.png"
---

<!-- more -->

# フィッシャー情報量
フィッシャー情報量は[スコア関数](/posts/probability_distribution/score.md)の分散で定義されます.
スコア関数は対数尤度の傾き（勾配）であったため、フィッシャー情報量は ==**対数尤度関数の鋭さ**== を表す量であると解釈できます.

:::def
確率変数 $X = (X_1, \dots, X_n)$ の同時確率密度関数を $f(x|\theta)$ とする.
また $\theta$ は一次元のパラメータとします.

- 尤度関数を $L_n(\theta|x) = f(x|\theta)$
- 対数尤度関数 $l(\theta|x) = \log{L_n(\theta|x)} = \log{f(x|\theta)}$
- スコア関数 $S_n(\theta, x) = \frac{\partial}{\partial \theta} l(\theta|x)=\frac{\partial}{\partial \theta} \log{f(x|\theta)}$

フィッシャー情報量は
$$
\begin{align}
I_n(\theta) := V[S_n(\theta, x)]
\end{align}
$$
で定義される
:::

では何故対数尤度関数の鋭さが ==**情報量**== として扱われるのか考えたいと思います.
まず基本として尤度関数とは, 観測されたデータを固定したときに, そのデータを生成するモデルの当てはまりのよさをパラメータの関数として評価したものであることを抑えておく必要があります。

これより対数尤度関数が鋭いというのは観測されたデータで推定されるパラメータがはっきりしており、逆に緩やかな場合は, 推定されるパラメータが曖昧になります。
したがって ==**観測されたデータから得る対数尤度関数が鋭いとき、観測されたデータはパラメータに対して多く情報を持っている**== と解釈できます.


