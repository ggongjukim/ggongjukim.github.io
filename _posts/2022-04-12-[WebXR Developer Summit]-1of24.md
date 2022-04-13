---
layout: single
title: "[WebXR Developer Summit] 01 of 24 Introduction"
categories : WebXR
tag : [WebXR, WebXRSummit]
toc : true
---

## |  The wider Web
- 이 문서는 [WebXR Developer Summit](https://www.youtube.com/watch?v=ZGlcrFxbsHc&list=PLKNvd3dXSaxBlJFtM1YAJhCLbFQiIPQsL&index=2) 을 필기 및 공부한 내용입니다 틀린게 있다면 댓글남겨주세요!
- wider Web의 세 파트
  - display mode
  - 과거에 기본적으로 flat screen 형태의 하나의 디스플레이만 가능 - > 키보드, 마우스, 터치스크린 + 펜, 음성 + 다른형태의 control or page controls overlay controls spatial 3d contols
  - 발표자 : WebXR의 발전을 추적하는 Immersive Web Weekly 뉴스레터의 편집자인 Trevor Flowers

### | Three display modes: 
<img src = "https://user-images.githubusercontent.com/75241542/163098731-a793d948-0028-445a-acd5-21bbb6618a0e.png" width="40%" height = "40%">

- 세 파트 있음
- Three display mode
  - Flat display
  - portal display
  - immersive display  
  - 오랫동안 웹은 flat 형태로 crt 모니터와 같이 유지했다 그 다음에는 태블릿과 스마트폰의 형태로 있었다 십년 동안 자연스러운 반응형 웹을 만들기 위해 노력했다 -> 이것은 엄청난 작업이 걸렸다 CSS의 모든 복잡성과 미디어 쿼리의 복잡성을 필요로 했기 때문에-> 이 핵심 아이디어는 실제로 웹을 좋은 위치에 위치시킵니다 두가지 추가 디스플레이 유형으로 병합됨에 따라 
  - portal display and immersive display
  - immersive display는 VR혹은 AR glasses을 생각하면 쉽다 
  - 오늘 모든 하드웨어를 처리하도록 만든 WebXR에 대해 이야기할때 몰입형 디스플레이를 기본값으로 이야기하게된다
  - 스마트폰으로 flat display 형태로 콘텐츠를 볼 수 있고, 스마트폰을  모션 정보를 얻은 다음 스마트폰을 들고있으면 포털로 사용할 수 있다. immersice displays도 물론  .. ? 4:40
  - 

### | Three control types: 
<img src = "https://user-images.githubusercontent.com/75241542/163107908-3c904c1c-4228-40f5-948a-3fe63bc00c1c.png" width="40%" height = "40%">

- 디스플레이 모드 이외에도 세가지 제어 유형이 있다.
- page controls, overlay controls , spatial controls
- page controls : 일반적인 html 의 page 컨트롤(button, link, text, images)
- overlay controls : portal mode에 있고 flat screen을 통해 공간을 보고있을떄  
  : 3D 공간 세계에 얹어있는 것처럼 보는 control이다
- spatial controls : portal mode와 immersive display ahen spatial controls 있다  
  : 3D 공간에서 촉각 컨트롤을 만드는 자료가 있다.
  : 공간 제어를 위한 새로운 장르의 디자인 기능을 도입했다
  : flat web에 대한 모든 반응형 복잡성은 폭발적으로 증가하고 있다 -> 플랫모드에서 페이지 컨트롤을 디자인 하는것이 아니라 세가지 디스플레이모드와 세가지 컨트롤 타입을 모두 디자인하기 때문에

### | New Input Types: (6: 30) 

<img src = "https://user-images.githubusercontent.com/75241542/163108012-032c2c82-855f-495b-8d37-76ac2f18dc1c.png" width="30%" height = "30%">

 - the wider web의 interaction은 훨씬 복잡허다
 - hand tracking, wands(VR의 컨트롤러), 음성 추적, 시선추적, 얼굴 추적등을 한다
 - 이 모든 것들이 결합되어 the wider web을 이루고 매우 복잡하다

### | Browsers (7:30)
 
<img src = "https://user-images.githubusercontent.com/75241542/163108094-a0dc50e9-0b61-4d69-b791-4e7e3d01a8f8.png" width="50%" height = "50%">

- 이 이미지에서 몇가지 기술 계층에 대해 이야기한다
- 맨 아래의 레이어에는 하드웨어(스마트폰, 피씨, XR glasses, 스마트워치) 에대한 계층이 있고
- 그 위에는 Web API를 제공하는 웹 브라우저가 있음!
- **Web API**
  - 이것에 대해 많이 이야기하게 되기 때문에 이 중 몇 가지를 살펴보겠다
  - ```WebAssembly```  
    - ```WebAssembly```는 기본적으로 ```javascript```보다 코드를 실행하는 더 빠른 방법이다
    - XR에 대해 기억해야할 점은, native 속도로 실행되는 코드를 작성할 수 있다는 것입니다.(8:14)
    - (so it has a lot of other capabilities that it brings to the table but for XR the thing to remember is that it lets us write code that runs at native speeds.)(8:14)
    - ```javascript```는 일반적으로 ```c++```와 ```Rust``` 같이 ```Native Language``` 보다는 약간 느립니다
    - ```WebAssembly```는 이런 속도를 브라우저에 가져온다
  
  - ```WebXR```은 브라우저가 지면 환경과 같은 정보를 ```HMD```로 부터 얻을 수 있게 한다
  - ```WebAudio```는 ```spatialization```(공간화) 역할
  - ```WebGPU```는 그래픽을 빠르게 표현함
  - ```WebRTC```는 브라우저와의 소통, 다른 브라우저 간의 소통의 역할
- ** Graphic Engine, Physics Engine**
  - 오늘 많이 이야기 할것이기 때문에 생략
- **App Framework**
  - threeJS, babylon.js, potassium es 같은 것들
  - 개발자가 모든 복잡함을 이해할 필요 없게 해주는 엔진
- **Application Code**
  - 그 위에 application code가 있음
  - 나중에 교육, 개인정보보호, 광고 등 지금 사용하고 있는 다양한 종류의 응용 프로그램에 대해 이야기 할것임
 
### | 마무리
- 오늘 이야기는 브라우저가 XR을 수행할 수 있을지 아닌지 확인하는것
- + geolocation, shared contents, digital bodies 및 서비스 간에 ID를 가져오는 방법과 같은 서비스










