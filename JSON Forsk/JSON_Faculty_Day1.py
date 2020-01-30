# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:22:05 2020

@author: Rajesh
"""

# Loading raw json data into python specific data.
import json

json_string = """

{
	"Faculty":

	{
		"Name": {
			"F_name": "Sachin",
			"M_name": "kumar",
			"L_name": "sharma"
		},
		"Photo": "www.gmail.com",
		"Gender": "Male",
		"Mobile": [8217083006, 9036126027],
		"E-mail": ["sachin123@gmail.com", "kumar90@hotmail.com"],
		"Branch_dept": "Computer Science",
		"Course_ID": 1234,
		"College_Name": "JECRC-Jaipur",
		"Board_Exam_Center": "RTU-Kota",
		"Subjects_Expert": ["Software", "Python", "Java"],
		"Research_Area": ["Artifical intellgence", "Machine Learning"],
		"Name1": {
			"F_name": "Rajesh",
			"M_name": "Ratan",
			"L_name": "sharma"
		},
		"Photo1": "www.gmail.com",
		"Gender1": "Male",
		"Mobile1": [8217083006, 9036126027],
		"E-mail1": ["sachin123@gmail.com", "kumar90@hotmail.com"],
		"Branch_dept1": "Computer Science",
		"Course_ID1": 9078,
		"College_Name1": "JECRC-Jaipur",
		"Board_Exam_Center1": "RTU-Kota",
		"Subjects_Experts": ["Software", "Python", "Java"],
		"Research_Areas": ["Computer science", "Data Science"]

	}
}

"""

print(type(json_string)) # String Type.

print(json_string)

faculty_data = json.loads(json_string)

print(faculty_data['Faculty'])

print(faculty_data['Faculty']['Name']['F_name'])

print(faculty_data['Faculty']['Name']['L_name'])

print(faculty_data['Faculty']['Course_ID'])

faculty_data["Faculty"]["Research_Areas"]

faculty_data["Faculty"]["Research_Area"]


# Writing/Storing the JSON data in a File 

with open("data/data_file.json", "w") as write_file:
    json.dump(json_string, write_file)
    
# json.dump(json_string, write_file, indent=2   )










