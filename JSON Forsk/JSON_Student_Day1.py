# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 13:44:31 2020

@author: Rajesh
"""

import json

json_string = """

{
	"student": {
		"name": {
			"First_Name": "Rajesh",
			"Middle_Name": "Kumar",
			"Last_Name": "sharma"
		},
		"Photo": "www.gmail.com",
		"Gender": "Male",
		"Mobile": [8217083006, 9036126027],
		"Course": "Computer Science in B.Tech",
		"Branch_dept": "Computer Science",
		"Course_ID": 1234,
		"College_Name": "JECRC-Jaipur",
		"Board_Exam_Center": "RTU-Kota",
		"Subjects": ["Software", "Python", "Java"]
	}
}

"""

print(type(json_string)) # String Type.

# Converts Python Data types to JSON Data Types.
my_data = json.loads(json_string)

print(type(my_data)) # Dict Type.

print(my_data)

print(my_data['student'])

print(my_data['student']['name'])

print(my_data['student']['Subjects'])

print(my_data['student']['Subjects'][0])

print(my_data['student']['Subjects'][-1])


# Converts Python Data types to JSON Data Types.

new_json_string = json.dumps(my_data)

print(type(new_json_string)) # String Type.

print(new_json_string)

new_json_string = json.dumps(my_data , indent = 5)

print (new_json_string) 

new_json_string = json.dumps(my_data , indent = 2 , sort_keys = True)

print (new_json_string)










