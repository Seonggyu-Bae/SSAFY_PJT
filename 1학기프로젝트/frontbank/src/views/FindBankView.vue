<template>
    <div class="main">
        <div class="header">
          <img src="@/images/find.png" alt="find" class="find">
          <h1 class="main-title" style="text-align: center;">주변 은행을 검색해보세요</h1>
        </div>
      <div class="map_wrap">
        <div id="map" style="width:100%; height: 65vh; position:relative; overflow:hidden;"></div>
        <div id="menu_wrap" class="bg_white">
          <div class="option">
            <div>
              <form @submit.prevent="changeStatus" class="search-form">
                <div class="search-container"></div>
                <label for="keyword">검색어</label>
                <input type="text" id="keyword" v-model="keyword" class="form-control" placeholder="은행명을 입력하세요">
                <button type="submit" class="btn btn-primary">검색</button>
              </form>
            </div>
          </div>
          <ul id="placesList"></ul>
          <div id="pagination"></div>
        </div>
      </div>
    </div>
  </template>


<script setup>
import { ref , onMounted, watch } from 'vue'

const keyword = ref('')
const isClicked = ref(false)
const changeStatus = function(){
  isClicked.value = !isClicked.value
}
var markers = [];
let map = null;
let infowindow = null;
let ps = null;



const initMap = () => {
  var mapContainer = document.getElementById('map'), // 지도를 표시할 div 
    mapOption = {
        center: new kakao.maps.LatLng(37.566826, 126.9786567), // 지도의 중심좌표
        level: 3 // 지도의 확대 레벨
    }

      // 지도를 생성합니다    
  map = new kakao.maps.Map(mapContainer, mapOption); 

  // 장소 검색 객체를 생성합니다
  ps = new kakao.maps.services.Places();  

  // 검색 결과 목록이나 마커를 클릭했을 때 장소명을 표출할 인포윈도우를 생성합니다
  infowindow = new kakao.maps.InfoWindow({zIndex:1});
}

  
// 키워드로 장소를 검색합니다
watch(isClicked, (newValue, oldValue) =>{
  searchPlaces();
})
// 키워드 검색을 요청하는 함수입니다
function searchPlaces() {

    var keyword = document.getElementById('keyword').value;

    if (!keyword.replace(/^\s+|\s+$/g, '')) {
        alert('키워드를 입력해주세요!');
        return false;
    }

    // 장소검색 객체를 통해 키워드로 장소검색을 요청합니다
    ps.keywordSearch( keyword, placesSearchCB); 
}

// 장소검색이 완료됐을 때 호출되는 콜백함수 입니다
function placesSearchCB(data, status, pagination) {
    if (status === kakao.maps.services.Status.OK) {

        // 정상적으로 검색이 완료됐으면
        // 검색 목록과 마커를 표출합니다
        displayPlaces(data);

        // 페이지 번호를 표출합니다
        displayPagination(pagination);

    } else if (status === kakao.maps.services.Status.ZERO_RESULT) {

        alert('검색 결과가 존재하지 않습니다.');
        return;

    } else if (status === kakao.maps.services.Status.ERROR) {

        alert('검색 결과 중 오류가 발생했습니다.');
        return;

    }
}

// 검색 결과 목록과 마커를 표출하는 함수입니다
function displayPlaces(places) {

    var listEl = document.getElementById('placesList'), 
    menuEl = document.getElementById('menu_wrap'),
    fragment = document.createDocumentFragment(), 
    bounds = new kakao.maps.LatLngBounds(), 
    listStr = '';
    
    // 검색 결과 목록에 추가된 항목들을 제거합니다
    removeAllChildNods(listEl);

    // 지도에 표시되고 있는 마커를 제거합니다
    removeMarker();
    
    for ( var i=0; i<places.length; i++ ) {

        // 마커를 생성하고 지도에 표시합니다
        var placePosition = new kakao.maps.LatLng(places[i].y, places[i].x),
            marker = addMarker(placePosition, i), 
            itemEl = getListItem(i, places[i]); // 검색 결과 항목 Element를 생성합니다

        // 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
        // LatLngBounds 객체에 좌표를 추가합니다
        bounds.extend(placePosition);

        // 마커와 검색결과 항목에 mouseover 했을때
        // 해당 장소에 인포윈도우에 장소명을 표시합니다
        // mouseout 했을 때는 인포윈도우를 닫습니다


        // 마커에 click 했을때
        // 해당 장소에 인포윈도우에 장소명, 큰지도보기, 길찾기 링크를 보여줍니다 ㅎㅎ
        // 노가다로 구현 성공
        // 지도를 click 하면 사라집니다
        (function(marker, title) {
          var iwContent = `<div style="padding:10px 40px 40px 40px ">${title}<br><div style="display: flex;"><a style="align-items: flex-start;" href="https://map.kakao.com/link/map/${title},${places[i].y},${places[i].x}" style="color:blue;" target="_blank">큰지도보기</a>&nbsp;&nbsp;&nbsp;&nbsp<a style="align-items: flex-end;" href="https://map.kakao.com/link/to/${title},${places[i].y},${places[i].x}" style="color:blue" target="_blank">길찾기</a></div></div>`;
          var iwPosition = new kakao.maps.LatLng(places[i].y, places[i].x);
          var infowindow = new kakao.maps.InfoWindow({
                position : iwPosition, 
                content : iwContent 
                })
            kakao.maps.event.addListener(marker, 'click', function() {

                infowindow.open(map ,marker)
            });

            kakao.maps.event.addListener(map, 'click', function() {
                infowindow.close();
            });
        })(marker, places[i].place_name);

        // 검색결과 항목에 mouseover 했을때
        // 1. 해당 장소의 인포윈도우에 장소명을 표시합니다
        // 2. 해당 장소를 기준으로 지도 범위를 재 설정합니다.
        // mouseout 했을 때는 인포윈도우를 닫습니다
        (function(marker, title) {
            itemEl.onmouseover =  function () {
                // 1
                displayInfowindow(marker, title, placePosition);
                // 2
                map.setBounds(bounds);
            };

            itemEl.onmouseout =  function () {
                infowindow.close();
            };
        })(marker, places[i].place_name);

        fragment.appendChild(itemEl);
    }

    // 검색결과 항목들을 검색결과 목록 Element에 추가합니다
    listEl.appendChild(fragment);
    menuEl.scrollTop = 0;

    // 검색된 장소 위치를 기준으로 지도 범위를 재설정합니다
    map.setBounds(bounds);
}

// 검색결과 항목을 Element로 반환하는 함수입니다
function getListItem(index, places) {

    var el = document.createElement('li'),
    itemStr = '<span class="markerbg marker_' + (index+1) + '"></span>' +
                '<div class="info">' +
                '   <h5>' + places.place_name + '</h5>';

    if (places.road_address_name) {
        itemStr += '    <span>' + places.road_address_name + '</span>' +
                    '   <span class="jibun gray">' +  places.address_name  + '</span>';
    } else {
        itemStr += '    <span>' +  places.address_name  + '</span>'; 
    }
                 
      itemStr += '  <span class="tel">' + places.phone  + '</span>' +
                '</div>';           

    el.innerHTML = itemStr;
    el.className = 'item';

    return el;
}

// 마커를 생성하고 지도 위에 마커를 표시하는 함수입니다
function addMarker(position, idx, title) {
    var imageSrc = 'https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_number_blue.png', // 마커 이미지 url, 스프라이트 이미지를 씁니다
        imageSize = new kakao.maps.Size(36, 37),  // 마커 이미지의 크기
        imgOptions =  {
            spriteSize : new kakao.maps.Size(36, 691), // 스프라이트 이미지의 크기
            spriteOrigin : new kakao.maps.Point(0, (idx*46)+10), // 스프라이트 이미지 중 사용할 영역의 좌상단 좌표
            offset: new kakao.maps.Point(13, 37) // 마커 좌표에 일치시킬 이미지 내에서의 좌표
        },
        markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imgOptions),
            marker = new kakao.maps.Marker({
            position: position, // 마커의 위치
            image: markerImage 
        });

    marker.setMap(map); // 지도 위에 마커를 표출합니다
    markers.push(marker);  // 배열에 생성된 마커를 추가합니다

    return marker;
}

// 지도 위에 표시되고 있는 마커를 모두 제거합니다
function removeMarker() {
    for ( var i = 0; i < markers.length; i++ ) {
        markers[i].setMap(null);
    }   
    markers = [];
}

// 검색결과 목록 하단에 페이지번호를 표시는 함수입니다
function displayPagination(pagination) {
    var paginationEl = document.getElementById('pagination'),
        fragment = document.createDocumentFragment(),
        i; 

    // 기존에 추가된 페이지번호를 삭제합니다
    while (paginationEl.hasChildNodes()) {
        paginationEl.removeChild (paginationEl.lastChild);
    }

    for (i=1; i<=pagination.last; i++) {
        var el = document.createElement('a');
        el.href = "#";
        el.innerHTML = i;

        if (i===pagination.current) {
            el.className = 'on';
        } else {
            el.onclick = (function(i) {
                return function() {
                    pagination.gotoPage(i);
                }
            })(i);
        }

        fragment.appendChild(el);
    }
    paginationEl.appendChild(fragment);
}

// 검색결과 목록 또는 마커를 클릭했을 때 호출되는 함수입니다
// 인포윈도우에 장소명을 표시합니다
function displayInfowindow(marker, title) {
    var content = '<div style="padding:5px;z-index:1;">' + title + '</div>'
    infowindow.setContent(content);
    infowindow.open(map, marker);
}

 // 검색결과 목록의 자식 Element를 제거하는 함수입니다
function removeAllChildNods(el) {   
    while (el.hasChildNodes()) {
        el.removeChild (el.lastChild);
    }
}












onMounted(()=>{
  if (window.kakao && window.kakao.maps) {
    initMap();
  }
})



</script>

<style scoped>

.map_wrap, .map_wrap * {margin:0;padding:0;font-family:'Malgun Gothic',dotum,'돋움',sans-serif;font-size:12px;}
.map_wrap a, .map_wrap a:hover, .map_wrap a:active{color:#000;text-decoration: none;}
.map_wrap {position:relative;width:100%;height:500px;}
#menu_wrap {position:absolute;top:0;left:0;bottom:0;width:250px;margin:10px 0 30px 10px;padding:5px;overflow-y:auto;background:rgba(255, 255, 255, 0.7);z-index: 1;font-size:12px;border-radius: 10px;}
.bg_white {background:#fff;}
#menu_wrap hr {display: block; height: 1px;border: 0; border-top: 2px solid #5F5F5F;margin:3px 0;}
#menu_wrap .option{text-align: center;}
#menu_wrap .option p {margin:10px 0;}  
#menu_wrap .option button {margin-left:5px;}

.header {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 10px;
  margin-top: 30px;
  margin-bottom: 30px;
}

.find {
  width: 70px;
  height: 60px;
  margin-right: 10px;
}

.main-title {
  font-weight: bold;
  margin: 0;
  text-align: center;
}

.search-form {
  text-align: center;
  font-weight: bold;
  margin: 8px;
}

.search-container {
  display: flex;
}

#keyword {
  flex: 1;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
  margin-right: 8px;
  font-weight: bold;
  margin-bottom: 8px;
}

.btn-primary {
  background-color: #0c0c0c;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  padding: 8px 16px;
  font-weight: bold;
}

.btn-primary:hover {
  background-color: #45a049;
}

.test{
  text-align: center;
  text-align: justify;
  align-content: space-around;
  align-items: flex-start;
}

</style>
