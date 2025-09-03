# class Jani(): # class definition
#     def Output(self):
#         print("this is class")
# # objrct name= class name() object creation
# vivo=Jani() 
# vivo.Output()  # method access object name.method 

# class Shiva():
#     a=10
#     def show(self):
#      print("this is class")
# kiran=Shiva()
# print(kiran.a)
# kiran.show()

# class Shalini(): #class definition
#     a=10
#     def ClassMethod(self):
#         print("this is class")
# Jani1=Shalini()  
# Jani=Shalini() #object declaration
# Jani.ClassMethod()
# print(Jani.a)


# class Naveen(): #class definition
#     a=10
#     def display(self):
#         print(self.a)
# # object name=method name declaration        
# ram=Naveen()
# syam=Naveen()
# #object name.method name() 
# ram.display() 
# syam.display()


# #we can access other function variables use in another function same program 
# class Chameli():
#     def __init__(self,a,b,c):
#         self.ee=a
#         self.rr=b
#         self.zfs=c
#     def Output(self):
#         print(self.ee,self.rr,self.zfs)
# Jani=Chameli(1,2,3)
# Jani.Output()


# class Mobile():
#     def __init__(jani,mobile_name,mobile_ram,mobile_battery,mobile_price):
#         jani.a=mobile_name
#         jani.b=mobile_ram
#         jani.c=mobile_battery
#         jani.d=mobile_price

#     def Mobile_Data(jani):
#         print("Mobile_Name:",jani.a)
#         print("Mobile_Ram:",jani.b)
#         print("Mobile_Battery:",jani.c)    
#         print("Mobile_Price:",jani.d)
        
        
# while True:
#  nam=input("Enter your name:")
#  ram=input("Enter ram size:")
#  bat=input("Enter battery size:")
#  pri=input("Enter the price:")


# hare=Mobile(nam,ram,bat,pri)   
# hare.Mobile_Data()

# #or


# class Mobile():
#     def __init__(jani,mobile_name,mobile_ram,mobile_battery,mobile_price):
#         jani.a=mobile_name
#         jani.b=mobile_ram
#         jani.c=mobile_battery
#         jani.d=mobile_price

#     def Mobile_Data(jani):
#         print("Mobile_Name:",jani.a)
#         print("Mobile_Ram:",jani.b)
#         print("Mobile_Battery:",jani.c)    
#         print("Mobile_Price:",jani.d)
        
        
# nam=input("Enter your name:")
# ram=input("Enter ram size:")
# bat=input("Enter battery size:")
# pri=input(float("Enter the price:"))


# hare=Mobile("nam","ram","bat","pri")   
# hare.Mobile_Data()

#Single Inheritence

# class Parent():
#     def output(self):
#         print("this is Parent class")
# class Child(Parent):    
#     def outputChild(self):   #output
#         print("this is Child class")
# i=Child()    
# i.output()
# i.outputChild()

#Mutiple Inheritence

# class Father():
#     def outputF(self):
#         print("this is Parent1 class")
# class Mother():
#     def outputM(self):
#         print("this is Parent2 class")        
# class Child(Father,Mother):
#     def outputChild(self):
#         print("this is Child class")  
# i=Child()
# i.outputF()
# i.outputM()            
# i.outputChild()

#Mutilevel Inheritence

# class GrandFather():
#     def output(self):
#         print("this is gf class")
# class Father(GrandFather):
#     def outputf(self):
#         print("this is father class")
# class Child(Father):
#     def outputChild(self):
#         print("this is child class")        
# i=Child()
# i.output()
# i.outputf()
# i.outputChild()   

# Hairarchical Inhritence     

# class Father:
#     def output(self):
#         print("this is father class")
# class Child1(Father):
#     def outputf(self):
#         print("this is child1 class")
# class Child2(Father):
#     def outputChild(self):
#         print("this is child2 class")                
# ice=Child2()
# cream=Child1()
# ice.output()
# ice.outputChild()
# cream.output()
# cream.outputf()

# a=10
# def fun():
#     b=20
#     print('this is fun',b,a)
# fun()


# #absraction base class work

# from abc import ABC, abstractmethod
# class Car(ABC):
#     @abstractmethod #decorator
#     def mileage(self):
#         pass
# class Tesla(Car):
#     def mileage(self):
#         print("this is mileage 30kmph")
# class Suzuki(Car):
#     def mileage(self):
#         print("this is mileage 20kmph")    
# class Duster(Car):
#     def mileage(self):
#         print("this is mileage 50kmph")
# class Renault(Car):
#     def mileage(self):
#         print("this is mileage 80kmph")                    

# #Driver code
# t=Tesla() 
# t.mileage()
# s=Suzuki()
# s.mileage()
# r=Renault()
# r.mileage()
# d=Duster()
# d.mileage()   




    



              






