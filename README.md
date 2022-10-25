# drf_week2
### DRF 권기현 튜터 원격강의 2주차

> 10/25(화)

- DRF로 프로젝트 세팅
- 시리얼라이저 model 활용
  - models에 정의된 objects들을 딕셔너리 형태 즉, JSON형태의 str으로 만들어 자동으로 response 할 수 있게 만들어 주는게 serializer 이다.
- 시리얼라이저를 활용해서 CRUD하기
- 포스트맨으로 DRF 개발을 테스팅
- 프로젝트에 Swagger를 적용하기
  - swagger url 설정
  - settings에 'django.contrib.staticfiles', 'drf_yasg' 설정
- 클래스형 뷰를 작성할 수 있다.
  - 함수와 다르게 class는 추후에 다른 함수나 class의 상속이 가능하다.
- fetch api를 써서 프론트엔드에서 DRF의 데이터를 가져와서 나타낼 수 있다.
  - front 폴더를 생성 및 html/js파일을 만들어 연동 후 백엔드에서 실행되고 있는 서버 주소와 연결해준다.
