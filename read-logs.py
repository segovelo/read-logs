# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 22:38:07 2022

@author: Sebastian
"""
correlation_id="1234"
# opening the file in read mode
my_file = open("logs1.txt", "r")
# reading the file
data = my_file.read()
# replacing end splitting the text
# when newline ('\n') is seen.
list1 = data.split("\n")
print(list1)
my_file.close()

i=0
j=0
correlation_id2=correlation_id
list2=[]
flag1=False
flag2=True
while i < len(list1) and flag2:
    index= list1[i].find(correlation_id.casefold())
    if (index > -1) or (flag1 and j<5):
        list2.append(list1[i])
        flag1=True        
        if index==-1:
            j=j+1
        else:
            j=0
    elif flag1:
        flag2=False
    i=i+1    
list3=list2[:len(list2)-j]
print("\n\n")
print("\n".join(list3))     
    
