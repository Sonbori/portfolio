---
title: "Random Forest로 Titanic 생존자 예측"
date: "2025-07-30"
tags: ["머신러닝", "Kaggle"]
summary: "Titanic 데이터셋으로 랜덤 포레스트 모델을 구현해 생존자 예측 정확도 82% 달성하기"
---

# 랜덤 포레스트 모델링

`sklearn.ensemble.RandomForestClassifier`를 활용해 다음과 같은 과정을 진행했습니다.

```python
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)