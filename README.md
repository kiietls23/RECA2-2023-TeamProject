# 🔗 목차

1. [RECA2-2023-TeamProject](#-reca2-2023-teamproject)
2. [최종 결과](#🔖-최종-결과)
3. [개발 기간](#📆-개발-기간)
4. [개발 인원](#💻-개발-인원6명)
5. [기술 스택](#✍-기술-스택)
6. [Application Architecture](#🛠️-application-architecture)
7. [ERD](#📚-erd)
8. [API Endpoints](#🎯-api-endpoints)
9. [프로젝트 진행 관리: Notion](#📝-프로젝트-진행-관리-notion)
10. [발표 PPT: Figma](#📝-발표-ppt-figma)

<br>

# 🚀 RECA2-2023-TeamProject
- 쇼핑몰 웹 페이지 제작

<br>

## 🔖 최종 결과
여기에 영상 넣기

<br>

## 📆 개발 기간
- 2023.04.17 ~ 2023.05.12(26일)

<br>

## 💻 개발 인원(6명)
이름 | github | blog
-- | -- | --
박신영(PM) | https://github.com/kiietls23 | https://logforlog.tistory.com/
계민준 | - | -
박민하 | https://github.com/miracle-21 | https://minha0220.tistory.com/
오재민 | - | -
이주승 | https://github.com/Yetwhom | -
이준서 | https://github.com/barqraria | -

<br>

## ✍ 기술 스택
Language | Framework | Database | Tool
| :----------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------: 
<img src="https://img.shields.io/badge/python-3.10.2-3776AB?style=for-the-badge&logo=python&logoColor=white"> | <img src="https://img.shields.io/badge/Flask-2.3.1-000000?style=for-the-badge&logo=Flask&logoColor=white"> <br> <img src="https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=Bootstrap&logoColor=white"> | <img src="https://img.shields.io/badge/MySQL-8.0.33-4479A1?style=for-the-badge&logo=MySQL&logoColor=white"> | <img src="https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=Notion&logoColor=white"> <br> <img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=Discord&logoColor=white">

<br>

## 🛠️ Application Architecture
![](https://velog.velcdn.com/images/miracle-21/post/72da80a1-c164-4005-b12f-80a3c9ffae55/image.png)

<br>

## 📚 ERD
![](https://velog.velcdn.com/images/miracle-21/post/1ffc5b2f-79fe-440b-9061-96dbde0057b8/image.png)

<br>

## 🎯 API Endpoints
|  | endpoint | HTTP Method | 기능 | 특이사항
| --- | --- | --- | --- |--- |
| 재민 | /main | GET | 메인페이지 | 지도 오류
|  | /user/info | POST  | 회원정보수정 | 잔액 확인/충전 미구현
|  | /user/pw_change | POST | 비밀번호변경 |
|  | /user/del | POST | 회원정보삭제 |
|  | /search | GET | 검색 | 태그 검색 미구현
| 주승 | /users/signin | GET | 로그인 | ID/PW 찾기 기능 미구현
|  | /users/signup | POST | 회원가입 | 중복확인 오류
|  | /users/log_out | GET | 로그아웃 |
| 준서 | /products/:id | GET | 상세페이지 | css 적용중 <br> href 미적용
| 민하 | /products/:id | POST | 장바구니 등록 |
|  | /cart/:user_id | GET | 장바구니 조회 | 개별 상품 결제버튼 미구현 <br> 결제버튼 위치 수정 필요
|  | /cart/:user_id | POST | 장바구니 수정/삭제 |
| 신영 | /orders/:user_id | POST | 상품 결제 |
|  | /user/history/:user_id | GET | 주문내역 조회 | 주문내역 저장 오류
| 민준 | /users/ | GET | 결제 내역 조회 |

<br>

# 📝 프로젝트 진행 관리: Notion
### 🔗 URL
https://www.notion.so/TeamProject-32c4481198da42359d62c2ccc416500b

![](https://velog.velcdn.com/images/miracle-21/post/bf83446a-c6d7-4a11-b653-797f12168c39/image.png)

<br>

# 📝 발표 PPT: Figma
### 🔗 URL
https://www.figma.com/file/a0OkfbXRif8G2KWNGhLzje/RECA2-2023-TEAMPROJECT?type=design&node-id=0%3A1&t=SpDVNHylJd0TIkx3-1


