# 模組使用
# import module name
# from module import function

# 取得當前目錄路徑
import os
print(os.getcwd())

from os import getcwd
print(getcwd())

# 幾個常用模塊
# math 數學，PI, sin, cos, tan, floor, ceil, sqrt

import math
print(math.pi)
print(math.sin(60))
print(math.cos(60))
print(math.tan(60))
print(math.floor(5/2))
print(math.ceil(5/2))
print(math.sqrt(9))

# datetime,time 時間模組
from datetime import datetime
import time
print(datetime.now())
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print(datetime.now().year)
print(datetime.now().month)
print(datetime.now().day)
print(datetime.now().hour)
print(datetime.now().minute)
print(datetime.now().second)

while True:
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    time.sleep(1)
