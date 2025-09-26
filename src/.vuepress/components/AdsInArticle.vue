<!-- .vuepress/components/AdsInArticle.vue -->
<template>
  <ins class="adsbygoogle"
       style="display:block;min-height:120px"
       data-ad-client="ca-pub-7160116077446563"
       data-ad-slot="＜ユニットのslot番号＞"
       data-ad-format="auto"
       data-full-width-responsive="true"></ins>
</template>
<script setup lang="ts">
import { onMounted } from "vue";
onMounted(() => { (window as any).adsbygoogle = (window as any).adsbygoogle || []; (window as any).adsbygoogle.push({}); });
</script>
