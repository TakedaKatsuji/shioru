---
date: 2026-06-11
icon: meteor-icons:newspaper
category:
  - 論文紹介
tag:
  - CIS-UNet
  - Segmentation
  - Swin Transformer
  - 大動脈
  - 医用画像

cover: "/assets/images/papers/CIS-UNet/thumbnail.png"
---

<!-- more -->

# CIS-UNet：Context-aware Shifted Window Self-Attentionによる大動脈マルチクラスセグメンテーション

今回は2024年に発表された論文
==**CIS-UNet: Multi-Class Segmentation of the Aorta in Computed Tomography Angiography via Context-Aware Shifted Window Self-Attention**==
（University of Florida, [arXiv:2401.13049](https://arxiv.org/abs/2401.13049)）を紹介します.

:::warning
本記事で使用している図表は元論文から引用しています.
- [論文リンク (arXiv)](https://arxiv.org/abs/2401.13049)
:::

::: tip TL;DR
- 大動脈本体だけでなく ==**13本の分枝動脈を含めた計14クラスを同時にセグメンテーション**== する3Dモデル
- CNNエンコーダ・デコーダに ==**Swin Transformerベースのボトルネック (CSW-SA)**== を組み合わせたハイブリッド構造
- Swin Transformerの ==**Patch Mergingを「ダウンサンプリング」ではなく「グローバル文脈の凝縮」に転用**== することで, ボトルネック1か所だけで大域的な空間情報を獲得
- SwinUNETRと比較して ==**Dice係数0.713 (vs 0.697), 平均表面距離2.78mm (vs 3.39mm)**== と精度・計算効率の両面で上回る
:::

<div style="display: flex; gap: 10px; justify-content: center; padding-bottom: 20px; padding-top: 10px;">
  <img src="/assets/images/papers/CIS-UNet/anatomy.png" style="max-width: 90%; height: auto;">
</div>

## 背景：なぜ「多クラス」セグメンテーションが必要か

大動脈は心臓から全身に血液を送る最大の動脈であり, 大動脈解離や大動脈瘤などの病変は緊急の治療を要します. 近年は ==**ステントグラフトを用いた血管内治療（EVAR/TEVAR）**== が標準治療となっており, 治療計画には大動脈本体だけでなく, 図のような ==**13本の分枝動脈**== それぞれの走行・分岐位置・径を3Dで正確に把握することが不可欠です.

しかし従来の大動脈セグメンテーション研究の多くは, 大動脈を ==**単一クラスの二値セグメンテーション問題**== として扱っており, 個々の分枝を区別できませんでした. これは血管が蛇行していたり分枝の分岐角度が非典型的な症例（特に大動脈解離患者）において, 治療計画に必要な情報が欠落することを意味します.

本論文では大動脈本体と13本の分枝（計14クラス）を ==**同時に**== セグメンテーションする ==**Context-Infused Swin-UNet (CIS-UNet)**== を提案しています.

<div class="table-wrapper">

| 略称 | 動脈名 | 主な灌流域 |
|------|--------|------------|
| Aorta | 大動脈 | 全身 |
| IA | 腕頭動脈 | 右鎖骨下動脈・右総頸動脈に分岐し, 右脳・右腕へ |
| LCC | 左総頸動脈 | 左大脳皮質 |
| LSA | 左鎖骨下動脈 | 左椎骨動脈経由で左後方循環, 左腕 |
| CA | 腹腔動脈 | 肝・脾・胃（肝動脈・脾動脈・左胃動脈に分岐） |
| SMA | 上腸間膜動脈 | 腸管全般 |
| LRA / RRA | 左 / 右腎動脈 | 左 / 右腎臓 |
| LCIA / RCIA | 左 / 右総腸骨動脈 | 内・外腸骨動脈に分岐 |
| LEIA / REIA | 左 / 右外腸骨動脈 | 左 / 右下肢 |
| LIIA / RIIA | 左 / 右内腸骨動脈 | 骨盤内臓器 |

</div>

## データセット

I型/III型を除く ==**B型大動脈解離 (TBAD)**== 患者を対象に, 2011〜2020年の造影CT (CTA) ==**59症例**== を収集し, 44症例を学習用, 15症例をテスト用に用いています.

- スライス厚 0.8〜2mm, 面内分解能 0.759〜1.007mm の3相CT（非造影・動脈相・遅延相）から動脈相を使用
- 学習前に ==**1.5mm × 1.5mm × 1.5mm の等方ボクセル**== にリサンプリング
- MONAIの `RandCropByPosNegLabeld` により ==**128×128×28のパッチ**== をランダムに切り出し
- 大動脈・13分枝の計14領域を, 大学院生3名が3D Slicerを用いて2Dスライス上で手動アノテーション（4軸/サジタル/コロナル断面を使い分け）し, 1mmガウシアンカーネルで3D方向の平滑化を実施
- 外科レジデント2名が最終確認・修正（1症例あたり約4時間）

## CIS-UNetのアーキテクチャ

<div style="display: flex; gap: 10px; justify-content: center; padding-bottom: 20px; padding-top: 10px;">
  <img src="/assets/images/papers/CIS-UNet/architecture.png" style="max-width: 100%; height: auto;">
</div>

CIS-UNetは ==**CNNエンコーダ＋対称なCNNデコーダ＋スキップ接続**== というU-Net型の構造をベースに, ボトルネック部分にのみSwin Transformerブロックを用いた ==**Context-aware Shifted Window Self-Attention (CSW-SA)**== を配置したハイブリッドモデルです（Fig.2(a)）.

### エンコーダ

入力ブロックは $7\times7\times7$ の畳み込みで $C_1$ チャンネルの特徴を抽出します. 続く各エンコーダブロックは

- ストライド2の畳み込みによる ==**ダウンサンプリング**==
- $3\times3\times3$ 畳み込み×3層からなる ==**残差接続付き特徴抽出ブロック**== を$L$個

から構成されます. 本論文ではチャンネル数を $C_1=64,\ C_2=128,\ C_3=256,\ C_4=512$ としており, 4段のダウンサンプリングを経て特徴マップは $\frac{H}{16}\times\frac{W}{16}\times\frac{D}{16}\times C_4$ まで縮小されます.

### CSW-SA：Patch Mergingの転用によるグローバル文脈の獲得

ここが本論文の核心的なアイデアです.

Swin Transformerの自己注意は ==**ウィンドウ内**== に限定されるため計算効率は良い一方で, 窓をまたいだ ==**長距離依存関係**== を直接捉えることができません. SwinUNETRなどはこれを緩和するために ==**各ダウンサンプリング段階すべて**== でShifted Window Self-Attentionを使いますが, その分計算コストが大きくなります.

CIS-UNetは ==**ボトルネック1か所だけ**== にSwin Transformerブロックを配置しつつ, 通常はダウンサンプリングに使われる ==**Patch Merging層を「グローバルな空間情報の凝縮」のために転用**== することで, 計算量を抑えながら大域的な文脈を獲得します.

:::expl CSW-SAの処理の流れ
1. エンコーダ最終層の特徴マップ $\left(\frac{H}{16}\times\frac{W}{16}\times\frac{D}{16}\times C_4\right)$ をパッチ分割・線形埋め込みし, $\frac{H}{16}\times\frac{W}{16}\times\frac{D}{16}\times F$ の特徴 $z$ を得る.
2. 通常のSwin Transformerブロックと同様に, Window-MSAとShifted Window-MSAを適用する：
$$
\begin{align}
\hat z &= \mathrm{W\text{-}MSA}(LN(z)) + z \\[6pt]
z' &= \mathrm{MLP}(LN(\hat z)) + \hat z \\[6pt]
\bar z &= \mathrm{SW\text{-}MSA}(LN(z')) + z' \\[6pt]
z'' &= \mathrm{MLP}(LN(\bar z)) + \bar z
\end{align}
$$
ここで $\mathrm{W\text{-}MSA}$・$\mathrm{SW\text{-}MSA}$ はそれぞれウィンドウ・シフト窓の Multi-head Self-Attention, $LN$はLayer Normalizationを表す.
3. 得られた $z''$ に ==**Patch Merging層**==（Fig.4）を適用し, 隣接パッチをチャネル方向に結合することで $\frac{H}{32}\times\frac{W}{32}\times\frac{D}{32}\times 2F$ まで空間方向に凝縮する. これにより各「画素」が広い受容野の情報を持つ ==**グローバルな空間文脈**== が得られる.
4. 凝縮された特徴を ==**転置畳み込みで元の解像度 $\frac{H}{16}\times\frac{W}{16}\times\frac{D}{16}\times F$ までアップサンプリング**== し, 手順1で得た線形埋め込み出力 $z$ とマージする.
5. $3\times3\times3$ 畳み込みを2回適用して, 出力特徴 $\frac{H}{16}\times\frac{W}{16}\times\frac{D}{16}\times F$ を得る. これがデコーダへ入力される.
:::

<div style="display: flex; gap: 10px; justify-content: center; padding-bottom: 20px; padding-top: 10px;">
  <img src="/assets/images/papers/CIS-UNet/patch_merging.png" style="max-width: 90%; height: auto;">
</div>

Patch Mergingは隣接する $2\times2\times2$ のパッチをチャネル方向に結合することで, 空間サイズを半分にしつつチャネル数を増やす操作です（Fig.4）. 通常のSwin Transformerでは ==**ダウンサンプリング**== のために使われますが, CIS-UNetではボトルネックの特徴をさらに凝縮して大域情報を取り出すために ==**1回だけ**== 使われている点がポイントです. 「シフト窓を全段で使う」のではなく「Patch Mergingで一時的に視野を広げる」という発想で, グローバル文脈の獲得とコストのトレードオフを解決しています.

### デコーダと損失関数

デコーダは4つの転置畳み込み層と4つのデコーダブロックから構成されます. 各デコーダブロックは

1. スキップ接続によるエンコーダ対応層の特徴との ==**結合 (concatenation)**==
2. $3\times3\times3$ 畳み込み×2層
3. 残差接続

を行い, 最終層は $1\times1\times1$ 畳み込みで14クラス分の確率マップ（$H\times W\times D\times C$）を出力します.

学習にはDiceロスとCross Entropyロスを組み合わせた ==**DiceCEロス**== を使用しています.

$$
\begin{align}
L_{DCE} = \lambda_{Dice}L_{Dice} + \lambda_{CE}L_{CE}
\end{align}
$$

$$
\begin{align}
L_{Dice} &= 1- \frac{2\sum_{c=1}^C\sum_{i=1}^N g_i^c s_i^c}{\sum_{c=1}^C\sum_{i=1}^N g_i^c + \sum_{c=1}^C\sum_{i=1}^N s_i^c} \\[6pt]
L_{CE} &= -\frac{1}{N}\sum_{i=1}^N\sum_{c=1}^C g_i^c\log{s_i^c}
\end{align}
$$

$g_i^c$はクラス$c$・ボクセル$i$におけるGTのワンホットラベル, $s_i^c$はモデルの予測確率, $N$はボクセル数, $C$はクラス数（14）です. 本論文では $\lambda_{Dice}=\lambda_{CE}=1$ として両者を等しく重み付けしています.

## 評価指標

各分枝ごとに ==**Dice係数 (DSC)**== と ==**平均表面距離 (MSD)**== を算出し, 全被験者で平均しています.

$$
\begin{align}
DSC(Y,\hat Y) = \frac{2|Y\cap\hat Y|}{|Y|+|\hat Y|}
\end{align}
$$

$$
\begin{align}
MSD = \frac{1}{N}\sum_{p\in Y}\left(\min_{q\in\hat Y}d(p,q)\right)
\end{align}
$$

$Y,\hat Y$ はそれぞれGTと予測のセグメンテーション表面, $d(p,q)$は点$p,q$間のユークリッド距離です. DSCは ==**領域の重なり**==, MSDは ==**境界形状のずれ**== を評価する指標と言えます.

## 結果

### Dice係数（主結果）

3D-UNet, SwinUNETR, dResNet, UNetRの4手法と比較した結果が以下です. CIS-UNetは ==**14分枝中9分枝で最高スコア**==, 平均DSCも ==**0.713**== と最も高い値を達成しています.

<div class="table-wrapper">

| 分枝 | 3D-UNet | SwinUNETR | dResNet | UNetR | **CIS-UNet** |
|------|---------|-----------|---------|-------|--------------|
| Aorta | 0.908 | 0.913 | 0.920 | 0.897 | **0.922** |
| IA | 0.729 | 0.728 | 0.728 | 0.681 | **0.741** |
| LCC | 0.635 | **0.657** | 0.612 | 0.582 | 0.644 |
| LSA | 0.750 | 0.753 | 0.776 | 0.782 | **0.792** |
| CA | 0.570 | **0.622** | 0.567 | 0.569 | 0.580 |
| SMA | 0.723 | 0.691 | **0.766** | 0.669 | 0.715 |
| LRA | 0.503 | 0.527 | 0.470 | 0.423 | **0.540** |
| RRA | 0.507 | 0.584 | 0.534 | 0.586 | **0.594** |
| LCIA | 0.786 | 0.807 | 0.788 | 0.766 | **0.837** |
| RCIA | 0.740 | 0.740 | 0.737 | 0.653 | **0.788** |
| LEIA | 0.743 | 0.776 | 0.783 | 0.745 | **0.805** |
| REIA | 0.702 | **0.784** | 0.774 | 0.726 | 0.783 |
| LIIA | 0.586 | 0.606 | 0.625 | 0.585 | **0.666** |
| RIIA | 0.514 | **0.573** | 0.546 | 0.492 | 0.570 |
| **Average** | 0.671 | 0.697 | 0.688 | 0.654 | **0.713** |

</div>

平均表面距離 (MSD) でもCIS-UNetが ==**14分枝中9分枝で最小**== となり, 平均MSDは ==**2.767mm**==（2位のSwinUNETRは3.394mm, 18.5%改善）でした. 一方でSMA・REIA・RIIAなど, サイズが小さく形状や走行の個体差が大きい分枝では依然として誤差が大きく, 改善の余地が残っています.

### 計算効率の比較

CSW-SAをボトルネックのみに使う設計により, CIS-UNetは ==**パラメータ数・推論速度の両面で効率的**== です.

<div class="table-wrapper">

| モデル | 平均DSC | パラメータ数 (M) | 推論時間 (ms) |
|--------|---------|------------------|----------------|
| SwinUNETR | 0.697 | 61.99 | 125 |
| 3D-UNet | 0.671 | 77.16 | 13 |
| UNetR | 0.654 | 92.618 | 49 |
| dResNet | 0.688 | 94.375 | 20 |
| **CIS-UNet** | **0.713** | 75.038 | 63 |

</div>

SwinUNETRはパラメータ数こそ最小ですが, ==**全エンコーダ層でSwin Transformerを使うため推論時間は最長（125ms）**== です. CIS-UNetはSwin Transformerをボトルネックのみに限定することで, ==**精度トップを維持しつつ2番目に少ないパラメータ数・3番目の速さ**== というバランスの良さを実現しています.

### Ablation：CSW-SAの効果

CSW-SA（Patch Mergingでグローバル文脈を獲得）と, オリジナルのShifted Window Self-Attention（SW-SA, 通常のSwin Transformerブロックのみ）を比較したアブレーションです.

<div class="table-wrapper">

| モデル | CSW-SA | SW-SA | 平均DSC | パラメータ数 (M) |
|--------|:------:|:-----:|---------|------------------|
| Tiny | ✓ | | 0.694 | 13.921 |
| Small | ✓ | | 0.697 | 21.5 |
| Base | | ✓ | 0.701 | 71.789 |
| Base | ✓ | | **0.713** | 75.038 |

</div>

同じBaseサイズでもCSW-SAを使うことでDSCが ==**0.701 → 0.713**== に向上しており, パラメータの増加はわずか約3.2M（71.789M → 75.038M）に留まります. ==**ウィンドウ自己注意にグローバル文脈を付加することの有効性**==がここから確認できます. 定性的にも, CSW-SAは断続的なセグメンテーションやアーティファクトを抑制し, より滑らかで連続的な結果を与えることが報告されています（Fig.6）.

### 他データセットへの汎化（BTCV）

CIS-UNetが大動脈以外でも有効かを確認するため, ==**腹部CTの13臓器セグメンテーションデータセットBTCV**==（脾臓・腎臓・肝臓・膵臓など）でもSwinUNETR・UNetRと比較しています（25症例で学習・5症例で検証）.

<div class="table-wrapper">

| モデル | 平均DSC | 平均MSD (mm) |
|--------|---------|--------------|
| UNetR | 0.780 | 2.71 |
| SwinUNETR | 0.819 | 1.13 |
| **CIS-UNet** | **0.835** | **0.93** |

</div>

大動脈データセットに対して特別なチューニングを行っていないにもかかわらず, ==**CIS-UNetが両指標でSwinUNETR・UNetRを上回る**== 結果となっており, アーキテクチャとしての汎用性の高さがうかがえます.

## まとめ

今回は大動脈とその13分枝を一括で扱う多クラスセグメンテーションモデル ==**CIS-UNet**== を紹介しました. 特に, Swin Transformerの ==**Patch Merging層を「ダウンサンプリング」から「グローバル文脈の凝縮」へ転用**== し, ボトルネック1か所に限定して適用するというアイデアはシンプルながら効果的で, 精度・計算効率のバランスに優れたアーキテクチャ設計の好例だと感じました.

血管内治療の術前計画において, 大動脈本体だけでなく分枝動脈の形状を自動かつ高精度に把握できることは, 手術計画の効率化や個別化治療の実現に直結する重要な貢献だと言えます.
