# 異常處理，錯誤處理
# try except

# print(1/0)
# print("hello world")

try:
    print(1/0)
except ZeroDivisionError:
    print('divided 0 is not allowed')

print("hello world")

# except 多層式異常處理，順序以最可能發生者排第一位
try:
    with open('/project/test.txt', 'r') as fp:
        for line in fp:
            print(line)
except FileNotFoundError:
    print('file not found')
except FileExistsError:
    print('file exists')

# except 自定義錯誤
try:
    with open('/project/test.txt', 'r') as fp:
        for line in fp:
            print(line)
except:
    print('unknown error')

# 可以使用 else 去定義沒有異常下要執行的代碼
try:
    with open('test.txt', 'r') as fp:
       pass
except:
    print('unknown error')
else:
    print('Open the file without no error')

# try final
try:
    with open('/project/test.txt', 'r') as fp:
       pass
except:
    print('unknown error')
finally:
    print('no matter what, run this')

# try raise 自定義錯誤
try:
    with open('/project/test.txt', 'r') as fp:
        for line in fp:
            print(line)
except:
    raise FileNotFoundError
