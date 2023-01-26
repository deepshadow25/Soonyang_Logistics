
# 📦물류센터 불량 패킹 검출 프로그램 구축📦
***
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
- 전체 이미지 개수 : 장
- 2 class : Hole, Wet
- 이미지 크기 : (640, 640) -> (1280, 1280)
- 데이터셋 형태 : 택배 상자 (갈색 판지)

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
>- 1차 Model result 분석, 평가
>  - Annotating 대폭 수정 
>- OCR / Model serving Reference Searching 시작
>  - App service 계획이 있었으나 차후로 미룸.
><br>
>
>**[2023.01.25 ~ 2023..]**  
>- 2차 Model training and testing
>  - 수정된 Annotating 적용
>  - Resolution 조정 (640*640 -> 1280*1280)
>- Github repository 결과물 정리
>  - Readme 작성


#### 👨‍👩‍👧‍👧Team Roles
***
| Member | Role |
| ---- | ---- |
| 김재현 | Data Processing, Model testing, OCR Modeling, Model web serving |
| 이성연 | Data Processing,  Model testing, Reference Searching and studying |
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
│     │		├── v7
│     │		└── v8
│     ├── EfficientDet 
│     └── RetinaNet
│  
├── Dataset
│     └──   
│ 
├── Serving  
│     └── YOLOv7x  
│   
├── OCR  
│     ├── 
│     ├── 
│     ├── 
│     └── 
```
---
