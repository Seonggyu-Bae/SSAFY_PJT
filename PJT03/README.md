오늘의 관통 프로젝트는

이번 한 주동안 배운 HTML, CSS, Bootstrap 을 활용한 반응형 웹 포트폴리오 사이트를 만드는 것이다.

나름대로 한다고 했으나 조잡하기 그지없다.

그래도 각 영역에서 원하는 요구조건을 써본것에 만족한다.

손에 익으면 금방할거같은데 아직 익숙하지도 않고 좀 그렇다...

크게 재미있는지도 모르겠다.

# 1. Header

Header에서는  Bootstrap의 NavBar 컴포넌트를 사용하여

클릭시 각 화면 구역으로 스크롤하여 이동하는 것을 구현했다.

# 2. frontpage

frontpage에서는 flex를 사용해서 사이드 아이콘과 텍스트영역 구간을 설정하였고

크기 조정시(770px 이하) 사진과 아이콘에 display: none 처리를 하였다.

# 3. my-intro

마찬가지로 flex를 사용하여 좌 우 영역을 나누고

크기조정시  flex-direction을 row에서 column으로 변경하였다.

# 4. Skills

카드 컴포넌트를 쓰긴했는데 그림자 적용을 못했고

Wrap을 사용하여 화면이 넓을때는 4개가 한줄에

좀 작을때는 한줄에 2개

젤 작을때는 한줄에 1개로 표현함

# 5. project

크기조정시 flex-direction을 row에서 column으로 변경하였다.

# 6.Contact

Bootstrap Input 활용

크기 조정 시, 
• 오른쪽 아이콘 영역 display: none 처리
• 이름, 이메일 입력 부분 flex-direction: column 으로 변경함
