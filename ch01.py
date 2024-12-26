# print 列印，它是內建函式
print("Hello World")
print("hello world\tHello World")
print("hello", "World", sep=" --- ")
print("hello", "World", end="!!!\n\n")
print("hello world")

# 變數的定義，可變數值的
# 命名規則： 由大小寫字母，數字，底數所組成，第一個字母不能是數字，且不能包含空白字和保留字
# 變數的設定，將 ＝ 右方的數值指定給左方名稱
# variable name  = value
# 變數具由下列幾種型式，整數，浮點數，字元，字串，布林值及複數
# type -> 確認變數型態

# 整數：int，為不含小數點的數值
a = 1
b = 100
c = -50
print(a, type(a))
print(b, type(b))
print(c, type(c))
print("\n")

# 浮點數：float，為包含小數點的數值
a = 2.5
b = 100.00001
print(a, type(a))
print(b, type(b))
print("\n")

#str 為字串型態，字串值必須以" "或單引號' '括起來
a = 'c'
b = "hello world"
print(a, type(a))
print(b, type(b))
print("\n")

#布林：bool ，僅兩個值True(數值為1)及False (數值為0)
a = True
b = False
print(a, type(a))
print(b, type(b))
print("\n")

# 複數：complex，為數學的複數，用小寫的 j 或大寫的 J 表示
a = 1 + 2j
print(a, type(a))
print("\n")

# IO 操作
# 使用 Input 取得使用者輸入資料
name = input("enter your name: ")
print("Hello, {}".format(name))
