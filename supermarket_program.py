from datetime import datetime
name=input("Enter your name:")
#list of items
lists=''' 
apple   Rs 100/kg
mango   Rs 120/kg
sugar   Rs 30/kg       
salt    Rs 20/kg
maggie  Rs 15/kg
boost   Rs 10/each
colgate Rs 20/each
'''
#declaration of items
price=0
pricelist=[]
finalprice=0
totalprice=0
ilist=[]
qlist=[]
plist=[]

#rates for items
items={'apple':100,'mango':120,'sugar':30,'salt':20,'maggie':15,'boost':10,'colgate':20}
option=int(input("for list of items press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit:"))
    if inp1==2:
      break
    if inp1==1:
       item=input("Enter your item:")
       quantity=int(input("Enter quantity:"))
       if item in items.keys():
          price=quantity*(items[item])
          pricelist.append((item,quantity,items,price))
          totalprice+=price
          plist.append(price)   
          qlist.append(quantity)
          ilist.append(item)
          gst=(totalprice*5)/100
          finalamount=gst+totalprice
       else:
          print("sorry you entered item is not available")
    else:
      print("you entered wrong number")
    inp=input("Can I Generate the bill yes or no:")
    if inp=="yes":
       pass
    if finalamount!=0:
       print(25*"=","Jani Super Market",25*"=")
       print(28*" ","Hyderabad")
       print("Name:",name,30*" ","Date:",datetime.now())
       print(75*"-")
       print("sno",8*" ","items",8*" ","Quantity",3*" ","price")
       for i in range(len(pricelist)): 
        print(i,8*" ",8*" ",ilist[i],3*" ",qlist[i],plist[i])
       print(75*"-")
       print(50*" ","Totalamount:","Rs",totalprice) 
       print("gst amount",50*" ","Rs",gst)
       print(75*"-")
       print(50*" ","finalamount","Rs",finalamount)
       print(75*"-")
       print(20*" ","Thank for visiting")
       print(75*"-")


       
           