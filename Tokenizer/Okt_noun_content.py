'''
Twitter(Okt) - 오픈소스 한글 형태소 분석기
'''

import pandas as pd
from konlpy.tag import Okt
import nltk

data = pd.read_excel('petition.xlsx')[['제목', '본문']]
okt = Okt()

# 콘텐트 토큰에서 개수 추출
for content in data['본문']:
    content_token = okt.nouns(content)
    print("본문에서 추출한 명사:", content_token)

    text = nltk.Text(content_token)

    print("전체 토큰의 개수: ", len(content_token))
    print("중복을 제외한 토큰의 개수:", len(set(content_token)))
    print("출현 빈도가 높은 상위 토큰 15개: ", text.vocab().most_common(15))
    print("-"*60)
