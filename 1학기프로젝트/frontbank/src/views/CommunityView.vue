<template>
  <div class="out">
    <img src="@/images/exchange.png" alt="" class="exchange-img">
    <div class="community-main">
      <br>
      <br>
      <h1 class="community-title">Community</h1>
      <br>
      <p class="management">자산관리의 모든 것을 묻고 답하는 공간입니다.</p>
      <hr>
      <br>
      <RouterLink class="write-post-btn" :to="{ name: 'CreatePostView' }">
        글쓰기
      </RouterLink>
      <ArticleList />
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useBankStore } from '@/stores/bank'
import { RouterLink, useRouter } from 'vue-router'
import ArticleList from '@/components/ArticleList.vue'

const store = useBankStore()
const user = store.user
const router = useRouter()
const isLogin = store.isLogin

onMounted(() => {
  if(isLogin){
    store.getArticles()
    store.getUsers()
  }
  else{
    router.push({name:"LogInView"})
  }
})

</script>

<style scoped>
.community-main {
  width: 800px;
  margin: 50px auto;
  padding: 20px;
  background-color: rgba(255, 255, 255, 0.9);
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.write-post-btn {
  display: inline-block;
  margin-bottom: 10px;
  padding: 8px 16px;
  font-size: 16px;
  color: #fff;
  background-color: #007bff;
  text-decoration: none;
  border-radius: 4px;
}

.management {
  font-weight: bold;
  font-size: 20px;
}

.write-post-btn:hover {
  background-color: #0056b3;
}

.background {
  position: relative;
  overflow: hidden;
  background-image: url("@/images/pink1.png");
  background-size: cover;
  background-position: top left;
  height: 100vh; /* 화면 전체 높이에 맞춤 */
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
}
.community-title {
  font-size: 50px;
  font-weight: bold;
}

.write-post-btn{
  background-color: #666565;
  border: 2px;
  color: #faf4f4;
  font-weight: bold;
  margin: 5px;
  width: 150px;
  height: 40px;
}

.out {
  margin-top: 100px;
}

.exchange-img {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: -1;
  opacity: 0.4;
}
</style>
