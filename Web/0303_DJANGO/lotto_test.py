url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1004'

response = requests.get(url).json()

bonus = response.get('bnusNo')
drwtNo1 = response.get('drwtNo1')
drwtNo2 = response.get('drwtNo2')
drwtNo3 = response.get('drwtNo3')
drwtNo4 = response.get('drwtNo4')
drwtNo5 = response.get('drwtNo5')
drwtNo6 = response.get('drwtNo6')

lotto_num = [drwtNo1, drwtNo2, drwtNo3, drwtNo4, drwtNo5, drwtNo6]

# 무작위 번호 생성 
my_nums = random.sample(range(1, 46), 6)