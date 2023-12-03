<template>
  <div>
    <ArticleListItem 
      v-for="article in store.articles"
      :key="article.id"
      :article="article"
    />
  </div>
</template>

<script setup>
import { useBankStore } from '@/stores/bank'
import ArticleListItem from '@/components/ArticleListItem.vue'

const store = useBankStore()

</script>
