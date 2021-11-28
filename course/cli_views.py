from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from course.models import Student
from django.contrib.auth import login, models, update_session_auth_hash
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from course.models import Progress

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
            print(student.roll_no)
            print(student)
            # print(student.user.username)
            course_names = []
            instructor_names = []
            progress_list = []
            for i in student.course_list.all():
                progress = Progress.objects.get(course = i, student = student)
                print(progress.assignments)
            response = {'courses' : course_names,'instructors':instructor_names}
            print(response)
            return Response(response)
        # except:
        #     print("failed")
        #     response = {'courses':[]}
        #     return Response(response)
    else:
        raise ValidationError({"400": f'Some Problem'})