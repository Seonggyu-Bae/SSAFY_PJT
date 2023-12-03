<template>
  <div class="out">
    <img src="@/images/exchange.png" alt="" class="exchange-img">
    <div class="community-main">
      <div v-if="article" class="container mt-5">
        <div class="post-detail">
          <div class="d-flex justify-content-end mb-3">
            <button @click="goBack" class="btn btn-secondary">뒤로가기</button>
          </div>
          <h1 class="post-title">{{ article.title }}</h1>
          <hr>
          <div class="post-content">
            <p class="large-content">{{ article.content }}</p>
          </div>
    
          <div class="post-meta">
            <p class="meta-item">작성자: {{ getUserName(article.user) }}</p>
            <p class="meta-item">작성일: {{ getTimeDifference(article.created_at) }}에 작성</p>
            <p class="meta-item">수정일: {{ getTimeDifference(article.updated_at) }}에 수정</p>
            <div v-if="article.user==store.user.id" class="meta-item">
              <button @click="modifyPost" class="btn btn-secondary">수정하기</button>
              <button @click="deletePost" class="btn btn-secondary">삭제하기</button>
            </div>
            
          </div>
    
          <form @submit.prevent="createComment" class="comment-form mt-4">
            <div class="mb-3">
              <label for="comment" class="form-label">댓글 작성</label>
              <textarea id="comment" v-model="content" class="form-control"></textarea>
            </div>
            <button type="submit" class="btn btn-secondary">댓글 달기</button>
          </form>
    
          <div class="comment-list mt-4">
            <!-- <h3 class="comment-header">댓글 목록</h3> -->
            <div v-for="comment in store.comments" class="comment-item">
              <div class="comment-content">{{ comment.content }}</div>
              <div class="comment-meta">
                <p class="meta-item">작성자: {{ getUserName(comment.user) }}</p>
                <p class="meta-item">작성일: {{ getTimeDifference(comment.created_at) }}에 작성</p>
                <button v-if="comment.user==store.user.id" @click="deleteComment(comment.id)" class="btn btn-danger meta-item">삭제하기</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>

import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useBankStore } from '@/stores/bank'
import { useRoute, useRouter } from 'vue-router'

const store = useBankStore()
const route = useRoute()
const article = ref(null)
const router = useRouter()
const users = store.users

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      // console.log(res.data)
      article.value = res.data
      console.log(article.value)
      store.getComments(article.value.id)
    })
    .catch((err) => {
      console.log(err)
    })

    
})

const articleId = route.params.id


const content = ref(null)


const createComment = function () {
  console.log(articleId)
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/articles/${articleId}/createcomment/`,
    data: {
      article: route.params.id,
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      console.log(res)
      store.getComments(articleId)
      content.value = null
      
    })
    .catch((err) => {
      console.log(err)
    })
}


const getUserName = (userId) => {
  const user = users.find(user => user.id === userId);
  return user ? user.username : 'Unknown';
}


const modifyPost = function(){
 router.push({name:'ModifyPostView', query: { id:articleId, title: article.value.title , content: article.value.content  } })

}

const deletePost = function(){
  axios({
    method: 'DELETE',
    url: `${store.API_URL}/api/v1/articles/${articleId}/`,
    // data: {
    //   article: route.params.id,
    //   content: content.value
    // },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      router.push({name:'community'})
      
    })
    .catch((err) => {
      console.log(err)
    })
}

const deleteComment = function(id){
  axios({
    method: 'DELETE',
    url: `${store.API_URL}/api/v1/articles/${id}/delete/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      router.go(0)
      
    })
    .catch((err) => {
      console.log(err)
    })
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

const goBack = () => {
  router.go(-1);
}

</script>

<style scoped>
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

.form-label {
  font-weight: bold;
}
.community-main {
  width: 800px;
  margin: 50px auto;
  padding: 20px;
  background-color: rgba(255, 255, 255, 0.9); /* 조정된 부분 */
  border-radius: 8px; /* 조정된 부분 */
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5); /* 조정된 부분 */
}
.post-detail {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.post-title {
  font-size: 36px;
  margin-bottom: 10px;
  font-weight: bold;
}

.post-content {
  font-size: 20px;
  margin-bottom: 20px;
}

.large-content {
  font-size: 24px;
}

.post-meta, .comment-meta {
  font-size: 14px;
  color: #555;
  text-align: right;
}

.comment-form {
  margin-top: 40px;
}

.comment-list {
  margin-top: 40px;
}

.comment-header {
  font-size: 24px;
  margin-bottom: 20px;
}

.comment-item {
  margin-bottom: 20px;
  border: 1px solid #ddd;
  padding: 15px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s ease-in-out;

}

.comment-item:hover {
  transform: translateY(-2px);
}

.comment-content {
  font-size: 18px;
  margin-bottom: 10px;
}

.meta-item {
  margin: 0;
  font-weight: bold;
}

.btn-secondary {
  background-color: #6d6b6b;
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