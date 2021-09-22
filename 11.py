coins=[]
first=int(input("가장큰코인을 입력하세요:"))
second=int(input("두번째로 큰코인을 입력하세요:"))
third=int(input("가장작은코인을 입력하세요:"))
num = int(input("가격을 입력하세요:"))
coins.append(first)
coins.append(second)
coins.append(third)
mok=num // max(coins)
namugi = num % max(coins)
if coins[1] > namugi:
    mok = mok + namugi // coins[2]
else:
    mok = mok + namugi // coins[1]
    namugi = namugi % coins[1]
    mok = mok + namugi // coins[2]
print(mok)


