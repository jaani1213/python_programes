# x=lambda a,b,c: a+b+c
# print(x(1,2,3))

# l1=[11,13,73,51] #list
# l2=[] #empty list
# for i in l1: #l1=[11,13,73,51]   
#     t=lambda a:a+1
#     l2.append(t(i))    
# print(l2)  

# age=[11,13,17,35,42,27]
# def myFunc(x):
#     if x < 17:
#         return False
#     else:
#         return True
# adults=filter(myFunc,age)
# print(list(adults))


# def caluculateAddition(n):
#     return n+n 
# number=(1,2,3,4)
# result=map(caluculateAddition,number)
# print(list(result))     


# from functools import reduce #reduce(function,sequence)
# d=reduce(lambda a,b:a+b,[23,45,42,56,12])
# print(d)

# # Generator-function
# def simpleGeneratorFun():
#     yield 1
#     yield 2
#     yield 3
# # x is a generator object      
# x = simpleGeneratorFun()
# # iterating over the generator object using next  
# print(x._next_())  # in python 3, _next_()
# print(x._next_())
# print(x._next_())    


# def even(x):
#     if x%2==0:
#         print(x)
# # difference bitween filter and map
# nums=[11,17,22,28,33,36]
# map=list(map(lambda x:x**2,nums))
# print(list(map))

# # filter=list(filter(lambda x:x%2==0, nums))
# # print(filter)
