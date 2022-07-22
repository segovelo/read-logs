# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 22:38:07 2022

@author: Sebastian
"""
from argparse import ArgumentParser
import re

def check_file(file_name):
    file_name = file_name.translate({ord(i): None for i in '!#@{}[]<>=+£$%^&*()?|,;:/\\\'\"'})
    index = file_name.find(".")
    if index > 0:
        file_name = file_name[0:index]
    elif index == 0:
        file_name = file_name[1:]
    file_name += ".log"    
    return file_name
    
        
def read(logs_file, correlation_id):
    logs_file = check_file(logs_file)
    # opening the file in read mode
    my_file = open(logs_file, "r")
    # reading the file
    data = my_file.read()
    # replacing end splitting the text
    # when newline ('\n') is seen.
    list1 = data.split("\n")
    for s in list1:
        print(s)
    my_file.close()
    
    i=0
    j=0
    list2=[]
    flag1=False
    flag2=True
    while i < len(list1) and flag2:
        found_id = re.search(correlation_id, list1[i], re.IGNORECASE)
        if found_id or (flag1 and j<5):
        #if (index > -1) or (flag1 and j<5):
            list2.append(list1[i])
            flag1=True
            if not found_id:
            #if index==-1:
                j=j+1
            else:
                j=0
        elif flag1:
            flag2=False
        i=i+1    
    list3=list2[:len(list2)-j]
    print("\n\n")
    print("\n".join(list3))
    return ("\n".join(list3))   

def save(data, save_file):
    save_file = check_file(save_file)
    with open(save_file, 'w') as f:
        f.write(data)
        f.close()

if __name__ == '__main__':
   parser = ArgumentParser(description='A command line tool for extract info from logs')
   parser.add_argument('-s', '--save', action='store', help='read correlation-id from logs')
   parser.add_argument('-l', '--logs', action='store', help='logs file passed as args')
   parser.add_argument('-c', '--corr', action='store', help='correlation-id passed as args')

   args = parser.parse_args()

   if args.corr:
       print("\n correlation-id passed as argument: % s\n\n" % args.corr)
   if args.logs:
       print("\n logs file passed as argument: % s" % args.logs)
       save(read(args.logs, args.corr), args.save)
   else:
       print('Use the -h or --help flags for help')
   
