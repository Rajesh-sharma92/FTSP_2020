# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 10:27:31 2020

@author: Rajesh
"""
Python Multithreading Daemon Threads :- 
------------------------------------
Question :- I need to send email to 20k people stored in database and also make 
sure that email does not go to multiple times, So i may achieve through multithreading.

Answer :- Yes. We can use Multithreading concept in this approach.

2x10K
l1 = 10k mail ids
l2 = 10k mail ids

def send_mail(list):
    send mail to every email in list
    
l1 
l2
t1 = Thread(target=send_mail,args=(l1,))    
t2 = Thread(target=send_mail,args=(l2,))    
t1.start()
t2.start()
--------------------------------------------------------------------------------------------------------------------------
Daemon Threads :-
--------------
The main purpose is to provide support for non-daemon threads(main thread).
Ex :- Garbage collector , GC.

NOTE :- Garbage collector always working on background and main thread always 
works on foreground(on screen).
NOTE :- Garbage collector is the daemon threads in multithreading concept.

Question :- Every python contains a thread and which is that ?
Answer :- Yes. It contains and name of that thread is MainThread.

Question :- Is it MainThread Deamon thread or not ?
Answer :- The MainThread is not Deamon Thread coz MainThread works on foreground
and Deamon Threads always working on background and like GC.

Ex :- 
from threading import *
mt = current_thread()
print(mt.isDaemon()) # False
print(mt.daemon) # False

********** Result ***********
False
False
---------------------------------------------------------------------------------------------
Question :- Is it possible to change the nature of Daemon Threads ?
Answer :- Yes. We can change the nature of Daemon Threads. Like see below Ex.
t.setDaemon(True) --- >> Daemon Thrads.
t.setDaemon(False) --->> Non - Daemon Threads.

Here we have some Restrications to setDaemon status.
i.e., Once a thread started(Active thread) we can  not change its Daemon Nature.
RuntimeError : can't set daemon status of active thread.

NOTE :- Here we can see that The MainThread is always started by PVM and we can
change its nature or not we will in the below example.

Ex :- 
from threading import *
mt = current_thread()
print(mt.isDaemon()) # False
print(mt.daemon) # False
mt.setDaemon(True)

************* Result ***********
RuntimeError: cannot set daemon status of active thread

NOTE :- In the above example we can see that we can not change the status of 
any started(Active threads) and PVM will throw an RuntimeError and happily we
can change its nature before any thread started.
-------------------------------------------------------------------------------------------
Question :- What is the default nature of every threads ?
Answer :- We know that the default nature of MainThread is always Non-Daemon Threads.

NOTE :- By default all threads are not Daemon threads nature because every threads 
having some property like Inherited from Parents.

NOTE :- If the parent thread nature is Daemon then Child thread will be Daemon Thread nature.
NOTE :- If the parent thread nature is Non-Daemon then Child thread will be Non-Daemon Thread nature.

NOTE :- Daemon nature for every threads are inherited from Parent to child threads.
--------------------------------------------------------------------------------------------------------------------
Ex :- 
from threading import *
def job():
    print('Executed by Child thread')
t = Thread(target=job)
print(t.isDaemon()) # False   
t.setDaemon(True) # Here we can change the nature of MainThread coz we Have not started MainThraed.
print(t.isDaemon()) # True

********* Result *********
False
True

NOTE :- In the above example we can see that t is object variable and it is 
created by MainThread and If we will be checking is Daemon or not then MainThread
will be Non-Daemon (False). but here we can set the nature of MainThread coz 
we have not the MainThread then we can change its nature by using the t.setDaemon(True) line
and later the MainThread nature will be change it.
---------------------------------------------------------------------------------------------------------------------------
Ex :- Here we are not changing the nature of the t1.

from threading import *
def job1():
    print('Executed by t1')
    t2 = Thread(target=job2)
    print('t2 is Daemon :', t2.isDaemon())
    t2.start()

def job2():
    print('Executed by t2')
    
t1 = Thread(target=job1) 
print('t1 is Daemon :', t1.isDaemon())
t1.start() 

********** Result ***********
t1 is Daemon : False
Executed by t1
t2 is Daemon : False
Executed by t2

NOTE :- In the above example we can see that t1 thread is created and executed by MainThread.
and The MainThread is Non-Daemon and then its child thread will be also Non-Daemon only
Like t1 is Non-Daemon only and t2 is created by t1 and it will be Non-Daemon only.
-----------------------------------------------------------------------------------------------------------------------
Ex :- Here we are changing the nature of the t1 to SetDaemon.

from threading import *
import time
def job1():
    print('Executed by t1')
    t2 = Thread(target=job2)
    print('t2 is Daemon :', t2.isDaemon())
    t2.start()

def job2():
    print('Executed by t2')
    
t1 = Thread(target=job1) 
t1.setDaemon(True)
print('t1 is Daemon :', t1.isDaemon())
t1.start()
time.sleep(10)

********** Result ***********
t1 is Daemon : True
Executed by t1
t2 is Daemon : True
Executed by t2
-------------------------------------------------------------------------------------
Question :- Can we make MainThread is Daemon or not ?
Answer :- No, We can not make MainThread is Daemon because to making any threads
is daemon, then the thread should not be in start position and MainThread always
will be in the started position by PVM.
NOTE :- MainThread always will be in Non-Daemon status.
--------------------------------------------------------------------------------------------------------
Question :- What is the Advantage of Daemon Threads over Non-Daemon Threads ? 
Answer :- Whenever last Non-Daemon thread terminates automatically all daemon 
threads will be terminated we are required to terminte explicitly.

Ex :- 
Cinama Shooting :-
---------------
Hero , Heroines ===> Non-Daemons.
Make-up persons and Camera Mans ==> Daemons.
NOTE :- If the shooting is completed and hero,heroines are not there. then what is
use to ask makeup & Camera persons to be available at Venue.

Car Games :-
---------
cars ===> Non-Daemons.
Background scanarios ===> Daemons.
---------------------------------------------------------------------------------------------------------
Ex :-

from threading import *
import time

def job():
    for i in range(10):
        print('Lazy Thread')
        time.sleep(2)
        
t = Thread(target=job)
t.start()
time.sleep(10)
print('End of Main Thread')

*********** Result **********
Lazy Thread
Lazy Thread
Lazy Thread
Lazy Thread
Lazy Thread
End of Main Thread
Lazy Thread
Lazy Thread
Lazy Thread
Lazy Thread
Lazy Thread
---------------------------------------------------------------------------------------------------------------------------
Ex :-

from threading import *
import time

def job():
    for i in range(10):
        print('Lazy Thread')
        time.sleep(2)
        
t = Thread(target=job)
t.setDaemon(True)
t.start()
time.sleep(10)
print('End of Main Thread')        

*********** Result **********

Lazy Thread
Lazy Thread
Lazy Thread
Lazy Thread
Lazy Thread
End of Main Thread

NOTE :- In the above example we can see that if the MainThread is ending then 
Child Thread also will be ended.
-----------------------------------------------------------------------------------------------------------
NOTE :- Wherever we are using supporting kind of activities then we should go for
Daemons Threads.
NOTE :- If there are Main Jobs then better go for Non-Daemons.
------------------------------------------------------------------------------------------------
Question :- If parent is Daemon, Can we make child as Non-daemons ?
Answer :- Yes, We can do it.

from threading import *
import time
def job1():
    print('Executed by t1')
    t2 = Thread(target=job2)
    t2.setDaemon(False)
    print('t2 is Daemon :', t2.isDaemon())
    t2.start()

def job2():
    print('Executed by t2')
    
t1 = Thread(target=job1) 
t1.setDaemon(True)
print('t1 is Daemon :', t1.isDaemon())
t1.start()
time.sleep(10)

************ Result *********
t1 is Daemon : True
Executed by t1
t2 is Daemon : False
Executed by t2

---------------------------------------------------------------------------------------------------------------



































































