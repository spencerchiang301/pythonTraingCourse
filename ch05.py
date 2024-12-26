# function 函數，把一些動覆的動作集合起來的一個程式區段
# def name:
#    code
from tkinter.font import names


def say_hello():
    print("Hello, world!")

for i in range(3):
    say_hello()

# 函數傳值
def add(a, b):
    print(a + b)

add(1, 2)
add(10, 20)

# 函數的預設值, 預設值的放後方
def say_hello(first_name, last_name = "wang"):
    print("Hello, ", first_name, last_name)

say_hello("jack")
say_hello("jack", "liu")

# args 傳一組參數
def say_hello2(*args):
    for name in args:
        print("Hello, ", name)

say_hello2("jack", "helen", "mary")

# kwargs 傳數組組合
def say_hello3(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

say_hello3(name = "jack", age = 20, phone = "123-456-7890")

#-----------------------------------------------------------------
#函數間互相呼叫
def call_say_hello():
    say_hello()
    say_hello2("jack", "helen", "mary")
    say_hello3(name = "jack", age = 20, phone = "123-456-7890")


# 函數回傳值
def say_hello5(name):
    return "Hello, " + name
print(say_hello5("jack"))

def get_total(a, b):
    total = 0
    for i in range(a, b + 1):
        total += i
    return total

print(get_total(1, 10))
print(get_total(1, 100))

# 函數內的變數生命週期, your_name 只存在say_hello6裡
def say_hello6():
    your_name = "jack"
    print("name = ", your_name)

say_hello6()
#print(your_name)
