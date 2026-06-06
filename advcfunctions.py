#exercise1:-
list_1=[1,2,3,4,5,6,7,8,9]
def squares_all(numbers):
    return numbers**2
result=map(squares_all,list_1)
print(list(result))

list_2=[10,20,30,40,50]
result_1=map(lambda numbers:numbers**2,list_2)
print(list(result_1))

#exercise2:-
list_3=[1,2,3,4,5,6,7]
def filter_positive(numbers):
    return numbers%2==0
result_3=filter(filter_positive,list_3)
print(list(result_3))

#exercise:-1

from functools import reduce
n=5
result=reduce(lambda x,y:x*y,range(1,n+1),1)
print(result)

from functools import reduce
def calculate_factorial(n):
    if n<0:
        return "factorial undifine for negative numbers"
    elif n==0 or n==1:
        return 1
    else:
        return reduce(lambda x,y:x*y,range(1,n+1,1))
print(calculate_factorial(5)) 

#exercise4:-

from functools import reduce
def count_vowel(string):
    vowel="aeiouAEIOU"
    return reduce(lambda count,char:count+1 if char in vowel else count,string,0)
print(count_vowel("pythonlife"))