'''
Job - 1: Create a dynamic list of 10- numbers and compute the following
a) Sum 
b) Min  
c) Max  
'''
import random
L = []
for i in range(10):
    ele = random.randint(100, 200)
    L.append(ele)
print("The generated random list of 10 - element", L)

# Sum of elements # 1
print("The sum of elements from random list is:", sum(L))
# Sum of elements # 2
SUM = 0
for element in L:
    SUM = SUM + element
print("The sum of elements from random list - method 2:", SUM)

print("The minimum element in the generated list is:", min(L))
MIN = L[0]
for element in L:
    if MIN > element:
        MIN = element
print("The minimum element in the generated list is:", MIN)

print("The maximum element in the generated list is:", max(L))
MAX = L[0]
for element in L:
    if MAX < element:
        MAX = element
print("The maximum element in the generated list is:", MAX)