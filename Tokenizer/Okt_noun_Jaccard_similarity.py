
'''
Twitter(Okt) - 오픈소스 한글 형태소 분석기
'''

import pandas as pd
from konlpy.tag import Okt
import nltk

data = pd.read_excel('petition.xlsx')[['제목', '본문']]
okt = Okt()

delete_word = ['이', '그', '그녀', '저', '것', '들', '제', '저희', '너', '되', '수', '않', '없', '아니',
               '때문', '곳', '등', '들', '중', '좀', '잘', '더', '더욱', '경우', '후', '때', '있', '하', ]
final_token = []
new_final_token = []
df = pd.DataFrame(columns=['청원글', '유사도'])

# 인풋
new_petition = okt.nouns(input("새로 청원할 글을 입력하세요: "))

# 1. 토큰화
# for i in range(10):
for i in range(data['제목'].count()):
    # 제목 토큰
    title_token = okt.nouns(data['제목'][i])
    # 콘텐트 토큰
    content_token = okt.nouns(data['본문'][i])
    text = nltk.Text(content_token)
    # 출현 빈도가 높은 본문 상위 토큰 15개
    selected_words = [f[0] for f in text.vocab().most_common(15)]

# 2. 제목이랑 본문상위토큰 합치기
    hap_token = title_token + selected_words
    # print("제목 토큰 & 본문에서 가장 많이 나온 명사 15개: \n", hap_token)

# 3. 불용어 제거하기
    for word in hap_token:
        if word not in delete_word:
            final_token.append(word)
    # print("불용어 제거한 최종 토큰: \n", final_token)
    # print("-" * 50)

# 4. 새로운 글 & 기존의 청원글과 자카드 유사도 검사
    def Jaccard_similarity(existing, new):
        # 중복되는 단어 제거
        existing = set(existing)
        new = set(new)
        return len(existing & new) / len(existing | new)

    # 새로운 청원글 토큰화
    new_text = nltk.Text(new_petition)
    new_selected_words = [f[0] for f in new_text.vocab().most_common(15)]
    # 새로운 청원글 불용어 제거
    for word in new_selected_words:
        if word not in delete_word:
            new_final_token.append(word)

    # 기존의 모든 청원글과 새로운 청원글의 자카드 유사도 출력
    print('"' + data['제목'][i] + '"' + " 청원글과의 유사도: ", Jaccard_similarity(final_token, new_final_token))

# 5. sorting된 순서로 자카드 유사도 가장 높은 상위 5개 글 제시
    df = df.append({'청원글':data['제목'][i], '유사도':Jaccard_similarity(final_token, new_final_token)}, ignore_index=True)
# print(df)
sorted_df = df.sort_values(by = ['유사도'], axis = 0, ascending=False, inplace=False)
sorted_petition = sorted_df.iloc[:5]

# 자카드 유사도가 가장 높은 상위 5개 청원글 출력
print("자카드 유사도가 가장 높은 상위 5개 청원글: \n", sorted_petition)
