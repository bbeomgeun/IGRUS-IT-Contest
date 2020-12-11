# IGRUS-IT-Contest
2020-2 IGRUS IT Contest

<H1> ICBM </H1>

 - Inha Client Broadcasting Music & Chat
 - 뮤직 플레이어가 구현되는 채팅 프로그램
 
 ---
 
 <h2> 계기 및 배경 </h2>
 
 <ol>
  <li> 채팅 프로그램에서 음악을 공유하고자 하는 소비자들의 니즈 </li>
  <li> 코로나19의 사회적 거리두기로 인한 비대면 활동에 도움 </li>
 </ol>

<h2> 기대 효과 </h2>

 <ol>
  <li> 채팅과 뮤직플레이어를 동시에 작동하면서 음악 공유 기능 가능 </li>
  <li> 음성을 공유함으로 다양하게 활용 가능(음악 감상 동아리, 스터디 등) </li>
 </ol>
 
 ---
 
 <h2> 프로그램 기능 및 기술 </h2>
 
 <img src = "https://user-images.githubusercontent.com/66156531/101857673-62ebd080-3bab-11eb-88fc-aac7a0872cfe.png">
 
  <h3> 기본 인터페이스 구현 </h3>
  
  <ul>
  <li> Python 그래픽 프레임워크인 PyQt를 사용하여 개발 </li>
  
   - Python Anaconda ver.3.7 라이브러리 사용 / PyQt ver 5.6
   
  <li> Designer Tool을 이용하여 대략적인 GUI 개발 </li>
  
   - PyuicS를 이용하여 .py 변환 후 추가 GUI 작업 진행
   
  <li> 메인 로직이 되는 class와 GUI class를 분할하여 디자인 패턴을 사용하여 가독성을 높임
  </ul>
  
  <h3> 로그인 및 회원가입 기능</h3>
  
  <ul>
  <li> 데이터베이스 </li>
  
   - 사용자 계정 정보를 저장하는 table 제작
   - PyMysql 라이브러리를 이용해서 서버의 데이터베이스와 연동
   
  </ul>
  
  <h3> 채팅 기능 </h3>
  
  <ul>
  <li> 서버 구축 </li>
  
   - AWS EC2 호스팅을 통한 우분투 서버 구축
   - Python 파일로 구성된 Server Side 프로그램 구동
   
  <li> 서버 통신 </li>
  
   - 소켓 프로그래밍을 통한 Server-Client 구조 구성
   - 통신 소켓을 통해 연결된 모든 Client들에게 서버에서 메세지를 전송하는 방식
   
</ul>

  <h3> 노래 검색 & 공유 기능 </h3>
  
  <ul>
  <li> 노래 검색 </li>
  
   - Selenium 라이브러리를 이용하여 웹 크롤링을 통해 구현
   - 상위 5개의 영상을 받아온 후 사용자 입력으로 몇 번째 영상을 재생시킬지 설정
   - 받아온 HTML을 PAFY 라이브러리를 통해 내부 데이터(듣기 전용 URL) 획득
   - Audio 전용 URL을 데이터베이스에 저장
   - 해당 소켓과 동일한 소켓을 가진 방에 해당 URL을 송출
  
   <li> 사용자 명령어 </li>
   
   - Search "검색어" : 유튜브에 "검색어"를 검색
   - Play : 검색 결과로 받아온 Audio URL 재생 명령어
   - Stop : 해당 재생 중인 노래 중지 명령어
   
</ul>
 
   
