<template>
  <div class="out">
    <img src="@/images/exchange.png" alt="background" class="exchange-img">
    <div class="community-main">
      <div class="container mt-5 text-center">
        <h1 class="mb-4 login">로그인</h1>
        <form @submit.prevent="logIn" class="mb-3">
          <div class="mb-3">
            <label for="email" class="form-label">이메일</label>
            <input id="email" type="text" v-model.trim="email" class="form-control">
          </div>
          <div class="mb-3">
            <label for="password" class="form-label">비밀번호</label>
            <input type="password" v-model.trim="password" class="form-control">
          </div>
          <button type="submit" class="btn btn-secondary1">로그인</button>
        </form>
        <button @click="goSignUp" class="btn btn-secondary2">혹시 회원이 아니신가요?</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useBankStore } from '@/stores/bank'
import { useRouter } from 'vue-router'

const router = useRouter()
const store = useBankStore()
const email = ref(null)
const password = ref(null)

const logIn = function () {
  store.logIn(email.value, password.value )
}

const goSignUp = function(){
  router.push({name:'SignUpView'})
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
  /* padding: 50px; */
  padding-left: 100px;
  padding-right: 100px;
  padding-bottom: 40px;
  background-color: rgba(255, 255, 255, 0.9);
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.login {
  font-weight: bold;
}

.form-label {
  font-weight: bold;
}

.btn-secondary1 {
  background-color: #a8a3a3;
  border: 2px;
  color: #faf4f4;
  font-weight: bold;
  margin: 5px;
  width: 150px;
  height: 40px;
}

.btn-secondary2 {
  background-color: #a8a3a3;
  border: 2px;
  color: #faf4f4;
  font-weight: bold;
  margin: 5px;
  width: 300px;
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
