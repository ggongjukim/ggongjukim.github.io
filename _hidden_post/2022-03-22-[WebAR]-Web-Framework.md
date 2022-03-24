---
layout: single
title: "[WebAR] Web Framework"
---
## Web Framework
- 프레임워크란 라이브러리의 집합으로서 웹 기반 증강현실 개발시 기본적인 뼈대를 제공한다.
- 

### AR.js
- 공식 문서 https://ar-js-org.github.io/AR.js-Docs/
- version 3 까지 출시
- github page로 호스팅 가능
- https 사용해야함
- 샘플 https://ar-js-org.github.io/AR.js/aframe/examples/image-tracking/nft/ 안되는데? loading 만 나왕! https://raw.githubusercontent.com/AR-js-org/AR.js/master/aframe/examples/image-tracking/nft/trex-image-big.jpeg 이건 그림
- pc chrome 에서 되고 moblie 에서 안되는데?
- https://github.com/AR-js-org/AR.js/issues/121문제좀 많은듯..
- ar js 참고 https://medium.com/chialab-open-source/build-your-location-based-augmented-reality-web-app-c2442e716564 

### React-xr
- VR에서 손트래킹도 한다 홀리쉿!
- react three fiber 공식 문서 https://docs.pmnd.rs/react-three-fiber/getting-started/introduction
- 유튜브 써밋 https://www.youtube.com/watch?v=CCT1YG_Ay9A&list=PLKNvd3dXSaxBlJFtM1YAJhCLbFQiIPQsL&index=10 
- 유튜브 아저씨 블로그 https://blog.dubenko.dev/react-xr/
- Poimandres 공식 문서 https://docs.pmnd.rs/react-three-fiber/getting-started/introduction 
- 블로그 Three.js is a library for 3D graphics, react-three-fiber is react renderer for Three.js, drei is a collection of reusable components for r3f and react-xr is a collection of hooks to help you build XR experiences in react-three-fiber applications.
- in this talk i want to share with you a project that i've been doing for some time now it's called react xr and it builds on top of react-three-fiber and provides web with componenets needed to quickly build yout applications with react.
- so this project is all about giving tools components to developers to easily create webxr experiences.
- first i want to talk about Poimandres
- it's a open source developer collective which react xr is part of bringing you such libraires as react spring directory fiber resistant and so much more
-  so if you want to join 디스코드로 오세요
- react three fiber is a library that allows you to use all of the threejs in react 
- so threejs is a powerful 3d engine 
- and react three fiber ties it together with react you get declarative way of making apps and games you have huge existing react ecosystem that includes animation libraries, state management so every library you can use in react you can use it here
- and also grow a number of libraries in the reactive fiber ecosystem. for example like physics library use-cannon drei, react-three-flex for 3d layout we also have accessibility library to enable navigation with keyboard for example and of course react xr 
- so react xr is a library that contains react components to help any react developer start creating xr experiences in low time becase it exteds in reactive fiber you can use all of the libraries like for example and you can see here the library use-cannon is used so it's a physics engine that works out of the box with the reactive fiber just add a couple lines of code and tou obejcts become interactive and physical objects 
- and all of those examples you see on screen extremely simple they're like 100 200 under lines of code and available on github so i encourage you to check them out


- 누군가 쓴 블로그 https://blog.dubenko.dev/react-xr/
### XR engine
- javascript 기반의 웹 프레임워크 
- 공식 문서 https://github.com/XRFoundation/XREngine/blob/dev/docs/docs/0_start-here.md 
- demo https://app.theoverlay.io/location/apartment?instanceId=7010b8f0-a998-11ec-85e0-adbd312207c1
- git https://github.com/XRFoundation/XREngine
- 공식문서 자료 https://github.com/XRFoundation/XREngine/blob/dev/docs/docs/0_start-here.md
- 설치 방법 https://github.com/XRFoundation/XREngine/blob/dev/docs/docs/0_installation/01-installation.md
- 엔티티 시스템 https://xrfoundation.github.io/xrengine-docs/docs/
- 사이트 https://xrfoundation.github.io/xrengine-docs/
- 코드 api로 되는건지 아니면 에디터로 되어있는건지 파악하기