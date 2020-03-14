# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 00:14:38 2020

@author: Rajesh
"""
Python Logging Module :- 
---------------------
Advantage of logging :- 
--------------------
1) To perform debugging and to prepare RCA.
2) To provide statistics like no. of requests per day.
-------------------------------------------------------------------------------------------------------------
While Performing logging :- It is rekated to Logging module.
------------------------
logging Levels :- 
--------------
There are total 6 levels of Python logging levels.

1. CRITICAL ---> 50
2. ERROR ---> 40
3. WARNING ---> 30
4. INFO ---> 20
5. DEBUG ---> 10
6. NOTSET ---> 0

NOTE :- Pls see this below statement.
NOTSET < DEBUG < INFO  < WARNING < ERROR < CRITICAL.

NOTE :- Default level ---> WARNING and Higher levels msg are coming.

NOTE :- If we want we can set the level like ---> ERROR and Higher levels msg are coming.
----------------------------------------------------------------------------------------------------------------------

How to implement logging :- 
------------------------
log file.
level messages.

basicConfig() function of logininng 

logging.basicConfig(filename='log.txt',level=logging.WARNING)

logging.debug(msg)
logging.info(msg)
logging.warning(msg)
logging.error(msg)
logging.critical(msg)
--------------------------------------------------------------------------------------------------------------

WAP in Python to log a file and warnings & Higher levels msgs.
-------------------------------------------------------------
import logging
logging.basicConfig(filename='log.txt',level=logging.WARNING)
# logging.basicConfig(filename='log.txt',level=30) # We can pass the number also.
print('logging module demo') 
logging.debug('debug information')
logging.info('Info information')
logging.warning('warning information')
logging.error('error information')
logging.critical('critical information')

************ Result *********
WARNING:root:warning information
ERROR:root:error information
CRITICAL:root:critical information
----------------------------------------------------------------------------------------
WAP in Python to log a file and Complete Information.
----------------------------------------------------------------
import logging
logging.basicConfig(filename='log.txt',level=logging.DEBUG)
print('logging module demo') 
logging.debug('debug information')
logging.info('Info information')
logging.warning('warning information')
logging.error('error information')
logging.critical('critical information')

************ Result *********
WARNING:root:warning information
ERROR:root:error information
CRITICAL:root:critical information
DEBUG:root:debug information
INFO:root:info information
WARNING:root:warning information
ERROR:root:error information
CRITICAL:root:critical information
--------------------------------------------------------------------------------------------
NOTE :- If we are not giving the level then what it prints.

import logging
logging.basicConfig(filename='log.txt',level=logging.DEBUG)
print('logging module demo') 
logging.debug('debug information')
logging.info('Info information')
logging.warning('warning information')
logging.error('error information')
logging.critical('critical information')

********** Result ***************
WARNING:root:warning information
ERROR:root:error information
CRITICAL:root:critical information

NOTE :- In above example we can see that If we are not given levels then Warning and
its higher levels will be included.
-----------------------------------------------------------------------------------------------------------
NOTE :- If we want to set the only new data and replace the old data.
NOTE :- We will use one thing is that filemode='w'
NOTE :- Here in the logging data default filemode is Append mode.

import logging
logging.basicConfig(filename='log.txt',level=logging.DEBUG,filemode='w')
print('logging module demo') 
logging.debug('debug information')
logging.info('Info information')
logging.warning('warning information')
logging.error('error information')
logging.critical('critical information')

********** Result ***************
DEBUG:root:debug information
INFO:root:info information
WARNING:root:warning information
ERROR:root:error information
CRITICAL:root:critical information
--------------------------------------------------------------------------------------
NOTE :- If we are going to set the level is Error then what its prints.

import logging
logging.basicConfig(filename='log.txt',level=logging.ERROR,filemode='w')
print('logging module demo') 
logging.debug('debug information')
logging.info('Info information')
logging.warning('warning information')
logging.error('error information')
logging.critical('critical information')

********** Result ***************
ERROR:root:error information
CRITICAL:root:critical information
----------------------------------------------------------------------------------------------------
NOTE :- If we are not specifying any filename & levels & filemode.
NOTE :- Default filemode is append means 'a'.
NOTE :- Default level is WARNING and its prints higher levels msgs.
NOTE :- Default filename means it will not create any default file but 
it show the default levels information on console.

import logging
logging.basicConfig()
print('logging module demo') 
logging.debug('debug information')
logging.info('Info information')
logging.warning('warning information')
logging.error('error information')
logging.critical('critical information')

********** Result ***************
WARNING:root:warning information
ERROR:root:error information
CRITICAL:root:critical information
logging module demo

-----------------------------------------------------------------------------------------------------

How to format log Messages :- 
--------------------------
import logging
logging.basicConfig(format='%(levelname)s')
print('logging module demo') 
logging.debug('debug information')
logging.info('Info information')
logging.warning('warning information')
logging.error('error information')
logging.critical('critical information')

********** Result ***************
WARNING
ERROR
CRITICAL
logging module demo
-----------------------------------------------------------------------------------------
How to format log Messages and All msgs :-
---------------------------------------
import logging
logging.basicConfig(format='%(levelname)s:%(message)s')
print('logging module demo') 
logging.debug('debug information')
logging.info('Info information')
logging.warning('warning information')
logging.error('error information')
logging.critical('critical information')

********** Result ***************
WARNING:warning information
ERROR:error information
CRITICAL:critical information
logging module demo
--------------------------------------------------------------------------------------------------------

How to add timestamp in log messsages :- 
-------------------------------------
import logging
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s')
print('logging module demo') 
logging.debug('debug information')
logging.info('Info information')
logging.warning('warning information')
logging.error('error information')
logging.critical('critical information')

********** Result ***************
2020-03-14 14:26:54,958:WARNING:warning information
2020-03-14 14:26:54,983:ERROR:error information
2020-03-14 14:26:54,985:CRITICAL:critical information
logging module demo
-----------------------------------------------------------------------------------------
How to add timestamp in log messsages as our desired date & timeformat :-
----------------------------------------------------------------------
import logging
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',datefmt='%d/%m/%Y %I:%M:%S %p')
print('logging module demo') 
logging.debug('debug information')
logging.info('Info information')
logging.warning('warning information')
logging.error('error information')
logging.critical('critical information')

********** Result ***************
14/03/2020 02:52:36 PM:WARNING:warning information
14/03/2020 02:52:36 PM:ERROR:error information
14/03/2020 02:52:36 PM:CRITICAL:critical information
logging module demo
------------------------------------------------------------------------------------------------------------------
import logging
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',datefmt='%d/%m/%Y %H:%M:%S')
print('logging module demo') 
logging.debug('debug information')
logging.info('Info information')
logging.warning('warning information')
logging.error('error information')
logging.critical('critical information')

********** Result ***************




































