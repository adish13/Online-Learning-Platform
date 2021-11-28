from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
import requests
from getpass import getpass
from prompt_toolkit.completion import WordCompleter


isInstructor = input("Type 'yes' if you are an instructor : ")
if isInstructor=="yes":
    username = input("Enter username : ")
    name = input("Enter your name : ")
    password = getpass()
else:
    username = input("Enter username : ")
    roll_num = input("Enter Roll Number : ")
    password = getpass()

Completer = WordCompleter(['courses', 'pending', 'download_assignments', 'download_resources', 'courses_instructor', 'list_tas','students'],
                             ignore_case=True)
while 1:
    cmd = prompt('float_moodle ~ ',
                        history=FileHistory('history.txt'),
                        auto_suggest=AutoSuggestFromHistory(),
                        completer=Completer,
    )
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
            response = requests.post('http://127.0.0.1:8000/cli/pending/', data = {'username':username,'roll_num':roll_num, 'password':password})
            course_list = response.json()['courses']
            pending_assignments_list = response.json()['pending_assignments_list']
            pending_resources_list = response.json()['pending_resources_list']
            for i in range(len(course_list)):
                print(str(i+1)+ " Course Name :" + course_list[i])
                print(" Pending Assignments :")
                print("  " + pending_assignments_list[i])
                print(" Pending Resources :")
                print("  "+pending_resources_list[i])
        except Exception as e:
            print("Error- ", e)

    elif (cmd == 'download_assignments'):
        try:
            response = requests.post('http://127.0.0.1:8000/cli/download_assignments/', data = {'username':username,'roll_num':roll_num, 'password':password})
            course_list = response.json()['courses']
            pending_assignments_list = response.json()['pending_assignments_list']
            for i in range(len(course_list)):
                print(str(i+1)+ " Course Name :" + course_list[i])
                print(" Download Assignments :")
                print("  " + pending_assignments_list[i])
        except Exception as e:
            print("Error- ", e)

    elif (cmd== 'download_resources'):
        try:
            response = requests.post('http://127.0.0.1:8000/cli/download_resources/', data = {'username':username,'roll_num':roll_num, 'password':password})
            course_list = response.json()['courses']
            pending_assignments_list = response.json()['pending_assignments_list']
            pending_resources_list = response.json()['pending_resources_list']
            for i in range(len(course_list)):
                print(str(i+1)+ " Course Name :" + course_list[i])
                print(" Download Resources :")
                print("  "+pending_resources_list[i])
        except Exception as e:
            print("Error- ", e)

    elif (cmd== 'courses_instructor'):
        print("hi")
        try:
            response = requests.post('http://127.0.0.1:8000/cli/courses_instructor/', data = {'username':username,'name':name,'password':password})
            course_list = response.json()['courses']
            for i in range(len(course_list)):
                print(str(i+1)+ " Course Name :" + course_list[i] + "\n")
        except Exception as e:
            print("Error- ", e)

    elif (cmd== 'list_tas'):
        print("List of available TAs")
        try:
            response = requests.post('http://127.0.0.1:8000/cli/list_tas/', data = {'username':username,'name':name,'password':password})
            ta_list = response.json()['tas']
            for i in range(len(ta_list)):
                print(str(i+1)+ " Name of the TA :" + ta_list[i] + "\n")
        except Exception as e:
            print("Error- ", e)

    elif (cmd== 'students'):
        print("hi")
        try:
            response = requests.post('http://127.0.0.1:8000/cli/students/', data = {'username':username,'name':name,  'password':password})
            course_list = response.json()['courses']
            students_list = response.json()['students_list']
            for i in range(len(course_list)):
                print(str(i+1)+ " Course Name :" + course_list[i] + "\n")
                print("  "+students_list[i])
        except Exception as e:
            print("Error- ", e)
