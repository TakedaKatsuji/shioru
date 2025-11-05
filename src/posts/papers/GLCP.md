---
date: 2025-11-04
icon: meteor-icons:newspaper
category:
  - 論文紹介
tag:
  - GLCP
  - Segmentation
  - MICCAI

cover: "/assets/images/papers/GLCP/thumbnail.png"
---

<!-- more -->

# GLCP: グローバルとローカルで持続性を保持した管状構造セグメンテーション

今回は**MICCAI 2025**で早期採択された論文
==**GLCP: Global-to-Local Connectivity Preservation for Tubular Structure Segmentation**== を紹介します。

:::warning
本記事で使用している画像は元論文・公式HPから引用しています.
- [論文リンク](https://papers.miccai.org/miccai-2025/paper/1868_paper.pdf)
- [github](https://github.com/FeixiangZhou/GLCP)
:::

::: tip TL;DR
- ==**MICCAI 2025で早期採択🎉**==
- スケルトンのグローバルなトポロジー情報に加えて ==**ローカルな不連続情報 (どこが不連続点なのか)**== を考慮することで管状構造に特化したセグメンテーションを実現
- nnUNetに数個の畳み込み層を追加するだけの ==**軽量設計**==
:::

<div style="display: flex; gap: 10px; justify-content: center; padding-bottom: 20px; padding-top: 10px;">
  <img src="https://github.com/FeixiangZhou/GLCP/raw/main/img/framework.png" style="max-width: 95%; height: auto;">
</div>

## 概要
管状構造のセグメンテーションは医療分野において重要な役割が果たしています. 代表的な管状構造としては ==**血管・気管・尿管**== などが挙げられます.
これらの構造では, ==**予測結果が断続的になる課題**== がしばしば発生していました. 既存研究の **clDice** や **Skelton Recall** などは枝レベルの連続性を評価できますがピクセル単位の局所的不連続には弱いという限界があります.　そこでこの研究では, ==**グローバル（枝レベル）とローカル（ピクセルレベル）の両方の情報を統合したフレームワーク**== を開発しています.

## イントロ
イントロダクションでは既存研究の動向を ==**モデルベース**・**特徴量ベース**・**Lossベース**== の三つに分類しそれぞれの特徴と課題に言及しています. 
この背景をもとにモチベーションを明確化し, 開発した以下二点を紹介しています.

- ==**Interactive Multi-head Segmentation (IMS)**==
- ==**Dual-Attention-based Refinement (DAR) module**==

### 既存研究手法の分類
| カテゴリ | 参考番号 | 概要 |
|-----------|-----------|------|
| **モデルベース** | 3, 15, 18, 26 | モデルレベルで管状構造の固有特性に適合させることを狙っているが、画像内の管状構造は本質的に疎であるため、これらの手法はそれらを正確に捕捉・描出するのにしばしば苦労する. |
| **特徴量ベース** | 13, 7, 27, 17 | 追加の特徴表現をモデルに組み込むことで管状構造の幾何学的・位相的特性を捉えることを目的としているが、冗長な特徴表現によって性能と効率性が損なわれる可能性がある. |
| **Lossベース** | 20, 11, 23, 19, 14, 28 | 環状構造のトポロジカルな連続性を強化するために様々な損失関数を導入しているが、局所的な不連続を無視

## 方法
このフレームワークは2つのIMS/DARの2種類のモジュールにわかれており ==**IMSがグローバルとローカル情報の抽出**==, ==**DARがIMSで取得した情報を用いてセグメンテーションマスクを精緻化**== を担当しています.
### Interactive Multi-head Segmentation (IMS)
### Dual-Attention-based Refinement (DAR) 

執筆中...
