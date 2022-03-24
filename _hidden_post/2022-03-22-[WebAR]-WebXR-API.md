---
layout: single
title: "[WebAR] WebXR API"
---

##  WebXR API
### [mozilla] 왈
- https://developer.mozilla.org/en-US/docs/Web/API/WebXR_Device_API
- WebXR is a group of standards which are used together to support rendering 3D scenes to hardware designed for presenting virtual worlds (virtual reality, or VR), or for adding graphical imagery to the real world, (augmented reality, or AR). The WebXR Device API implements the core of the WebXR feature set, managing the selection of output devices, render the 3D scene to the chosen device at the appropriate frame rate, and manage motion vectors created using input controllers.
- WebXR는 3D scene 렌더링을 지원하기 위해 함께 사용되는 표준들의 그룹이다
- 가상 환경을 표현하거나 현실 세계에 정보를 더하기위해
- WebXR Device API는 WebXR 기능 세트의 핵심을 구현한다.
- 출력할 장치 선택 및 관리하고
- 3d 장면을 선택한 장치에 적절한 프레임 속도로 렌더링하고
- 입력 컨트롤러를 사용하여 모션 벡터를 관리한다.
- While the older WebVR API was designed solely to support Virtual Reality (VR), WebXR provides support for both VR and Augmented Reality (AR) on the web. Support for AR functionality is added by the WebXR Augmented Reality Module.
- 이전 WebVR API는 VR(가상 현실)만 지원하도록 설계되었지만 WebXR은 웹에서 VR과 AR(증강 현실)을 모두 지원합니다.
- AR 기능에 대한 지원은 WebXR Augmented Reality Module에 의해 추가되었습니다.
### [webxr] 공식문서
- https://immersive-web.github.io/webxr/
-  이 사양은 웹에서 센서 및 헤드 마운트 디스플레이를 포함한 가상 현실(VR) 및 증강 현실(AR) 장치에 대한 액세스 지원을 설명합니다. => webxr device api
### [네이버랩스]
- https://d2.naver.com/helloworld/5644368
- WebVR API의 한계에 따라 WebVR을 대체하는 새로운 API인 WebXR Device API가 2017년 10월에 제안됐다("Bringing Mixed Reality to the Web" 참고). 기존의 가상 현실에 더해 증강 현실의 지원도 포함됐으며, 'Immersive Web'의 개념을 주창한다.
- Immersive Web Immersive Web은 웹에서 몰입 환경을 구현할 수 있도록 앞으로 다가올 새로운 기술의 모음이라 정의할 수 있다
### [my own 내 생각 의견] 왈
- arcore 설치해야한다 
- 사용자 활동으로 (버튼을 눌러야 활성화가 된다) => 일반적인 표준 https://immersive-web.github.io/webxr/#applicationflow
- https 를 사용해야한다
- immersive web, immersive working group mozilla? 얘네가 webxr device api 구현한거 ?
