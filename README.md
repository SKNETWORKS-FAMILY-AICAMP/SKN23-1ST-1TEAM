# 이차저차: 실거래 기반 중고차 가치 평가 솔루션

### 팀 이름: 않이이개외돼조

> **"딜러 믿지마\! 인터넷 믿어\!"**

-----


## 1\. 팀 소개

| <img width="675" height="675" alt="정용희" src="https://github.com/user-attachments/assets/26e83aff-9169-4ffa-a28e-2d201c1694f1" /> <br> 정용희 | ![양창일](https://github.com/user-attachments/assets/10474968-c8ef-4e16-9179-e2a63d32f8c2)<br> 양창일 |  ![김지우](https://github.com/user-attachments/assets/141df313-40bd-4b78-8ec7-1a5a3db71e10) <br> 김지우 | ![정희영](https://github.com/user-attachments/assets/5d870743-1b73-4aa8-884d-e8d60eb2ad56) <br> 정희영 |  
| :---: | :---: | :--- | :---: |
| **PM/QA** | **Crawling**<br>(Team Leader)| **Front** | **Back** |

-----

## 2\. 프로젝트 개요

### 프로젝트 명

**이차저차: 실거래 기반 중고차 가치 평가 솔루션**

> "딜러 믿지마\! 인터넷 믿어\!"

### 프로젝트 소개

중고차 시장 구전적인 신뢰에서 탈피하여 데이터 기반으로 처음 중고차를 구매하는 사람들에게 도움을 주는 솔루션 입니다.

### 프로젝트 필요성

  * **시장의 성장:** 최초 구매자들 60\~70퍼센트가 중고차를 첫 차량으로 선택하고 있고 경기에 따라 합리적인 가격으로 구매 가능한 중고차로 시선이 집중되고 있습니다.
  * **정보의 불균형:** 하지만 초보 구매자들은 차량 전문 지식이 부족하고 딜러가 제시하는 가격이나 불투명한 정보에 의존해야 하는 구조적 한계가 관찰 되었습니다.
  * **데이터 신뢰의 부재:** 기존 플랫폼의 정보는 판매자의 주관과 실제로 방문을 기반으로 하고 있어 사용되는 리소스가 과다 할 수 있습니다.

### 기존 서비스 분석

기존 시장의 주요 플레이어들은 각기 다른 강점을 가지고 있으나, 일반 소비자를 위한 '객관적 데이터 분석' 측면에서는 아쉬움이 존재했습니다.

| 경쟁사 (플랫폼) | 트래픽 (Monthly) | 가치 (Value) | 비고 |
| :--- | :--- | :--- | :--- |
| **엔카 (Encar)** | 104K | $12.2K | 경쟁사 대비 많은 트래픽 |
| **KB차차차** | 37.3K | $4.9K | 금융권의 자회사로 안정적인 서비스 |
| **헤이딜러** | 6.2K | $1.7K | APP기반 쉬운 접근 구조 |
| **카이즈유 (Data Source)** | 1.9K | $246 | 데이터 전문성은 매우 높으나 B2B 중심이라 일반 소비자의 접근성 및 가독성이 낮음 |

  * **키 포인트:** 카이즈유 데이터는 훌륭하나 사용자 친화적인 부분이 부족하다.
  * 본 프로젝트는 \*\*데이터 전문성(카이즈유)\*\*과 \*\*대중성(엔카)\*\*을 결합하여, 일반 소비자도 비교적 신뢰할 수 있는 지표를 통해 의사결정을 돕는 솔루션으로 기획되었습니다.

### 프로젝트 목표

  * **정보 비대칭 해소:** 국토교통부 원천 데이터를 가공한 카이즈유를 크롤링하여 데이터 신뢰성 확보
  * **투자 관점의 구매 지원:** 첫차의 유지 기간이 길지 않는 소비 패턴을 반영하여 감가상각 및 손익분기 예측을 통해 실제 비용을 기준으로 합리적 의사결정을 돕습니다.
  * **데이터 통합:** 정성적 데이터인 헤이딜러와 정량적 데이터인 카이즈유 데이터를 동시 제공.

-----

## 3\. 기술 스택

## Backend / ETL

![Python](https://img.shields.io/badge/Python_3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-43B02A?style=for-the-badge&logo=BeautifulSoup&logoColor=white)



## Database

![MySQL](https://img.shields.io/badge/MySQL_8.0-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

## Dashboard / Visualization

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
  <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"> 
  <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white"> 
  <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">


# VCS
<img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white"> <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">

| 분류 | 기술 | 설명 |
| :--- | :--- | :--- |
| **Language** | Python | 주 개발 언어 |
| **Frontend** | Streamlit | 빠르고 직관적인 데이터 앱 구축 |
| | Streamlit-AgGrid | 데이터 테이블 시각화 및 인터랙티브 그리드 구현 |
| | CSS | 모바일 적응형 디자인 및 UI 커스터마이징 |
| **Data Collection** | Requests | API 추출용 라이브러리 |
| | BeautifulSoup | HTML 파싱 및 정적 데이터 추출 |
| | Opinet API | 실시간 유가 정보 수집 |
| **Data Processing** | Pandas / NumPy | 대용량 데이터 전처리 및 수치 연산 |
| **Database** | MySQL | DB 관리 |
| **Collaboration** | GitHub / Discord | 형상 관리 및 프로젝트 문서화 |

-----

## 4\. 일자 별 수행 내용

| 구분 | 작업 항목 | 기간 | 담당자 | 상태 |
| :--- | :--- | :--- | :--- | :--- |
| **기획** | 아이디어 브레인스토밍 및 주제 선정 | 1일차 | 전원 | 완료 |
| | 요구사항 정의 및 와이어프레임 작성 | 1일차 | 팀리더 | 완료 |
| **설계** | 데이터베이스 모델링 (ERD) | 1일차 | 백엔드 | 완료 |
| | 크롤링 대상 사이트 및 API 분석 | 1일차 | 팀리더 | 완료 |
| **개발** | 데이터 수집 (크롤링, 오피넷 API) 및 전처리 | 2일차 | 팀리더 / QA | 완료 |
| | DB 구축 및 데이터 적재 | 2일차 | 백엔드 | 완료 |
| | 프론트엔드 UI 구현 (Streamlit) | 2일차 | 프론트 | 완료 |
| | 핵심 기능 구현 (감가상각, BEP) | 2일차 | QA | 완료 |
| **테스트** | 통합 테스트 및 버그 수정 | 3일차 | 전원 | 완료 |
| **배포** | 최종 발표 자료 작성 및 시연 준비 | 3일차 | 전원 | 완료 |

-----

## 5\. 요구 기능 목록

  * **차량 조회 기능:** 차량을 최소한의 설정으로 조회 할 수 있게 할 것.
  * **시세 시각화:** 조회된 차량에 대한 가격 변동 추이를 그래프를 이용해 제공 할 것.
  * **감가상각 예측:** 조회된 차량 구매 시 추후 예상 잔존 가치(%)를 수치와 그래프로 보여줄 것.
  * **손익분기점 분석:** 유사 차종 선택 시 연비 대비 손익 분기점을 계산하여 제공 할 것.
  * **사용자 리뷰 요약:** 엔카 이차 어때 같은 정성적 FaQ를 제공하여 문의점을 최소화 할 것.

### 기획 와이어 시트

![캡처](images/blueprint.png)

![캡처](images/detail_page.png)

![캡처](images/compare_page.png)

![캡처](images/contents.png)



-----

## 6\. ERD
![캡처](/images/ERDFi.png)

### 구조 및 관계 설명

본 프로젝트의 데이터베이스는 중고차 가치 평가 및 예측 서비스 제공을 위해 계층적인 구조로 설계되었습니다.

  * **계층형 데이터 구조:** `CAR (차량)` -\> `GRADE (등급)` -\> `PRICE (가격) 및 각종 통계 데이터`

### 테이블 별 상세 설명

  * **CAR (차량 정보 테이블):** 브랜드와 차종 정보를 저장하는 최상위 테이블입니다.
  * **GRADE (등급 정보 테이블):** CAR 테이블과 1:N 관계를 가지며, 차종별 세부 등급 정보를 저장합니다.
  * **PRICE (가격 정보 테이블):** GRADE 테이블과 1:N 관계를 가지며, 연식별 신차 가격과 중고차 시세 데이터를 저장합니다.

### 특이사항

  * **데이터 매칭:** CAR 테이블을 중심으로 카이즈유(스펙/가격) 데이터와 엔카(리뷰/통계) 데이터를 통합하여, 정량적/정성적 데이터를 아우르는 분석 환경을 구축했습니다.
  * **예측 데이터 저장:** PRICE 테이블에 현재 시세뿐만 아니라 예측된 미래 가치 컬럼을 두어, 실시간 연산 부하를 줄이고 조회 속도를 최적화했습니다.

-----

## 7\. 수행 결과

### 1\) 메인 대시보드
![캡처](images/detail_page_fi.png)
### 2\) 차량 비교
![캡처](images/compare_pagefi.png)
### 3\) FAQ
![캡처](images/faqfi.png)
-----

## 8\. 트러블 슈팅

### 1\) 동적 페이지 크롤링 및 데이터 분석 난관 극복

  * **상황:** 엔카, 이차어때 등 데이터 소스 사이트가 Vue.js 기반의 동적 웹 페이지로 구성되어 있고, 수집해야 할 데이터 양이 방대함.
  * **문제:**
      * 초기 Selenium 사용 시 수집 속도 저하로 대량 데이터 확보 불가.
      * 수집된 데이터 테이블 구조가 복잡하여 분석 및 정제에 16시간 이상 소요되는 등 난이도가 높음.
  * **✅ 해결 방안:**
      * **기술적 접근 전환:** 웹사이트의 네트워크 트래픽 분석을 통해 API 호출 시점과 JSON 데이터 흐름을 포착, Requests와 BeautifulSoup으로 직접 API를 호출하여 속도를 개선했습니다.
      * **분석 효율화:** 복잡한 데이터 구조를 파악한 후, Python Pandas를 활용하여 전처리 로직을 모듈화하고 자동화하여 분석 시간을 단축했습니다. 코딩 자체보다는 데이터 구조 이해와 분석 설계에 집중하여 문제를 해결했습니다.

<!-- end list -->

```python
# Vue.js(Axios)가 사용하는 내부 API 주소를 직접 호출하는 부분
url = "https://www.carisyou.com/usedcar/axios/getChartData.do" # API 엔드포인트 발견
headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": f"https://www.carisyou.com/price/{carClassNbr}", # 헤더 조작
    # ...
}
data = {
    "carClassNbr": carClassNbr, # 필요한 파라미터만 전송
    "dealTypeSelected": "매입,매도",
    # ...
}
res = s.post(url, headers=headers, data=data) # POST 요청으로 JSON 데이터 확보
# 이후 데이터 평탄화 - CSV로 저장 후 DB에 작성
```

### 2\) gradeFuelRate 데이터 결측치 처리 (Data Handling)

  * **상황:** 연비 비교 분석을 위해 차량 등급별 연비 정보(gradeFuelRate)를 조회하는 과정에서 일부 차종의 해당 컬럼 데이터가 NULL 또는 0인 경우가 발견됨.

**오류 내용:**

```python
ZeroDivisionError: division by zero
Traceback:
File "C:\Users\Playdata\Documents\myproject\venv\Lib\site-packages\streamlit\runtime\scriptrunner\exec_code.py", line 129, in exec_func_with_error_handling
result = func()
# ... (중략)
File "C:\Users\Playdata\Documents\myproject\app2.py", line 218, in main
cost_b = (annual_km / eff_b) * get_current_price(row_b['fuel'], prices)
# ~~~~~~~~~~^~~~~~~
```

  * ** 해결 방안:** null 체크 및 0으로 나누기 체크를 통해 예외의 경우 1로 대입하여 정상화

<!-- end list -->

```python
try:
    eff_b = float(row_b['gradeFuelRate'])
except:
    eff_b = 1

price_b = float(row_b['gradeUsedCarPrice'])

try:
    cost_b = (annual_km / eff_b) * get_current_price(row_b['fuel'], prices)
except:
    cost_b = (annual_km / 1) * get_current_price(row_b['fuel'], prices)
```

-----

## 9\. 비고

  * **모바일 적응형 UI 구현:** 사용자 접근성을 높이기 위해 CSS 기반의 미디어 쿼리를 활용하여 모바일 환경에서도 최적화된 화면을 제공하도록 UI/UX를 개선했습니다. (코드 레벨에서의 세부적인 UI 최적화 진행)
  * **데이터 관리 효율화:** 초기 데이터 관리에 엑셀을 고려했으나, 대량 데이터 처리 및 협업 과정에서의 비효율성 특히 늦은 업로드 속도를 체감하고, CSV와 DB 중심의 데이터 파이프라인을 구축하여 생산성을 높였습니다.

### 기능 구현 우선순위 분석표

이후 기능 구현 가능 목표

  * **유지비 시뮬레이션:** 모든 차종은 어려우나 현실적으로 가능한 현대 기아 위주의 부품 가격을 로드해서 조회하여 예상 정비 소요를 분석 할 수 있음.
  * **차량 즐겨 찾기 및 알람:** 사용자가 추후 방문 했을 때 기존에 검색했던 차량을 쉽게 접근.
  * **인기 옵션 리스트 제공:** 초보자에게도 매력적일 수 있는 옵션에 다한 정보를 제공.

-----

## 10\. 한 줄 회고

  * **양창일:** "시간이 촉박한 가운데 브레인스토밍 단계부터 데이터 통합 기획의 중요성을 절감했습니다. 특히, 상이한 사이트(카이즈유, 엔카)의 데이터를 사용자에게 하나의 화면에서 보여주기 위해 발생한 예상치 못한 예외 상황(Irregular)들을 해결하며, 기획의 정밀함이 개발 효율에 미치는 영향을 깊이 이해하게 되었습니다."
  * **김지우:** "단순한 기능 구현을 넘어 \*\*사용자 경험(UX)\*\*에 집중했습니다. 차량 스펙 시트를 읽기 어려워하는 일반 사용자를 타겟으로 하여, Streamlit의 한계 내에서도 최대한 직관적인 UI를 구현하려 노력했습니다. 첫 프로젝트였지만 좋은 팀원들 덕분에 기술적 난관(CSV to DB 전환, 레이아웃 깨짐 등)을 극복하고 완주할 수 있었습니다."
  * **정희영:** "DB를 설계하고 쿼리를 최적화하는 과정에서 데이터 엔지니어링의 경제성을 깊이 고민했습니다. 대용량 데이터를 다루는 실무적인 감각을 다시 한번 느낄 수 있었던 값진 경험이었습니다."
  * **정용희:** "훌륭한 팀원들 덕분에 연비 계산을 통한 사용자에게 제공할 수 있는 컨텐츠를 기획 후 적용 할 수 있었습니다. 

-----

## 11\. 참고문헌/자료

  * [CEO Message] 한국 자동차 시장에서 중고차 시장이 가지는 의미
      * 국내 중고차 시장 규모가 2024년 약 240만 대로 신차 시장(160만 대)을 앞지르며, 프리미엄 차종의 거래가 활발해지고 있음을 확인.
  * 현대차그룹부터 BMW까지…인증 중고차 시장 ‘활짝’
      * 국내 중고차 시장 규모가 2026년까지 35조 원으로 성장할 것이라는 전망과 기업들의 인증 중고차 사업 진출 현황 참조.
  * [SCOOP Posting] 중고차 매매업은 왜 신뢰 잃었을까
      * 허위 매물, 품질 보증 미비 등 소비자 불신의 원인을 파악하고, 이를 기술적으로 해결하기 위한 서비스 방향성 수립에 참고.
  * 우리나라 중고차 시장의 문제점과 대기업 진출
      * 정보 비대칭 문제와 불투명한 거래 관행 등 시장의 구조적 문제점을 파악하고, 객관적인 데이터 제공의 필요성을 재확인.
  * 소비자 10명 중 6명 “생애 첫차로 중고차 OK” - 헤럴드경제 (2022.04.06)
      * 중고차에 대한 2030 세대의 긍정적 인식 변화와 생애 첫차 구매 수요 증가를 확인하여 서비스 타겟팅 설정에 활용
  * 카이즈유: [https://www.carisyou.com/](https://www.carisyou.com/)
  * 엔카: [https://www.encar.com/mocha.do](https://www.encar.com/mocha.do)
  * 무공해 누리집: [https://ev.or.kr/nportal/evcarInfo/initEvcarChargePrice.do](https://ev.or.kr/nportal/evcarInfo/initEvcarChargePrice.do)
  * 오피넷: [https://www.opinet.co.kr/user/main/mainView.do](https://www.opinet.co.kr/user/main/mainView.do)
