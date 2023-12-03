<template>
  <div class="out">
    <img src="@/images/exchange.png" alt="background" class="exchange-img">
    <div class="container">
      <div class="router">
      <router-link :to="{ name: 'MyPageView' }" class="btn btn-secondary">마이 페이지</router-link>
      <router-link :to="{ name: 'RecommendView' }" class="btn btn-secondary">금융 상품 추천</router-link>
      <hr><br><br>
      </div>
      <img class="user-img" src="@/images/user.png" alt="user.png">
      <span class="profile-page">{{user.username}}님 안녕하세요</span>
        <div class="profile-info" v-if="!editMode">
          <h5><strong>NICKNAME:</strong> {{ user.nickname || '아직 닉네임을 정하지 않았습니다' }}</h5><br>
          <h5><strong>나이:</strong>  {{ user.age ? user.age + '살' : '나이 정보가 없습니다' }}</h5><br>
          <h5><strong>E-mail:</strong> {{ user.email || '정보 미입력' }}</h5><br>
          <h5><strong>보유금액:</strong> {{ formatCurrency(user.money) ? formatCurrency(user.money) + '원' : '보유금액 정보 미입력' }}</h5><br>
          <h5><strong>연봉:</strong> {{ formatCurrency(user.salary) ? formatCurrency(user.salary) + '원' : '연봉 정보 미입력' }}</h5><br>
          <h5><strong>찜한 금융상품 목록</strong></h5>
          <P>{{ user.financial_products || '아직 찜한 상품이 없습니다' }}</P>
        </div>
        <div class="profile-info" v-else>
          <label for="name">NICKNAME </label>
          <input v-model="nickname" placeholder="닉네을 입력하세요" id="nickname"><br>
          <label for="name">AGE </label>
          <input v-model="age" placeholder="나이를 입력하세요" id="age" @input="validateNumeric"><br>
          <label for="name">MONEY </label>
          <input v-model="money" placeholder="보유 자산을 입력하세요" id="money" @input="validateNumeric" ><br>
          <label for="name">SALARY </label>
          <input v-model="salary" placeholder="연봉을 입력하세요" id="salary" @input="validateNumeric" ><br>
        </div>
        <button class="btn btn-secondary" @click="toggleEditMode">
          {{ editMode ? '저장하기' : '수정하기' }}
        </button>
    </div>
  </div>
</template>

<script setup>
import { useBankStore } from '@/stores/bank'
import { onMounted, ref } from 'vue'
import { useRouter } from 'vue-router';

const store = useBankStore()
const user = store.user
const router = useRouter()
const editMode = ref(false)



const nickname = ref()
const age = ref()
const money = ref()
const salary = ref()




const toggleEditMode = () => {
  editMode.value = !editMode.value
  const payload = {
    nickname: nickname.value,
    age: age.value,
    money: money.value,
    salary: salary.value,
  }
  if (editMode.value==false) {
    store.addUserData(payload)
    toggleEditMode()
  }
}

const formatCurrency = (value) => {
  // 콤마 추가 함수
  return value ? value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",") : null;
}

const validateNumeric = (event) => {
      // Use a regular expression to allow only numeric input
      event.target.value = event.target.value.replace(/[^0-9]/g, '');
    }

// 컴포넌트가 마운트된 후에 실행될 함수
onMounted(() => {
  // 사용자 데이터가 없으면 데이터를 가져오도록 처리
  if (!user.name) {

  }
})


</script>

<style scoped>
.user-img {
  width: 70px;
  height: 70px;
  margin-right: 20px;
  margin-bottom: 20px;
}

.profile-page {
  font-size: 30px;
  font-weight: bold;
}

.profile-info {
  width: 30%;
  padding: 25px;
  border: 5px solid #6e6c6c;
  width: 800px;
  border-radius: 8px;
  margin-bottom: 20px;
  box-sizing: border-box;
  background-color: rgb(234, 234, 248);
}

.background-container {
  position: relative;
  overflow: hidden;
  background-image: url("@/images/pink1.png");
  background-size: cover;
  background-position: center;
  height: 100vh; /* 화면 전체 높이에 맞춤 */
  display: flex;
  align-items: center;
  justify-content: center;
}

.container {
  z-index: 1;
}

.btn-secondary {
  background-color: #575656;
  border: 2px;
  color: #faf4f4;
  font-weight: bold;
  margin: 5px;
  width: 150px;
  height: 40px;
}

input {
    width: 70%;
  padding: 10px;
  margin-bottom: 15px;
  margin-left: 5px;
  box-sizing: border-box;
  border: 2px solid #ccc;
  border-radius: 5px;
  background-color: #fff;
}

label {
  font-weight: bold;
}

</style>
