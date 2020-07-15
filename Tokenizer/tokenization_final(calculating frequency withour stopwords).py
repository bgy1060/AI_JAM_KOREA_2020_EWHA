'''
Twitter(Okt) - 오픈소스 한글 형태소 분석기
'''

import pandas as pd
from konlpy.tag import Okt
import nltk

data = pd.read_excel('petition.xlsx')[['제목', '본문']]
okt = Okt()

#불용어 리스트 (필요시마다 추가 가능)
stop_words = ['이', '등등', '저희', '및', '기타','있', '하', '것', '들', '그', '되', '수', '보', '않', '없', '나', '주', '등', '생각하', '년', '자신', '지', '받', '를', '의', '내', '수', '더', '씨', '제', '저의', '제가', '자','저', '너무']


# 제목+본문 토큰에서 개수 추출
for i in range(data['제목'].count()):
    title_token2 = okt.nouns(data['제목'][i])
    content_token2 = okt.nouns(data['본문'][i])

    #본문에서 자주 사용된 상위 15개 단어 추출
    text1 = nltk.Text(content_token2)
    chosen_content_tokens =[f[0] for f in (text1.vocab().most_common(15))]

    #제목에서 자주 사용된 상위 15개 단어 추출
    text2 = nltk.Text(title_token2)
    chosen_title_tokens = [f[0] for f in (text2.vocab().most_common(15))]

    #제목+본문에서 자주 사용된 상위 15개 단어 추출
    union = title_token2 + chosen_content_tokens
    text3 = nltk.Text(union)
    chosen_every_tokens = [f[0] for f in (text3.vocab().most_common(15))]

    print("="*80)
    #불용어 제거 전 결과 출력
    print("제목+본문에서 추출한 상위 15개 명사:", chosen_every_tokens)

    print("불용어 제거 전 전체 토큰의 개수: ", len(chosen_every_tokens))
    print("불용어 제거 전 중복을 제외한 토큰의 개수:", len(set(chosen_every_tokens)))

    # 불용어 제거
    unique_every_tokens = set(chosen_every_tokens)
    for words in unique_every_tokens:
        if words in stop_words:
            while words in chosen_every_tokens: chosen_every_tokens.remove(words)

    #불용어 제거 후 결과 출력
    print("불용어 제거 후 추출한 최고 상위 15개 명사 :", chosen_every_tokens)
    print("불용어 제거 후 전체 토큰의 개수: ", len(chosen_every_tokens))
    print("불용어 제거 후 중복을 제외한 토큰의 개수:", len(set(chosen_every_tokens)))