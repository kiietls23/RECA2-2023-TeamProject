if (data) {
    ShowMultipleMarkers(map, data);
}
if (current) {
    let locPosition = new kakao.maps.LatLng(current.Ma, current.La); // 마커가 표시될 위치를 geolocation으로 얻어온 좌표로 생성합니다
    // 마커를 표시합니다
    displayMarker(locPosition);
    let options = {
        enableHighAccuracy: false,
    };
    navigator.geolocation.getCurrentPosition(
        function (position) {
            let lat = position.coords.latitude; // 위도
            let lon = position.coords.longitude; // 경도
            let locPosition = new kakao.maps.LatLng(lat, lon); // 마커가 표시될 위치를 geolocation으로 얻어온 좌표로 생성합니다
            if (locPosition.La !== current.La && locPosition.Ma !== current.Ma) {
                console.log(locPosition, current);
                console.log('다름');
                setCurrent(locPosition);
                // 마커를 표시합니다
                displayMarker(locPosition);
            }
        },
        null,
        options,
        );
} else {
    let options = {
        enableHighAccuracy: false,
    };
    navigator.geolocation.getCurrentPosition(
        function (position) {
            let lat = position.coords.latitude; // 위도
            let lon = position.coords.longitude; // 경도
            let locPosition = new kakao.maps.LatLng(lat, lon); // 마커가 표시될 위치를 geolocation으로 얻어온 좌표로 생성합니다
            setCurrent(locPosition);
            // 마커를 표시합니다
            displayMarker(locPosition);
        },
        null,
        options,
    );}


    function setZoomable(zoomable) {
        map.setZoomable(zoomable);
    }
    setZoomable(false);

    let mapContainer = useRef(null); // 지도를 표시할 div
	let mapOption = {
		center: new kakao.maps.LatLng(33.450701, 126.570667), // 지도의 중심좌표
		level: 2, // 지도의 확대 레벨
		// 두번 클릭시 확대 기능을 막습니다
		disableDoubleClickZoom: true,
	};


    kakao.maps.event.addListener(map, 'dragend', function () {
        let centerCoord = map.getCenter();
        setCenterCoord(centerCoord);
        let message =
                    '지도를 드래그 하고 있습니다. ' +
                    '지도의 중심 좌표는 ' +
                    centerCoord.toString() +
                    ' 입니다.';
            });


