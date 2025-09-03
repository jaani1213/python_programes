# a=10
# print(a)


# johnbasha=786
# print(johnbasha)
# print("johnbasha")

# a,b,c=1,2,3
# print(a,b,c)

# a=b=c=100
# print(c)

# good
# _jani=1
# jani147=786
# jani_147=236
# jani=123
# Name=11
# name=123
# NAME=147


# bad
# 12jani=768
# @jani=100
# jani!=121


# Cases
# johnBasha=147
# John_Basha=147
# JohnBasha=147
# print(johnBasha)
  
# address location
# a=10
# b=786
# print(id(a))
# print(id(b))

# a=10 #int
# b=100 #int
# c=1.5 #float
# h=-3.5 #float
# d=-2.7 #bool
# e=True #bool
# f=False #bool
# g=1+5j #complex
# print(type(a),type(b),type(c),type(d),type(e),type(f),type(g),type(h))



# a=100
# # int-----> float
# print(float(a))


# e=222.324
# # float----->int
# print(int(e))


# d=input("Type something:")
# print(d)

# Simple Interest

# p=100
# t=2
# r=9
# si=(p*t*r)/100
# print(si)

# p=float(input("enter principle amount:"))
# t=float(input("enter time:"))
# r=float(input("enter interest(in %):"))
# SI=(p*t*r)/100
# print("Simple Interest=",SI,"\u20B9")

# # Compound Interest
principal = int(input("Enter the principal amount: "))
rate = int(input("Enter rate of interest: "))
time = int(input("Enter time in years: " ))
Amount = principal * (pow((1 + rate / 100), time))
CI = Amount - principal
print("Compound interest is", CI)



# # (a+b)**2

# a=input("add value")
# b=input("add value")

#  (a+b)**2

# a=int(input("add a value:"))
# b=int(input("add b value:"))
# result=(a+b)**2
# print(result)

# a=int(1)
# b=int(1)
# res=(a+b)**2
# print(res)