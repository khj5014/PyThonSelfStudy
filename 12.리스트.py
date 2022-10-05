#리스트 []

# 지하철 칸별로 10 , 20, 30
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10,20,30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호 몇번째 칸?
print(subway.index("조세호"))

# 하하 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)

# 정형돈을 유재석 과 조세호 사이에 태움
subway.insert(1,"정형돈")
print(subway)

for i in range(0,3):
    print(subway.pop())
    print(subway)
    i+1

