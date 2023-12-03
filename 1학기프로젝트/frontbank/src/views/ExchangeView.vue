<template>
  <div class="out">
    <img src="@/images/exchange.png" alt="" class="exchange-img">

    <div class="exchange-calculator">
      <div class="title-container">
        <h2 class="title">환율 계산기</h2>
      </div>

      <div class="search-section">
        <h5 class="search-title">나라를 고르고 금액을 입력해보세요</h5>
        <hr class="custom-hr">
        <p class="where-country">어느 나라로 떠나실건가요?</p>
        <select class="form-select" v-model="selectedCountry">
          <option disabled value="total">전체 국가</option>
          <option v-for="info in infos" :key=info.id>{{ info.cur_nm }}</option>
        </select>
      </div>
  
      <div class="input-section">
        <label for="foreign" class="where-country">{{ selectedCountry }}</label>
        <input type="number" class="form-control" v-model="amount" id="foreign" @input="handleAmountInput">
      </div>
  
      <div class="input-section">
        <label for="korea" class="where-country">원(\)</label>
        <input type="number" class="form-control" v-model="korea" id="korea" @input="handleKoreaInput">
      </div>


      <div v-if="amount" style="text-align: center;">
        <p>한국 원 : {{ korea.toLocaleString('ko-KR') }}\</p> 
        <p style="">↕</p>
        <p>{{ selectedCountry }} : {{ amount.toLocaleString('ko-KR') }}</p>
      </div>
    </div>
    
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useBankStore } from '@/stores/bank'

const amount = ref()
const korea = ref(null)
const store = useBankStore()
const selectedCountry = ref(null)
const result = ref(null)

onMounted(() => {
  store.getExchanges()
})

const calculateExchangeRate = () => {
  const selectedCountryInfo = store.exchanges.find(info => info.cur_nm === selectedCountry.value)

  if (selectedCountryInfo) {
    result.value = parseInt(amount.value) * parseInt(selectedCountryInfo.deal_bas_r.replace(',', ''))
    if(selectedCountry.value=='일본 옌'){
      korea.value = result.value/100
    }
    else{
      korea.value = result.value
    }
  } else {
    result.value = null
    korea.value = null
  }
}


const calculateExchangeRate1 = () => {
  const selectedCountryInfo = store.exchanges.find(info => info.cur_nm === selectedCountry.value)
  console.log(result.value)
  if (selectedCountryInfo) {
    result.value = (parseInt(korea.value) / parseInt(selectedCountryInfo.deal_bas_r.replace(',', '')));
    amount.value = result.value
    if(selectedCountry.value=='일본 옌'){
      amount.value = result.value*100
    }
    else{
      amount.value = result.value
    }
  } else {
    result.value = null
    amount.value = null
  }
}


const handleAmountInput = () => {
  if (amount.value < 0) {
    amount.value = 0
  }
  calculateExchangeRate()
}

const handleKoreaInput = () => {
  if (korea.value < 0) {
    korea.value = 0
  }
  calculateExchangeRate1()
}


const infos = ref(store.exchanges)

// watch([amount, selectedCountry], calculateExchangeRate)


</script>

<style scoped>
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

.out {
  position: relative;
  margin-top: 100px;
}

.exchange-calculator {
  position: relative;
  max-width: 450px;
  margin: auto;
  padding: 20px;
  border: 5px solid #888888;
  border-radius: 15px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  z-index: 1;
  background-color: white;
}

.title-container {
  text-align: center;
  margin-bottom: 20px;
}

.title {
  border: 2px solid #a3a0a0;
  border-radius: 10px;
  background-color: #60609b;
  color: white;
  padding: 10px;
  font-weight: bold;
}
.search-section {
  margin-bottom: 20px;
}

.search-title {
  font-weight: bold;
}

.custom-hr {
  border: 2px solid #a3a0a0;
}
.input-section {
  margin-bottom: 15px;
}

label {
  display: inline-block;
  margin-bottom: 5px;
}

input {
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
  border: 1px solid #ccc;
  border-radius: 4px;
}

select {
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.where-country {
  font-weight: bold;
}

.out {
  margin-top: 100px;
}
</style>
