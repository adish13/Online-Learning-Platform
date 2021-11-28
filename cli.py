from getpass import getpass
from colorama import init
import requests

init()

username = input("Enter username : ")
roll_num = input("Enter Roll Number : ")
password = getpass()
while True:
    # command to view courses
    cmd = input('Float_Moodle $ ')
    if (cmd =='courses'):
        response = requests.post('http://127.0.0.1:8000/cli/courses/', data = {'username':username, 'roll_num':roll_num, 'password':password})
        try:
            course_list = response.json()['courses']
            instructor_list = response.json()['instructors']
            for i in range(len(course_list)):
                print(str(i+1)+" Course Name : " + course_list[i] + " Instructor Name : " + instructor_list[i])
        except Exception as e:
            print("Error- ", e)
    
    # Command to view pending assignments and resources
    elif (cmd =='pending'):
        try:
            response = requests.post('http://127.0.0.1:8000/cli/pending/', data = {'username':username, 'roll_num':roll_num,'password':password})
            for i,task in enumerate(response.json()['pending']):
                print(i+1,task)
        except Exception as e:
            print("Error- ", e)
