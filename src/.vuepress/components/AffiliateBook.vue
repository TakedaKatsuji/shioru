<!-- src/.vuepress/components/AffiliateBook.vue -->
<template>
  <figure class="aff-book">
    <img
      class="aff-book__img"
      :src="img"
      :alt="alt || title"
      loading="lazy"
      decoding="async"
      referrerpolicy="no-referrer"
    />
    <figcaption class="aff-book__body">
      <h3 class="aff-book__title">
      <a
        v-if="amazon"
        :href="amazon"
        target="_blank"
        rel="nofollow sponsored noopener"
        :aria-label="`Amazon: ${title}`"
        class="aff-book__titlelink"
      >{{ title }}</a>
      <a
        v-else-if="rakuten"
        :href="rakuten"
        target="_blank"
        rel="nofollow sponsored noopener"
        :aria-label="`楽天ブックス: ${title}`"
        class="aff-book__titlelink"
      >{{ title }}</a>
      <span v-else>{{ title }}</span>
    </h3>
      <p v-if="author" class="aff-book__meta">{{ author }}</p>
      <p v-if="$slots.default || desc" class="aff-book__desc">
        <slot>{{ desc }}</slot>
      </p>

      <div class="aff-book__btns">
        <a
          v-if="amazon"
          class="aff-book__btn"
          :href="amazon"
          target="_blank"
          rel="nofollow sponsored noopener"
          :aria-label="`Amazon: ${title}`"
        >
          Amazonで見る
        </a>
        <a
          v-if="rakuten"
          class="aff-book__btn aff-book__btn--sub"
          :href="rakuten"
          target="_blank"
          rel="nofollow sponsored noopener"
          :aria-label="`楽天ブックス: ${title}`"
        >
          楽天で見る
        </a>
      </div>
    </figcaption>
  </figure>
</template>

<script setup lang="ts">
import type { Book } from '../books'
import { BOOKS } from '../books'

type Props = {
  id?: keyof typeof BOOKS
  title?: string; img?: string; amazon?: string; rakuten?: string
  author?: string; alt?: string; desc?: string
}
const p = defineProps<Props>()
const preset = (p.id ? BOOKS[p.id] : undefined) as Book | undefined

const title   = p.title   ?? preset?.title   ?? ''
const author  = p.author  ?? preset?.author
const img     = p.img     ?? preset?.img     ?? ''
const amazon  = p.amazon  ?? preset?.amazon
const rakuten = p.rakuten ?? preset?.rakuten
const alt     = p.alt     ?? title
const desc    = p.desc    ?? preset?.desc ?? ''
</script>


<style scoped>
.aff-book{
  display:grid;
  grid-template-columns:110px 1fr;
  gap:14px;
  padding:14px;
  border:1px solid var(--vp-c-divider, #e5e7eb);
  border-radius:12px;
  background:var(--vp-c-bg, #fff);
}
.aff-book__img{
  width:110px;height:160px;object-fit:cover;border-radius:8px;border:1px solid rgba(0,0,0,.06);
  background:#fafafa;
}
.aff-book__body{display:flex;flex-direction:column;gap:8px;min-width:0}
.aff-book__title{margin:0;font-size:1rem;line-height:1.3}
.aff-book__meta{margin:0;color:var(--vp-c-text-2,#6b7280);font-size:.9rem}
.aff-book__desc{margin:.25rem 0 0;color:var(--vp-c-text-1,#374151);font-size:.95rem}

/* 常に横2分割 */
.aff-book__btns{display:flex;gap:8px}
.aff-book__btns > a{flex:1 1 0;min-width:0}

/* ボタン配色: Amazon=紺, 楽天=赤 */
.aff-book__btn{
  display:inline-flex;align-items:center;justify-content:center;
  width:100%;padding:8px 12px;border-radius:999px;
  text-decoration:none;font-weight:700;text-align:center;
  background:#0f2747;border:1px solid #0f2747;color:#fff;
}
.aff-book__btn--sub{
  background:#c40000;border-color:#c40000;color:#fff;
}
.aff-book__btn:hover{filter:brightness(.97)}
.aff-book__btn:focus-visible{outline:2px solid currentColor;outline-offset:2px}

/* ダーク最適化 */
html.dark .aff-book{background:var(--vp-c-bg,#111);border-color:#2a2a2a}
html.dark .aff-book__img{background:#0f0f0f;border-color:#222}

@media (max-width:640px){
  .aff-book{grid-template-columns:90px 1fr}
  .aff-book__img{width:90px;height:130px}
}
</style>
