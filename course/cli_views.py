from django.http import response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
import course
from course.models import Resources, Student
from django.contrib.auth import login, models, update_session_auth_hash
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from course.models import Progress
from instructor.models import Assignment, Instructor
from course.models import Resources
from django.shortcuts import redirect

def rest_login(request):
    data = {}
    # reqBody = json.loads(request.body)
    print(request)
    username = request.data.get("username")
    password = request.data.get('password')
    try:
        Account = User.objects.get(username=username)
    except BaseException as e:
        raise ValidationError({"400": f'{str(e)}'})
    token = Token.objects.get_or_create(user=Account)[0].key
    print(token)
    if not Account.check_password(password):
        raise ValidationError({"message": "Incorrect Login credentials"})
    if Account:
        if Account.is_active:
            login(request, Account)
            request.session.save()
            return True
        else:
            return False

    else:
        return False

@api_view(["POST"])
@permission_classes([AllowAny]) 
def cli_courses(request):
    if rest_login(request):
        # try:
            x = request.data.get("roll_num")
            student = Student.objects.filter(roll_no=x).first()
            print(student.roll_no)
            print(student)
            # print(student.user.username)
            course_names = []
            instructor_names = []
            for i in student.course_list.all():
                course_names.append(i.name)
                instructor_names.append(i.instructor.name)
            response = {'courses' : course_names,'instructors':instructor_names}
            print(response)
            return Response(response)
        # except:
        #     print("failed")
        #     response = {'courses':[]}
        #     return Response(response)
    else:
        raise ValidationError({"400": f'Some Problem'})


@api_view(["POST"])
@permission_classes([AllowAny]) 
def cli_pending(request):
    if rest_login(request):
        # try:
            x = request.data.get("roll_num")
            student = Student.objects.filter(roll_no=x).first()
            course_names = []
            pending_assignments_list = []
            pending_resources_list=[]
            for i in student.course_list.all():
                assignments_list = ''
                resources_list =''
                course_names.append(i.name)
                assignments = Assignment.objects.filter(course = i)
                resources = Resources.objects.filter(course=i)
                progress = Progress.objects.get(course = i, student = student)
                for a in assignments:
                    if not a in progress.assignments.all():
                        assignments_list += (str(a.name)+" Due At: " + str(a.deadline)[:-9] + "\n  ")
                pending_assignments_list.append(assignments_list)
                for r in resources:
                    if not r in progress.resources.all():
                        resources_list+=(str(r.title)+"\n  ")
                pending_resources_list.append(resources_list)
            response = {'courses' : course_names,'pending_assignments_list':pending_assignments_list,'pending_resources_list':pending_resources_list}
            return Response(response)
        # except:
        #     print("failed")
        #     response = {'courses':[]}
        #     return Response(response)
    else:
        raise ValidationError({"400": f'Some Problem'})


@api_view(["POST"])
@permission_classes([AllowAny]) 
def cli_download_assignments(request):
    if rest_login(request):
            x = request.data.get("roll_num")
            student = Student.objects.filter(roll_no=x).first()
            course_names = []
            pending_assignments_list = []
            for i in student.course_list.all():
                assignments_list = ''
                course_names.append(i.name)
                assignments = Assignment.objects.filter(course = i)
                for a in assignments:
                    assignments_list += (str(a.name)+ " URL: http://127.0.0.1:8000"+str(a.file.url) + "\n  ")
                pending_assignments_list.append(assignments_list)
            response={'courses' : course_names,'pending_assignments_list':pending_assignments_list}
            return Response(response)
    else:
        raise ValidationError({"400": f'Some Problem'})


@api_view(["POST"])
@permission_classes([AllowAny]) 
def cli_download_resources(request):
    if rest_login(request):
            x = request.data.get("roll_num")
            student = Student.objects.filter(roll_no=x).first()
            course_names = []
            pending_resources_list = []
            for i in student.course_list.all():
                resources_list = ''
                course_names.append(i.name)
                resources = Resources.objects.filter(course = i)
                for a in resources:
                    resources_list += (str(a.name)+ " URL: http://127.0.0.1:8000"+str(a.file_resource.url) + "\n  ")
                pending_resources_list.append(resources_list)
            response={'courses' : course_names,'pending_resources_list':pending_resources_list}
            return Response(response)
    else:
        raise ValidationError({"400": f'Some Problem'})


@api_view(["POST"])
@permission_classes([AllowAny]) 
def cli_progress_instructor(request):
    if rest_login(request):
            x = request.data.get("username")
            teacher = Instructor.objects.filter(roll_no=x).first()
            course_names = []
            pending_resources_list = []
            for i in student.course_list.all():
                resources_list = ''
                course_names.append(i.name)
                resources = Resources.objects.filter(course = i)
                for a in resources:
                    resources_list += (str(a.name)+ " URL: http://127.0.0.1:8000"+str(a.file_resource.url) + "\n  ")
                pending_resources_list.append(resources_list)
            response={'courses' : course_names,'pending_resources_list':pending_resources_list}
            return Response(response)
    else:
        raise ValidationError({"400": f'Some Problem'})