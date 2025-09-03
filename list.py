# # # jani[] #empty list
# # jani=list()
# # print(type(jani))

# jani=[1,1.5,786,"python",True]
# jan1=list([1,2.2,"Python".True])
# print(jani)
# print(jani1)

# jani=[5,6.9,"pyhton",True,-1.6]
# print(jani[3])
# print(jani[1:4])

# jani_john=[2,66,845,"python",True,88,3.7,-5.8,5,35,87]
# # slicing 
# positive
# (start:stop:skip)
# print(jani_john[0:9:2])
# negavive
# print(jani_john[5:0:-2]) 
# all negative
# print(jani_john[-1:-8:-2])
# print(jani_john[:])
# print(jani_john[::])
# print(jani_john[1:])
# print(jani_john[1::])
# print(jani_john[-1:])
# print(jani_john[::-1])
# print(jani_john[:-1])

# Methods
# jani=[1,2,87,464,786,464,43,3,25,76,56,65]
# jani.append([12])
# print(jani)
# jani.extend([12])
# print(jani)

# jani=[1,2,87,464,786,464,43,786,3,25,76,56,65]
# print(jani.count(786))
# print(len(jani))
# print(jani.index(1))
# jani.clear()
# print(jani)


# jani=[1,2,87,464,786,464,43,786,3,25,76,56,65]
# j=jani
# print(j==jani)
# print(id(j))
# print(id(jani))
# b=jani.copy()
# jani.append('abc')
# print(b)


# jani=[1,2,87,786,464,4786,785,655,942,3,25,76,765,65,6325]
# jani.insert(5,"Bhai")
# print(jani)

# jani=[1,2,87,786,464,4786,785,655,942,3,25,76,765,65,6325]
# jani.pop(8)
# jani.remove(87)
# jani.reverse()  #ascending order
# print(jani)

# a=[1,2,87,786,464,4786,785,655,942,3,25,76,765,65,6325]
# a.sort(reverse=True) #descending order
# print(a)


# List Comprehension

# s=[1,2,4,3,24,64]
# print(range(4))

# s=[1,2,3,4,5,3,6,2,9]
# for i in range(len(s)):
#     if s[i]==2:
#         print(i)


#str1=[1,2,3,4,5,3,2,5,7,8,9,0,3]
# n=[]
# for k in str1:
#     if k!=3:                          
#         n.append(k)
# print(n)

# newlist = []
# for x in ["apple","banana","mango","cherry"]:
#     if "a" in x:
#         newlist.append(x)
#     print (newlist) 
   
                #    or

# fruit=["apple","banana","mango","cherry"]   
# newlist=[x for x in fruit if "a" in x]            
# print(newlist)


    
# list = ["EVEN" if i%2==0 else "odd" for i in range(10)]
# print(list)








     



