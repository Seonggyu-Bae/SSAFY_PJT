관통프로젝트 10(FINAL PJT)
=============

주제 : 금융 상품 비교 애플리케이션
-------------

### 목표

1. [ 예금 & 적금 금리 비교](#1.-예금-&-적금-금리-비교)  

2. 신혼 여행을 위한 환율 계산기  

3. 내 집 주변 은행 검색  

4. 나에게 맞는 상품 추천  

---

### 프로젝트에 사용한 것

- API
  - [한국수출입은행 환율정보 API](https://www.koreaexim.go.kr/ir/HPHKIR020M01?apino=2&viewtype=C)
  - [카카오맵 API](https://apis.map.kakao.com/)
  - [금융감독원 API](https://finlife.fss.or.kr/finlife/api/fdrmDpstApi/list.do?menuNo=700052)
- 주요 라이브러리
  - BootStrap
  - [vue-chartjs](https://vue-chartjs.org/)
  - Django REST Framework
- 사용 아키텍처
  - [Django REST Framwork](https://www.django-rest-framework.org/) & [Vue3](https://vuejs.org/) & [Pinia](https://pinia.vuejs.org/)

    ![Alt text](images/good.png)

### 팀원 정보

- 팀장 : [배성규](https://github.com/Seonggyu-Bae)
- 팀원 : [이주미](https://github.com/iamjumi)

### 업무 분담 내역

- 배성규
  - 회원 커스터마이징
  - 예적금 금리비교
  - 근처 은행 검색
  - 커뮤니티
  - 프로필 페이지
- 이주미
  - 환율계산기
  - 전체 애플리케이션 CSS

---

### 설계 내용(아키텍처 등) 및 실제 구현 정도

- 설계 전 목업
    ![Alt text](images/01_메인페이지.png)
    ![Alt text](images/03_예적금금리비교_전체조회.png)
    ![Alt text](images/04_예적금금리비교_상세조회.png)
    ![Alt text](images/05_환율계산기.png)
    ![Alt text](images/06_근처은행검색.png)
    ![Alt text](images/07_커뮤니티게시판.png)
    ![Alt text](images/08_금융추천알고리즘.png)

[실제 구현 정도](#서비스-대표-기능들에-대한-설명)  

--- 

### 데이터베이스 모델링(ERD)

![Alt text](images/erd.png)

---

### 금융 상품 추천 알고리즘에 대한 기술적 설명

- 랜덤 알고리즘을 이용한 무작위 추천

- [주식과 코인에 빚투를 하고 실패하여 개인회생의 문을 두드리는 청년들이 많다](https://www.mk.co.kr/news/society/10880256)

- 우리는 무리한 투자보다는 원금이 보장되는 예적금을 통해 결혼자금, 주택자금을 마련하자!

---

### 서비스 대표 기능들에 대한 설명

#### 메인 페이지

![Alt text](image.png)

1. (왼쪽) Carousel 을 이용한 사이트 기능 홍보 및 바로가기 기능

2. (오른쪽) 은행별 상품 홍보(광고) 배너

#### 1. 예금 & 적금 금리 비교

1. 원하는 상품 유형(예금, 적금 버튼을 클릭)
   
    ![Alt text](images/image.png)

2. 리스트에서 원하는 상품을 선택하거나 원하는 은행이 있다면 검색후 상품 선택
   
    ![Alt text](images/image-1.png)
   
    ![Alt text](images/image-2.png)

3. 상세 정보를 읽고 상품이 마음에 든다면 찜 하기 가능
   
    ![Alt text](images/image-5.png)

---

#### 2. 환율계산기

1. 여행 목적지를 선택
    ![Alt text](images/image-7.png)

2. 양쪽 모두 입력이 가능함
   
   - 목적지 -> 원화
   
   - 원화   -> 목적지
     
     ![Alt text](images/image-6.png)

#### 3. 은행 검색

1. 검색어를 입력 (ex. 서울 강남구 국민은행)
   
    ![Alt text](images/image-8.png)

2. 검색결과 확인
   
    ![Alt text](images/image-9.png)

#### 4. 나에게 맞는 상품 추천

1. 마이페이지로 이동
   
    ![Alt text](images/image-12.png)

2. 마이페이지에는 내가 찜한 상품확인과 상품들의 금리를 바 차트로 확인가능

3. 금융상품버튼을 눌러 페이지 이동

4. 추천받기 버튼을 눌러 랜덤으로 상품 추천을 받는다
    ![Alt text](images/image-10.png)

---

### 기타(느낀 점 후기 등)

배성규 : 첫 프로젝트라 정해진 기간안에 모든 기능을 구현 할 수 있을지에 대한 부담감이 컸다. 그래도 결국 하면된다는 것을 이번에도 확인 할 수 있었다. 필수 기능들을 다 구현할 수 있어서 다행이라 생각하고 진이 빠져서 추가 기능을 구현하지못한것은 아쉽다. 그리고 코드의 가독성과 디테일들을 챙기지 못해서 좀 아쉬운데 수정 할 기분이 나면 수정 해야겠다.

이주미 : 사실 나한테는 이번 필수 기능들이 어려운 편에 속했다. 그래서 오히려 그것을 발판으로, 이번 관통 프로젝트를 기회로 vue 공부를 더 많이 할 수 있었고 이것저것 더 찾아보게 되는 계기가 된 것 같다. 이번 프로젝트는 날 발전시킨 좋은 시간이었다.