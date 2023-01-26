
# 물류센터 불량 패킹 검출 프로그램 구축
***
#### 👨🏿‍🤝‍👨🏿Member
[김재현](https://github.com/jh941213) | [이성연](https://github.com/deepshadow25)
:-: | :-: | 
<img src="https://user-images.githubusercontent.com/115054681/214764862-b2a12ce8-50e6-46bb-b020-db979ebe8713.jpg" width="100" height="100"/>|<img src="https://user-images.githubusercontent.com/115054681/214764898-9d3809a4-b20d-48f6-b911-b9521355fc51.png" width="100" height="100">
***				
## Index

### Main Project

- [📝Project Summary](#project-summary)
- [🗓Procedures](#procedures)
- [👨‍👩‍👧‍👧Team Roles](#team-roles)
- [❄Features](#features)
- [🏁Result](#result)
- [🤍Conclusion](#conclusion)

### [Appendix](#appendix)
- [♟Requirements](#requirements)
- [📁Folder Structure](#folder-structure)


### Main Project

#### 📝Project Summary

프로젝트 주제


- 개요 및 기대효과


- 활용 장비 및 재료
서버:
라이브러리: 
개발 및 협업 툴: 

- 데이터 셋의 구조도
데이터셋 통계

전체 이미지 개수 : 장

2 class : Hole, Wet

이미지 크기 : (640, 640) -> (1280, 1280)

데이터셋 형태 : COCO Dataset

Annotation file




images :


#### 🗓Procedures

#### 👨‍👩‍👧‍👧Team Roles

| 김재현 | Data Processing, Model testing, OCR Modeling, Model web serving |
| ----- | --- |
| 이성연 | Data Processing,  Model testing, Reference Searching and studying |


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
├── mmdetection  
│     ├── ResNet152  
│     ├── ResNest200  
│     └── SwinT    
│  
├── UniverseNet  
│     └── UniverseNet  
│ 
├── yolov7  
│     └── YOLOv7x  
│   
└── dataset  
│     ├── train.json  
│     ├── train_split.json  
│     └── valid_split.json  
