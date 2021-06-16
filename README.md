# AI_JAM KOREA 2020 EWHA 데장코알라

## 1. 프로젝트 소개

### 1) 프로젝트 주제

- 국민청원 추천 시스템 구현 및 효율화 서비스 제안

<br/>

### 2) 프로젝트 제안 배경

청와대 국민 청원 게시판은 국민들이 직접 원하는 법을 국회에 제안하거나 사회적 이슈가 되고 있는 사건들에 대해 해결 방안들을 제시할 수 있는 사이트로, 청원이 20만명 이상의 동의를 얻으면, 정부나 청와대 관계자들이 그에 대해 답변을 달아준다.

국민 청원 사이트를 이용하며 **비슷한 내용의 청원들이 중복되어 올라오는 것**을 본 경험이 있을 것이다. 20만명 이상의 동의를 받아야 답변을 받을 수 있는 국민 청원 게시판의 특성상, 하나의 청원에 대하여 국민들이 집중적으로 관심을 갖는 것이 중요한데, 비슷한 내용의 청원이 있는지 몰라 계속 무분별하게 올리다 보면 그 관심이 분산되어 답변을 받지 못할 확률이 커진다. 실제로 2019년 1월 6일 김민희 차장은 간 조선 인터뷰를 통해서 청와대 국민 청원 게시판에 엇비슷한 경우의 청원이 150개씩 매일 올라와 청원글이 묻히기 쉬우며, 똑같은 내용의 청원이 여러개로 분산되면서 20만명 이상의 동의를 얻기가 힘들어 진다고 밝힌 바 있다.

본 프로젝트에서는 이에 문제점을 느끼고 데이터 분석과 딥러닝을 통해 이러한 문제를 해결할 수 있는 서비스를 제안한다.

<br/>

### 3) 프로젝트 목표

- 사용자가 청원을 입력하면, 해당 청원과 비슷한 내용을 가진 진행 중인 청원을 추천해 준다. (최대 5개)

- 새로운 청원을 입력하면, 미리 해당 청원은 몇 명 정도의 동의를 받을 것인지 예측을 해준다. 

<br/>

### 4) 필요 지식 & 기술

- 청와대 국민 청원 사이트에서 현재 진행 중인 청원, 만료된 청원, 답변된 청원의 데이터를 크롤링 해온다. 이때 청와대 국민 청원 사이트는 **selenium** **패키지**를 사용했다.

- 각 청원 별로 제목과 본문 데이터의 키워드를 뽑을 줄 알아야 한다. 이는 **한글 자연어 처리 과정**을 통해, 각 내용을 토큰화 시키는 과정이 먼저 필요하다. 청원은 주로 명사가 많이 사용된다는 점을 착안해서 명사로 내용을 **토큰화** 시키고, 대명사, 조사, 지시사, 감탄사 등의 내용에 중요한 영향을 끼치지 않는 **불용어 부분을 제거**한다. 제거한 토큰들의 빈도를 분석해, 가장 많이 사용된 토큰의 상위 10개를 뽑아 키워드로 지정한다.

- 사용자가 인풋으로 넣은 청원 역시 토큰화 과정을 거쳐 키워드를 뽑아낸다. 그럼 그 청원과 이미 있는 청원들 사이의 **자카드 유사도**를 비교하여, 유사도가 높다고 판단된 상위 (최대) 5개까지의 청원들을 추천해 준다.

- 청원수를 미리 예측 할 때는, **FastText(단어 임베딩 및 텍스트 분류 학습을 위한 라이브러리)**를 이용하여, 토큰끼리 유사도가 높은 관계를 찾는다. 그 관계로부터 청원수를 계산하여 출력해준다.
  -  자카드 유사도를 통해 새로운 청원글과 기존의 청원글에서 추출한 명사 토큰 사이 유사도가 높은 관계를 찾는다.
  - FastText를 사용하여 인풋 청원 토큰 5개와 각 5개의 추천 청원 토큰 5개를 FastText 사용하여 토큰들을 모두 2차원 벡터로 표현한다.
  - 2차원 벡터로 표현된 데이터를 좌표 평면 상에 점으로 시각화한다.
  - 토큰별 유사도(점 사이 거리)를 측정한다.
  - 해당 청원의 유사도와 동의받은 사람의 수를 곱하여 평균을 계산한다.

<br/>

### 5) 프로젝트 기대효과

본 서비스를 통해 이미 있는 청원에 동의하게 유도하여 사용자들의 관심을 한 곳으로 모을 수 있고, 게시판 관리자 입장에서도 비슷한 내용의 주제가 무분별하게 올라오는 경우를 막아 게시판을 보다 쉽게 관리할 수 있을 것으로 기대된다. 더 나아가 청원수 예측까지 해주게 된다면, 관리자 입장에서는 가치 있는 청원이 묻히는걸 방지할 수 있고, 사용자 입장에서는 계속해서 쏟아지는 청원의 노출로 인한 피로도가 감소될 수 있을 것이다. 또한, 해당 청원에 대한 청원수를 미리 예측해 봄으로, 국민들의 정치적 이슈 트렌드 역시 미리 파악할 수 있을 것이다.

<br/>

## 2. 데이터 수집

### 1) 데이터 소스

- 청와대 국민 청원 사이트
  -  https://www1.president.go.kr/petitions/?c=0&only=1&page=1&order=1

<br/>

### 2) 수집 데이터

- 현재 진행 중 청원, 만료된 청원 데이터
- 청원 제목, 청원수, 카테고리, 시작일, 마감일, 본문 데이터를 openpyxl 형태의 데이터로 수집

![img](https://lh3.googleusercontent.com/hXPamcA5GBheQEgv1LXGiOstRvB2GCfMh46fqBpxdSLJmbg-nXxXfNrH6ubI_sFR68o4r4R8VI-ltHi8iBiGE-APCC8Z2VfkHPTtWmCpCHIWWcGd3-QQS7r07Uty09euaIrrGfFNcu4)

<br/>

## 3. 데이터 전처리 및 토큰화

- Twitter(Okt- 오픈소스 한글 형태소 분석기) 이용하여 명사 추출  
- 출현 빈도가 높은 상위 토큰 추출

```python
content_token = okt.nouns(content)
text = nltk.Text(content_token)
print("출현 빈도가 높은 상위 토큰 15개: ", text.vocab().most_common(15))
```

- 불용어 제거

```python
# 3. 불용어 제외하기
    delete_word = ['이', '그', '그녀', '저', '것', '들', '제', '저희', '너', '되', '수', '않', 	'없', '아니','때문', '곳', '등', '들', '중', '좀', '잘', '더', '더욱', '경우', '후', '때', 	'있', '하', ]
    final_token = []
    for word in hap_token:
        if word not in delete_word:
            final_token.append(word)
    print("대명사 등 의미 없는 단어 제거한 최종 토큰: \n", final_token)
```

<br/>

## 4. Fast Text를 이용한 유사도 계산

- 새로운 글과 기존의 청원글 자카드 유사도 검사

```python
 def Jaccard_similarity(existing, new):
        # 중복되는 단어 제거
        existing = set(existing)
        new = set(new)
        return len(existing & new) / len(existing | new)
```

- 기존에 존재하는 청원글과 새로운 청원글의 자카드 유사도 출력

```python
df = df.append({'청원글':data['제목'][i], '청원수': data['청원수'][i], 
                '상위토큰': final_token, '유사도':Jaccard_similarity(final_token, 		 					new_final_token)},ignore_index=True)
final_token = []
```

- 자카드 유사도가 가장 높은 상위 5개 글 제시

```python
sorted_df = df.sort_values(by = ['유사도'], axis = 0, ascending=False, inplace=False)  # 유사도 기준 내림차순으로 정렬
sorted_petition = sorted_df.iloc[:5]  # 상위 5개 글 추출 

# 자카드 유사도가 가장 높은 상위 5개 청원글 출력
print("자카드 유사도가 가장 높은 상위 5개 청원글: \n", sorted_petition)  
# 제목, 청원수, 상위토큰, 유사도 출력
```

  

![img](https://lh5.googleusercontent.com/L1dHOo9VdgUANx01VcYBM1YAATZ9MXSHavNwPq9aRH8X8OijbyUH8KaIenO3v1ZyzOFs4WebB4W99Q3BoqdO9AsWTs8jWGHGqIxTo_m0lGvPn6WoCkjjRKcGVPXUac5yl2Zp7yTd8AE)

- 유사도 그래프 출력

```python
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
```

![img](https://lh6.googleusercontent.com/orovDDQo99xGWD3xD2Ue1g3xot4N9s0iZSi3shpXzwqsXsVI6c9dMeRumDM1NoC0AGFQoCGG4GLdwiFOZ_TaqSCTf8bFAGQA1aLDgZHvEoPCHOihpaMdy7XG8pzhoxDSExMyS3uctN8)

- 유사도 기반 청원수 예측

```python
numerator = 0
denominator = 0

for i in range(5):   # 5개의 기존 청원글
    for k in range(5): # 5개의 상위토큰           
        similarity_rate = ko_model.wv.similarity(new_final_token[k], 							sorted_petition.iloc[i].iloc[2][k]) # 1:1 유사도
        similarity_rate_hap += similarity_rate
    similarity_rate_mean = similarity_rate_hap / 5   # 상위토큰 5개의 유사도 평균
    
    weighted_petition_number = similarity_rate_mean * sorted_petition.iloc[i].iloc[1] 
    # 유사도*청원수
    numerator += weighted_petition_number  # 분자(유사도*청원수 총합)
    denominator += similarity_rate  # 분모(유사도 총합) 
    
final_prediction = numerator/denominator
print("예상 청원수: ", final_prediction)
```

