# Module : 소스 코드의 재사용을 가능하게 하며, 소스 코드를 하나으이 이름 공간으로 구분하고 관리한다.
# 파이썬은 모듈 단위로 파일로 저장된다.
# 모듈의 멤버 : 변수, 실행문, 함수, 클래스
# main module 확인 : __name__ = '__main__'

# 내장된 모듈
print('뭔가를 하다가...')

import sys
print(sys.path)
#sys.exit()

import math
print(math.pi)
print(math.sin(math.radians(30)))

import calendar
calendar.setfirstweekday(6) # 0 ~ 6
calendar.prmonth(2022, 3)

print(dir(calendar))

import time
print(time.localtime())
#print('start...')
#time.sleep(3) #지연시간
#print('finish')

import os
print(os.getcwd()) #현재 작업경로

print()
import random
print(random.random())
print(random.randint(1, 10))

from random import randint
print(randint(1, 10))

#from random import import *  /모든 랜덤 임포트 메모리를 많이사용한다 권장하지 않는다
print('프로그램 종료')
