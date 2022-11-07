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
### 1. gitlab에 repo 하나 생성하여 README.md 파일과 master.txt 작성
![0](https://user-images.githubusercontent.com/75241542/200239693-76b10236-cdf1-4c43-9b8b-5cab4790f72f.png)
![1](https://user-images.githubusercontent.com/75241542/200239652-7a01c9da-161b-450e-b26e-e30616e7d865.png)
<br><br><br>
### 2. dev 브랜치를 master에서 생성하고 dev.txt 작성
![2](https://user-images.githubusercontent.com/75241542/200239749-bf79af27-8ef3-4264-82b4-b0fc20fdd144.png)
![3](https://user-images.githubusercontent.com/75241542/200239758-949d73b0-8c1b-42aa-93fe-0264727879d3.png)
<br><br><br>
### 3. clone 하여 dev 브랜치에서 새로운 브랜치 생성(feature-FE-0)하기
![4](https://user-images.githubusercontent.com/75241542/200239825-74f2ebfd-a8c4-45e6-9beb-641b88f857ef.png)
![5](https://user-images.githubusercontent.com/75241542/200239886-58b57a94-4a2d-4316-9961-262e5845b7e8.png)

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
<br><br><br>
### 4. `dev` 브랜치에서 `feature-FE-0` 브랜치 생성하고 새로운 파일 만들기
```
git checkout -b "feature-FE-0"
```
![6](https://user-images.githubusercontent.com/75241542/200240033-53d7e32d-611d-4f3f-86e4-d95bff27f3e3.png)

<br><br><br>

### 5. add commit push 하고 pr(Pull Request) 하기 

![7](https://user-images.githubusercontent.com/75241542/200240245-a91fdd26-3537-4cc4-a8a2-5ff1cb0aba4e.png)

```
git add .
git commit -m "커밋내용"
git push origin (브랜치 이름)
```

pr 하기
![8](https://user-images.githubusercontent.com/75241542/200240275-ed6615c1-c267-4c92-b6e7-159bd3b1843f.png)
![9](https://user-images.githubusercontent.com/75241542/200240282-2baac5d5-6f17-4c07-9275-90bcf05fc903.png)
![10](https://user-images.githubusercontent.com/75241542/200240290-83322830-49db-4040-9460-cced52e88e50.png)
![11](https://user-images.githubusercontent.com/75241542/200240299-75f58048-db10-4dae-ad82-0da1c6b050f0.png)

### 6. merge 버튼 누른 결과


![12](https://user-images.githubusercontent.com/75241542/200240360-13cdb07e-6c96-481b-b90d-59998910fd87.png)

![13](https://user-images.githubusercontent.com/75241542/200240366-8fb42e6b-a877-4e50-866f-f335bd9d2066.png)

