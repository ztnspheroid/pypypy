# 4---------------------------------------
# n=int(input())

# def rrr():
#     l=[i for i in str(n)]
#     if l[-1]=='0':
#         del l[-1]
#         l.reverse()
#     else:
#         l.reverse()
#     return l

# if n!=0:
#     print(*rrr(),sep='')
# else:
#     print('Программа завершена!')
#  5----------------------------------------------
# s=input('Введите текст: ')
# n=int(input('Какую цифру ищем?'))
# b=input('Какую букву ищем?')
# l=[i for i in s]
# def func():
#     for i in l:
#         if i==str(n):
#             x=l.count(str(n))
#             return x
# def func1():
#     for i in l:   
#         if i==b:
#             y=l.count(b)
#             return y
# print(f'Количество цифр {n} : {func()}')
# print(f'Количество bukv {b} : {func1()}')
#  6--------------------------------------------
# x=float(input())
# y=float(input())

# def f():
#     if -1<=x<=1 and -1<=y<=1:
#         a='Монетка где-то рядом'
#     else:
#         a='Монетка где-то рядом net'
#     return a
# print(f())
#  7-----------------------------
# l=[]
# l.extend(input())
# print(min(l))
#   8------------------------------------------
# a=int(input())
# b=int(input())
# y=[]
# def an():
#     l=[i for i in range(1,a) if a%i==0]
#     return l

# def bn():
#     m=[i for i in range(1,b) if b%i==0]
#     return m

# for i in an():
#     for j in bn():
#         if i==j:
#             y.append(i)

# print(max(y))
#   9-------------------------
# s=input('enter k,b,n:')
import random
# y=random.choice(['k','n','b'])
# def knb():
    
#     if s=='k' and y=='n':
#         return 'v'
#     if s=='n' and y=='k':
#         return 'p'
#     if s=='n' and y=='b':
#         return 'v'
#     if s=='b' and y=='n':
#         return 'p'
#     if s=='b' and y=='k':
#         return 'v'
#     if s=='k' and y=='b':
#         return 'p'
#     else:
#         return 'nichya'
# print(f'{s} protiv {y}')
# print('rezultat :',knb())


# n=int(input())
# x=random.randint(1,10)
# while n!=x:
#     n=int(input())
#     print(x)              ???????????????????????
    
        
