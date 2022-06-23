# OurRealTrip
- 마이리얼트립을 모티브로 구현한 웹 사이트 구현 프로젝트입니다.
- 개발 기간: 2021.03.02 ~ 2021.03.12
- 개발 인원: Back 4명 / Front 3명
- 기술 스택: Python, Django, MySQL, AWS, Kakao Login API
- GitHub: [https://github.com/jahnx/17-2nd-OurRealTrip-backend](https://github.com/jahnx/17-2nd-OurRealTrip-backend)

## 구현 목록

로그인페이지 / 항공 메인페이지 / 항공 리스트페이지
숙박 메인페이지 / 숙박 리스트페이지 / 숙박 디테일페이지

## 담당 기능
- Aquery Tool을 사용한 DB모델링 
![OURREALTRIP_20210315_08_59](https://user-images.githubusercontent.com/72085261/111140749-0c38cd00-85c6-11eb-9ba8-2c361739f76b.png)
- models.py 작성
- 항공권 관련 DB csv 파일 작성
- 유저가 선택한 조건에 맞는 항공권 리스트 데이터 응답 기능 구현
- 가격 낮은순, 출발시간 빠른순/늦은순 정렬 기능 구현
- 출발 시간대에 따른 필터링 기능 구현
- FlightView에 대한 unit test작성
- 유저가 선태한 왕복 항공권 데이터 DB 저장 기능 구현
- FlightRoundTripView에 대한 unit test작성
- AWS를 통한 서버구축 및 배포
- API문서 작성 <br>
![API_document](https://user-images.githubusercontent.com/72085261/111141132-836e6100-85c6-11eb-932d-2dda95b2d8b1.gif)

## 백엔드 전체 구현 목록
### 모델링
- ERD(관계형 모델링 설계) 및 model 생성 / Aquery Tool을 활용한 항공, 숙박 모델링 구현 및 models.py 생성
- DB CSV 파일 작성
- db_uploader.py 작성

### 회원가입 및 로그인 (SignUp & SignIn)
- bcrypt를 사용한 암호화
- 자체 로그인 기능 구현 및 unit test 
- jwt access token 전송 및 유효성 검사 기능 구현
- 카카오 소셜 로그인 구현 및 unit test
- 비회원, 회원 decorator 기능 구현 

### 숙소
- **숙소 리스트 기능 구현:**
Django ORM(Q객체, chianing, annotate, aggregate 등)을 활용한 다양한 filtering 구현 및 unit test
- **숙소 상세 페이지:**
user의 입력값과 맞는 데이터를 바탕으로 예약 가능한 숙소 room 불러오기 구현 및 unit test
- **숙소 예약 기능 구현:**
POST 요청정보 DB에 Create 구현 및 unit test 
- **Django ORM-DB QUERY:**
select_related, prefetch_related를 통한 Caching 활용

### 항공
- **항공 리스트 기능 구현:**
Django ORM(Q객체, chaining 등)을 활용한 다양한 filtering 구현 및 unit test
- **항공 예약 기능 구현:**
POST 요청정보 DB에 Create 구현 및 unit test 
- **Django ORM-DB QUERY:**
select_related를 통한 Caching 활용

### 배포 
- **데이스베이스 구축 및 배포:**
AWS(EC2, RDS) 데이터베이스 구축 및 배포

### Document
- [API Document](https://www.notion.so/API-Document-e1c56cbbc3a3418b8f1d211aaf4fcd71)

## 프로젝트 결과 시연 영상
[떠나요 OurRealTrip으로 🛫](https://www.youtube.com/watch?v=bpsRyUtgs-8)
