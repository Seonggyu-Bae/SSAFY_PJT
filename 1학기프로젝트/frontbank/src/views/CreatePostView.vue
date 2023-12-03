<template>
  <div class="out">
    <img src="@/images/exchange.png" alt="" class="exchange-img">
    <div class="article-form-container">
      <br>

      <h1 class="write">게시글 작성</h1>
      <hr>
      <br>
      <form @submit.prevent="createArticle" class="article-form">
        <div class="form-group">
          <label for="title" class="title">제목</label>
          <input type="text" v-model.trim="title" id="title" class="form-control">
        </div>
        <div class="form-group">
          <label for="content" class="title">내용</label>
          <textarea v-model.trim="content" id="content" class="form-control"></textarea>
        </div>
        <br>
        <button type="submit" class="btn btn-secondary">작성하기</button>
      </form>
      <button @click="router.push({name:'community'})" class="btn btn-secondary">돌아가기</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useBankStore } from '@/stores/bank'
import { useRouter } from 'vue-router'

const title = ref(null)
const content = ref(null)
const store = useBankStore()
const router = useRouter()

const createArticle = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/articles/`,
    data: {
      title: title.value,
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      console.log(res)
      router.push({ name: 'DetailView', params: {id: res.data.id }})
    })
    .catch((err) => {
      console.log(err)
    })
}

const goBack = function(){
  router.go(-1)
}



</script>


<style scoped>

.write {
  font-weight: bold;
}
.article-form-container {
  padding: 20px;
  width: 800px;
  margin: 50px auto;
  background-color: rgba(255, 255, 255, 0.9); /* 조정된 부분 */
  border-radius: 8px; /* 조정된 부분 */
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5); /* 조정된 부분 */
}


.article-form {
  margin-bottom: 20px;
}

.form-group {
  margin-bottom: 15px;
}

.form-control {
  width: 100%;
  padding: 8px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.btn {
  padding: 10px 20px;
  font-size: 16px;
  border-radius: 4px;
  cursor: pointer;
}

.title {
  font-weight: bold;
}

.btn-primary {
  background-color: #007bff;
  color: #fff;
}

.btn-secondary {
  background-color: #6c757d;
  color: #fff;
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

.btn-secondary {
  background-color: #636060;
  border: 2px;
  color: #faf4f4;
  font-weight: bold;
  margin: 5px;
  width: 150px;
  height: 40px;
}

hr {
  border: 2px solid rgb(32, 32, 32);
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
