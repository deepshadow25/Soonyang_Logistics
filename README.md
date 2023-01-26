
# 물류센터 


#### 🔥Member
[김재현](https://github.com/jh941213) | [이성연](https://github.com/deepshadow25)
---- | ---- | 
 |  | 

				
## Index

🏅Project Summary 

🗓Procedures

👨‍👩‍👧‍👧Team Roles

🌿Features

📊Result

👨‍💻Conclusion

💻Requirements

Appendix Folder Structure



### 🏅Project Summary

#### 프로젝트 주제


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



👩‍👩‍👧‍👦Team Roles
김재현 : 
이성연 : 

🗃️Procedures

🌿Features


📊Result


데이터 전처리

			
모델 개요
큰 BackBone 구조의 Object Detection Model들이 학습을 잘하고 데이터가 가지고 있는 문제를 해결하기 어려워 앙상블을 통해 성능 향상을 목표 Cascade, Yolo, UniverseNet 학습에 사용 학습한 모델들의 Confusion Matrix를 시각화하고 이를 바탕으로 모델별로 가중치를 결정하고 Weight Box Fusion을 통해서 앙상블


시연결과
Confusion Matrix


				
Metric : mAP50


👨‍💻Conclusion
잘한 점들

아쉬운 점들

프로젝트를 통해 배운점

💻Requirements

🏗️Folder Structure
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
