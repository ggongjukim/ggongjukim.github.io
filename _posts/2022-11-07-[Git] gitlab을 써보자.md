---
layout: single
title: "[Git] gitlab을 써보자"
categories : git
tag : [git, gitlab]
toc : true
---

## 연습내용
master와 dev브랜치가 있을때  
dev에서 브랜치를 하나 생성한다  
그리고 해당 브랜치에서 생성한 내용을 dev에 merge

## 연습
1. gitlab에 repo 하나 생성하여 README.md 파일과 master.txt 작성
// 0.png
// 1.png
2. dev 브랜치를 master에서 생성하고 dev.txt 작성
//2
//3

3. clone 하여 dev 브랜치에서 새로운 브랜치 생성(feature-FE-0)하기
//4


//5
origin/dev 브랜치를 가져오기 위해서는 아래 명령어를 사용해야한다

```
git checkout -t origin/dev
```

원격저장소에 있는 브랜치를 가져온다는 뜻이다  
그러기 위해서는 원격저장소의 상태를 업데이트 해줘야한다

```
git remote update
```

`git branch` 명령어를 썼을때 
`master` 하나였다가 `dev` 브랜치가 생긴것을 볼 수 있다
 
4. `dev` 브랜치에서 `feature-FE-0` 브랜치 생성하고 새로운 파일 만들기
```
git checkout -b "feature-FE-0"
```
//6

5. add commit push 하고 pr(Pull Request) 하기 
//7
```
git add .
git commit -m "커밋내용"
git push origin (브랜치 이름)
```

pr 하기
//8
//9
//10

6. merge 버튼 누른 결과







