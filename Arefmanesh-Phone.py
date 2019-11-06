#!/usr/bin/env python
# coding: utf-8

# In[18]:


########## Initializing##########

from time import sleep,time,datetime

from random import random

from random import random, randint, choice

import os

import winsound

from msvcrt import getch

import re


dic = {}

try:
    open("./phoneBook.txt", 'w').close()
except OSError as e:  ## if failed, report it back to the user ##
    print ("Error: %s - %s." % (e.filename, e.strerror))
    

try:
    open("./log.txt", 'w').close()
except OSError as e:  ## if failed, report it back to the user ##
    print ("Error: %s - %s." % (e.filename, e.strerror))


# In[ ]:


from msvcrt import getch
########## Add New contact to phonebook##########

def add_to_file(v):

    f = open("./phoneBook.txt" ,'a',encoding='UTF-8') 
    f.write(v + ': ' + dic[v] + '\n')
    f.close()
    
    print('New Contact added to phonebook')



########## Writing log to File ##########

def log_to_file (per,bt,dur):
    
    f = open("./log.txt" ,'a',encoding='UTF-8') 
        
    f.write("go out call to %s is started on %s and took %d Second(s) \n" %(per,bt,int(dur)) )
    f.close()
    
    return
    
    

########## Calculate duration of call ##########
    
def timer(func):
    def wrapper(*a,**kw):
        t0 = time()
        
        z = func(*a,**kw)
        
        if show:
            
            du=int(time()-t0)
            print('The call took',int(time()-t0),'seconds.')
            
        
        return du
    return wrapper

show=True




@timer
def call_num(cn):
       
    print ("Call is started")
    
    for i in range (randint(1,10)):## Generation random time for call, after this time call will be ended
        sleep(1)
        print ('{}\r'.format(i+1), end='') ## Display seconds of call

    
    print ("Call Ended")

            
    return dic.get(str(cn)) 



#################Main Program###########

while True:
    key = ord(getch())
    if key == 27: #ESC
        print('Hee')
        break
    elif key == 13: #Enter 
        
        print('Ahaan')

        a=0 ## Duration of call

        n = input ("Please Enter CAll Number:")
   
        m = re.match('\d',n) ## phone number must be digit


        if m:
    
            ### searching in phonebook if there is not in it, create new contact
            if n in dic.keys():
                print ("You are calling to %s" %dic.get(n))
            else:
                nam=input ("Please Enter Name:")
                dic[n] = nam
        
                add_to_file(n)## create new contact
        
    
    
            ### start call
            print ("is dialing...!")
    
    
            ### probability for type of call: Busy or Dialing
            busy = choice([True, False])
            if busy: 
                for i in range(5):
                    winsound.Beep(400, 500)## making busy sound
                    sleep(0.5)
                print('The number you have dialled is Busy')
        
        
            else:
                for i in range(2):
                    winsound.Beep(400, 1000)## making normal sound
                    sleep(2)
    
    

                a=call_num(n)## calculation duration of call
        
    
            ### record start time of call
            now = datetime.datetime.now()
            ty=now.strftime("%Y-%m-%d %H:%M:%S")
    
    
            ###Recording log in the file
            log_to_file (dic[n],ty,a)
        
    
                
        else:
            print('Phone Number must be digit.')
    
    
    


# In[ ]:





# In[ ]:





# In[ ]:




