'''
Twitter(Okt) - 오픈소스 한글 형태소 분석기
'''

import pandas as pd
from konlpy.tag import Okt
import nltk

data = pd.read_excel('petition.xlsx')[['제목', '본문']]
okt = Okt()

# 1. 토큰화
for i in range(data['제목'].count()):
    title_token = okt.nouns(data['제목'][i])      # 제목 토큰
    content_token = okt.nouns(data['본문'][i])    # 콘텐트 토큰
    text = nltk.Text(content_token)
    selected_words = [f[0] for f in text.vocab().most_common(15)]  # 출현 빈도가 높은 본문 상위 토큰 15개: ('단어', '빈도수') 중 단어만

# 2. 제목이랑 본문상위토큰 합치기
    hap_token = title_token + selected_words
    print("제목 토큰 & 본문에서 가장 많이 나온 명사 15개: \n", hap_token)

# 3. 불용어 제외하기
    delete_word = ['이', '그', '그녀', '저', '것', '들', '제', '저희', '너', '되', '수', '않', '없', '아니',
                   '때문', '곳', '등', '들', '중', '좀', '잘', '더', '더욱', '경우', '후', '때', '있', '하', ]
    final_token = []
    for word in hap_token:
        if word not in delete_word:
            final_token.append(word)
    print("대명사 등 의미 없는 단어 제거한 최종 토큰: \n", final_token)
    print("-" * 50)


