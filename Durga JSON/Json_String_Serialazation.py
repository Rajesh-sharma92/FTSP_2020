# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 22:40:56 2020

@author: Rajesh
"""
##### JSON MODULE #########

----> JAVA SCRIPT OBJECT NOTATION.
--> There are 4 functions in json module.
1) python dict object ==> JSON. ( Serialaztion and it contains 2 methods like dumps() , dump() )

2) JSON ==> python dict object. ( Deserialaztion and it contains 2 methods like loads() , load() )

""" 
NOTE :- python dict object ==> Json String. Then we will be going for method called is dumps().
and Reverse method is called as loads().

NOTE :- python dict object ==> Json file. Then we will be going for method called is dump().
and Reverse method is called as load(). 
  
"""




# Demo Program for serialazation.

import json 

employee = { 'name' : 'Rajesh',
            'age' : 35,
            'salary' : 1000.0,
            'isMarried' : True,
            'isHavingGF' : None
            }

# serialize pyhton dict obj to json json string.

json_string = json.dumps(employee)

print(json_string)

    ############### Result ##################

{"name": "Rajesh", "age": 35, "salary": 1000.0, "isMarried": true, "isHavingGF": null}

# NOTE :- True --> true , None --> null.


# serialize pyhton dict obj to json json string with proper format.

json_string = json.dumps(employee , indent = 4)

print(json_string)

    ############### Result ##################

{
    "name": "Rajesh",
    "age": 35,
    "salary": 1000.0,
    "isMarried": true,
    "isHavingGF": null
}

# serialize pyhton dict obj to json json string with proper format and sorted by alphabetical order.

json_string = json.dumps(employee , indent = 4 , sort_keys = True)

print(json_string)

    ############### Result ##################

{
    "age": 35,
    "isHavingGF": null,
    "isMarried": true,
    "name": "Rajesh",
    "salary": 1000.0
}

### Python dict object to json file. #####

with open ('emp.json' , 'w') as f:
    json.dump(employee , f , indent = 4 , sort_keys=True)
    print('open emp.json to see json data')
    










