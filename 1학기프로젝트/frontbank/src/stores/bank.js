import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useBankStore = defineStore('bank', () => {

  const API_URL = 'http://127.0.0.1:8000'
  const router = useRouter()

  // 게시글, 댓굴, 환율정보, 모든유저정보(id, username), 로그인유저정보
  const articles = ref(null)
  const comments = ref(null)
  const exchanges = ref(null)
  const users = ref(null)
  const user = ref(null)

  // 예적금 상품 정보
  const deposits = ref(null)
  const depositoptions = ref(null)
  const savings = ref(null)
  const savingoptions = ref(null)


  
  // 로그인 관련 정보
  const token = ref(null)
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })




  // DRF에 article 조회 요청을 보내는 action
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) =>{
        articles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  // 모든 사용자들의 id와 이름을 조회해서 users에 저장하는 함수
  const getUsers = function () {
    axios({
      method: 'get',
      url: `${API_URL}/user/list/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) =>{
        users.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  // DRF에 user 조회 요청을 보내는 action
  const getUser = function () {
      axios({
        method: 'get',
        url: `${API_URL}/user/`,
        headers: {
          Authorization: `Token ${token.value}`
        }
      })
        .then((res) =>{
          console.log(res)
          user.value = res.data
        })
        .catch((err) => {
          console.log(err)
          user.value = null
        })
      
  }



  const signUp = function (payload) {
    const { username, password1, password2, email} = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2, email
      }
    })
      .then((res) => {
        logIn(email, password1)
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const logIn = function (email, password) {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        email, password
      }
    })
      .then((res) => {
        token.value = res.data.key
      })
      .then((res) => {
        requestDeposits()
        requestSavings()

      })
      .then((res) => {
        loadsavingdata()
        loadsavingoptions()
        loaddepositoptions()
        loaddepositdata()
      })
      .then((res) => {
        getUser()
      })
      .then((res) => {
        router.push({name:'homeView'})
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const addUserData = function (payload) {
    const { nickname, age, money, salary } = payload
    axios({
      method: 'PUT',
      url: `${API_URL}/user/`,
      headers: {
        Authorization: `Token ${token.value}`
      },
      data: {
        nickname, age, money, salary
      }
    })
      .then((res) => {
        console.log(res)
        getUser()
      })
      .then(() =>{
        router.go(0)
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const logOut = function () {
    axios
      .post(`${API_URL}/accounts/logout/`)
      .then((res) => {
        token.value = null;
        user.value = null;
        localStorage.removeItem('bank');
        
      })
      .catch((err) => {
        console.log(err);
      });
  };

  // url에 게시글 pk를 넘겨서 그 게시글의 댓글만 불러옴
  const getComments = function (article_pk) {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/${article_pk}/comments/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) =>{
        // console.log(res)
        comments.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  // DRF에 exchanges 조회 요청을 보내는 action
  const getExchanges = function () {
    axios({
      method: 'get',
      url: `${API_URL}/exchanges/exchanges/`,
      // headers: {
      //   Authorization: `Token ${token.value}`
      // }
    })
      .then((res) =>{
        // console.log(res)
        exchanges.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const goMypage = function(){
    if(token==null){
      router.push({ name: 'LogInView' })
    }
    else{
      router.push({ name: 'MyPageView' })
    }
  }


  const loaddepositdata = function () {
    axios({
      method: 'get',
      url: `${API_URL}/deposits/deposit-products/`,
      // headers: {
      //   Authorization: `Token ${token.value}`
      // }
    })
      .then((res) =>{
        console.log('예금상품저장 (store에) 완료')
        deposits.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const loaddepositoptions = function () {
    axios({
      method: 'get',
      url: `${API_URL}/deposits/deposit-product-options/`,
      // headers: {
      //   Authorization: `Token ${token.value}`
      // }
    })
      .then((res) =>{
        console.log('예금옵션저장 (store에) 완료')
        depositoptions.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }


  const loadsavingdata = function () {
    axios({
      method: 'get',
      url: `${API_URL}/deposits/saving-products/`,
      // headers: {
      //   Authorization: `Token ${token.value}`
      // }
    })
      .then((res) =>{
        console.log('적금 상품 저장 (store에) 완료')
        savings.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const loadsavingoptions = function () {
    axios({
      method: 'get',
      url: `${API_URL}/deposits/saving-product-options/`,
      // headers: {
      //   Authorization: `Token ${token.value}`
      // }
    })
      .then((res) =>{
        console.log('적금 options 저장 (store에) 완료')
        savingoptions.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const requestDeposits = function(){
    axios({
      method: 'get',
      url: `${API_URL}/deposits/save-deposit-products/`,
      // headers: {
      //   Authorization: `Token ${token.value}`
      // }
    })
      .then((res) =>{
        console.log('Deposit Data Saved in DB')
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const requestSavings = function(){
    axios({
      method: 'get',
      url: `${API_URL}/deposits/save-saving-products/`,
      // headers: {
      //   Authorization: `Token ${token.value}`
      // }
    })
      .then((res) =>{
        console.log('Saving Data Saved in DB')
      })
      .catch((err) => {
        console.log(err)
      })
  }





  return { articles, comments, exchanges, users, user, deposits, savings, depositoptions, savingoptions, API_URL, 
    getArticles, getComments, getExchanges, getUsers, getUser, signUp, logIn, 
    token, isLogin,
    logOut, goMypage, addUserData,
    loaddepositdata, loaddepositoptions, loadsavingdata, loadsavingoptions, requestDeposits, requestSavings, }
}, { persist: true })

