import pandas as pd
from konlpy.tag import Okt

data = pd.read_excel('petition.xlsx')[['제목', '본문']]
print(data)

## Twitter(Okt) - 오픈소스 한글 형태소 분석기
okt = Okt()
# 타이틀 토큰
for d in data['제목']:
    title_token = okt.nouns(d)
    print(title_token)
# 콘텐트 토큰
for a in data['본문']:
    content_token = okt.nouns(a)
    print(content_token)
#콘텐트에서 가장 많이 나온 명사 7
