# (1)
# Написать функцию, которая на вход принимает int и возвращает true или false 
# в зависимости является ли это число палиндром. 
# Число является палиндромом, если оно читается справа налево и слева направо одинаково 
def polindrom(a:int):
    b = a
    d = 0
    while(b!=0):
        number = b%10
        d = d*10 + number
        b = int(b/10)
    print("Result is: ", d)
    if(d==a):
     return True
    else:
     return False

# (2) 
# Написать функцию, которая принимает на вход список из положительных целочисленных элементов 
# и возвращает три списка: 
#     1. в первом - числа, которые делятся на 2
#     2. во втором - числа, которые делятся на 3
#     3. с третьем - числа, которые делятся на 5
def spiski(l:list):
    l2 = []
    l3 = []
    l5 = []
    for i in l:
        if int(i)%2 == 0:
            l2.append(i)
        if int(i)%3 == 0:
            l3.append(i)
        if int(i)%5 == 0:
            l5.append(i)
    print("list :2 >>> ", l2)
    print ("list :3 >>> ", l3)
    print ("list :5 >>> ", l5)

# (3)
# Написать функцию, принимающую на вход int, и выводит число, обратное этому int 
def opposite():
    print("#3: Input number (returns opposite) >> Input: x=")
    x = int(input())
    b = abs(x)
    d = 0
    while(b!=0):
        number = b%10
        d = d*10 + number
        b=int(b/10)
    if x>=0: print("Output: ", d)
    else:
        d = -d 
        print("Output: ", d)

# (4)
# Написать функцию, которая будет расчитывать квадратный корень n-ой степени методом Ньютона
def Nsqrt(n:int, x:int):
    approx = x/n
    close = (approx*(n-1) + x/approx**(n-1))/n
    while close != approx:
        approx = close
        close = (approx*(n-1) + x/approx**(n-1))/n
    return approx

# (5)
# Написать функцию, принимающую 1 аргумент — число от 0 до 100000, 
# и возвращающую true, если оно простое, false если нет.
def SimpleNumb(x:int):
    n = x
    f = 1
    counter = 2
    if n == 1:
        f = 2
        return True
  
    while f<2:
        if n%counter == 0:
                f=f+1
        counter = counter + 1
    if counter-1==n: return True
    else: return False

a:int
n:int
l:list

#(1)
print("#1: Input number (polindrom/not) >> ")
a = int(input())
print(polindrom(a))

#(2)
print("#2: Input list (>0) >> ")
l = input().split()
spiski(l)

#(3)
opposite()

#(4)
print("#4: Input root degree >> ")
n = int(input())
print("#4: Input number under root >> ")
a = int(input())
print(Nsqrt(n,a))

#(5)
print("#5: Input number (0 to 100000). Is it simple? >> ")
a = int(input())
print(SimpleNumb(a))
