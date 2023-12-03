<template>
  <RouterLink class="title" :to="{ name: 'DetailView', params: { id: article.id }}">
    <div class="article-list-item">
      <strong>{{ article.title }}</strong>
      <hr>
      <div class="metadata">
        <p class="author">작성자: {{ getUserName(article.user) }}</p>
        <p class="timestamp">{{ getTimeDifference(article.created_at) }}에 작성</p>
      </div>
    </div>
  </RouterLink>
</template>


<script setup>
import { RouterLink } from 'vue-router'
import { ref } from 'vue'
import { useBankStore } from '@/stores/bank'

const store = useBankStore()

const users = store.users

defineProps({
  article: Object
})


const getUserName = (userId) => {
  const user = users.find(user => user.id === userId);
  return user ? user.username : 'Unknown';
}



const getTimeDifference = (createdAt) => {
  const now = new Date();
  const createdDate = new Date(createdAt);
  const diffInMilliseconds = now - createdDate;

  // 밀리초를 날짜, 시간, 분 단위로 변환
  const diffInDays = Math.floor(diffInMilliseconds / (1000 * 60 * 60 * 24));
  const diffInHours = Math.floor((diffInMilliseconds % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  const diffInMinutes = Math.floor((diffInMilliseconds % (1000 * 60 * 60)) / (1000 * 60));

  // 현재 시간과의 차이에 따라 다른 문자열 반환
  if (diffInDays > 0) {
    return `${diffInDays}일 전`;
  } else if (diffInHours > 0) {
    return `${diffInHours}시간 전`;
  } else {
    return `${diffInMinutes}분 전`;
  }
}




</script>

<style scoped>
.article-list-item {
  margin-bottom: 20px;
  padding: 15px;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s ease-in-out;
}

.article-list-item:hover {
  transform: translateY(-2px);
}

.title {
  font-size: 18px;
  text-decoration: none;
  color: #333;
}

.title:hover {
  color: #007BFF;
}

.metadata {
  display: flex;
  justify-content: space-between;
}

.author, .timestamp {
  font-size: 14px;
  color: #777;
  margin: 5px 0;
}
</style>
