# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 11:29:55 2022

@author: acabr
"""
letters = ['a', 'b', 'c'] #This is a comment
integers = [1,2,3]

#def func1():
#    newlist = [letters[0], integers[0], letters[1], integers[1], letters[2], integers[2]]
#    print(newlist)
#func1()
newlist = [0] * 6

def func2(list1,list2):
    for i in range(0,len(list1)):
        #print(i,list1[i])
        #print(i,list2[i])
        #newlist = [list1[i], list2[i]]
        newlist_index = 2*i
        newlist[newlist_index]=letters[i]
        newlist[newlist_index+1]=integers[i]
    #print(newlist_index,newlist)#unindent to only print the final iterationn
    print(newlist)
        
func2(letters,integers)
#there's another way to do it - append function
