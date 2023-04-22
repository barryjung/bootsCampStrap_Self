# bootsCampStrap_self
팀프로젝트 복습을 위한 self프로젝트.
더욱 컴팩트하게 만들었습니다.

## self개발 순서
venv 생성
django, dotenv, autopep 설치
프로젝트 생성
dotenv secret키 설정
user, tweet 앱생성
회원가입 기능
로그인, 로그아웃 기능
트윗 홈, 트윗 작성 기능
트윗 상세, 수정, 삭제 기능
마이페이지, 프로필 수정 기능

유저, 트윗 이미지 업로드, 수정 기능
팔로우, 팔로우 리스트, 팔로우 페이지 기능
댓글 작성, 리스팅, 수정, 삭제 기능
좋아요 기능
수정, 삭제에 URL보안
admin페이지 커스터마이징

트윗 수정, 삭제 시 파일 삭제
템플릿 단순화
팔로우 오류수정

---

## 특징과 달라진 점

**회원가입, 로그인, 로그아웃**
+ 장고의 기본 제공 기능을 가능한 한 활용했습니다.
    + AbstractUser, UserCreationForm
    + *new!* UserChangeForm 활용
    + Loginview, Logoutview
    + *new!* Loginview가 내포하고 있는 AuthenticationForm 활용

**가능한대로 간결하게**
+ 원 프로젝트와 동작은 같지만 가능한대로 간결하게 작성했습니다.
    + *new!* request.user를 적극 활용해서 login_required와 사용자 대조를 생략했습니다.
    + *new!* 함수내 변수명, DTL변수명, URL명 등을 간결하고 직관적이게 작성했습니다.
    + *new!* 역참조명 등 작성하지 않아도 자동생성이 되는 부분은 자동생성 명을 이용했습니다.

**사진삭제는 모델에서 처리**
+ 트윗을 수정, 삭제할 경우 기존의 이미지 파일은 지웁니다.
    + *new!* 두 기능 모두 모델 메소드로 처리하도록 바꿨습니다.

**부트스트랩만을 이용한 깔끔한 템플릿**
+ *new!* form페이지를 하나로 뭉쳤습니다.


---
