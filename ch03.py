# condition 判定式
# if else (單條件判斷式)
a = 50
if a > 60:
    print("及格")
else:
    print("不及格")

# if elif else （多條件判斷式)
a = 88
if a > 80:
    print("考的不錯")
elif a > 60 and a <= 80:
    print("有考及格")
else:
    print("考不及格")

# 簡易寫法
a = 70
print("及格" if a > 60 else "不及格")

z = 2
print(z ** 2 if z > 0 else "z <= 0")
z = -3
print(z ** 2 if z > 0 else "z <= 0")

# 多層次判斷式
a = 88
if a > 60:
    if a > 90:
        print("考的很棒")
    elif a > 70 and a <= 90:
        print("考的不錯")
    else:
        print("有考及格")
else:
    print("不及格")

#match case
lang = "Java"
if lang == "JavaScript":
    print("Java")
elif lang == "PHP":
    print("Php")
elif lang == "Python":
    print("Python")
elif lang == "Rust":
    print("Rust")
else:
    print("others")

match lang:
    case "Java":
        print("Java")
    case "PHP":
        print("Php")
    case "Python":
        print("Python")
    case "Rust":
        print("Rust")



