# surveySlide

해커톤을 향해! 

[구글독](https://docs.google.com/document/d/1XZCP1MxqWVhv2nqjzUlk0TddqXnlzX_GbkSbKYpatqs/edit?usp=sharing) 

[데이터베이스 구조 예시](https://docs.google.com/spreadsheets/d/1Z5tycA0LzGOusHoBt94dwG9l6CGxMWActRw-Y4dbcBY/edit?usp=sharing)

## 1. 일정

설입 커피나무(예정)

주 2회

월 7시, 토 7시? 정하기



[8월 8일] 해커톤 결과 발표(오전 10시), 고대 연합 아이티어톤(오후 2시부터)

## 2. 깃허브 사용

각자 이름으로 브랜치 파서 업로드 후 풀리퀘

[깃 커밋 메시지 작성 요령 (이건 그냥 참고용)](https://blog.ull.im/engineering/2019/03/10/logs-on-git.html)



**깃허브에서 클론해오기**

​	git clone https://github.com/born9507/surveySlide.git

**브랜치 목록 확인**	

​	git branch -a

**해당 브랜치로 이동(원격브랜치와 같은 이름을 사용하면 자동으로 원격브랜치와 함께 트래킹된다! )**

​	git checkout (브랜치 이름)



**작업 순서도**

1. 먼저 원격 브랜치 내용을 다 가져온다 ( git pull )
2. 작업 진행
3. 내 작업 사항을 stage 에 올린다 ( git add .  )
4. 커밋 메시지를 작성하여 커밋한다 ( git commit -m '커밋 메시지' )
5. 원격 저장소에 내 진행 상황을 업로드한다 ( git push )
6. **맡았던 작업이 모두 마무리 되면 깃허브 사이트에서 풀리퀘!**
7. **풀리퀘가 끝나면 내 브랜치로 돌아가서, git merge master 로 마스터 브랜치 내용 가져오기**



## 3. 웹페이지 디자인

- 주요 기능
- 개인정보들을 처음에 회원가입할때 입력하기보다 설문의 형태로 입력하면 포인트 주게끔



### index.html

#### 로그인 전

- **로그인, 회원가입 페이지**

  ![](img/github-main.png)
  - 회원가입
  - 로그인
  - 가격정책(pricing)

- 서비스소개(슬라이드해서 내려가면 아래처럼 소개 나오게끔)

  ![](img/github-intro.png)



#### 로그인 후

- **디자인**: 페이스북의 피드처럼 설문이 하나씩 올라오도록

![](img/facebook-feedpage.png)

![](img/mainpage.png)

- 메인에는 설문지 리스트
- 헤더
  - 소개 (intro.html)
  - 설문 제작 (forms.html)
  - 설문 결과 (result.html)
  - 드롭다운 메뉴
    - 내 프로필
      - 회원정보 수정 (mypage.html)
      - 내가 참여한 설문 (participated.html)
      - 내가 만든 설문 (made.html)
    - 충전/환전 (coin.html)
    - 설정 (settings.html)
    - 로그아웃 



### surveyMake.html

![](img/img3.png)

- 구글 설문조사 설문 제작 사이트 클론
- CRUD 활용하면 되지 않을까?
- ajax 이용해서 새로고침 없이 질문 목록 추가할 수 있도록



### mypage.html

- 회원정보 수정 페이지



### 나머지 페이지들 디자인도 여기에 추가! XD 활용해서 디자인!

### 디자인 시안

![](img/index_example.jpg)






## 4. 나중에 할 것

앱 제작

잠금화면 단에서 설문 조사 가능하게 

자바 코데카데미 듣기?
