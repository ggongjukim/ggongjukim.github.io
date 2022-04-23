---
layout: single
title: "[Vulkan] 01 window 만들기"
categories : Vulkan
tag : [Vulkan, ComputerGraphics]
toc : true
---
### | notice
- 이 포스팅은 [Opening a window](https://www.youtube.com/watch?v=lr93-_cC8v4&list=PL8327DO66nu9qYVKLDmdLW_84-yE4auCR&index=2)을 보고 작성하였습니다
- 오류가 있다면 댓글 남겨주세요..@ 

### | 학습목표
- window를 생성하는 클래스 만들기!

  
### | lve_window.hpp

 - lve이름의 namespace로 만들고 class를 만들기
 - priavate으로 GLFWWindow 포인터 만들기
 - glfw는 플랫폼에 제한을 받지 않는 창 도구이기 떄문에 glfw가 vulkan 헤더를 포함해야한다는 신호로 **#define GLFW_INCLUDE_VULKAN** 작성
 - window 초기화 함수 (void initWindow())
 - width height 멤버변수로 window 가로세로 길이 저장, windowName 창 이름
 - public으로 멤버변수 초기화하기 위한 public 생성자
 - window 정리하는 소멸자
 - 복사 생성자와 복사 연산자 삭제하기
    - resource acquisiton is initialization! 
    - resource creation happens when we initialize our variables
    - 소멸자로 지울 수 있음
    - 만약 실수로 lve window를 복사해서 glfw 창에 대한 두 개의 포인터를 갖는 것은 바람직하지않음 
    - 소멸자가 호출되면 glfw window가 정리되고 다른 포인터가 덩그러니 남게 되기 때문에
    ``` c++
        LveWindow(const LveWindow&) = delete;
		LveWindow& operator=(const LveWindow&) = delete;
    ```
 - sholudClose()는 glfwwindowsholudclose라는 gltw 함수를 호출해서 사용자가 window를 닫으려고 시도했는지에 대한 여부를 쿼리함


``` c++
#pragma once

#define GLFW_INCLUDE_VULKAN
#include <GLFW/glfw3.h>
#include <string>

namespace lve {

	class LveWindow {
	public:
		LveWindow(int w, int h, std::string name);생성자를 만들자
		~LveWindow();
		
		LveWindow(const LveWindow&) = delete;
		LveWindow& operator=(const LveWindow&) = delete;

		bool shouldClose() { return glfwWindowShouldClose(window); }

	private:
		void initWindow();

		const int width;
		const int height;
		std::string windowName;
		GLFWwindow* window;
	};
}  // namespace lve
```
***

### | lve_window.cpp
 - 헤더 파일을 포함
 - 생성자에는 멤버변수 초기화를 위한 멤버 이니셜라이저 목록 사용. 생성자 안에 initWindow함수 호출
 - initWindow() 은 
    - glfwInit : glfw 라이브러리를 초기화
    - glfwWindowHint : glfw에게 opengl context를 생성하지 않도록 함
    - glfwWindowHint : 창크기변경 비활성화 나중에 특별한 방법으로 조절하는 방법 만들거임 tutorial 10에서 
    - window 포인터 초기화를 위해 glfwcreatewinodw 명령으로 가로 세로 이름을 설정해줌
    - 4번째 인자는 fullscreen 설정하는거. 지굼은 그냥 window 모드라 nullptr 사용

 - 소멸자에는 glfwDestroyWindow,glfwTerminate호출. glfwDestroyWindow에는 window 포인터를 인자로 줌
 ``` c++
#include "lve_window.hpp"

namespace lve {
	LveWindow::LveWindow(int w, int h, std::string name) : width{ w }, height{ h }, windowName{ name } {
		initWindow();

	LveWindow::~LveWindow() {
		glfwDestroyWindow(window);
		glfwTerminate();
	}

	void LveWindow::initWindow() {
		glfwInit();
		glfwWindowHint(GLFW_CLIENT_API, GLFW_NO_API);생성하지 않도록 함
		glfwWindowHint(GLFW_RESIZABLE, GLFW_FALSE);

		window = glfwCreateWindow(width, height, windowName.c_str(), nullptr, nullptr);
	}
}  // namespace lve
 ```
***


### | first_app.hpp
 - 앱을 제어하는 클래스 만들자
 - lve_window.hpp 헤더를 추가
 - 같은 네임스페이스에 FistApp 클래스 
 - private 멤버변수 추가. FirstApp 클래스 만들어지고 없어짐에 따라 window 만들어지고 없어진다
 - public으로 window 가로 세로 상수 정의 
 - public으로 run 함수 추가 
``` c++
#pragma once

#include "lve_window.hpp"

namespace lve {
	class FirstApp {
	public:
		static constexpr int WIDTH = 800;
		static constexpr int HEIGHT = 600;
		void run(); 

	private:
		LveWindow lveWindow{ WIDTH, HEIGHT, "Hello Vulkan!" };
	};
}
```
***

### | first_app.cpp
 - 헤더 추가
 - run 함수 구현
    - while 사용해서 window 닫고 싶은지 확인하는 shouldClose를 호출
    - window를 닫고 싶이 않으면 window의 모든 이벤트를 처리하는 glfwPollEvents호출

 ```c++
#include "first_app.hpp"

namespace lve {

    void FirstApp::run() {

        while (!lveWindow.shouldClose()) {
            glfwPollEvents();
        }
    }
     
}
 ```
***
### | main.cpp
 - FirstApp 클래스 포함하고 main함수 구현
 - 앱 인스턴스 만들기
 - try catch로 run함수 호출하고 return을 성공하면 success 실패하면 failure
``` c++
#include "first_app.hpp"

#include <cstdlib>
#include <iostream>
#include <stdexcept>

int main() {
    lve::FirstApp app{};
     
    try {
        app.run();
    }
    catch (const std::exception& e) {
        std::cerr << e.what() << '\n';
        return EXIT_FAILURE;
    }
    return EXIT_SUCCESS;
}
 ```
***
### | 결과
- 창이 만들어진다
![save](https://user-images.githubusercontent.com/75241542/164917256-f2015df6-ca0c-467f-a332-2e5fc905b776.PNG)






