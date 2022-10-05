#방법 1
print("a"+"b")
print("나는 %d살입니다" %20)
print("나는 %s을 좋아해요" %"파이썬")
print("Apple 은 %c 로 시작해요."% "A")

#방법 2
print("나는 {}살입니다".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파란", "빨강"))
print("나는 {0}색과 {1}색을 좋아해요".format("파란", "빨강"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란", "빨강"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age=20 )) 

#방법 4
age = 20
color = "빨간"
print(f"나는{age}살이며, {color}색을 좋아해요")