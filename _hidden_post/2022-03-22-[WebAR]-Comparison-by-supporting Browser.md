---
layout: single
title: "[WebAR] Comparison by Spporting Browser"
---
### memo
- firefox 안됐었나???? 되는거 있었던거 같은데 모지?
- https://jsantell.com/webxr-polyfill/ 폴리필에 관한 글
- https://d2.naver.com/helloworld/0527763 네이버 랩스 글
- https://blog.lgcns.com/1911 브라우저에 대한 자세한 이야기
- https://github.com/Rufus31415/Simple-WebXR-Unity webxr unity 추가 에셋.. ?
- https://www.youtube.com/watch?v=ypSkIYpJjE8 이거 유튭 바야할지도...
- https://blog.mozilla.org/en/products/firefox/firefox-reality-now-available/ firefox reality 엔진? 
- 유료 플랫폼 studio로 할땐 호환 브라우저가 다른지 문의 해야함
- WebGL (canvas.getContext(‘webgl’) 또는 canvas.getContext(‘webgl2’))
- getUserMedia (navigator.mediaDevices.getUserMedia)
- deviceorientation (window.DeviceOrientationEvent)
- Web-Assembly/WASM (window.WebAssembly) 공부하기 

### 비교할 브라우저 선정
- 스탯카운터의 통계! https://gs.statcounter.com/
- 어떻게 하징 .. . .? 선정했다를 어떻게해지 구냥 일단함
- https://www.androidpolice.com/2021/07/11/best-android-web-browser/
### WebXR device api
- chrome ios 는 왜 안되는가?  https://github.com/immersive-web/webxr-samples/issues/111
- https://webkit.org/status/#specification-webxr webkit 개발 중이래
- android chrome 은 되고 ios chrome은 안되는 이유 => ios 는 모두 webkit을 써야함 https://www.quora.com/Does-Chrome-use-WebKit-on-iOS
- arcore ios 지원함 https://developers.google.com/ar/develop/ios/augmented-faces/quickstart
### openxr api
- 모르는데 ?..
- https://www.jonpeddie.com/news/xr-has-a-real-chance-now-thanks-to-khronos/
- Google은 최근 WebXR의 기본 백엔드로 OpenXR이 포함된 Chromium 81을 출시하여 Google Chrome 및 Microsoft Edge 브라우저에서 모든 OpenXR 호환 하드웨어를 사용할 수 있도록 했습니다.
- chrome for android 가 그럼 chromium 81을 쓰냐? https://www.androidpolice.com/2021/07/11/best-android-web-browser/
- 마지막으로 Microsoft는 혼합 현실 개발자 를 위한 OpenXR 샘플을 오픈 소스로 출시하여 OpenXR을 사용하여 HoloLens 2의 전체 기능에 액세스하는 방법을 보여줍니다. Firefox Reality 브라우저는 또한 OpenXR을 사용하여 HoloLens 2 플랫폼에서 실행됩니다.(요거 뺴던지)
- https://www.businesswire.com/news/home/20190729005227/en/Khronos-Releases-OpenXR-1.0-Specification-Establishing-a-Foundation-for-the-AR-and-VR-Ecosystem
- https://developer.mozilla.org/en-US/docs/Web/API/WebXR_Device_API

***
### framework AR.js
- 다된다
- 다중카메라 잘 안될수도있음
- ios에서 위치기반 경고 팝업창이 아농ㄹ 수 있다. 

### react-xr
- react three fiber로 aframe threejs babylon 얘네랑 같이 묶어야할지도 ...?
-  webxr api 그냥 를 쓰는거 같아서 ...

### XR engine
- WebGL client deployable to iOS, Android and desktop

***
### 8thwall
- https://www.8thwall.com/docs/web/
- https://www.8thwall.com/docs/web/#web-browser-requirements
- https 해야함
### onirix
- .com 만 가능했던거 같은데 어디서 봤지?
- https://docs.onirix.com/onirix-sdk/web-ar#compatibility-and-browser 지원 브라우저
- Onirix AR Engine SDK is compatible with the following browsers: 이렇게 되어있는데 그럼 다른 방법으로 개발하면 지원하는 browser가 다르다는건가?
- 잉? 문화재단꺼 safari말고도 firefox랑 되는거 같은뎅? 아닌가? 
- https 해야한다는 말 .. .없눈뎅 ?.. 

### blippar 
- 기업에 문의
- demo가 ios 크롬은 되고 safari는 안됨 아이패드
- ios safari 핸드폰에서는 스캔은 되는데 모델이 안나옴
- 버전에 대한 구체적인 정보와 왜 안되는지 알려조

### zappworks
- unity 베타 버전인거 같은데?

### AWE
- https://awe.media/support/supported_devices
- https://browser.geekbench.com/ios-benchmarks 600 점 이상의 기기 권장 
- https://browser.geekbench.com/android-benchmarks GeekBench 테스트

### letsee
- - WebGL (canvas.getContext(‘webgl’) 또는 canvas.getContext(‘webgl2’))
- getUserMedia (navigator.mediaDevices.getUserMedia)
- deviceorientation (window.DeviceOrientationEvent)
- Web-Assembly/WASM (window.WebAssembly)
- Letsee WebAR SDK의 실행은 https 를 통해서만 가능합니다. 이것은 브라우저가 카메라에 접근하기 위해 필요합니다.

***
### unity 
- Google Chrome on Android (Supports both AR and VR sessions).
- Samsung Internet Browser on Android (Supports both AR and VR sessions).

### Wonderland engine
- 게임 샘플 https://github.com/WonderlandEngine/wastepaperbin-ar
- https://discordapp.com/channels/758943204715659264/759287532902416435/838472409807323136
- webxr api, 8thwall로 구현 가능하다라고하는게 맞지않으깡 .. . ?
- https://wonderlandengine.com/about/features/#highlights webgl2 쓴다
- Wonderland Engine은 WebXR(WebVR 및 WebAR)용으로 특별히 설계되었습니다. 8thwall 및 AR.js, 컨트롤러 입력 및 WebXR 1.0 장치 API 지원과의 통합이 제공됩니다.
