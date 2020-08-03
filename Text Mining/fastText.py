import gzip
from gensim import models
ko_model = models.fasttext.load_facebook_model('cc.ko.300.bin.gz')
from sklearn.decomposition import PCA
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from konlpy.tag import Okt
import nltk


# 새로운 글 & 기존 글(상위 5개) 토큰 사이 유사도 검사
# 1. 데이터 불러오기

data = pd.read_excel('last_petition_datacrawling.xlsx')[['제목', '청원수', '본문']]
okt = Okt()

delete_word = ['현재', '지금', '상반기', '하반기', '이', '그', '그녀', '저', '것', '들', '제', '저희', '너', '되', '물', '수', '않', '없', '아니',
               '때문', '곳', '등', '들', '중', '좀', '잘', '더', '더욱', '경우', '후', '때', '있', '하', '생각', '청원', '국민청원']

final_token = []
new_final_token = []
df = pd.DataFrame(columns=['청원글', '청원수', '상위토큰', '유사도'])


# 2. 인풋 받기
# 인풋
new_petition = okt.nouns(input("새로 청원할 글을 입력하세요: "))


# 3. 새로운 청원글 토큰화

# 새로운 청원글 토큰화
new_text = nltk.Text(new_petition)
new_selected_words = [f[0] for f in new_text.vocab().most_common(15)]
print(new_selected_words)

# 새로운 청원글 불용어 제거
for word in new_selected_words:
    if word not in delete_word:
        new_final_token.append(word)
        
new_final_token = new_final_token[:5]

print(new_final_token)

# 3. 기존 청원글 토큰화

# for i in range(10):
for i in range(data['제목'].count()):
    # 제목 토큰
    title_token = okt.nouns(data['제목'][i])
    # 콘텐트 토큰
    content_token = okt.nouns(data['본문'][i])
    text = nltk.Text(content_token)
    # 출현 빈도가 높은 본문 상위 토큰 15개
    selected_words = [f[0] for f in text.vocab().most_common(15)]
    
# 4. 제목이랑 본문상위토큰 15개 합치기
    hap_token = title_token + selected_words
#     print("제목 토큰 & 본문에서 가장 많이 나온 명사 15개: \n", hap_token)
    
# 5. 불용어 제거하기
    for word in hap_token:
        if word not in delete_word:
            final_token.append(word)
            
# 5-2. 불용어 제거한 후, 5개 토큰만 추출
    final_token = final_token[:5]
#     print("불용어 제거한 최종 토큰: \n", final_token)
    

#     print("-" * 50)
    
# 6. 새로운 글 & 기존의 청원글과 자카드 유사도 검사
    def Jaccard_similarity(existing, new):
        # 중복되는 단어 제거
        existing = set(existing)
        new = set(new)
        return len(existing & new) / len(existing | new)

    # 기존의 모든 청원글과 새로운 청원글의 자카드 유사도 출력
#     print('"' + data['제목'][i] + '"' + " 청원글과의 유사도: ", Jaccard_similarity(final_token, new_final_token))
#     print("-" * 50)

    df = df.append({'청원글':data['제목'][i], '청원수': data['청원수'][i], 
                    '상위토큰': final_token, '유사도':Jaccard_similarity(final_token, new_final_token)}, 
                   ignore_index=True)
    final_token = []
    
    # 8. sorting된 순서로 자카드 유사도 가장 높은 상위 5개 글 제시
    
    sorted_df = df.sort_values(by = ['유사도'], axis = 0, ascending=False, inplace=False)  # 유사도 기준 내림차순으로 정렬
sorted_petition = sorted_df.iloc[:5]  # 상위 5개 글 추출 

# 자카드 유사도가 가장 높은 상위 5개 청원글 출력
print("자카드 유사도가 가장 높은 상위 5개 청원글: \n", sorted_petition)  # 제목과 청원수, 상위토큰, 유사도 나옴.

# 9. 유사도 그래프
words = []

# 그래프
for i in range(5):
    words += sorted_petition.iloc[i].iloc[2] + new_final_token # 기존 글 다섯개 토큰 + 새로운 글 다섯개 토큰
    
pca = PCA(n_components=2)
xys = pca.fit_transform([ko_model.wv.word_vec(w) for w in words])
xs = xys[:,0]
ys = xys[:,1]

mpl.rcParams['axes.unicode_minus'] = False # 마이너스 부호 깨짐 방지
plt.rc('font', family = 'NanumGothic')   #나눔고딕을 기본 글꼴로 설정
plt.figure(figsize=(14, 10), )
plt.scatter(xs, ys, marker='o')
for i, v in enumerate(words):
    plt.annotate(v, xy=(xs[i], ys[i]))
    

# 10. 새로운 청원글 & 기존 청원글 상위토큰(단어) 1:1 유사도 검사

# 새로운 청원글의 상위토큰: new_final_token
# 기존 청원글 5개의 상위 토큰: sorted_petition['상위토큰']
prediction = 0
similarity_rate = 0
similarity_rate_hap = 0


for i in range(5):   # 5개의 기존 청원글
    for k in range(5): # 5개의 상위토큰           
        similarity_rate = ko_model.wv.similarity(new_final_token[k], sorted_petition.iloc[i].iloc[2][k]) # 1:1 유사도
#         print(similarity_rate)

# 유사도 기반 청원수 예측
numerator = 0
denominator = 0

for i in range(5):   # 5개의 기존 청원글
    for k in range(5): # 5개의 상위토큰           
        similarity_rate = ko_model.wv.similarity(new_final_token[k], sorted_petition.iloc[i].iloc[2][k]) # 1:1 유사도
        similarity_rate_hap += similarity_rate
    similarity_rate_mean = similarity_rate_hap / 5   # 상위토큰 5개의 유사도 평균
    
    weighted_petition_number = similarity_rate_mean * sorted_petition.iloc[i].iloc[1] # 유사도*청원수
    numerator += weighted_petition_number  # 분자(유사도*청원수 총합)
    denominator += similarity_rate  # 분모(유사도 총합) 
    
final_prediction = numerator/denominator
print("예상 청원수: ", final_prediction)
