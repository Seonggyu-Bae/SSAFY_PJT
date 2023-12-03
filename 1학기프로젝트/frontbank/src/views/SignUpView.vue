<template>
  <div class="out">
    <img src="@/images/exchange.png" alt="background" class="exchange-img">
    <div class="community-main">
      <div class="container mt-5">
        <h1 class="mb-4 signup-page">회원가입 페이지에 오신걸 환영합니다</h1>
        <form @submit.prevent="signUp" class="mt-4">
          <div class="row mb-3">
          </div>
          <div class="mb-3">
            <label for="username" class="form-label font-weight-bold">이름</label>
            <input id="username" type="text" v-model.trim="username" class="form-control">
          </div>
          <div class="mb-3">
            <label for="email" class="form-label font-weight-bold">이메일</label>
              <input type="email" id="email" v-model.trim="email" class="form-control">
          </div>
          <div class="mb-3">
            <label for="password1" class="form-label font-weight-bold">비밀번호</label>
            <input id="password1" type="password" v-model.trim="password1" class="form-control">
          </div>
          <div class="mb-3">
            <label for="password2" class="form-label font-weight-bold">비밀번호 확인</label>
            <input id="password2" type="password" v-model.trim="password2" class="form-control">
          </div>
          <br>
          <button type="submit" class="btn btn-secondary">회원가입하기</button>
        </form>
        <br>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useBankStore } from '@/stores/bank'

const store = useBankStore()
const username = ref('')
const password1 = ref('')
const password2 = ref('')
const email = ref('')


const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    email: email.value
  }
  store.signUp(payload)
}


</script>

<style>
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

.community-main {
  max-width: 800px;
  margin: 50px auto;
  padding: 20px;
  background-color: rgba(255, 255, 255, 0.9);
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.signup-page{
  font-weight: bold;
  padding: 20px;
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
