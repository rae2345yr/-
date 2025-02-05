# -*- coding: utf-8 -*-
"""LAB03 - 애국가 워드클라우드.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OuVCWOBSnfJuQEpZyqXc5lIWDkKH-_C8

1. 애국가 가서 텍스트 파일로 저장 후 디렉토리에 업로드
2. 패키지 설치 후 라이브러리 불러오기
3. 파일에서 텍스트를 읽어와 분석 및 형태소 분리 후 빈도수를 변수 c에 저장
4. 워드 클라우드 객체를 생성하고 빈도수가 큰 단어가 크게 나타나도록 워드클라우드를 그리기
"""

#폰트 설정
import sys

# Google Colab 환경에서 실행 중인지 확인
if 'google.colab' in sys.modules:
    # debconf를 Noninteractive 모드로 설정
    !echo 'debconf debconf/frontend select Noninteractive' | \
    debconf-set-selections

    # fonts-nanum 패키지를 설치
    !sudo apt-get -qq -y install fonts-nanum

    # Matplotlib의 폰트 매니저 가져오기
    import matplotlib.font_manager as fm

    # 나눔 폰트의 시스템 경로 찾기
    font_files = fm.findSystemFonts(fontpaths=['/usr/share/fonts/truetype/nanum'])

    # 찾은 각 나눔 폰트를 Matplotlib 폰트 매니저에 추가
    for fpath in font_files:
        fm.fontManager.addfont(fpath)

#한국어 자연어 처리 패키지 설치
!pip install konlpy

from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
from konlpy.tag import Okt
import numpy as np

#애국가 파일을 읽기모드, UTF-8 인코딩으로 열기 및 분석
with open('/content/Data visualization/애국가.txt', 'r', encoding='utf-8') as f: text = f.read()
okt = Okt()
nouns = okt.nouns(text)
words = [n for n in nouns if len(n)>1]
c = Counter(words)

#워드클라우드 생성하기
wc = WordCloud(font_path='/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf',\
width=400, height=400, scale=2.0, max_font_size=250)
gen = wc.generate_from_frequencies(c)
plt.figure()
plt.imshow(gen)
wc.to_file('/content/Data visualization/애국가.png')