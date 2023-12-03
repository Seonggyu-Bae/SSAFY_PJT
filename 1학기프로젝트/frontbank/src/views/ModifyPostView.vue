<template>
  <div>
    <img src="@/images/exchange.png" alt="" class="exchange-img">
    <div class="community-main">
      <div class="article-form-container">
        <h1 class="write">게시글 수정하기</h1>
        <form @submit.prevent="ModifyPost" class="article-form">
          <div class="form-group">
            <label for="title" class="title">제목</label>
            <input type="text" v-model.trim="title" id="title" class="form-control">
          </div>
          <div class="form-group">
            <label for="content" class="title">내용</label>
            <textarea v-model.trim="content" id="content" class="form-control"></textarea>
          </div>
          <button type="submit" class="btn btn-secondary">수정하기</button>
        </form>
        <button @click="router.go(-1)" class="btn btn-secondary">돌아가기</button>
      </div>
    </div>
  </div>
</template>
  
<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useBankStore } from '@/stores/bank'
import { useRouter, useRoute } from 'vue-router'


const store = useBankStore()
const router = useRouter()
const route = useRoute()

const title = ref('');
const content = ref('');
const articleId = ref('');

onMounted(() => {
  title.value = route.query.title
  content.value = route.query.content
  articleId.value = route.query.id
})


const ModifyPost = function () {
  axios({
    method: 'PUT',
    url: `${store.API_URL}/api/v1/articles/${articleId.value}/`,
    data: {
      title: title.value,
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      router.push({ name: 'DetailView', params: {id: res.data.id }})
    })
    .catch((err) => {
      console.log(err)
    })
}
  
</script>
  
  
  <style scoped>
  .article-form-container {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
  }
  
  .article-form {
    margin-bottom: 20px;
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  .form-label {
  font-weight: bold;
}
  
  .btn-primary {
    background-color: #007bff;
    color: #fff;
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

.write {
  font-weight: bold;
}

.community-main {
  width: 700px;
  margin: 50px auto;
  padding: 20px;
  background-color: rgba(255, 255, 255, 0.9); /* 조정된 부분 */
  border-radius: 8px; /* 조정된 부분 */
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5); /* 조정된 부분 */
}

.btn-secondary {
  background-color: #a8a3a3;
  border: 2px;
  color: #faf4f4;
  font-weight: bold;
  margin: 5px;
  width: 150px;
  height: 40px;
}

.title {
  font-weight: bold;
  margin-bottom: 8px; /* Add margin to the bottom */
}

.form-control {
  width: 100%;
  padding: 8px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-bottom: 12px; /* Add margin to the bottom */
}

.btn {
  padding: 10px 20px;
  font-size: 16px;
  border-radius: 4px;
  cursor: pointer;
  margin-right: 8px; /* Add margin to the right */
}

.btn-secondary {
  background-color: #666464;
  border: 2px;
  color: #faf4f4;
  font-weight: bold;
  margin: 5px;
  width: 150px;
  height: 40px;
}

  </style>
  