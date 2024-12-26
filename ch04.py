# 廻圈, 主要運用在執行重覆的動作
# for 廻圈, 若沒有設啟始值，啟始值預設都是 0
# for 變數 in (啟始，終值，間隔）

for i in range(10):
    print(i)

for i in range(1, 10, 2):
    print(i)

for i in range(1, 10):
    print(i)

# 多層次廻圈, 九九乘法表
for i in range(1, 10):
    for j in range(1, 10):
        print(" {} * {} = {}".format(i, j, i*j), end="\t")
    print("")

# while 廻圈, 它必須要有一個條件式去控制廻圈何時中止
# while { }
a = 1
while a <= 10:
    print(a)
    a += 1

# break and continue
# break 用於中止廻圈執行
a = 1
while a <= 10:
    print(a)
    a += 1
    if a == 5:
        break

for i in range(1, 10):
    print(i)
    if i == 5:
        break

# continue 當符合某種條件時，略過執行條件
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i)

# 計算 1 至 10 間奇數總和
sum = 0
for i in range(1, 10):
    if i % 2 == 0:
        continue
    sum += i
    print("sum now: ", sum)
print("total is ", sum)


# 配合 input 取得 連續數字的總合, 按 Q, q 輸出答案
total = 0
while True:
    number = input("enter a number: ")
    if number in ["Q", 'q']:
        break
    total += int(number)
print("total: {}".format(total))



