
# 📦물류센터 불량 패킹 검출 프로그램 구축📦
<img src="https://camo.githubusercontent.com/d4f32e957f02d8c924440af9d8e7fd559efcee461d4ed5b19791b1f0d8076f0f/68747470733a2f2f7777772e6461696c796c6f672e636f2e6b722f6e6577732f70686f746f2f3230313230342f333838385f313733335f343631322e6a7067">


## 👨🏿‍🤝‍👨🏿Member
[김재현](https://github.com/jh941213) | [이성연](https://github.com/deepshadow25)
:-: | :-: 
<img src="https://user-images.githubusercontent.com/115054681/214764862-b2a12ce8-50e6-46bb-b020-db979ebe8713.jpg" width="100" height="100"/>|<img src="https://user-images.githubusercontent.com/115054681/214764898-9d3809a4-b20d-48f6-b911-b9521355fc51.png" width="100" height="100">
***				
## Index
- ### [Main Project](#main-project)
- [📝Project Summary](#project-summary)
- [🗓Procedures](#procedures)
- [👨‍👩‍👧‍👧Team Roles](#team-roles)
- [❄Features](#features)
- [🏁Result](#result)
- [🤍Conclusion](#conclusion)
- ### [Appendix](#appendix)
- [♟Requirements](#requirements)
- [📁Folder Structure](#folder-structure)
***
### Main Project
***
#### 📝Project Summary
프로젝트 주제
- 개요 및 기대효과
- 활용 장비 및 재료
서버:
라이브러리: 
개발 및 협업 툴: 
- 데이터 셋의 구조도

데이터셋 통계

1. 상자 데이터
- 전체 이미지 개수 : 3,011장
- 2 class : Hole, Wet
- 이미지 크기 : (640, 640) -> (1280, 1280)
- 데이터셋 형태 : 택배 상자 (갈색 판지)

2. 택배송장 데이터
- 전체 송장 개수 : 187장
GS 편의점 송장 80장
CU 편의점 송장 106장
시험데이터 추가 1장 (실제 송장으로 ocr 테스트)

Annotation file




images :


#### 🗓Procedures

[timetable](https://timetreeapp.com/calendars/Bs7yrwhD6Q5H)

>**[2023.01.02 ~ 2023.01.06]**
>- 프로젝트 주제 탐색 및 선정
>- 프로젝트 계획 구상
><br>
>
>**[2023.01.06 ~ 2023.01.18]**
>- 데이터 수집 및 전처리
>  - Anomaly Detection 특성상 불량데이터를 구하기 어려웠으므로 이를 직접 만들어냄.
>  - 가장 보편적인 택배 상자(갈색 판지 상자)의 데이터만을 고려
><br>
>
>**[2023.01.14 ~ 2023.01.16]**
>- 1차 Model training and testing
>  - Real Time & Anomaly Detection
>  - Train, valid dataset split
>  - Data Augmentation
><br>
>
>**[2023.01.17 ~ 2023.01.24]**
>- 1차 Anomaly Detection model result 분석, 평가
>  - Annotating 대폭 수정 
>- OCR / Model serving Reference Searching 시작
>  - App service 계획이 있었으나 차후로 미룸.
><br>
>
>**[2023.01.25 ~ 2023.01.27]**  
>- 2차 Detection Model training and testing
>  - 수정된 Annotating 적용
>  - Resolution 조정 (640*640 -> 1280*1280)
>  - 결과 분석, 평가 후 3차로 넘어감
>- Github repository 결과물 정리
>  - Readme 작성
><br>
>
>**[2023.01.28 ~ 2023.02.06]**  
>- OCR model 준비
>  - 택배 운송장 데이터 준비 (임의의 주소데이터 생성, 송장 인쇄)
>  - OCR API test (Google Cloud Vision, Naver Clova)
>  - OCR model searching (EazyOCR, Tesseract 등)
>- 3차 Detection model training and testing
>  - use EfficientDet models. (D0, D1)
>  - also used Yolo models : Yolo가 Eff.Det보다 나음 확인
>- App 구현 계획을 Web Serving으로 수정. (Insight 다시보기)
>  - 고객에게 알림을 발송하는 기능이 필요없음.
>  - 물류회사(공장) 내부에서만 사용하는 프로그램으로 사용 : 웹으로만 구현해도 됨.
><br>
>
>**[2023.02.07 ~ 2023.02.]**
>- Presentation 준비
>  - Data, Model, OCR, Git, any other process 정리
>  - 발표 대본 제작, 디자인 구상
><br>
>
>**[2023.02.17]**
>- 중간발표 및 점검.

#### 👨‍👩‍👧‍👧Team Roles
***
| Member | Role |
| ---- | ---- |
| 김재현 | Data Processing(Anomaly Box Data), Model testing (Yolo v7, v8), OCR Modeling, Model web serving, Making Presentation File |
| 이성연 | Data Processing(Anomaly Box Data, WayBill Data), Model testing (Yolo v4, EfficientDet), Reference Searching and studying, Presentation |
***

#### ❄Features


#### 🏁Result


데이터 전처리

			
모델 개요


시연결과
Confusion Matrix


				
Metric : mAP50


#### 🤍Conclusion

잘한 점들

아쉬운 점들

프로젝트를 통해 배운점

### Appendix

#### ♟Requirements

#### 📁Folder Structure
---
```
├── Model
│     ├── Yolo  ├── v4
│     │		├── v5
│     │		├── v7
│     │		└── v8
│     ├── CoreML (yolo v2, v3 based)
│     └── EfficientDet ├── D0
│     		       └── D1
│  
├── Dataset
│     ├── Anomaly Box ├── Wet 2305
│     │		      └── Hole 2231
│     └── Waybill ├── CU 106
│     	          └── GS 80
│ 
├── Serving  
│     └── YOLOv8s  
│   
├── OCR  
│     ├── 
│     ├── 
│     ├── 
│     └── 
```
---
