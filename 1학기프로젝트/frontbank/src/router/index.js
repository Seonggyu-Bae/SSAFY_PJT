import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'

import ExchangeView from '@/views/ExchangeView.vue'
import FindBankView from '@/views/FindBankView.vue'
import CommunityView from '@/views/CommunityView.vue'

import DetailView from '@/views/DetailView.vue'
import CreatePostView from '@/views/CreatePostView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import MyPageView from '@/views/MyPageView.vue'
import ModifyPostView from '@/views/ModifyPostView.vue'

import DepositDetailView from '@/views/DepositDetailView.vue'
import SavingDetailView from '@/views/SavingDetailView.vue'
import ProductView from '@/views/ProductView.vue'
import ProfilePageView from '@/views/ProfilePageView.vue'


import RecommendView from '@/views/RecommendView.vue'
// import { useBankStore } from '@/stores/bank'
// const store = useBankStore()


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'homeView',
      component: HomeView
    },
    {
      path: '/product',
      name: 'product',
      component: ProductView
    },
    {
      path: '/exchange',
      name: 'exchange',
      component: ExchangeView
    },
    {
      path: '/findbank',
      name: 'findbank',
      component: FindBankView
    },
    {
      path: '/community',
      name: 'community',
      component: CommunityView,
 
    },


    {
      path: '/articles/:id',
      name: 'DetailView',
      component: DetailView
    },
    {
      path: '/create',
      name: 'CreatePostView',
      component: CreatePostView
    },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    },
    {
      path: '/mypage',
      name: 'MyPageView',
      component: MyPageView
    },
    {
      path: '/modifypost/:id',
      name: 'ModifyPostView',
      component: ModifyPostView
    },

    {
      path: '/depositdetail/:id',
      name: 'DepositDetail',
      component: DepositDetailView
    },

    {
      path: '/savingdetail/:id',
      name: 'SavingDetail',
      component: SavingDetailView
    },

    {
      path: '/profile',
      name: 'ProfilePageView',
      component: ProfilePageView
    },
    {
      path: '/recommend',
      name: 'RecommendView',
      component: RecommendView
    }

  ]


})

export default router
