<template>
  <div class="out">
    <img src="@/images/exchange.png" alt="background" class="exchange-img">
    <div class="container">

      <div class="community-main">
        <div class="title">
          <h1 class="greeting">😉 {{ user.username }}님, 반갑습니다 !</h1>
        </div>
  
        <div class="nav-links">
          <router-link :to="{ name: 'ProfilePageView' }" class="btn btn-secondary">프로필 페이지</router-link>
          <router-link :to="{name : 'RecommendView'}" class="btn btn-secondary">금융 상품 추천</router-link>
        </div>
      </div>

      <div class="community-main">
        <div class="section">
          <div class="section">
            <h3 class="product">💰내가 찜한 상품</h3>
            <div v-if="isFinancialProductsExist" class="products">
              <div class="product-container" v-if="depositArray.length">
                <h4>[ 예금 ]</h4>
                <p @click="router.push({name:'DepositDetail', params:{id:deposit.id}})" v-for="deposit in filteredDeposits" class="sub">{{ deposit.fin_prdt_nm }}</p>
              </div>
              <div class="product-container" v-if="savingArray.length">
                <h4>[ 적금 ]</h4>
                <p @click="router.push({name:'SavingDetail', params:{id:saving.id}})" v-for="saving in filteredSavings" class="sub">{{ saving.fin_prdt_nm }}</p>
              </div>
            </div>
          </div>
          <h2 class="section-title">내가 찜한 예금 상품 금리 비교</h2>
          <div class="chart">
            <Bar 
              id="deposit-chart-id"
              :options="chartOptions"
              :data="chartData"
            />
          </div>
        </div>
        
        <div class="section">
          <h2 class="section-title">내가 찜한 적금 상품 금리 비교</h2>
          <div class="chart">
            <Bar 
              id="saving-chart-id"
              :options="chartOptions"
              :data="chartData1"
            />
          </div>
        </div>
      </div>
      
    </div>
  </div>
</template>

<script setup>
import { useBankStore } from '@/stores/bank'
import { onMounted, ref } from 'vue'
import { useRouter } from 'vue-router';

import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)





const store = useBankStore()
const user = store.user
const router = useRouter()
const deposits = store.deposits
const depositoptions = store.depositoptions
const savings = store.savings
const savingoptions = store.savingoptions



const isFinancialProductsExist = ref(user.financial_products !== null)

  // user.financial_products를 쉼표로 분리하여 배열로 만듦
const financialProductsArray = user?.financial_products?.split(',') || [];


// financialProductsArray에서 '예금'이라는 단어를 가지고있는 상품만 모은 배열
const depositArray = financialProductsArray.filter((x) => x.includes("예금"));

// financialProductsArray에서 '적금'이라는 단어를 가지고있는 상품만 모은 배열
const savingArray = financialProductsArray.filter((x) => x.includes("적금"));



const filteredDeposits = deposits.filter(
  deposit => depositArray.includes(deposit.fin_prdt_nm));

// 필터링된 객체들의 id를 추출하여 options 배열 생성
const options = filteredDeposits.map(deposit => deposit.id);
// kor_co_nm, id




const filteredSavings = savings.filter(saving => 
  financialProductsArray.includes(saving.fin_prdt_nm.trim()))

const options1 = filteredSavings.map(saving => saving.id);


// depositoption
const matchedProducts = options.map(optionId => {
  const matchedOption = depositoptions.filter(option => option.product === optionId);
  return matchedOption ? matchedOption : null;
});



// savingoption 
const matchedProducts1 = options1.map(optionId => {
  const matchedOption = savingoptions.filter(option => option.product === optionId);
  return matchedOption ? matchedOption : null;
});




const depositData1 = ref([])
const depositData2 = ref([])

const savingData1 = ref([])
const savingData2 = ref([])



const twelveMonthProducts = matchedProducts
  .map(productOptions => 
    productOptions.filter(option => option.save_trm === 12))
  .flat();


const twelveMonthProducts1 = matchedProducts1
.map(productOptions => 
  productOptions.filter(option => option.save_trm === 12))
.flat();




const extractChartData = twelveMonthProducts.forEach(option => {
  // Intr_rate를 차트 데이터에 추가
  depositData1.value.push(option.intr_rate);
  // Intr_rate2를 차트 데이터에 추가
  depositData2.value.push(option.intr_rate2);
});


const extractChartData1 = twelveMonthProducts1.forEach(option => {
  // Intr_rate를 차트 데이터에 추가
  savingData1.value.push(option.intr_rate);
  // Intr_rate2를 차트 데이터에 추가
  savingData2.value.push(option.intr_rate2);
});





// 차트 데이터
const chartData = ref({
  labels: depositArray,
  datasets: [
    { label: '저축금리', data: depositData1.value, backgroundColor: 'rgba(75, 192, 192, 0.2)', borderColor: 'rgba(75, 192, 192, 1)', borderWidth: 1 },
    { label: '최대우대금리', data: depositData2.value, backgroundColor: 'rgba(255, 99, 132, 0.2)', borderColor: 'rgba(255, 99, 132, 1)', borderWidth: 1 }
  ]
})

const chartData1 = ref({
  labels: savingArray,
  datasets: [
    { label: '저축금리', data: savingData1.value, backgroundColor: 'rgba(75, 192, 192, 0.2)', borderColor: 'rgba(75, 192, 192, 1)', borderWidth: 1 },
    { label: '최대우대금리', data: savingData2.value, backgroundColor: 'rgba(255, 99, 132, 0.2)', borderColor: 'rgba(255, 99, 132, 1)', borderWidth: 1 }
  ]
})



const chartOptions = ref({
  responsive: true,
  maintainAspectRatio: true,
})


onMounted(()=>{
  store.getUser()
  store.loadsavingdata()
  store.loadsavingoptions()
  store.loaddepositoptions()
  store.loaddepositdata()
})


</script>
<style scoped>

.btn-secondary {
  background-color: #a8a3a3;
  border: 2px;
  color: #faf4f4;
  font-weight: bold;
  margin: 5px;
  width: 150px;
  height: 40px;
}

.background-container {
  position: relative;
  overflow: hidden;
  background-image: url("@/images/pink1.png");
  background-size: cover;
  background-position: top left;
  display: flex;
  align-items: center;
  justify-content: flex-start;
}

.nav-links {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-bottom: 20px;
}

.container {
  text-align: center;
  padding: 20px;
  align-items: center;
}

.chart {
  align-items: center;
  width: 80%;
  height: 50%;

}

#my-chart-id {
  margin-bottom: 50px;
  width: 100%;
  height: 100%;
}



.product-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 10px;
}

.product-container h4 {
  margin-bottom: 5px;
}


.section {
  margin-bottom: 40px;
  margin-top: 40px;
}

.section-title {
  margin-bottom: 60px;
  font-size: 24px;
  font-weight: bold;

}

.products {
  display: flex;
  justify-content: space-around;
}

.greeting {
  font-weight: bold;
  padding: 40px;
}

.community-main {
  width: 800px;
  margin: 50px auto;
  padding: 20px;
  background-color: rgba(255, 255, 255, 0.9);
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
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

.chart {
  margin: 0 auto;
  width: 80%;
  height: 50%;
}

.product {
  font-weight: bold;
}

.product-container {
  display: flex;
  flex-direction: column;
  margin-top: 10px;
  text-align: center;
  padding-top: 20px;
}

.product-container h4 {
  padding-bottom: 10px;
  /* margin-bottom: 5px; */
}

.sub {
  padding-left: 20px m;
}
</style>