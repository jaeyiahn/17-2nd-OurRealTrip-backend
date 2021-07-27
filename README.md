![our-real-trip](https://user-images.githubusercontent.com/75108432/111068776-848f8780-850d-11eb-8f2c-6f7c5949f210.png)

## 마이리얼트립 기업 소개

'아워리얼트립'은 여행을 떠나기 위해 필요한 모든 것을 쉽고, 빠르게 검색하고 예약할 수 있는 플랫폼인 마이리얼트립을 모티브로 구현한 프로젝트입니다.

<br>
<br>
<br>

### 🛫 나만의 여행이 아닌 우리들의 진짜 여행🛫

# OurRealTrip

### 마이리얼트립 클론코딩 팀

2021.03.02 ~ 2021.03.12(11일)

## 팀원 소개
### 😎 front-end

-이정민(PM) 곽진석 박경토

### 😍 back-end

-강승연 안재이 정희영 허민지

<br>

## 📚 Stack

-**front-end:** <br>
HTML / CSS / JavaScript / React / CRA / React DOM / React Router DOM / Styled-Components / Slick / SNS Login API / React-date API / RESTfulAPI

-**back-end:** <br>
PYTHON / Django / bcrypt / pyjwt / RESTfulAPI / Aquery Tool / MySQL / cors / AWS / Kakao Login API

-**Communication Tool:** <br>
Notion / Slack / Trello / Git / GitHub / Zoom

<br>

## 구현 목록

로그인페이지 / 항공 메인페이지 / 항공 리스트페이지
숙박 메인페이지 / 숙박 리스트페이지 / 숙박 디테일페이지

<br>

## 내가 한 일들
- Aquery Tool을 사용한 DB모델링 
![OURREALTRIP_20210315_08_59](https://user-images.githubusercontent.com/72085261/111140749-0c38cd00-85c6-11eb-9ba8-2c361739f76b.png)
- models.py 작성
- 항공권 관련 DB csv 파일 작성
- 유저가 선택한 조건에 맞는 항공권 리스트 데이터 응답 기능 구현
![flignt_list](https://user-images.githubusercontent.com/72085261/111140883-31c5d680-85c6-11eb-8eee-ec2c7164b602.gif)
- 가격 낮은순, 출발시간 빠른순/늦은순 정렬 기능 구현
![flignt_list_ordering](https://user-images.githubusercontent.com/72085261/111140956-47d39700-85c6-11eb-88c7-2ef1b6c2cbee.gif)
- 출발 시간대에 따른 필터링 기능 구현
![flignt_list_filtering](https://user-images.githubusercontent.com/72085261/111141005-56ba4980-85c6-11eb-94e8-e7e27c0d4f46.gif)
- FlightView에 대한 unit test작성
- 유저가 선태한 왕복 항공권 데이터 DB 저장 기능 구현
- FlightRoundTripView에 대한 unit test작성
- API문서 작성 <br>
![API_document](https://user-images.githubusercontent.com/72085261/111141132-836e6100-85c6-11eb-932d-2dda95b2d8b1.gif)
<br>
<br>

### 😎 FRONT
<br>

### 이정민

- URL에 따른 Navbar Change 및 로그인 token으로 바뀌는 Navbar 레이아웃 <br>
- 카카오 소셜 로그인 구현 <br>
- 숙박 메인페이지 : 캘린더API 활용 및 레이아웃 구현 <br>
- 숙박 메인페이지 : 기본 성인 1명, 객실 1개 기준 최대 9명 인원 수 DropMenu 구현 <br>
- 숙박 리스트페이지 : 레이아웃 구현 및 백엔드 데이터를 이용한 숙박 리스트 구현 <br>
- 숙박 리스트페이지 : Query String을 사용한 통신 (카테고리, Sorting, Range, Multi check box) <br>
- 숙박 리스트페이지 : 상품의 개수에 따른 페이지네이션 구현 <br>
- 숙박 디테일페이지 : 레이아웃 구현 및 백엔드 데이터를 이용한 객실 구현 <br>

<br>

### 곽진석

- 항공메인페이지 : 전체 레이아웃 구현 및 슬릭을 활용한 메인페이지 슬라이드 구현
- 항공메인페이지 : 캘린더API를 활용한 메인페이지 캘린더 구현
- 항공메인페이지 : 여행지역 및 인원수를 Drop Menu를 통해 구현 및 리스트 페이지로 API 통신 전달
- 항공리스트페이지 : 레이아웃 구현 및 백엔드로 부터 받은 데이터 두개 이상 선택 시 예약정보 레이아웃 구현
- 항공리스트페이지 : 비디오태그와 애니메이션을 통한 로딩페이지 레이아웃 구현
- 항공리스트페이지 : Query String을 사용한 통신 (SelectBox, Multi check box)

<br>

### 박경토

- Navbar : styled components를 활용한 레이아웃 구현
- Navbar : window.location을 이용한 항공 및 숙박 메인페이지 이동 구현
- Footer : styled components를 활용한 레이아웃 구현
- Login : styled componenets를 활용한 레이아웃 구현

<br>

### 😍 BACK
<br>

### 모델링

- ERD(관계형 모델링 설계) 및 model 생성 / Aquery Tool을 활용한 항공, 숙박 모델링 구현 및 models.py 생성
- DB CSV 파일 작성
- db_uploader.py 작성

<br>

### 회원가입 및 로그인 (SignUp & SignIn)

- bcrypt를 사용한 암호화
- 자체 로그인 기능 구현 및 unit test 
- jwt access token 전송 및 유효성 검사 기능 구현
- 카카오 소셜 로그인 구현 및 unit test
- 비회원, 회원 decorator 기능 구현 

<br>

### 숙소

- **숙소 리스트 기능 구현:** <br>
Django ORM(Q객체, chianing, annotate, aggregate 등)을 활용한 다양한 filtering 구현 및 unit test
- **숙소 상세 페이지:** <br>
user의 입력값과 맞는 데이터를 바탕으로 예약 가능한 숙소 room 불러오기 구현 및 unit test
- **숙소 예약 기능 구현:** <br>
POST 요청정보 DB에 Create 구현 및 unit test 
- **Django ORM-DB QUERY:** <br>
select_related, prefetch_related를 통한 Caching 활용

<br>

### 항공

- **항공 리스트 기능 구현:** <br>
Django ORM(Q객체, chaining 등)을 활용한 다양한 filtering 구현 및 unit test
- **항공 예약 기능 구현:** <br>
POST 요청정보 DB에 Create 구현 및 unit test 
- **Django ORM-DB QUERY:** <br>
select_related를 통한 Caching 활용

<br>

### 배포 

- **데이스베이스 구축 및 배포:** <br>
AWS(EC2, RDS) 데이터베이스 구축 및 배포

<br>

### Document

- [API Document](https://www.notion.so/API-Document-e1c56cbbc3a3418b8f1d211aaf4fcd71)

<br>

## 프로젝트 결과 시연 영상

[떠나요 OurRealTrip으로 🛫](https://www.youtube.com/watch?v=bpsRyUtgs-8)
