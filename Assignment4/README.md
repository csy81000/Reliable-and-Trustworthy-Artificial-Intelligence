# Reliable and Trustworthy Artificial Intelligence - Assignment #4

본 저장소는 선형 완화(Linear Relaxation) 및 분지한계법(Branch-and-Bound) 기반의 최첨단 신경망 검증 도구인 **$\alpha,\beta$-CROWN**을 활용한 과제 #4의 구현 및 분석 내용을 담고 있습니다. SMT 기반의 접근 방식을 사용하는 Marabou와 달리, $\alpha,\beta$-CROWN은 GPU 가속을 활용하여 대규모 네트워크에서도 뛰어난 확장성과 빠른 검증 속도를 보여줍니다.

## Installation
1. Install Conda Environment:
   `conda env update -n base -f environment.yaml`
2. Install auto_LiRPA:
   `cd auto_LiRPA && pip install -e .`

## How to Run
`python test.py`

## Overview
Problem 1: $\alpha,\beta$-CROWN 모델 디렉토리 탐색 
제공 모델 아키텍처 및 포맷: 주로 PyTorch(.pth) 및 ONNX 포맷으로 구성된 다양한 피드포워드 신경망(MLP), 합성곱 신경망(CNN), 잔차 네트워크(ResNet) 아키텍처를 지원합니다.  
검증 설정(Verification Configurations): 계층적인 YAML 설정 파일을 통해 데이터셋, 입력 스펙, 모델 경로, 바운드 전파 설정, 솔버 하이퍼파라미터(Timeout, Branching strategy 등)를 체계적으로 관리합니다.  
Marabou와의 차이점: Marabou는 수동으로 제약 조건을 명세해야 하는 SMT 기반 방식인 반면 , $\alpha,\beta$-CROWN은 auto_LiRPA 연산 그래프 분석을 바탕으로 복잡한 선형 완화 과정을 자동화하여 훨씬 뛰어난 대규모 네트워크 검증 가속을 제공합니다.  

Problem 2: 외부 모델 검증 실험   
대상 모델 및 데이터셋: 성능 비교 분석을 위해 MNIST 데이터셋을 타겟으로 하는 2개의 선형 레이어(Linear Layer)와 ReLU 활성화 함수 기반의 다층 퍼셉트론(MLP) 모델을 구축하였습니다.  
검증 속성 (Property): 지정된 반경 $\epsilon = 0.01$을 가지는 $l_{\infty}\text{-ball}$ 입력 섭동(Perturbation) 하에서의 국소적 강건성(Local Robustness)을 검증했습니다.  
결과 도출: Alpha-CROWN 바운드 전파 알고리즘과 Beta-CROWN의 분지한계법(Branch-and-Bound) 반복 연산을 결합하여 정밀한 출력 경계를 도출했습니다.




