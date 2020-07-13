'''
Twitter(Okt) - 오픈소스 한글 형태소 분석기
'''

import pandas as pd
from konlpy.tag import Okt

data = pd.read_excel('petition.xlsx')[['제목', '본문']]
# print(data.head())

okt = Okt()

# 타이틀 토큰
print("<제목에서 추출한 명사>")
for title in data['제목']:
    title_token = okt.nouns(title)
    print(title_token)
print("-"*60)

# 콘텐트 토큰
print("<본문에서 추출한 명사>")
for content in data['본문']:
    content_token = okt.nouns(content)
    print(content_token)


