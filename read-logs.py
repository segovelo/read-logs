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
    index= 15 + list1[i].find("correlation-id".casefold())
    if index > 14:
        correlation_id2=list1[i][index:index+4]
    else:
        correlation_id2=""       
    if correlation_id.casefold()==correlation_id2.casefold() or (len(correlation_id2)==0 and flag1 and j<3):
        list2.append(list1[i])
        flag1=True
        
        if len(correlation_id2)==0:
            j=j+1
        else:
            j=0
    elif flag1:
        flag2=False
    i=i+1    
list3=list2[:len(list2)-j]
print("\n".join(list3))     
    
