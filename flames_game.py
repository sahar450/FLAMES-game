player1=input("enter name 1:")
player2=input("enter name 2:")
list1=list(player1)
list2=list(player2)
list3=[]
count =0
u = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
print("list1 :",list1)
print("list2 :",list2)

for i in list1:
    if i not in list2:
        list3.append(i)
        
        
        
for j in list2:
    if j not in list1:
        list3.append(j)
            
            
for item in list3:
    count +=1           


if count >= len(u):
    u=[u[-1]]

else:
    u=u[count:]    
               






print("list3 :",list3)           
print("count :",count)
print("u :", u)