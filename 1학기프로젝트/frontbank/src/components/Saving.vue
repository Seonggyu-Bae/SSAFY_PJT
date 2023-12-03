<template>
  <br>
  <br>
  <div class="container mt-5">
    <h1 class="text-center mb-4"> 적금상품 목록</h1>
    <br>
    <div class="search-container mb-3">
      <label for="bankSearch" class="visually-hidden">은행명 검색:</label>
      <input type="text" v-model="bankSearch" class="form-control bank-search" id="bankSearch" placeholder="은행명을 입력하세요">
    </div>
    <div class="table-container">
      <table class="table table-striped table-hover">
        <thead class="table-dark">
          <tr>
            <th>공시 제출월</th>
            <th>은행명</th>
            <th>상품명</th>
            <th>옵션 정보</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="saving in filteredDeposits" :key="saving.id" @click="goDetail(saving)">
            <td class="month">{{ saving.dcls_month }}</td>
            <td class="bankname">{{ saving.kor_co_nm }}</td>
            <td class="productname">{{ saving.fin_prdt_nm }}</td>
            <td>
              <div v-if="savingoptions.length">
                <div v-for="option in getSortedOptionInfo(saving.id)" :key="option.id" class="option-info">
                  <strong>{{ option.save_trm }}개월:</strong> {{ option.intr_rate }}%
                </div>
              </div>
              <div v-else>
                No options available.
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { useBankStore } from '@/stores/bank'
import { onMounted, ref, computed } from 'vue'
import { useRouter } from 'vue-router';

const store = useBankStore()
const router = useRouter()

const savings = ref(store.savings);
const savingoptions = ref(store.savingoptions);
const bankSearch = ref('');

const getSortedOptionInfo = (savingId) => {
  const matchingOptions = savingoptions.value.filter(option => option.product === savingId)
  
  if (matchingOptions.length > 0) {
    return matchingOptions.sort((a, b) => b.intr_rate - a.intr_rate);
  } else {
    return [];
  }
}

const filteredDeposits = computed(() => {
  return savings.value.length > 0
    ? savings.value.filter(saving => saving.kor_co_nm.includes(bankSearch.value))
    : [];
});

const goDetail = function(saving){
  console.log(saving.id)
  router.push({name:'SavingDetail', params: {id: saving.id }})
}
</script>


<style scoped>
/* 추가적인 스타일링을 하려면 여기에 작성하세요 */
body {
  background-color: #f4f4f4;
}

.container {
  max-width: 800px;
  margin: 0 auto;
}

.bank-search {
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 5px;
  box-sizing: border-box;
}


.search-container {
  text-align: center;
}

.table-container {
  overflow-x: auto;
}

.month {
  font-weight: bold;
}

.bankname {
  font-weight: bold;
}

.productname {
  font-weight: bold;
}

.table {
  width: 100%;
  margin-top: 20px;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.table th, .table td {
  padding: 15px;
  text-align: left;
}

.table th {
  font-weight: bold;
}

.table tbody tr:nth-child(even) {
  background-color: #f9f9f9;
}

.table-striped tbody tr:nth-child(odd) {
  background-color: #e1e1e1; /* 줄무늬 스타일 추가 */
}

.table-hover tbody tr:hover {
  background-color: #d3d3d3; /* 호버 효과 추가 */
  cursor: pointer;
}

.option-info {
  margin-bottom: 4px;
}

.text-center {
  font-size: 35px;
  color: white;
  font-weight: bold;
  padding-top: 20px;
}

.productname {
  width: 40%; /* 상품명 칸 너비 조정 */
}

.optioninfo {
  width: 30%; /* 옵션 정보 칸 너비 조정 */
}
</style>