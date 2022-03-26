---
layout: single
title: "[WebAR] Platform"
---
### memo... 
- 흠 .. 뭔가 시원함이 없네
- 증강현실의 기본요소들을 설명해야하지 않을까 하는 생각이 드네... 
- 가상 scene이런것들 아니면 라이프사이클같은거 ...?  
- 협업한 회사들 쓸까?
- end to end 종합 솔루션 e2es xr engine 도 이런 말 있었는데 
- https://docs.zap.works/universal-ar/general/terminology/ 용어 설명 
- 플랫폼도 완전 no code 를 추구하는 방식
### 8thWall

### Onirix
- https://docs.onirix.com/onirix-sdk
- onirix 위치 기반도 되는거 같은데 왜 document에는 scene이 네개 밖에 없딩?
- Onirix Web AR Player 이거는 왜 공간추적이 안된다그 그러지? 
- 웹 브라우저에서 실행하도록 최적화된 사내 컴퓨터 비전 알고리즘과 결합된 WebGL 또는 WebAssembly와 같은 일반 JavaScript 및 기타 웹 표준을 사용하여 구축되었습니다.
- spatial은 onirix app 으로 공간을 추적하고 스캔한다 
- AR engine sdk : Onirix AR Engine SDK는 웹 브라우저에서 실행되는 증강 현실 경험을 생성할 수 있는 소스 개발 키트입니다.
- Embed sdk  
  * Onirix Embed SDK를 사용하면 사용자 정의 도메인 또는 온라인 코드 편집기에서 경험을 임베드할 때 이벤트를 수신하고 장면을 제어할 수 있습니다.  
  * AR 장면에서 발생하는 이벤트를 듣고 여러 유형의 작업을 트리거할 수 있습니다. 이는 특히 사용자 정의 도메인에 Onirix 경험을 포함할 때 Onirix와 통합하는 데 권장되는 방법입니다.   
- Unity sdk 도 제공한다
- [Onirix Web AR Player]
   * Onirix Web AR Player allows you to display complete AR experiences in a web browser.  
   * Prepare your experience with some models and interaction, and share instantly with your audience in a frictionless way.  
   * Onirix Web AR Player를 사용하면 웹 브라우저에서 완전한 AR 경험을 표시할 수 있습니다. 일부 모델 및 상호 작용으로 경험을 준비하고 마찰 없는 방식으로 청중과 즉시 공유하십시오.
- iframe 이 몬뎅?
-  Onirix는 표면 인식, 이미지 인식, QR code 인식, 공간 인식이 가능하다. 
-  onirix player

### Blippar
- WebAR SDK 공식문서 https://support.blippar.com/hc/en-us/articles/4406622267283-Introduction
- BLIPPBUILDER
- HTML 및 WebGL과 같은 2D 및 3D를 지원하는 웹 콘텐츠 표준과 호환됩니다.
- https://support.blippar.com/hc/en-us
- blippbuilder도 slam된대 어떻게? 마커 기반이랑 마커리스만 나왔는데 
- 드래그앤 드롭 인터랙티브 타임라인
### zappworks
- 모 하는애? ar? webar?
- 구현 방법 : 세가지 zapper studio/zapper design/ 
- 배포 방법 : webar, 커스텀 앱, zapper apps
- universial ar https://docs.zap.works/universal-ar/
- zappar 와 zapworks의 관계 ? https://www.zappar.com/contact/
- 
### AWE
- https://awe.media/
- https://awe.media/support/adding-and-updating-objects
- https://github.com/awe-media/awe.js
- AR VR 웹 어플리케이션 
- awe app domain
- 가장 강력한 기능 중 하나는 동일한 앱 내에서 한 유형의 경험을 다른 유형의 경험으로 쉽게 원활하게 연결할 수 있다는 것
- 시작하려면 awe 앱에서 콘솔 출력을 활성화해야 합니다. 오버헤드를 줄이고 프로덕션 앱이 브라우저 콘솔을 오염시키는 것을 방지하기 위해 이 기능을 껐습니다. 그러나 개발 중에 상호 작용하려면 이 기능을 켜고 싶습니다.
- Copy this line into your Javascript console and hit enter, then reload your page.
- 저장된 개체(예: awe.projections.list())에 액세스하고 관리
- awe.js API는 THREE.js 위에 있으며 장면, 미디어 개체, 상호 작용, 센서, 장치 유형 등을 쉽게 관리할 수 있습니다.
- natural 어쩌고 그거 한다고 함
- 
### ~Hololink~
- drag and drop editor AR 경험을 만드는 것은 Hololink의 직관적인 브라우저 기반 편집기를 사용하면 매우 쉽습니다. 이를 통해 기록적인 시간 내에 작업 프로토타입을 생성할 수 있습니다.
- 시각적 개요를 통한 상호 작용
- 인터랙티브하게 만들어 의미 있는 AR 경험을 디자인하세요. 
- Hololink의 사용자 중심 인터페이스는 상호 작용에 대한 시각적 개요를 제공하여 그 어느 때보다 빠르게 프로토타입을 만들 수 있습니다
- 안될듯

### exokit
- https://github.com/exokitxr
- https://exokit.org/
- https://medium.com/webmr/introducing-exokit-a-javascript-web-engine-for-the-post-screen-era-49eaf378f36e
- https://kandi.openweaver.com/javascript/exokitxr/exokit-browser

### ~XR.+~
- 스크립트 얘기가 전혀없눈데
- 홈페이지 https://xr.plus/experiences/
- 공식문서 https://docs.xr.plus/your-first-web-ar-project/
- 
### 3.1.3.8 Letsee 
- 공식 문서 https://developers.letsee.io/api-v1.1.3/
- 홈페이지 https://www.letsee.io/ko/
- 튜토리얼 https://www.notion.so/Letsee-WebAR-SDK-970d6621cbec487f8c1f7488a5ca86a3
- 깃헙 https://github.com/letsee
- Letsee WebAR SDK 의 가장 큰 특징은 Web 의 interaction, event 제어를 AR contents 내부에서 그대로 사용할 수 있게 하여, 별도의 도움이 없이도 AR 환경 위에서 동작하는 웹 컨텐츠를 제작할 수 있다는 것 
- https 이어야함 -> 다른것도 https여야만 하는지 
- https://www.notion.so/Getting-Started-11b26d08982f45f59a695d83d104080c 요구사항 기기
- Letsee WebAR SDK 는 WebRTC를 이용하여 Camera 로부터 vision을 획득하여 Video Stream 재생을 합니다. 그리고 이 Video Stream 을 바탕으로 각종 tracking 을 수행하여 AR 경험을 제공
- webrtc 도 써야대눈뎅!!!
- https://support.google.com/domains/answer/7630973?hl=ko https 

6개만 쓰고 awe exo 킷으로 바꾸어 쓰기
일단 8thwall onirix blippar zappar letsee
playcanvas는 ?
