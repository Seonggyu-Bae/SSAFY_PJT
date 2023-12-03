<template>
  <div class="background">
    <div class="container mt-5">
      <div class="metadata">
        <button @click="router.go(-1)" class="btn btn-outline-dark">목록</button>
        <button @click="exitProduct(selectedDeposit)" class="btn btn-outline-dark" v-if="isKorCoNmInArray">이미 찜 한 상품입니다 ^^</button>
        <button v-else style="align-content: end;" @click="gaIp( selectedDeposit )" class="btn btn-outline-danger">찜하기</button>
      </div>
      <h1 class="text-center mb-4">상품 상세</h1>
      <div class="card p-4 total">
        <h3 class="mb-3 bank-name">{{ selectedDeposit.kor_co_nm }}</h3>
        <h3 class="mb-4 product-name">{{ selectedDeposit.fin_prdt_nm }}</h3>
        <p class="month"><strong>공시 제출월:</strong> {{ selectedDeposit.dcls_month }}</p>
        <hr>
        <h3 class="money-info">금리 정보</h3><br>
        <table class="table">
          <thead>
            <tr>
              <th class="bold">금리 유형</th>
              <th class="bold">저축 기간</th>
              <th class="bold">저축 금리</th>
              <th class="bold">최고 우대금리</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="rate in getSortedOptionInfo(id)" :key="rate.id">
              <td>{{ rate.intr_rate_type_nm }}</td>
              <td>{{ rate.save_trm }}개월</td>
              <td>{{ rate.intr_rate }}%</td>
              <td>{{ rate.intr_rate2 }}%</td>
            </tr>
          </tbody>
        </table>
        <br>
        <p><strong>만기 후 이자율</strong><br> {{ selectedDeposit.mtrt_int }}</p>
        <hr>
        <p><strong>기타 유의사항</strong><br>{{ selectedDeposit.etc_note }}</p>
        <p><strong>가입대상:</strong> {{ selectedDeposit.join_member }}</p>
        <p><strong>가입방법:</strong> {{ selectedDeposit.join_way }}</p>
        <p><strong>최고한도:</strong> {{ selectedDeposit.max_limit ? selectedDeposit.max_limit.toLocaleString('ko-KR') + '\\' : '없음' }}</p>
        <p><strong>우대조건:</strong> {{ selectedDeposit.spcl_cnd }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useBankStore } from '@/stores/bank'
import { ref, computed } from 'vue'
import { useRoute,useRouter } from 'vue-router'
import axios from 'axios'

const store = useBankStore()
const route = useRoute()
const router = useRouter()

const id = route.params.id
const user = store.user
const deposits = ref(store.deposits);
const depositoptions = ref(store.depositoptions)

// user.financial_products를 쉼표로 분리하여 배열로 만듦
const financialProductsArray = computed(() =>{
  return user?.financial_products?.split(',') || [];
})

// 선택된 상품 정보가 담겨있는 변수(유저가 확인하고 싶은 상품의 정보임)
const selectedDeposit = computed(() => {
  return deposits.value.find(deposit => deposit.id == id);
})


// 유저가 선택한 상품인지 아닌지 확인하는 변수(T/F 반환)
const isKorCoNmInArray = computed(() => {
  return financialProductsArray.value.includes(selectedDeposit.value?.fin_prdt_nm || '');
})



// 선택된 상품의 옵션(금리정보등)를 받아오는 함수
const getSortedOptionInfo = (depositId) => {
  const matchingOptions = depositoptions.value.filter(option => option.product == depositId)
  if (matchingOptions.length > 0) {
    return matchingOptions
  } else {
    return [];
  }
}





const gaIp = (selected) =>{
  const financial_products = selected.fin_prdt_nm
    axios({
      method: 'PUT',
      url: `${store.API_URL}/user/add_product/${store.user.id}/`,
      headers: {
        Authorization: `Token ${store.token}`
      },
      data: {
        financial_products
      }
    })
    .then((res) => {
      console.log(res)
      store.getUser()
    })
    .then((res) => {
      const pop = window.confirm('찜 목록에 추가되었습니다.')
      if(pop){
        router.go(0)
      }
    })
    .catch((err) => {
      console.log(err)
    })
      
  
}


const exitProduct = (selected) =>{
  const financialProduct = selected.fin_prdt_nm;
  const confirmation = window.confirm('찜 해제 하시겠습니까?');
  
  if (!confirmation) {
    return;
  }
  axios({
    method: 'patch',
    url: `${store.API_URL}/user/update_product/${store.user.id}/`,
    headers: {
      Authorization: `Token ${store.token}`
    },
    data: {
      productToRemove: financialProduct
    }
  })
    .then((res) => {
      console.log(res);
      store.getUser();
    })
    .then((res) => {
      const good = window.confirm('찜 해제 되었습니다.')
      if(good){
        router.go(0)
      }
    })
    .catch((err) => {
      console.error(err);
    });
};




</script>

<style scoped>
.interest-info-container {
  display: flex;
  flex-wrap: nowrap;
  overflow-x: auto;
}

.interest-info {
  flex: 0 0 auto;
  margin-right: 10px;
}

.text-center {
  color: white;
  font-weight: bold;
  padding-top: 40px;
  padding-bottom: 20px;
}
.metadata {
  display: flex;
  justify-content: space-between;
}

.background {
  position: relative;
  background-image: url('@/images/navy-background.png'); /* 배경 이미지 경로 설정 */
  background-size: cover; /* 배경 이미지가 컨테이너에 맞게 나타나도록 설정 */
  background-position: center; /* 배경 이미지 중앙 정렬 */
  height: 100vh; /* 화면 높이에 맞게 설정 */
}

.money-info {
  font-weight: bold;
}
.btn {
  /* 버튼 공통 스타일 설정 */
  padding: 8px 16px;
  font-size: 16px;
  margin-right: 10px;
}

.btn-outline-dark {
  /* 목록 버튼 스타일 설정 */
  color: white;
  border: 2px solid white;
  font-weight: bold;
}

.btn-outline-danger {
  /* 찜하기 버튼 스타일 설정 */
  color: #e06975;
  border: 2px solid rgb(211, 106, 106);
  font-weight: bold;
}

.other-info {
  margin-top: 20px;
}

.other-info p {
  margin-bottom: 10px;
}

.bank-name {
  padding-top: 20px;
  font-weight: bold;
  font-size: 40px;
}

.product-name {
  font-size: 30px;
  font-weight: bold;
  padding-bottom: 20px;
}

hr {
  border: 2px solid black;
}

.bold {
  font-size: 17px;
}

.table {
  width: 100%;
  margin-bottom: 1rem;
  color: #212529;
  background-color: transparent;
  border-collapse: collapse;
}

.table th,
.table td {
  padding: 0.75rem;
  vertical-align: top;
  border-top: 1px solid #dee2e6;
}

.table thead th {
  vertical-align: bottom;
  border-bottom: 2px solid #dee2e6;
}

.table tbody + tbody {
  border-top: 2px solid #dee2e6;
}
</style>
