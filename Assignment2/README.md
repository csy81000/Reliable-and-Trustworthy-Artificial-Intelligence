# Reliable and Trustworthy Artificial Intelligence - Assignment #2

DeepXplore를 이용한 신경망 차분 테스트(Differential Testing) 및 적대적 공격과의 연계 분석

## 1. 개발 환경 설정 (Setup Instructions)
본 프로젝트는 DeepXplore의 원본 환경을 최대한 유지하면서, 현대적인 아나콘다 환경에서 구동 가능하도록 패키지 버전을 조정하였습니다.

* **OS:** Windows 10/11
* **언어:** Python 2.7.12
* **가상환경 이름:** deepx

### 환경 구축 순서:
1. `conda create -n deepx python=2.7.12`로 가상환경 생성
2. `pip install tensorflow==1.15.0` 설치 (원본 사양인 1.3.0의 배포 문제로 인해 1.15.0으로 대체)
3. `pip install keras==2.0.8` 설치
4. `pip install "protobuf<3.20"` 설치 (Protobuf 버전 충돌 에러 해결을 위한 조치)

## 2. DeepXplore 코드 수정 및 에러 해결 사항
원본 DeepXplore 코드를 실행하는 과정에서 발생한 다음 문제들을 해결하였습니다.

* **TensorFlow ModuleNotFoundError:** 가상환경 내 엔진 미설치 문제 해결.
* **Protobuf Descriptor TypeError:** 최신 버전의 Protobuf와 TF 1.15 간의 충돌을 방지하기 위해 Protobuf를 3.20 미만으로 다운그레이드함.
* **Argument Error:** `gen_diff.py` 실행 시 인자 개수 불일치 문제를 파악하고 올바른 파라미터(weight_diff, weight_nc, seeds, grad_iterations, threshold)를 적용함.
* **Path Error:** `Drebin` 등 특정 예제 폴더 내의 데이터 경로 문제를 파악하고, 과제 목표에 맞춰 CIFAR-10 환경으로 전환 준비를 마침.

## 3. 실행 방법 (How to Run)
본 프로젝트의 핵심 로직은 test.py에 통합되어 있으며, 실행 시 차분 테스트 수행 및 결과 저장이 자동으로 이루어집니다.

## 4. 실험 결과  
발견된 불일치 입력 개수: 5개 이상 (시각화 완료) 뉴런 커버리지(Neuron Coverage): 테스트 스크립트 실행 결과에 따라 각각 기록됨.   
분석: 두 모델의 가중치 초기화 및 학습 방식 차이로 인해 특정 경계 영역에서 예측 불일치가 발생함을 확인하였습니다.


## 5. 제출 파일 목록 (Submission Checklist)  
requirements.txt: 모든 의존성 목록  
test.py: DeepXplore 실행 및 결과 출력 스크립트  
results/: 시각화된 불일치 사례 PNG 파일 폴더  
report.pdf: 문제 2번에 대한 에세이  
README.md: 본 설명 문서  
