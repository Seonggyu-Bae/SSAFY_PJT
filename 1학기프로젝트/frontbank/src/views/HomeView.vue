<template>
  <div class="background d-flex justify-content-around" style="margin: 0px;">
    <div class="main-container">
      <br>
      <div class="d-flex justfiy-content-between carousel">
      <div class="carousel-container">
        <div id="carouselExampleAutoplaying" class="carousel slide" data-bs-ride="carousel">
          <div class="carousel-inner">
            <div class="carousel-item active">
              <img @click="router.push({name:'product'})" src="@/images/first.png" class="d-block w-100" alt="first-img">
            </div>
            <div class="carousel-item">
              <img @click="router.push({name:'exchange'})" src="@/images/second.png" class="d-block w-100" alt="second-img">
            </div>
            <div class="carousel-item">
              <img @click="router.push({name:'findbank'})" src="@/images/third.png" class="d-block w-100" alt="third-img">
            </div>
          </div>
          <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>
        </div>
        <div class="additional-images">
            <img src="@/images/daegu.png" alt="daegu" class="daegu">
            <!-- <img src="@/images/kakaobank.png" alt="kakaobank" class="kakaobank"> -->
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
const router = useRouter()
const isInfoLoaded = ref(store.isInfoLoaded)
const communityPosts = ref([])
const bg = document.querySelector('.background')
const token = store.token
const isLogin = computed(() =>{
  if(token==null){
    return false
  }
  else{
    return true
  }
})

</script>

<style scoped>
.carousel-and-image {
  display: flex;
  flex-direction: column; /* 세로로 정렬 */
  align-items: center; /* 가운데 정렬 */
}

.carousel-container {
  max-width: 800px;
  margin: 0 auto;
  display: flex;
  flex-wrap: nowrap; /* 가로로 나열 */
}

.carousel-container img {
  border-radius: 30px;
  margin-right: 10px; /* 이미지 사이 간격 조정 */
}
.carousel-item img {
  border-radius: 30px;
}

/* .main-container {
  padding: 50px;
} */

/* img[alt="daegu-image"] {
  border-radius: 30px;
  margin-top: 20px;
} */

.main-title {
  font-size: 2rem;
  margin-bottom: 20px;
}

.welcome-message {
  font-size: 1.2rem;
  font-weight: bold;
  color: #0c0c0c; /* Blue color, you can change it */
  margin-bottom: 30px;
}

.btn-primary {
  background-color: #007bff;
  color: #fff;
  padding: 10px 20px;
  font-size: 1rem;
  text-decoration: none;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.btn-primary:hover {
  background-color: #0056b3; /* Darker shade of blue on hover */
}

.background {
  position: relative;
  overflow: hidden;
  background-image: url("@/images/mainpage6.png");
  background-size: cover;
  background-position: top left;
  height: 100vh;
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  background-repeat: round;
}

.features-section {
  margin-top: 50px;
}

.feature-card {
  border: 1px solid #929090;
  border-radius: 5px;
  padding: 10px;
  margin: 10px;
}

.feature-card h3 {
  font-size: 1.2rem;
}

.feature-card p {
  font-size: 1rem;
}

.community-main {
  width: 600px;
  max-width: 800px;
  margin: 50px auto;
  padding: 20px;
  background-color: rgba(218, 196, 196, 0.8);
  border-radius: 10px;
  box-shadow: 0 0 20px rgba(5, 5, 5, 0.1);
}

.community-title {
  font-weight: bold;
  padding-left: 50px;
  padding-right: 20px;
}

.title {
  font-weight: bold;
  font-size: 23px;
}

.content {
  font-style: italic;
}

.comparision{
  width: 600px;
  height: 380px;
}

.carousel-container {
  max-width: 100%;
  margin: 0 auto;
  display: flex;
  flex-wrap: nowrap; /* 가로로 나열 */
}

.carousel-container img {
  border-radius: 30px;
  margin-right: 10px; /* 이미지 사이 간격 조정 */
}
.carousel-item img {
  border-radius: 30px;
}

.additional-images {
  display: flex;
  flex-direction: column;
  margin-top: 20px; /* daegu.png와의 간격 조정 */
}

.additional-images img {
  border-radius: 30px;
  margin-bottom: 10px; /* 이미지 사이 간격 조정 */
}

/* ... (existing styles) */

.daegu {
  width: 350px;
  height: 540px;
  margin-left: 50px;
}

.carousel {
  margin-top: 10px;
}
</style>