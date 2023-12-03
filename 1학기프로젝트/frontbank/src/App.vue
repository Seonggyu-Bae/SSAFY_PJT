<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container">
        <RouterLink class="navbar-brand" to="/">Best 픽</RouterLink>

        <!-- 메뉴들 중앙 정렬 -->
        <div class="navbar-nav d-flex justify-content-center">
          <RouterLink class="nav-link" to="/product">예적금비교</RouterLink>
          <RouterLink class="nav-link" to="/exchange">환율계산기</RouterLink>
          <RouterLink class="nav-link" to="/findbank">주변은행찾기</RouterLink>
          <RouterLink class="nav-link" to="/community">커뮤니티</RouterLink>
        </div>

        <div class="navbar-nav ms-auto d-flex">
          <div v-if="isLogin" class="nav-item">
            <a class="nav-link" @click="logout">로그아웃</a>
            <a class="nav-link" @click="goMypage">마이페이지</a>
          </div>
          <div v-else class="nav-item d-flex">
            <RouterLink class="nav-link me-2" :to="{ name: 'SignUpView' }">회원가입</RouterLink>
            <RouterLink class="nav-link" :to="{ name: 'LogInView' }">로그인</RouterLink>
          </div>
        </div>
      </div>
    </nav>
    <div style="display: flex; flex-direction: column; min-height: 100vh;">
    <RouterView style="flex: 1; margin-bottom:100px" />

    <footer>
        <span class="info0">개인정보처리방침</span>
        <span class="info1">사고신고</span>
        <span class="info1">상담신청</span>
        <span class="info">웹접근성이용안내</span>
        <span class="info">예적금비교안내</span>
        <span class="info">영업점위치찾기</span>
        <span class="info">환율정보안내</span>
        <br>

        <span class="info0">고객센터</span>
        <span class="info1">0000-0000</span>
        <span class="sub">평일 09:00~18:00</span>
        <span class="sub">전화번호 010-9353-2519</span>
        <span class="sub">이메일 mikj5@naver.com</span>
        <span class="info">ⓒONEPICK. All rights reserved.</span>

        <img class="img" src="@/images/facebook.png" alt="facebook">
        <img class="img" src="@/images/instagram.png" alt="instagram">
        <img class="img" src="@/images/twiter.png" alt="twiter">
      </footer>
    </div>

  </div>
</template>


<script setup>
import { RouterLink, RouterView, onBeforeRouteUpdate } from 'vue-router'
import { useBankStore } from '@/stores/bank'
import { onMounted, ref, computed } from 'vue'
import { useRouter } from 'vue-router';

const store = useBankStore()
const router = useRouter()

const logout = () => {
  store.logOut()
}


const goMypage = function(){
  store.goMypage()
}


const isLogin = computed(() =>{
  return store.token !== null;
})



</script>



<style scoped>
/* Optional Background Color */
body {
  background-color: #f8f9fa;
  margin: 0;
  padding: 0;
  font-family: 'Arial', sans-serif;
}

/* Optional Box Shadow */
.navbar {
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
}

/* Optional Logo Style */
.navbar-brand {
  font-size: 1.5rem;
  font-weight: bold;
  padding-right: 20px;
}

/* Optional Button Style */
.btn-outline-dark {
  color: #343a40;
  border-color: #343a40;
}

footer {
  height: 100px;
  background-color: #696868;
  position: fixed;
  bottom: 0;
  width: 100%;
  text-align: center;
  padding-top: 20px;
}

.info0 {
  font-weight: bold;
  color: white;
}

.info {
  font-weight: bold;
  color: white;
  padding-left: 15px;
}

.info2 {
  font-weight: bold;
  color: white;
  padding-left: 30px;
}

.info1 {
  color: white;
  padding-left: 30px;
}

.sub {
  color: white;
  padding-left: 25px;
}

.img {
  width: 40px;
  height: 30px;
  padding-left: 10px;
  border-radius: 5px;
}
</style>
