# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 22:38:07 2022

@author: Sebastian
"""
from argparse import ArgumentParser
import csv
import json
from pprint import pprint

def read(logs_file, correlation_id):
    # opening the file in read mode
    my_file = open(logs_file, "r")
    # reading the file
    data = my_file.read()
    # replacing end splitting the text
    # when newline ('\n') is seen.
    list1 = data.split("\n")
    print(list1)
    my_file.close()
    
    i=0
    j=0
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
 

if __name__ == '__main__':
   parser = ArgumentParser(description='A command line tool for extract info from logs')
   parser.add_argument('-r', '--read', action='store_true', help='read correlation-id from logs')
   parser.add_argument('-l', '--logs', action='store', help='logs file passed as args')
   parser.add_argument('-c', '--corr', action='store', help='correlation-id passed as args')

   args = parser.parse_args()
   correlation_id = "" 
   logs_file=""
   if args.logs:
       logs_file=args.logs
       print("\n logs file passed as argument: % s" % args.logs)
   if args.corr:
       correlation_id = args.corr
       print("\n correlation-id passed as argument: % s" % args.corr)
   if args.read:
       read(logs_file, correlation_id)
   else:
       print('Use the -h or --help flags for help')
   
