<template>
  <img src="@/images/navy-background.png" alt="background" class="full">
  <h1 class="intro">예적금 상품을 확인하세요</h1>
  <div class="container">
    <button @click="selected='예금'" class="btn btn-primary">예금 상품</button>
    <br>
    <button @click="selected='적금'" class="btn btn-primary">적금 상품</button>
    <Deposit  v-if="selected==='예금'"/>
    <Saving v-if="selected==='적금'"/>
  </div>
  <img src="@/images/growthgraph.png" alt="graph-img" class="graph-img">
</template>

<script setup>
import { ref, onMounted } from 'vue'
import Deposit from '@/components/Deposit.vue';
import Saving from '@/components/Saving.vue'
import { useBankStore } from '../stores/bank';

const store = useBankStore()

const selected = ref('')

onMounted(()=>{

    store.loaddepositdata()
    store.loaddepositoptions()
    store.loadsavingdata()
    store.loadsavingoptions()

})
</script>

<style scoped>
.full {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: -1;
}

.container {
  margin-top: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.btn-secondary {
  background-color: #dbd8d8;
  border: 2px;
  color: #030303;
  font-weight: bold;
  font-size: 20px;
  margin: 5px;
  width: 150px;
  height: 40px;
}

.intro {
  padding-top: 100px;
  color: aliceblue;
  font-weight: bold;
  text-align: center;
  padding-bottom: 50px;
}

.graph-img {
  width: 800px;
  height: 350px;
  margin-left: 600px;
}

.btn-primary {
  background-color: #3498db;
  border: none;
  color: #fff;
  font-weight: bold;
  font-size: 20px;
  margin: 5px;
  padding: 10px 20px;
  width: 150px;
  cursor: pointer;
  border-radius: 5px;
  transition: background-color 0.3s ease;
}

.btn-primary:hover {
  background-color: #2980b9;
}
</style>