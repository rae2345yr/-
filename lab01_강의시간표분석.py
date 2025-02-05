# -*- coding: utf-8 -*-
"""LAB01_강의시간표분석

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17IeA_ectCeE0NrCy4qHAoZ_EK7q_lrmp
"""



"""1. 열이름과 시간표 데이터를 리스트로 작성합니다"""

import pandas as pd

# 데이터 생성
columns = ["과목번호", "과목명", "강의실", "시간수"]
data = [
    ["C1", "AI", "R1", 3],
    ["C2", "빅데이터", "R2", 2],
    ["C3", "경영학", "R3", 3],
    ["C4", "디자인", "R4", 4],
    ["C5", "건축", "R2", 2],
    ["C6", "예술", "R3", 1]
]

"""2)시간표 데이터를 데이터프레임 객체 df로 변환하여 csv파일로 저장합니다."""

# 데이터프레임 생성
df = pd.DataFrame(data, columns=columns)
df

"""3. Timetable.csv파일을 데이터 프레임 객체 df2로 읽고 열을 추가합니다."""

#경로지정하고 csv형식으로 파일 저장
df.to_csv("/content/Timetable.csv")

#파일 불러오기
df2 = pd.read_csv('/content/Timetable.csv')

#열 추가
df2["교수"] = ["임영웅", "이순신", "삼순이", "홍천재", "짬퐁이", "윤석열"]
df2 = df2.drop(columns=["Unnamed: 0"])
df2

"""4.강의실을 기준으로 그룹화하여 최대 시간 수를 구합니다."""

#최댓값 가져오기
max = df2.groupby("강의실")["시간수"].max()
#출력
max