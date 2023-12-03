<template>
  <div class="out">
    <div class="community-main">
      <img src="@/images/exchange.png" alt="background" class="exchange-img">
      <div class="main">
        <h1 class="title">☝🏻 세상에 나쁜 금융 상품은 없다</h1>
        <h3>주식, 코인 하지말고 원금이 보장되는 예적금 합시다</h3>
        <p>(버튼을 누르면 랜덤으로 예금, 적금 1가지씩 추천해드립니다)</p>
        <button @click="test()" class="btn btn-secondary-1">금융상품 추천받기</button>
        <div class="flex-container">
          <!-- 첫 번째 반절 -->
          <div class="half-width" v-for="randomDeposit in randomDeposits" :key="randomDeposit.id">
            <h3>예금</h3>
            <div class="item-container">
              <p class="name">{{ randomDeposit.fin_prdt_nm }}</p>
              <button @click="depositDetail(randomDeposit.id)" class="btn btn-secondary">상세 정보 보기</button>
            </div>
          </div>
          <!-- 두 번째 반절 -->
          <div class="half-width" v-for="randomSaving in randomSavings" :key="randomSaving.id">
            <h3>적금</h3>
            <div class="item-container">
              <p class="name">{{ randomSaving.fin_prdt_nm }}</p>
              <button @click="savingDetail(randomSaving.id)" class="btn btn-secondary">상세 정보 보기</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>



<script setup>
import { useBankStore } from '@/stores/bank'
import { onMounted, ref, computed } from 'vue'
import { useRouter } from 'vue-router';


const store = useBankStore()

const deposits = store.deposits
const savings = store.savings

const router = useRouter()
const randomDeposits = ref(null)
const randomSavings = ref(null)


const getRandomItems = (arr, count) => {
  const shuffled = arr.sort(() => 0.5 - Math.random());
  return shuffled.slice(0, count);
}
const test = function(){
    randomDeposits.value = getRandomItems(deposits, 1);
    randomSavings.value = getRandomItems(savings, 1);
    console.log('hi')
  }





const depositDetail = function (depositId) {
  router.push({ name: 'DepositDetail', params: { id: depositId } });
}

const savingDetail = function (savingId) {
  router.push({ name: 'SavingDetail', params: { id: savingId } });
}



</script>






<style scoped>
.flex-container {
  display: flex;
  flex-wrap: wrap; /* 중요: 여러 행으로 나누도록 설정 */
}

.half-width {
  width: 50%;
  box-sizing: border-box;
}

.item-container {
  border: 2px solid #ddd; /* 아이템 구분을 위한 테두리 추가 (선택적) */
  padding: 10px; /* 아이템 내부 패딩 추가 (선택적) */
  margin: 10px;
}

.main{
  text-align: center;
}

.title {
  margin: 60px;
  font-weight: bold;
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

.community-main {
  width: 800px;
  margin: 50px auto;
  padding: 20px;
  background-color: rgba(255, 255, 255, 0.9);
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.btn-secondary-1 {
  background-color: #6c757d;
  color: #fff;
  margin-top: 30px;
  margin-bottom: 30px;
  font-weight: bold;
  padding: 12px;
  
}

.btn-secondary {
  background-color: #6c757d;
  color: #fff;
}

.name {
  font-weight: bold;
}
</style>