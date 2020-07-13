## 토큰화

# 1. Hannanum - KAIST 말뭉치를 이용해 생성된 사전
from konlpy.tag import Hannanum

hannanum = Hannanum()

hannanum.analyze  # 구(Phrase) 분석
hannanum.morphs  # 형태소 분석
hannanum.nouns  # 명사 분석
hannanum.pos  # 형태소 분석 태깅

print(hannanum.analyze(u'롯데마트의 흑마늘 양념 치킨이 논란이 되고 있다.'))
print(hannanum.morphs(u'롯데마트의 흑마늘 양념 치킨이 논란이 되고 있다.'))
print(hannanum.nouns(u'다람쥐 헌 쳇바퀴에 타고파'))
print(hannanum.pos(u'웃으면 더 행복합니다!'))

# 2. Kkma - 세종 말뭉치를 이용해 생성된 사전 (꼬꼬마)
from konlpy.tag import Kkma

kkma = Kkma()

kkma.morphs  # 형태소 분석
kkma.nouns  # 명사 분석
kkma.pos  # 형태소 분석 태깅
kkma.sentences  # 문장 분석

print(kkma.morphs(u'공부를 하면할수록 모르는게 많다는 것을 알게 됩니다.'))
print(kkma.nouns(u'대학에서 DB, 통계학, 이산수학 등을 배웠지만...'))
print(kkma.pos(u'다 까먹어버렸네요?ㅋㅋ'))
print(kkma.sentences(u'그래도 계속 공부합니다. 재밌으니까!'))


# 3. Komoran- Java로 쓰여진 오픈소스 한글 형태소 분석기
from konlpy.tag import Komoran

komoran = Komoran()

komoran.morphs  # 형태소 분석
komoran.nouns  # 명사 분석
komoran.pos  # 형태소 분석 태깅

print(komoran.morphs(u'우왕 코모란도 오픈소스가 되었어요'))
print(komoran.nouns(u'오픈소스에 관심 많은 멋진 개발자님들!'))
print(komoran.pos(u'혹시 바람과 함께 사라지다 봤어?'))

# 4. Twitter(Okt) - 오픈소스 한글 형태소 분석기
from konlpy.tag import Okt

okt = Okt()

okt.morphs  # 형태소 분석
okt.nouns  # 명사 분석
okt.phrases  # 구(Phrase) 분석
okt.pos  # 형태소 분석 태깅

print(okt.morphs(u'단독입찰보다 복수입찰의 경우'))
print(okt.nouns(u'유일하게 항공기 체계 종합개발 경험을 갖고 있는 KAI는'))
print(okt.phrases(u'날카로운 분석과 신뢰감 있는 진행으로'))
print(okt.pos(u'이것도 되나욬ㅋㅋ'))
